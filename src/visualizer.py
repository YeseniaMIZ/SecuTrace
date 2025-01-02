# src/visualizer.py
import matplotlib.pyplot as plt

def visualize_timeline(events):
    """Visualize incident timeline."""
    timestamps = [event['timestamp'] for event in events]
    event_types = [event['type'] for event in events]

    plt.plot(timestamps, event_types)
    plt.xlabel('Timestamp')
    plt.ylabel('Event Type')
    plt.title('Incident Timeline')
    plt.show()