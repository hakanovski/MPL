"""
src/resolver.py
====================================
The Ontology Resolver (The Librarian).
Responsible for loading both the 'Magi Master List' and 'Solomonic Key'.
"""

import json
import os
import re
from typing import Dict, Any, Optional

class OntologyError(Exception):
    """Raised when knowledge cannot be found."""
    pass

class Resolver:
    def __init__(self, magi_path: str = "data/MAGI_225.json", solomon_path: str = "data/72_solomon_sigil_shapes.json"):
        self.knowledge_base: Dict[str, Any] = {}
        
        # Load the Historical Magi (Human Spirits)
        self._load_magi(magi_path)
        
        # Load the Goetia (Daemons)
        self._load_solomon(solomon_path)

    def _load_magi(self, path):
        if not os.path.exists(path):
            print(f"⚠️ Warning: Magi file '{path}' not found.")
            return

        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if "categories" in data:
                    for category in data["categories"]:
                        for magus in category.get("magi", []):
                            full_name = magus.get("name", "")
                            if not full_name: continue

                            # ID Generation: "Hermes Trismegistus" -> "hermes"
                            first_word = full_name.split(' ')[0].lower()
                            full_slug = re.sub(r'[^a-zA-Z0-9]', '_', full_name.lower())
                            
                            magus["_type"] = "MAGUS"
                            self.knowledge_base[first_word] = magus
                            self.knowledge_base[full_slug] = magus
            print(f"📚 Magi Loaded.")
        except Exception as e:
            print(f"⚠️ Magi Error: {e}")

    def _load_solomon(self, path):
        if not os.path.exists(path):
            print(f"⚠️ Warning: Solomon file '{path}' not found.")
            return

        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if "entities" in data:
                    for entity in data["entities"]:
                        # ID Generation: "Bael" -> "bael"
                        name = entity.get("name", "").lower()
                        # Clean up name (remove numbering like '001_')
                        clean_name = name.split('_')[-1] if '_' in name else name
                        
                        entity["_type"] = "DAEMON"
                        self.knowledge_base[clean_name] = entity
                        self.knowledge_base[entity.get("id")] = entity
            print(f"👹 Goetia Loaded.")
        except Exception as e:
            print(f"⚠️ Goetia Error: {e}")

    def resolve(self, entity_id: str) -> Optional[Dict[str, Any]]:
        if not entity_id: return None
        return self.knowledge_base.get(entity_id.lower())
