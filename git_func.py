'''
Project instructions
Your task is to create a program that prints specific facts about a local git repository. You can use any language, and you are welcome to import existing packages.

Your program should take in one argument:
git_dir: directory in which to assess git status

Your program should print the following things:
active branch (boolean)
whether repository files have been modified (boolean)
whether the current head commit was authored in the last week (boolean)
whether the current head commit was authored by Rufus (boolean)

Sample Output Format
The program should print something like
active branch: master
local changes: False
recent commit: True
blame Rufus: True
'''

import subprocess, os

class GitTool:
    def __init__(self):
        self.author = 'Rufus'
        self.cwd = None
    def check_input(self):
        user_input = input("Enter the path of your file: ")
        while not os.path.exists(user_input):
            print("I did not find the file at you input path! " + str(user_input))
            user_input = input("Enter the path of your file: ")
        return user_input if user_input else None
    def start(self):
        try:
            self.cwd = self.check_input()
            branch_name = self.get_active_branch()
            modified_status = self.modified_status()
            commited_status = self.commited_last_week()
            author_status = self.authored()
            txt = "active branch: {branch_name}\nlocal changes: {modified_status}\nrecent commit: {commited_status}\nblame Rufus: {author_status}\n".format \
            (branch_name = branch_name, modified_status = modified_status, commited_status = commited_status, author_status = author_status)
            print(txt)
        except:
            print("Sorry, unknown error happened. The environment may be not supported! ")

    def get_active_branch(self):
        # active branch (boolean)
        output = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode()

        return output.strip()

    def modified_status(self):
        # whether repository files have been modified (boolean)
        output = subprocess.check_output(["git", "diff-index", "--name-only", "HEAD"]).decode()
        return output is not None

    def commited_last_week(self):
        # whether the current head commit was authored in the last week (boolean)
        output = subprocess.check_output(["git", "log", "-1", "--since=\"1 seconds ago\""]).decode()
        return output is not None

    def authored(self):
        # whether the current head commit was authored by Rufus (boolean)
        output = subprocess.check_output(["git", "log", "-1", "--pretty=format:\'%an\'"]).decode()
        return output == self.author

if __name__ == "__main__":
    gittool = GitTool()
    gittool.start()