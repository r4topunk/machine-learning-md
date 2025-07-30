#!/usr/bin/env python3
import csv
import json
import sys
from datetime import datetime
from pathlib import Path

# Read what Claude Code is doing
input_data = sys.stdin.read()
hook_data = json.loads(input_data)

# Extract tool information from correct structure
tool_name = hook_data.get('tool_name', '')
tool_input = hook_data.get('tool_input', {})

# Only track file operations that matter
if tool_name in ['Read', 'Write', 'Edit']:
    file_path = tool_input.get('file_path', 'unknown')
    
    # Convert to relative path from project root
    if file_path != 'unknown':
        project_root = Path.cwd()
        try:
            relative_path = Path(file_path).relative_to(project_root)
            file_path = str(relative_path)
        except ValueError:
            # If file is outside project directory, keep as is
            pass
    
    # Create simple log entry with session info
    log_entry = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'session': hook_data.get('session_id', 'unknown')[:8],  # Short session ID
        'action': tool_name,
        'file': file_path
    }
    
    # Append to CSV log file
    csv_file = Path('.claude/important_files.csv')
    csv_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Check if file exists to determine if we need headers
    file_exists = csv_file.exists()
    
    with open(csv_file, 'a', newline='') as f:
        writer = csv.writer(f)
        
        # Write header if file is new
        if not file_exists:
            writer.writerow(['timestamp', 'session_id', 'action', 'file_path'])
        
        # Write the log entry
        writer.writerow([log_entry['time'], log_entry['session'], log_entry['action'], log_entry['file']])

# Always let the action continue
sys.exit(0)