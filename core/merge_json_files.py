import json

def merge_json_files(file_paths, output_path):
    """Liest mehrere JSON-Dateien und führt ihre Inhalte in einer neuen Datei zusammen.

    Args:
        file_paths (list): Eine Liste der Pfade zu den JSON-Dateien.
        output_path (str): Der Pfad für die Ausgabedatei.
    """
    merged_data = []  # Oder {} für ein Dictionary, je nach Struktur deiner Dateien

    for file_path in file_paths:
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                if isinstance(data, list):
                    merged_data.extend(data)
                elif isinstance(data, dict):
                    merged_data.append(data) # Oder merged_data.update(data), falls eindeutige Schlüssel
                else:
                    print(f"Warnung: Datei {file_path} enthält kein JSON-Objekt oder -Array.")
        except FileNotFoundError:
            print(f"Fehler: Datei {file_path} nicht gefunden.")
        except json.JSONDecodeError:
            print(f"Fehler: Datei {file_path} enthält kein gültiges JSON.")

    with open(output_path, 'w') as outfile:
        json.dump(merged_data, outfile, indent=2) # indent für bessere Lesbarkeit

# Beispielhafte Verwendung
file_paths = ['datei1.json', 'datei2.json', 'datei3.json']
output_path = 'merged_data.json'
merge_json_files(file_paths, output_path)