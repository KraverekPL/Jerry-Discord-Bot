import configparser

# Initialization of config parser
configParserForPublicConfig = configparser.ConfigParser()
configParserForSensitiveConfig = configparser.ConfigParser()

# Load config files
configParserForPublicConfig.read("./config/public_config.ini")
configParserForSensitiveConfig.read("./config/sensitive_config.ini")


# Sensitive data
bot_token = configParserForSensitiveConfig.get('DEFAULT', 'BOT_TOKEN')

# Public config
log_level = configParserForPublicConfig.get('DEFAULT', 'log_level')
url_tree_repo = configParserForPublicConfig.get('DEFAULT', 'url_tree_images_repository')
class_parameter_value = configParserForPublicConfig.get('DEFAULT', 'class_parameter_value')

