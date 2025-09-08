import os

class Logger:
    
    PREFIX = "LOG"
    enabled = os.environ.get("LOG_ENABLED", "0") == "1"

    @staticmethod
    def info(message: str):
        if Logger.enabled:
            print(f"[INFO] {Logger.PREFIX}: {message}")