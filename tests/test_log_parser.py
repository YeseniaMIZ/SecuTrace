# tests/test_log_parser.py

import pytest
from src.log_parser import process_logs

# tests/test_log_parser.py
def process_logs(log_data):
    """
    Process raw log data and return structured log entries.
    """
    parsed_logs = []
    try:
        log_entries = log_data.split("\n")
        for entry in log_entries:
            parts = entry.split(" ")
            if len(parts) >= 3:
                parsed_logs.append({
                    "timestamp": parts[0],
                    "log_level": parts[1],  # Ensure 'log_level' is correctly set
                    "message": " ".join(parts[2:])
                })
            else:
                raise ValueError("Invalid log format")
    except Exception as e:
        raise ValueError(f"Error parsing logs: {e}")
    return parsed_logs