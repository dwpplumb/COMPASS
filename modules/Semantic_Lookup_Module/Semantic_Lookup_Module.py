Semantic_Lookup_Module### semantic_lookup_module.py
"""
Dieses Modul ermöglicht semantisches Lookup auf Basis vorstrukturierter Lösungsräume.
Es wurde ursprünglich für Sudoku entworfen, ist aber generalisierbar für jede Problemklasse,
deren Lösung durch Transformation, Hashing oder Signaturbildung vorab klassifizierbar ist.
Kompatibel mit dem COMPASS-System.
"""

from typing import Any, Dict, Optional
import hashlib
import json
import os

class SemanticLookup:
    def __init__(self, db_path: str):
        """Initialisiert das Lookup-Modul mit Pfad zur vorbereiteten Datenbank."""
        self.db_path = db_path
        self.index = self._load_index()

    def _load_index(self) -> Dict[str, str]:
        """Lädt die Hashmap der Schlüssel zur Datenbankdatei."""
        index_file = os.path.join(self.db_path, "index.json")
        if os.path.exists(index_file):
            with open(index_file, "r") as f:
                return json.load(f)
        return {}

    def _compute_hash(self, input_data: str) -> str:
        """Erzeugt einen stabilen SHA256-Hash für die Eingabe."""
        return hashlib.sha256(input_data.encode("utf-8")).hexdigest()

    def query(self, input_data: str) -> Optional[Dict[str, Any]]:
        """Fragt die Lösung oder Bewertung zur Eingabe ab."""
        h = self._compute_hash(input_data)
        if h in self.index:
            entry_file = os.path.join(self.db_path, self.index[h])
            with open(entry_file, "r") as f:
                return json.load(f)
        return None

    def insert(self, input_data: str, solution: Any, metadata: Dict[str, Any]) -> None:
        """Fügt eine neue Lösung mit Zusatzdaten in die Datenbank ein."""
        h = self._compute_hash(input_data)
        file_name = f"{h}.json"
        self.index[h] = file_name
        entry_path = os.path.join(self.db_path, file_name)
        with open(entry_path, "w") as f:
            json.dump({
                "input": input_data,
                "solution": solution,
                "metadata": metadata
            }, f, indent=2)
        # Aktualisiere Index
        with open(os.path.join(self.db_path, "index.json"), "w") as f:
            json.dump(self.index, f, indent=2)


# Beispielhafte Nutzung für Sudoku
if __name__ == "__main__":
    sl = SemanticLookup("sudoku_lookup_db")
    puzzle = "...26.7.168..7..9.19...45....1...3...8.2...6...3...5....61...93.5..4..2.7.9."

    result = sl.query(puzzle)
    if result:
        print("Lösung gefunden:", result["solution"])
    else:
        print("Nicht gefunden. Lösung berechnen und speichern...")
        # Beispiel-Lösung + Bewertung einfügen (hier simuliert)
        solved = "435269718682571493197834562....."  # etc.
        sl.insert(puzzle, solved, {
            "entropy": 1.32,
            "connection_value": 0.87,
            "reconfig_cost": 3,
            "compass_signature": [1.0, 0.8, 0.2, 0.4]
        })
