import matplotlib.pyplot as plt

def plot_anomalies(logs):
    """
    Plots anomalies in the logs.
    """
    timestamps = [log['timestamp'] for log in logs]
    anomalies = [log['anomaly'] == 'Anomaly' for log in logs]
    
    plt.figure(figsize=(10, 6))
    plt.scatter(timestamps, anomalies, color='red' if anomalies else 'blue', label="Anomalies")
    plt.xlabel('Timestamp')
    plt.ylabel('Anomaly Detected')
    plt.title('Log Anomalies Detection')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()