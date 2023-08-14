#!/bin/bash
chatBTP reset
# Add all changes to the staging area
git add .
# Get a summary of the changes
summary=$(git  diff --staged | chatBTP ask -m"You are to act as the developer reviewing  a commit . Your mission is to review the  commit  and find any significant problems, and spelling errors  . I'll send you an output of 'git diff --staged' command.
  Use the present tense. " --noSession=true --ascii --stdin)
# Check if the chatBTP command was successful
if [ $? -ne 0 ]; then
    echo "chatBTP command failed, aborting"
    exit 1
fi

echo  "$summary"
