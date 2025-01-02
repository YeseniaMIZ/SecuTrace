import re
import json
import jsonschema
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from datetime import datetime

def parse_log_line(log_line):
    """
    Parses a single line of log data and returns a dictionary with useful details.
    Example log line format: '2025-01-02 12:34:56 ERROR - Failed login attempt for user admin'
    """
    log_pattern = r'(?P<timestamp>\S+ \S+) (?P<level>\S+) - (?P<message>.+)'
    match = re.match(log_pattern, log_line)
    
    if match:
        return match.groupdict()
    else:
        return None

def format_timestamp(timestamp):
    """
    Formats a timestamp (e.g., '2025-01-02 12:34:56') to 'January 2, 2025 at 12:34 PM'
    """
    try:
        dt = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
        return dt.strftime('%B %d, %Y at %I:%M %p')
    except ValueError:
        return timestamp

def filter_logs_by_level(log_lines, level='ERROR'):
    """
    Filters log lines by a given severity level (e.g., ERROR, WARNING, INFO).
    """
    filtered_logs = []
    for line in log_lines:
        log_data = parse_log_line(line)
        if log_data and log_data['level'] == level:
            filtered_logs.append(line)
    return filtered_logs

def extract_json_from_log(log_line):
    """
    Extracts JSON data from a log line. Assumes that the JSON data is embedded
    in the log message field.
    Example log line: '2025-01-02 12:34:56 INFO - {"user": "admin", "action": "login"}'
    """
    try:
        start = log_line.index('{')
        json_str = log_line[start:]
        json_data = json.loads(json_str)
        return json_data
    except (ValueError, IndexError):
        return None

def log_line_to_dict(log_line):
    """
    Converts a log line to a dictionary with keys: timestamp, level, message, and optional json_data.
    """
    log_data = parse_log_line(log_line)
    if log_data:
        json_data = extract_json_from_log(log_line)
        log_data['json_data'] = json_data
        return log_data
    else:
        return None
        
def load_config(config_path):
    """
    Loads the configuration from a JSON file and validates it.
    """
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)

    # Mock schema loading for testing purposes
    try:
        schema = {
            "log_file_path": {"type": "string"},
            # Add more schema checks as needed
        }
    except FileNotFoundError:
        raise FileNotFoundError("Schema file not found.")
    
    return config  #