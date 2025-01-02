from .utils import parse_log_line, format_timestamp

# src/log_parser.py
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
def parse_logs(log_data):
    # Assume the log data is a string and parse it accordingly
    parsed_logs = []
    try:
        log_entries = log_data.split("\n")
        for entry in log_entries:
            parts = entry.split(" ")
            if len(parts) >= 3:
                parsed_logs.append({
                    "timestamp": parts[0],
                    "level": parts[1],
                    "message": " ".join(parts[2:])
                })
            else:
                raise ValueError("Invalid log format")
    except Exception as e:
        raise ValueError(f"Error parsing logs: {e}")
    return parsed_logs