#!/bin/bash

# The $1 represents the name you type when you run the script.

# 1. Create the folder using the name provided
mkdir $1

# 2. Go inside the new folder
cd $1

# 3. Create a blank Readme file
touch Readme.md

# 4. Write a default title into the Readme
echo "# Project: $1" > Readme.md

# 5. Print a success message
echo "Successfully created project: $1"