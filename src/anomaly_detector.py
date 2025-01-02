# src/anomaly_detector.py

def detect_anomalies(events):
    """Detect anomalies in system behavior."""
    anomalies = []
    for event in events:
        if event['type'] == 'login' and event['ip'] not in trusted_ips:
            anomalies.append(event)
    return anomalies

trusted_ips = ['192.168.1.1', '192.168.1.2']