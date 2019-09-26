#!/usr/bin/env bash


while getopts ":f:b:" opt; do
  case $opt in
    f) FILE_NAME="$OPTARG"
    ;;
    b) BRANCH_NAME="$OPTARG"
    ;;
    \?) echo "Invalid option -$OPTARG" >&2
    ;;
  esac
done

echo "automated git push process starts here..."
GIT_STATUS=$(git status)
git checkout develop
git checkout -b ${BRANCH_NAME}
git add ${FILE_NAME}
git push -u origin ${BRANCH_NAME}