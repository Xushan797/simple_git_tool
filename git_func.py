import subprocess


class GitTool:

    def __init__(self):
        self.author = 'Xushan797'
    def start(self):
        print(self.authored())

    def get_active_branch(self):
        output = subprocess.getoutput("git rev-parse --abbrev-ref HEAD")

    def modified_status(self):
        pass
    def authored(self):
        # git log -1 --pretty=format:\'%an\'
        output = subprocess.getoutput("git log -1 --pretty=format:\'%an\'")
        # result = subprocess.run(['git', 'log', '-1', '--pretty=format:\'%an\''], stdout=subprocess.PIPE)
        # author =  result.stdout.decode('utf-8')
        return output == self.author



if __name__ == "__main__":
    gittool = GitTool()
    gittool.start()