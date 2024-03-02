import os
import configparser

# Initialization of config parser
configParserForPublicConfig = configparser.ConfigParser()
configParserForSensitiveConfig = configparser.ConfigParser()

# Paths to config files
public_config_path = "./config/public_config.ini"
sensitive_config_path = "./config/sensitive_config.ini"

# Check if config files exist
if not os.path.isfile(public_config_path) or not os.path.isfile(sensitive_config_path):
    raise FileNotFoundError("One or both configuration files not found.")

# Load config files
configParserForPublicConfig.read(public_config_path)
configParserForSensitiveConfig.read(sensitive_config_path)

# Sensitive data
bot_token = configParserForSensitiveConfig.get('DEFAULT', 'BOT_TOKEN', fallback='')

# Public config
log_level = configParserForPublicConfig.get('DEFAULT', 'log_level', fallback='INFO')
url_tree_repo = configParserForPublicConfig.get('DEFAULT', 'url_tree_images_repository', fallback='')
class_parameter_value = configParserForPublicConfig.get('DEFAULT', 'class_parameter_value', fallback='')