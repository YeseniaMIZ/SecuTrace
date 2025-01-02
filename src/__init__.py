# src/__init__.py

from .log_parser import parse_logs
from .anomaly_detection import detect_anomalies
from .alert_system import send_alert
from .visualizer import plot_anomalies

print("SecuTrace package has been initialized!")