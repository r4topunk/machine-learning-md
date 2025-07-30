#!/usr/bin/env python3
import csv
from pathlib import Path
from collections import Counter

def main():
    # Look for CSV log file (matches current tracking system)
    csv_file = Path('.claude/important_files.csv')
    
    if not csv_file.exists():
        print("No file operations logged yet!")
        print("The tracking system will create important_files.csv after some file operations.")
        exit()

    # Read CSV and extract file paths
    file_paths = []
    read_operations = []
    
    try:
        with open(csv_file, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                file_path = row.get('file_path', '')
                action = row.get('action', '')
                
                if file_path and file_path != 'unknown':
                    file_paths.append(file_path)
                    
                    # Track read operations specifically
                    if action == 'Read':
                        read_operations.append(file_path)
    
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        exit()

    if not file_paths:
        print("No valid file operations found in log!")
        exit()

    # Analysis and output
    print("\n🔍 MOST ACCESSED FILES:")
    print("-" * 50)
    
    for item, count in Counter(file_paths).most_common(10):
        print(f"{count:3d}x | {item}")
    
    if read_operations:
        print("\n📖 MOST READ FILES:")
        print("-" * 50)
        
        for item, count in Counter(read_operations).most_common(10):
            print(f"{count:3d}x | {item}")
    
    # File type analysis
    extensions = []
    for path in file_paths:
        if '.' in path:
            ext = path.split('.')[-1]
            extensions.append(ext)
    
    if extensions:
        print("\n📄 FILE TYPES:")
        print("-" * 50)
        
        for ext, count in Counter(extensions).most_common(5):
            print(f"{count:3d}x | .{ext} files")
    
    # Directory analysis
    directories = []
    for path in file_paths:
        if '/' in path:
            dir_name = path.split('/')[0]
            directories.append(dir_name)
    
    if directories:
        print("\n📁 TOP DIRECTORIES:")
        print("-" * 50)
        
        for dir_name, count in Counter(directories).most_common(5):
            print(f"{count:3d}x | {dir_name}/")
    
    print(f"\n📊 SUMMARY:")
    print(f"Total file operations: {len(file_paths)}")
    print(f"Unique files accessed: {len(set(file_paths))}")
    print(f"Read operations: {len(read_operations)}")
    
    print("\n💡 TIP: Consider adding frequently accessed files to your CLAUDE.md!")

if __name__ == "__main__":
    main()