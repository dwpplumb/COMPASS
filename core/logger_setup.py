import logging
import os

def setup_logger(name='COMPASS', log_file='logs/compass.log', level=logging.DEBUG):
    """
    Setzt einen Logger auf, der alle Logeinträge in eine Datei schreibt.
    :param name: Name des Loggers
    :param log_file: Pfad zur Logdatei
    :param level: Logging-Level
    :return: Logger-Instanz
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Verhindert doppelte Logeinträge
    if not logger.handlers:
        # Stelle sicher, dass das Verzeichnis existiert
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        # Erstellt einen FileHandler
        fh = logging.FileHandler(log_file, mode='a', encoding='utf-8')
        fh.setLevel(level)

        # Definiert das Log-Format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        # Fügt den Handler dem Logger hinzu
        logger.addHandler(fh)

    return logger
