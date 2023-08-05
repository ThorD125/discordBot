#!/bin/bash

# Step 1: Git pull the latest changes
git pull


# Step 2: Terminate the running script
# Change "./index.py" to the actual name of your Python script if different
./restart.sh

# Step 3: Execute the Python3 script
python3 "$running_script" &
