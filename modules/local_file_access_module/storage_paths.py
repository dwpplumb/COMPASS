import os
from datetime import datetime

# Basisverzeichnis von COMPASS
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SSD- und HDD-Verzeichnisse (symbolische Verknüpfungen)
SSD_DIR = os.path.join(BASE_DIR, 'ssd')
HDD_DIR = os.path.join(BASE_DIR, 'hdd')

# Fallback-Verzeichnis im BASE_DIR
FALLBACK_DIR = os.path.join(BASE_DIR, 'fallback_logs')

# Unterverzeichnisse
MODELS_DIR = os.path.join(SSD_DIR, 'models')
RUNTIME_DIR = os.path.join(SSD_DIR, 'runtime')
CONFIG_DIR = os.path.join(SSD_DIR, 'config')
ARCHIVE_DIR = os.path.join(HDD_DIR, 'archive')
BACKUP_DIR = os.path.join(HDD_DIR, 'backups')
LOG_DIR = os.path.join(HDD_DIR, 'logs')
DATA_DIR = os.path.join(HDD_DIR, 'data')
CMB_RAW_DIR = os.path.join(DATA_DIR, 'cmb', 'raw')
CMB_PROCESSED_DIR = os.path.join(DATA_DIR, 'cmb', 'processed')
CMB_META_DIR = os.path.join(DATA_DIR, 'cmb', 'meta')
DATABASE_DIR = os.path.join(HDD_DIR, 'db')  # zukünftige Datenbankablage
ONLINE_CACHE_DIR = os.path.join(HDD_DIR, 'webcache')  # ggf. temporäre Onlinedaten



def ensure_directory(path):
    """Stellt sicher, dass das Verzeichnis existiert."""
    os.makedirs(path, exist_ok=True)

def get_model_path(model_name):
    path = os.path.join(MODELS_DIR, model_name)
    if os.path.exists(path):
        return path
    else:
        log_fallback(f"Modellpfad nicht gefunden: {path}")
        return None

def get_runtime_file_path(file_name):
    path = os.path.join(RUNTIME_DIR, file_name)
    if os.path.exists(path):
        return path
    else:
        log_fallback(f"Laufzeitdatei nicht gefunden: {path}")
        return None

def get_archive_file_path(file_name):
    path = os.path.join(ARCHIVE_DIR, file_name)
    if os.path.exists(path):
        return path
    else:
        log_fallback(f"Archivdatei nicht gefunden: {path}")
        return None

def get_backup_file_path(file_name):
    path = os.path.join(BACKUP_DIR, file_name)
    if os.path.exists(path):
        return path
    else:
        log_fallback(f"Sicherungsdatei nicht gefunden: {path}")
        return None

def log_fallback(message):
    """Schreibt eine Nachricht in das Fallback-Protokoll."""
    ensure_directory(FALLBACK_DIR)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = os.path.join(FALLBACK_DIR, f"fallback_{timestamp}.log")
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"{timestamp} - {message}\n")

def get_daily_log_dir():
    today = datetime.now().strftime('%Y-%m-%d')
    path = os.path.join(RUNTIME_DIR, 'logs', today)
    ensure_directory(path)
    return path