# GIT AND GITHUB

Git is a version control system and GitHub is a platform where we can track all the changes made to a file, basically storing the file's history.

## Git:
creating a new folder.

**git init** — creates an empty local repository.

**git clone <url>** — retrieve an entire repository from a hosted location via URL.

**git status** — show modified files in the working directory, staged for your next commit.

**git add <file name>**— add a file as it looks now to your next commit (stage).

**git reset <file name>** — unstage a file while retaining the changes in the working directory.

**git commit -m “[message]”** — commit your staged content as a new commit snapshot.

**git log** — show the commit history for the currently active branch.

**git rm <file>** — delete the file from the project and stage the removal for commit.

**git stash** — Save modified and staged changes.

**git stash pop** — write working from the top of the stash stack.

**git stash clear** — clear the stash stack.

**git reset — — hard [commit]** — clear staging area, rewrite working tree from the specified commit.


## GitHub:
**git branch** — list your branches. a * will appear next to the currently active branch.

**git remote add origin/[alias] <URL>** — add a git URL as an alias.

**git remote -v** — gives the URLs that are attached to the project.

### Branch:
The branch is the collection of the changes we made. By default the name of the branch would be main. Whenever we need to add some features or debug an issue we must create a new branch other than the main such that the main project won’t be affected.


The command for adding a new branch: **git branch <new_branch_name>**


HEAD, this is known as a head pointer which points to the latest commit we made.


**git checkout <branchname>**: will make that branch to be active(the head pointer would be pointing to that branch) and all the commits we did will be added to that branch and not to the main branch.


**git merge <branch name>**: This will merge the new branch to the main.


### Working with existing projects in GitHub:
Not everyone has access to make changes in the main project, the user needs to fork the repository to his account to make any changes in that project. This will be reflected in the user repositories with the user’s name. Now users can make any sort of changes they are intended to make. The owner of the project can only approve user changes and he can merge if the changes are appropriate. The URL from which we fork is known as the upstream URL.


The command for adding upstream URL: **git remote add <parent URL>**  
Caution: Do the changes only in the new branch

After making changes in the user’s branch, the user needs to request the owner via pull request.  
pushing the user’s branch — command for that is : **git push origin <new_branch_name>**


After this, the user needs to create a new pull request and if the owner is satisfied with the changes the pull request will be accepted. After raising the pull request any commits the user makes will be added to that pull request only not adding a new one.


So basically a branch can make only one pull request, if the user wants to work on multiple features he needs to create multiple branches(multiple pull requests). (1 Branch → 1 pull request).


### Removing an existing commit in a pull request :


To remove the existing commit we need to unstage that particular commit this can be done by ; **git reset unique id of commit below it**. This makes the commit unstaged and after that, we can stash that commit. Pushing this change would be somewhat different the command would be :  
**git push origin <branch_name> -f** (force pushing the commits).


If the user’s pull request is accepted by the owner then the owner will update his main branch and those changes won’t be reflected in the user’s fork main branch. For updating the user main these steps need to be followed, switch to the main branch.


**git fetch — — all — — prune**: this command will fetch all the changes that are made upstream.  

**git reset — — hard upstream/main**: this command would make the both mains same.  

**git push origin main**: will push the changes into main.  

**git pull upstream main**: This will also do the same updating the fork main branch. Again pushing should be done.  



### Squashing the commits:
copy the unique ID of the commit that is below the commits that the user wants to squash or pick.  
Command :**git rebase -i <unique_id>** (i is an interactive environment)  

After that user needs to edit the pick and squash according to the need pick →s →s will squash that into a single commit and add the message and that would squash the commits.


### Merge Conflicts:
When two users make the same changes in the same line git would be confused, the owner needs to resolve it manually and the desired one would be merged to the main branch.