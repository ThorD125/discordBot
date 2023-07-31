#!/bin/bash

# Step 1: Git pull the latest changes
git pull

# Step 2: Terminate the running script
# Change "index.py" to the actual name of your Python script if different
running_script="runningscript.py"
pids=$(ps aux | grep "$running_script" | grep -v grep | awk '{print $2}')
if [ -n "$pids" ]; then
  echo "Terminating running instances of $running_script..."
  kill -9 $pids
  sleep 1
fi

# Step 3: Execute the Python3 script
python3 "$running_script"
