# fullstack-interview-test
Interview test for fullstack Software Engineers

## Geting started

1. After cloning the project, go to the backend folder and create a .env file that contains:

    GITHUB_TOKEN = Your Github token


    GITHUB_REPO = the name of your repository
    
Note: you can check the instructions to get your github token in [here](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/)

2. return to the project's base directory

3. in two separate terminal windows, run: 

 `make back`
 
 and 
 
 `make front` 
 
4. the project is now running on `http://localhost:8080/`
 

## Endpoints

| Endpoint                  | Method | Description                  | Parameters                                                             |
|---------------------------|--------|------------------------------|------------------------------------------------------------------------|
| /get_branches             | GET    | Get all branches             |                                                                        |
| /get_branch               | GET    | Get branch details           | branch_name                                                            |
| /get_commits/             | GET    | Get all branch commits       | headers: 'branch_name'                                                 |
| /get_commit               | GET    | Get commit details           | headers: 'commit_sha'                                                  |
| /get_open_pull_requests   | GET    | Get all open pull requests   |                                                                        |
| /get_closed_pull_requests | GET    | Get all closed pull requests |                                                                        |
| /get_pull_request         | GET    | Get pull request details     | headers: 'pull_request_number'                                         |
| /create_pull_request      | POST   | Create pull request          | data: 'pull_request_title', 'pull_request_body', 'pull_request_branch' |
| /merge_pull_request       | POST   | Merges and closes open PR    | headers: 'pull_request_number'                                         |


## Views

- Branches
![image](https://user-images.githubusercontent.com/37568592/177251677-860b333d-1fcf-4a4d-a241-bc9fd508ac27.png)
- Branch details
![image](https://user-images.githubusercontent.com/37568592/177251717-26702ba8-6f87-4d8a-b886-fc68dded779d.png)
- Commit details modal
![image](https://user-images.githubusercontent.com/37568592/177251963-a908d466-7af0-4e1e-b53b-3484882e8643.png)
- Pull requests
  - Open pull requests
  ![image](https://user-images.githubusercontent.com/37568592/177252016-2591b399-55dc-4a2f-93b9-3819405b4fc6.png)
  - Closed pull requests
  ![image](https://user-images.githubusercontent.com/37568592/177252050-68ea8766-751c-44a9-bfeb-1d54afc7edfa.png)
- Pull request details
![image](https://user-images.githubusercontent.com/37568592/177252094-a055bc51-36cb-4bae-b88d-2e294b3fa1e5.png)
- Create pull request modal
![image](https://user-images.githubusercontent.com/37568592/177252113-02d45017-cc45-4ad6-adb0-4165ca6bee10.png)


## Welcome!
If you're reading this, it means we're interested in working with you and solving amazing and difficult problems in real-estate tech in Mexico.

This README provides the instructions to a small, self-contained test for a FullStack Software Engineer position.

## What we're looking for
We're looking for a talented and driven full-stack engineer, comfortable with building responsive front end experiences, as well as with designing and building rigorous APIs and backend services. 

This means that this test is designed to gather signal on your coding structure, the tradeoffs and decisions you make on API design, and how you build a lightweight frontend app to show the data coming from your API. We're excited to see what you build!

## The test
Today, we'll be building an API wrapper around the git information of this project. We suggest forking this repo and start working on it on your private fork, the url of which is the only thing you need to send us when you're done.

The main objects we'll be dealing with are:
- Commits
- Authors
- Branches
- PRs

We'd like to see a visual representation of the git history of this repo as a **JS web-app**, using the API previously described. To be specific, we'd like to see the following:
- A view where we can see the existing branches
- A branch detail view where we can see all the commits to one specific branch, with commit messages, authors and timestamps.
- A commit detail view where we can see the commit message, timestamp, number of files changed and author names / emails.
- A "PR" create view, where we can choose two branches (base and compare), and merge them together, just like Pull Requests work in Github. 
- A "PR" list view, where we see all created PRs and the following info: Author, Title, Description and Status (`Open`, `Closed`, `Merged`). If the status is `Open`, there should be a button that allows us to mark it as `Closed`.

For the **PR create view**, we'll ask the user for a PR title and description, and we'll give them 2 options: either save it (Status = `Open`), or merge it. Note that merge operations can fail due to conflicts or other reasons, so make sure you handle and show whatever error happens when merging. There's no need to do something about these errors other than show them in the frontend. After a successful merge, the PR should move to a `Merged` status.

## Deliverables
We expect this test to take around 4 hours, but not significantly more (your time is very valuable!). We're giving you a week from the date you receive it to complete it and send us your repo URL, using **whatever stack you feel most comfortable with**. Due to this, we ask that you also provide a `README` with instructions for running your project, both back and frontend, along with setup instructions (or provide a Dockerfile and a `docker run` instruction).

It's up to you to design how this should look code-wise, but we don't expect you to model all git objects in a DB. We're ok with reading them using a library wrapper for git like [GitPython](https://gitpython.readthedocs.io/en/stable/), on-demand. The only DB design required is the one for PRs.

## Grading
We'll grade this project according to completion percentage of the features requested, good coding style for both back and frontend. For us, good coding means:
- It's readable. We read code much more often than we write it, so it's important that we're clear on what we're doing and comment any hairy parts (which we don't really expect to have in this test!).
- It's reasonably well ordered and with a logically thought-out structure. We like to do separation of concerns, and deal with routing, DB models, serialization, etc in their own file structure / files. 
- Clear, understandable variable names. No one wants to read the whole file to understand what the variable `c1_2` means.

We also care about being able to run your test without significant effort on our part, so make sure you test the instructions you provide on your README.

### Things we won't be grading
- Design chops: we care that you know enough CSS not to be surprised when you need to work on it, but we're not picky about your solution's UX/UI.

### Bonus points
- Your code has tests.

If you come across any questions or anything we didn't cover on this README, feel free to reach out to us and we'll get you an answer as soon as possible. Happy coding!
