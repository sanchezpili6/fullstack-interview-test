import {Apis} from "@/helpers/API";

const get_branches = async () => {
    const response = await Apis.get(`/get_branches`);
    return response.data;
}

const get_branch = async (branch_name) => {
    const response = await Apis.get(`/get_branch/`, {headers: {'branch_name': branch_name}});
    return response.data;
}

const get_commits = async (branch_name) => {
    const response = await Apis.get(`/get_commits/`, {headers: {'branch_name': branch_name}});
    return response.data;
}

const get_commit = async(commit_sha)=> {
    const response = await Apis.get(`/get_commit/`, {headers: {'commit_sha': commit_sha}});
    return response.data;
}

const get_open_pull_requests = async () => {
    const response = await Apis.get(`/get_open_pull_requests`);
    return response.data;
}

const get_closed_pull_requests = async () => {
    const response = await Apis.get(`/get_closed_pull_requests`);
    return response.data;
}

const get_pull_request = async (pull_request_number) => {
    const response = await Apis.get(`/get_pull_request/`, {headers: {'pull_request_number': pull_request_number}});
    return response.data;
}

const close_pull_request = async (pull_request_number) => {
    const response = await Apis.get(`/close_pull_request/`, {headers: {'pull_request_number': pull_request_number}});
    return response.data;
}

const create_pull_request = async (pull_request_title, pull_request_body, pull_request_branch) => {
    const response = await Apis.post(`/create_pull_request/`,
         {'pull_request_title': pull_request_title, 'pull_request_body': pull_request_body,
                'pull_request_branch': pull_request_branch});
    return response.data;
}

const merge_pull_request = async (pull_request_number) => {
    const response = await Apis.post(`/merge_pull_request/`,{'pull_request_number': pull_request_number});
    return response.data;
}

export {
    get_branches,
    get_branch,
    get_commits,
    get_commit,
    get_open_pull_requests,
    get_closed_pull_requests,
    get_pull_request,
    close_pull_request,
    create_pull_request
}
