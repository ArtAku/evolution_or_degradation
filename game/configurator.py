from environs import Env

# https://pypi.org/project/environs/
env = Env()
env.read_env()  # read .env file, if it exists

logger_config = {
    "FILE_LOG_LEVEL": env.log_level("FILE_LOG_LEVEL", "ERROR"),
    "CONSOLE_LOG_LEVEL": env.log_level("CONSOLE_LOG_LEVEL", "DEBUG"),
    "FILE_LOG_NAME": env.str("FILE_LOG_NAME", "file.log"),
}

redis_config = {
    "REDIS_HOST": env("REDIS_HOST", "localhost"),
    "REDIS_PORT": env.int("REDIS_PORT", 5000)
}
