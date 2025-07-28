#!/bin/bash

# Run the Python script to generate .tst files
echo "Generating .tst test files from episodes markdown"
python generate_tst.py

# Delay 2 seconds
sleep 2

# Set the GAP executable path
GAP_EXEC="gap"

# Set the test entry script
TEST_SCRIPT="testall.g"

# Set the log directory and log file path
LOG_DIR="log"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_FILE="$LOG_DIR/test-output_${TIMESTAMP}.log"

# Create the log directory if it doesn't exist
mkdir -p "$LOG_DIR"

# Print start message
echo "Running GAP tests..."
echo "Output log will be saved to: $LOG_FILE"
echo "-------------------------------------"

# Delay 2 seconds
sleep 2

# Run GAP and simultaneously record logs (stdout + stderr), show real-time output on terminal
"$GAP_EXEC" -q "$TEST_SCRIPT" 2>&1 | tee "$LOG_FILE"

# Print completion message
echo "Tests completed, log saved at $LOG_FILE"
