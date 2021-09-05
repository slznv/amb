import os


LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
LOG_AS_JSON = bool(int(os.environ.get("LOG_AS_JSON", 0)))

STORAGE = "IN_MEMORY"
