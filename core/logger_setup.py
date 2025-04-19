import logging
import os
from datetime import datetime
from modules.local_file_access_module.storage_paths import RUNTIME_DIR

def setup_logger(name='COMPASS', level=logging.DEBUG):
    """
    Setzt einen Logger auf, der Logeinträge in ein tagesbasiertes Verzeichnis unter ssd/runtime/logs/YYYY-MM-DD schreibt.
    :param name: Name des Loggers
    :param level: Logging-Level
    :return: Logger-Instanz
    """
    today = datetime.now().strftime('%Y-%m-%d')
    log_dir = os.path.join(RUNTIME_DIR, 'logs', today)
    os.makedirs(log_dir, exist_ok=True)
    
    log_file = os.path.join(log_dir, f'{name.lower()}.log')
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Verhindert doppelte Logeinträge
    if not logger.handlers:
        fh = logging.FileHandler(log_file, mode='a', encoding='utf-8')
        fh.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger
