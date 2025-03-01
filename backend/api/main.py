from flask import Blueprint
from flask import jsonify
from flask import request
from github import Github
from dotenv import dotenv_values

main_blueprint = Blueprint('main', __name__)
g = Github(dotenv_values().get('GITHUB_TOKEN'))
repo = g.get_repo(dotenv_values().get('GITHUB_REPO'))
default_branch_date = repo.get_branch("master").commit.commit.author.date.strftime('%Y-%m-%d %H:%M:%S')
branches = list(repo.get_branches())


def get_status(branch_last_commit_date):
    if branch_last_commit_date == default_branch_date:
        return "up-to-date"
    elif branch_last_commit_date > default_branch_date:
        return "ahead"
    else:
        return "behind"


@main_blueprint.route('/get_branches', methods=['GET'])
def get_branches():
    branches_names = []
    for branch in branches:
        date = branch.commit.commit.committer.date
        short_date = date.strftime('%Y-%m-%d')
        date = date.strftime('%Y-%m-%d %H:%M:%S')
        status = get_status(date)
        branches_names.append({'name': branch.name, 'date': short_date, 'status': status})
    return jsonify(branches_names)


@main_blueprint.route('/get_commits/', methods=['GET'])
def get_commits():
    branch_name = request.headers.get('branch_name')
    commits_list = list(repo.get_commits(branch_name))
    commits_dict = []
    for commit in commits_list:
        commits_dict.append({'sha': commit.sha, 'message': commit.commit.message,
                             'author': commit.commit.author.name, 'date': commit.commit.author.date})
    return jsonify(commits_dict)


@main_blueprint.route('/get_commit/', methods=['GET'])
def get_commit():
    commit_sha = request.headers.get('commit_sha')
    commit = repo.get_commit(commit_sha)
    files = [commit.files[i].filename for i in range(len(commit.files))]
    return jsonify({'sha': commit.sha, 'message': commit.commit.message, 'author': commit.commit.author.name,
                    'date': commit.commit.author.date, 'additions': commit.stats.additions,
                    'number_of_changed_files': len(files),
                    'deletions': commit.stats.deletions,
                    'author_email': commit.commit.author.email,
                    'files': files})


@main_blueprint.route('/get_branch/', methods=['GET'])
def get_branch():
    branch_name = request.headers.get('branch_name')
    branch = repo.get_branch(branch_name)
    date = branch.commit.commit.committer.date
    short_date = date.strftime('%Y-%m-%d')
    date = date.strftime('%Y-%m-%d %H:%M:%S')
    status = get_status(date)
    return jsonify({'name': branch.name, 'total_commits': branch.commit.stats.total,
                    'date': short_date,
                    'status': status})


@main_blueprint.route('/get_open_pull_requests/', methods=['GET'])
def get_open_pull_requests():
    pull_requests = list(repo.get_pulls())
    pull_requests_dict = []
    for pull_request in pull_requests:
        pull_requests_dict.append({'number': pull_request.number, 'title': pull_request.title,
                                   'author': pull_request.user.login, 'date': pull_request.created_at,
                                   'status': pull_request.state})
    return jsonify(pull_requests_dict)


@main_blueprint.route('/get_closed_pull_requests/', methods=['GET'])
def get_closed_pull_requests():
    pull_requests = list(repo.get_pulls(state='closed'))
    pull_requests_dict = []
    for pull_request in pull_requests:
        pull_requests_dict.append({'number': pull_request.number, 'title': pull_request.title,
                                   'author': pull_request.user.login, 'date': pull_request.created_at,
                                   'status': pull_request.state})
    return jsonify(pull_requests_dict)


@main_blueprint.route('/get_pull_request/', methods=['GET'])
def get_pull_request():
    pull_request_number = request.headers.get('pull_request_number')
    pull_request = repo.get_pull(int(pull_request_number))
    return jsonify({'number': pull_request.number, 'title': pull_request.title,
                    'author': pull_request.user.login, 'date': pull_request.created_at,
                    'status': pull_request.state, 'body': pull_request.body, 'merged': pull_request.merged})


@main_blueprint.route('/create_pull_request/', methods=['POST'])
def create_pull_request():
    content = request.get_json()
    pull_request_title = content.get('pull_request_title')
    pull_request_body = content.get('pull_request_body')
    pull_request_branch = content.get('pull_request_branch')
    pull_request = repo.create_pull(title=pull_request_title, body=pull_request_body, head=pull_request_branch,
                                    base='master')
    return jsonify({'status': 'success', 'pull_request_number': pull_request.number})


@main_blueprint.route('/merge_pull_request/', methods=['POST'])
def merge_pull_request():
    content = request.get_json()
    pull_request_number = content.get('pull_request_number')
    pull_request = repo.get_pull(int(pull_request_number))
    pull_request.merge()
    pull_request.edit(state='merged')
    return jsonify({'status': 'success'})


print(dir(repo.get_pull))
