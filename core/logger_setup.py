import logging
import os
from datetime import datetime

# Basisverzeichnis von COMPASS
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Fallback-Verzeichnis für Logs
FALLBACK_DIR = os.path.join(BASE_DIR, 'fallback_logs')
os.makedirs(FALLBACK_DIR, exist_ok=True)

def setup_logger(name: str, log_file: str = None, level=logging.INFO) -> logging.Logger:
    """
    Erstellt und konfiguriert einen Logger mit optionalem Dateihandler.
    Falls kein log_file angegeben ist, wird ein Fallback-Log im fallback_logs-Verzeichnis erstellt.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

    # Verhindert doppelte Handler
    if not logger.handlers:
        # StreamHandler für Konsolenausgabe
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        # FileHandler für Datei-Logging
        if log_file:
            log_path = os.path.join(BASE_DIR, log_file)
        else:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            log_path = os.path.join(FALLBACK_DIR, f"fallback_{timestamp}.log")

        file_handler = logging.FileHandler(log_path, encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
