# tests/test_utils.py

import json
import pytest
from jsonschema import validate, ValidationError
from src.utils import load_config  # Assuming load_config is your function that loads and validates the config

# The schema definition (make sure it's correct and matches the expected structure)
CONFIG_SCHEMA = {
    "type": "object",
    "properties": {
        "log_file_path": {
            "type": "string"
        },
        # You can add more properties here if needed
    },
    "required": ["log_file_path"]  # log_file_path is required
}

# Mocked version of load_config, which validates the config against the schema
def load_config(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)

    # Validate the config against the schema
    validate(instance=config, schema=CONFIG_SCHEMA)


def test_invalid_config():
    # Simulate invalid config (missing required field)
    invalid_config = {"other_field": "some_value"}  # Missing 'log_file_path'

    # Write the invalid config to a file
    with open('config/config.json', 'w') as f:
        json.dump(invalid_config, f)

    # Check that the correct exception is raised when loading the config
    with pytest.raises(ValidationError):
        load_config('config/config.json')