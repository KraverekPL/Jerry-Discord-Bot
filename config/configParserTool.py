import configparser

# Initialization of config parser
configParserForPublicConfig = configparser.ConfigParser()
configParserForSensitiveConfig = configparser.ConfigParser()

# Load config files
configParserForPublicConfig.read("./config/public_config.ini")
configParserForSensitiveConfig.read("./config/sensitive_config.ini")


# Sensitive data
botToken = configParserForSensitiveConfig.get('DEFAULT', 'BOT_TOKEN', fallback='No key')

# Public config
logLevel = configParserForPublicConfig.get('DEFAULT', 'log_level', fallback='No key')
