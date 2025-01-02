# tests/test_anomaly_detection.py

import pytest
from src.anomaly_detection import detect_anomalies

def test_anomaly_detection_valid_data():
    logs = [
        {"timestamp": "2025-01-01T00:00:00", "value": 0.1, "level": "INFO"},
        {"timestamp": "2025-01-01T01:00:00", "value": 0.2, "level": "INFO"},
        {"timestamp": "2025-01-01T02:00:00", "value": 0.9, "level": "ERROR"},
    ]
    anomalies = detect_anomalies(logs)
    # assert checks for anomalies here...
    
def test_anomaly_detection_no_anomalies():
    logs = [
        {"timestamp": "2025-01-01T00:00:00", "value": 0.1, "level": "INFO"},
        {"timestamp": "2025-01-01T01:00:00", "value": 0.2, "level": "INFO"},
        {"timestamp": "2025-01-01T02:00:00", "value": 0.5, "level": "INFO"},
    ]
    anomalies = detect_anomalies(logs)
    # assert checks for anomalies here...