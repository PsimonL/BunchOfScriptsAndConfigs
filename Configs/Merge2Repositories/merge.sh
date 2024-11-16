#! /bin/bash

# Clone 1st repo, let's call it REPO_A
git clone https://github.com/user/REPO_A.git
# Go to folder of repository REPO_A
cd REPO_A

# Add remotely new repo REPO_B. Now you can reach REPO_B from REPO_A using git.
git remote add REPO_B https://github.com/user/REPO_B.git

# Print list of all remote repos connected to current repo.
git remote -v
# Sample output:
# origin  https://github.com/user/REPO_A.git (fetch)
# origin  https://github.com/user/REPO_A.git (push)
# REPO_B   https://github.com/user/REPO_B.git (fetch)
# REPO_B   https://github.com/user/REPO_B.git (push)

# Fetch REPO_B
git fetch REPO_B
# Create new branch for safety purposes
git checkout -b merge-REPO_B
# Combine the history and content of the main branch from REPO_B into the current branch.
# This "--allow-unrelated-histories" flag allows Git to merge repositories with different starting points in their histories.
git merge --allow-unrelated-histories REPO_B/main

# Push to remote 
git add .
git commit -m "Merge 2 repositories completed"
git push origin master