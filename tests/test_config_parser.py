import pytest
from src.config_parser import parse_config

def test_parse_yaml():
    config = parse_config('configs/sample_config.yaml')
    assert isinstance(config, dict)
    assert 'network' in config

def test_parse_json():
    config = parse_config('configs/sample_config.json')
    assert isinstance(config, dict)
