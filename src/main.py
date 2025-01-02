from src.log_parser import parse_logs
from src.anomaly_detector import detect_anomalies
from src.alert_system import send_alert
from src.visualizer import plot_anomalies

def main():
    # Example log lines
    log_lines = [
        '2025-01-02 12:34:56 ERROR - Failed login attempt for user admin',
        '2025-01-02 12:35:00 INFO - User admin logged in successfully',
        '2025-01-02 12:36:10 ERROR - Invalid password attempt for user admin',
    ]
    
    # Parse the logs
    logs = parse_logs(log_lines)
    
    # Detect anomalies
    logs_with_anomalies = detect_anomalies(logs)
    
    # Send an alert if anomalies are found
    for log in logs_with_anomalies:
        if log['anomaly'] == 'Anomaly':
            send_alert('admin@example.com', 'Anomaly Detected', f"Anomaly detected at {log['timestamp']} with message: {log['message']}")
    
    # Visualize the anomalies
    plot_anomalies(logs_with_anomalies)

if __name__ == '__main__':
    main()