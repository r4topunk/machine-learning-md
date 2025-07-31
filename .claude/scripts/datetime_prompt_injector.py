#!/usr/bin/env python3
"""
Simple datetime injector for Claude Code
Adds current date and time to the prompt
"""

import sys
from datetime import datetime

try:
    # Get current date and time
    now = datetime.now()
    
    # Print datetime info that will be added to Claude's context
    print(f"Current date and time: {now.strftime('%A, %B %d, %Y at %I:%M:%S %p')}")
    
    # Exit successfully
    sys.exit(0)
    
except Exception:
    # Exit with error
    sys.exit(1)