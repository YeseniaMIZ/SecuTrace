import numpy as np
from sklearn.ensemble import IsolationForest

def detect_anomalies(logs):
    """
    Detects anomalies in logs using Isolation Forest model.
    Assumes that logs contain structured data like 'timestamp', 'level', and 'message'.
    """
    # Example: Convert logs into numerical data for anomaly detection
    features = []
    for log in logs:
        timestamp = log['timestamp']
        level = log['level']
        features.append([hash(timestamp), hash(level)])  # Hashing to turn categorical data into numbers
    
    # Using Isolation Forest for anomaly detection
    model = IsolationForest(contamination=0.1)
    model.fit(features)
    predictions = model.predict(features)  # -1 for anomalies, 1 for normal
    
    

    # Mark the anomalies
    for i, log in enumerate(logs):
        log['anomaly'] = 'Anomaly' if predictions[i] == -1 else 'Normal'
    
    return logs
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