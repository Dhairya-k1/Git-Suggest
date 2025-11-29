# :tada: Git Suggest

The Git Workflow Manager is a tool designed to streamline the Git experience, making version control more efficient, less prone to error and intuitive for developers of all skill levels. By abstracting away complex commands and automating common workflows, it allows developers to focus on writing code rather than managing version control complexities.

## ✨Features

* **Intelligent Command Suggestions**: The tool analyzes your repository's state and suggests relevant Git commands to guide you through your workflow.


## How to Use
To use the functionality, navigate to your Git repository in Git Bash and run the following command:

```bash
python main.py suggest
```
## Future Projects
**1. AI README Generator**: Analyzes code and creates a README, saving time and keeps documentation up-to-date.

* How it works: It works by using AI to analyze your project's codebase to understand its structure and purpose. It then uses that information to automatically write or update the README with accurate and relevant content.

**2. Automated Branch Cleanup**: It would scan for and identify branches that have already been merged into the main branch. This saves a developer the hassle of manually checking and deleting old branches, which can accumulate quickly.

* How it works: The tool would use git branch --merged to find branches that can be safely deleted. It could then prompt the user to confirm the deletion or offer a command to run it automatically.
