

# SecuTrace

SecuTrace is an incident tracking and analysis tool that visualizes security incidents, analyzes logs, helps detect anomalies, and generates real-time alerts.

## Features
- **Incident Timeline Visualization**
- **Cross-System Correlation**
- **Real-Time Alerts**
- **Anomaly Detection**
- **Impact Analysis**

## Installation

### Prerequisites:
- Python 3.x
- Git


### Step 1: Clone the repository
First, clone the repository to your local machine using the following command:

	```bash
	git clone https://github.com/your-username/SecuTrace.git
	cd SecuTrace
	```
### Step 2: Set up a virtual environment
It’s recommended to use a virtual environment for this project to manage dependencies.

1. Install `virtualenv` if you don’t have it already:

```bash
    pip install virtualenv
```

2. Create a new virtual environment:

```bash
    python -m venv venv
```

3. Activate the virtual environment:

    On Windows

	```bash
 	  venv\Scripts\activate
	```

    On Mac/Linux

	```bash
   	 source venv/bin/activate
 	```

### Step 3: Install dependencies
Install the required Python packages by running:

```bash
pip install -r requirements.txt
```

### Step 4: Verify the installation
After setting up the environment and installing dependencies, verify by testing the installation:

```bash
pytest tests/
```

## Usage

### Log Parsing
You can parse log data by calling the `process_logs()` function, which takes log data as input and returns structured data.

Example:

```python
from src.log_parser import process_logs
log_data = "2025-01-01T00:00:00 INFO Log message here"
logs = process_logs(log_data)
print(logs)
```

This will parse the given log data and output structured logs with timestamp, log level, and message.

### Anomaly Detection
To detect anomalies in log data, use the `detect_anomalies()` function. This function analyzes the logs and detects unusual patterns.

Example:

```python
from src.anomaly_detection import detect_anomalies

log_data = ["2025-01-01T00:00:00 INFO Log message here"]
anomalies = detect_anomalies(log_data)
print(anomalies)
```

### Configuration Validation
To make sure the configuration file is valid, call the `load_config()` function. This function loads the configuration from a JSON file and validates it according to the defined schema.

Example:

```python
from src.utils import load_config

config = load_config('config/config.json')
```

This will load and validate the configuration file (`config/config.json`).

## Configuration File Format
The configuration file (`config/config.json`) must contain the following fields:

```json
{
 "log_file_path": "/path/to/logfile.log",
 "log_level": "INFO",
 "schema_file_path": "/path/to/schema.json"
}
```

Ensure that the paths provided for `log_file_path` and `schema_file_path` are correct, and that the `log_level` is one of the accepted log levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).

## Running Tests
You can run all tests to ensure that everything is functioning as expected:

```bash
pytest tests/
```

This will run all the tests in the tests folder. You can also run tests for a specific module like this:

```bash
pytest tests/test_log_parser.py
```
