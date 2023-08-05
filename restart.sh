running_script="./index.py"
pids=$(ps aux | grep "$running_script" | grep -v grep | awk '{print $2}')
if [ -n "$pids" ]; then
  echo "Terminating running instances of $running_script..."
  kill -9 $pids
  sleep 1
fi

# Step 3: Execute the Python3 script
python3 "$running_script" &
