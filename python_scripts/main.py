import sys
from git import Repo
from git_suggestion import suggest_git_commands 

def main():
    # 1. Setup the Repository Object
    try:
        repo = Repo(".")
        if repo.bare:
            print("This is not a valid Git repository.")
            sys.exit(1)
    except Exception as e:
        print(f"Error accessing Git repository: {e}")
        sys.exit(1)

    # 2. Get Suggestions
    try:
        suggestions = suggest_git_commands(repo)
    except Exception as e:
        print(f"Error getting suggestions: {e}")
        sys.exit(1)

    if not suggestions:
        print("No actions needed. Your repo is clean.")
        sys.exit(0)

    # 3. Print Suggestions 
    print("\n    Git Suggestions:")
    print("--------------------------------------------------")
    
    for item in suggestions:
        print(f" {item['command']}")
        print(f" ↳{item['reason']}")
        print("") 

    print("--------------------------------------------------")

if __name__ == "__main__":
    main()