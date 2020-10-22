#!/usr/bin/env bash

# Format our python code with black and iSort
if command -v isort > /dev/null 2>&1 ; then
    isort --quiet .
else
    echo "iSort is not installed. Could not be run"
fi

if command -v black > /dev/null 2>&1 ; then
    black --quiet .
else
    echo "Python Black is not installed. Could not be run"
fi

# Symlink the VERSION file
ln -s {{cookiecutter.project_slug}}/VERSION VERSION

# Initialize a git repo and set the origin
git init
git add .
git commit -m "Initial Commit"
git remote add origin git@github.com:fchorney/{{cookiecutter.project_slug}}.git

exit 0
