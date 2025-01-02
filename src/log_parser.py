# src/log_parser.py
import json

def parse_log(log_file):
    """Parse a log file and return a list of events."""
    events = []
    with open(log_file, 'r') as file:
        for line in file:
            event = json.loads(line)
            events.append(event)
    return events

def analyze_events(events):
    """Analyze events to detect security incidents."""
    suspicious_events = []
    for event in events:
        if event['type'] == 'failed_login' and event['user'] == 'admin':
            suspicious_events.append(event)
    return suspicious_events