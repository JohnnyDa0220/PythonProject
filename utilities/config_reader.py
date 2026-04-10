import configparser
import os
from pathlib import Path

def get_config():
    """
    Read configuration from configproperties.ini
    Supports environment variable overrides
    """
    conf = configparser.ConfigParser()
    
    # Build path to config file (relative to project root)
    project_root = Path(__file__).parent.parent
    config_path = project_root / 'config' / 'configproperties.ini'
    
    conf.read(str(config_path))
    return conf

def get_properties(section, value):
    """
    Get property from config file with environment variable support
    Format: section_value (e.g., URL_website_url for environment variable)
    """
    config = get_config()
    
    # Check for environment variable first (e.g., URL_website_url)
    env_var = f"{section}_{value}".upper()
    if env_var in os.environ:
        return os.environ[env_var]
    
    # Fallback to config file
    data = config[section][value]
    return data

def get_config_path(file_type):
    """
    Get absolute path for log, screenshot, or other files
    Supports both relative and absolute paths
    """
    project_root = Path(__file__).parent.parent
    relative_path = get_properties("PATH", f"{file_type}_path")
    
    # Convert relative path to absolute
    full_path = project_root / relative_path
    full_path.mkdir(parents=True, exist_ok=True)
    
    return str(full_path)