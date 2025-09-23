import os

class Logger:
    
    PREFIX = "LOG"
    enabled = os.environ.get("LOG_ENABLED", "0") == "1"

    COLORS = {
        "INFO": "\033[94m",    # B
        "WARN": "\033[93m",    # Y
        "ERROR": "\033[91m",   # R
        "VERBOSE": "\033[97m", # White
        "RESET": "\033[0m",
    }

    @staticmethod
    def info(message: str):
        if Logger.enabled:
            print(f"{Logger.COLORS['INFO']}[INFO] {Logger.PREFIX}: {message}{Logger.COLORS['RESET']}")

    @staticmethod
    def warn(message: str):
        if Logger.enabled:
            print(f"{Logger.COLORS['WARN']}[WARN] {Logger.PREFIX}: {message}{Logger.COLORS['RESET']}")

    @staticmethod
    def error(message: str):
        if Logger.enabled:
            print(f"{Logger.COLORS['ERROR']}[ERROR] {Logger.PREFIX}: {message}{Logger.COLORS['RESET']}")

    @staticmethod
    def verbose(message: str):
        if Logger.enabled:
            print(f"{Logger.Colors.WHITE}[VERBOSE] {Logger.PREFIX}: {message}{Logger.Colors.RESET}")
    