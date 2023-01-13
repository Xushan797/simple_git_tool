Pronto.ai take home coding


> A simple tool that prints specific facts about a local git repository.


## Getting Started

Project instructions  
Your task is to create a program that prints specific facts about a local git repository. You can use any language, and you are welcome to import existing packages.  

Your program should take in one argument:  
git_dir: directory in which to assess git status  
  
Your program should print the following things:  
active branch (boolean)  
whether repository files have been modified (boolean)  
whether the current head commit was authored in the last week (boolean)  
whether the current head commit was authored by Rufus (boolean)  
  
Sample Output Format:  
The program should print something like:  
active branch: master  
local changes: False  
recent commit: True  
blame Rufus: True  

### Prerequisites 

The submission can be tested with a MacOS with Python 3. I develop and test the service using a MacOs with Python 3.10.0.

### Setup & Build

Clone this repo and check out to the corresponding repo path. Run the following command:

```sh
python3 git_func.py  
```

### Simple test example

I run the code via my local environment:

```sh
/Users/loaner/Desktop/leetcode/venv/bin/python /Users/loaner/Desktop/leetcode/test/hello-world/git_func.py
Enter the path of your file: /Users/loaner/Desktop/leetcode/test/hello-world/
active branch: main
local changes: True
recent commit: True
blame Rufus: False
```


  
## Implementation

I mainly use Python subprocess package to call the corresponding git command.  
First, check the input path is exists.  
Then it would print out the information as needed.  
  
(in my understanding:  
active branch: The branch you are currently working on  
whether repository files have been modified: whether uncommited changes exists  
current head commit: last commit)

## Authors 

* **Xushan Qing** - *Duke University* - [Xushan Qing](https://www.linkedin.com/in/xushan-qing/)