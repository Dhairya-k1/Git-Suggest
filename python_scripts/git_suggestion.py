from git import Repo

def suggest_git_commands(repo):
   
    suggestions = []

    try:
        #Check for untracked files
        untracked_files = repo.untracked_files
        if untracked_files:
            suggestions.append({
                "command": "git add .",
                "reason": f"Number of Untracked files : {len(untracked_files)}. Add them to staging area."
            })

        #Check for staged changes
        diff_staged = repo.git.diff("--staged")
        if diff_staged:
            suggestions.append({
                "command": "git commit -m 'Your commit message'",
                "reason": "You have staged changes. Commit them in order to save your progress."
            })

        #Check for unstaged changes
        diff_unstaged = repo.git.diff()
        if diff_unstaged and not diff_staged:
            suggestions.append({
                "command": "git add .",
                "reason": "You have unstaged changes. Stage them before committing."
            })

        #Check if the current branch is ahead of or behind the remote
        current_branch = repo.active_branch.name
        tracking_branch = repo.active_branch.tracking_branch()

        if tracking_branch:
            remote_ref = repo.remotes[tracking_branch.remote_name].refs[tracking_branch.remote_head]
            remote_commit = remote_ref.commit
            local_commit = repo.head.commit

            #Check if local is ahead
            ahead_count = repo.git.rev_list(f"{remote_commit}..HEAD", count=True)
            if ahead_count != "0":
                suggestions.append({
                    "command": f"git push origin {current_branch}",
                    "reason": f"Your branch '{current_branch}' is ahead of the remote. Push your changes."
                })

            #Check if remote is ahead
            behind_count = repo.git.rev_list(f"HEAD..{remote_commit}", count=True)
            if behind_count != "0":
                suggestions.append({
                    "command": f"git pull origin {current_branch}",
                    "reason": f"Remote branch '{tracking_branch}' is ahead. Pull the latest changes."
                })

        #Check for multiple local branches and suggest merging 
        if len(repo.branches) > 1 and current_branch != "main":
            suggestions.append({
                "command": f"git checkout main && git merge {current_branch}",
                "reason": f"Current branch is '{current_branch}'. Merge it into 'master' branch when ready."
            })

        #No suggestions, default case
        if not suggestions:
            suggestions.append({
                "command": "git status",
                "reason": "No sugesstions. Check the repository status for more details."
            })

        return suggestions

    except Exception as e:
        return [{"command": "git status", "reason": f"Error : {e}. Check status manually."}]