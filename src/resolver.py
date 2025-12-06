"""
src/resolver.py
====================================
The Ontology Resolver (The Librarian).
Responsible for loading the 'Ultra Master List' (JSON) 
and flattening the categories so the Interpreter can invoke Magicians by name.
"""

import json
import os
import re
from typing import Dict, Any, Optional

class OntologyError(Exception):
    """Raised when knowledge cannot be found."""
    pass

class Resolver:
    def __init__(self, data_path: str = "data/magi_225.json"):
        self.data_path = data_path
        self.knowledge_base: Dict[str, Any] = {}
        self._load_ontology()

    def _load_ontology(self):
        """
        Loads the complex JSON Grimoire (Categories -> Magi).
        It flattens the structure so we can search by simple IDs.
        Example: "Hermes Trismegistus" becomes ID "hermes".
        """
        if not os.path.exists(self.data_path):
            print(f"⚠️ Warning: Ontology file '{self.data_path}' not found. The engine is blind.")
            return

        try:
            with open(self.data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # Navigate through Categories to find Magi
                if "categories" in data:
                    for category in data["categories"]:
                        cat_name = category.get("name", "Unknown")
                        
                        for magus in category.get("magi", []):
                            # We need a Key (ID) to invoke them.
                            # Logic: Take the first word of the name, lowercase it.
                            # "Hermes Trismegistus" -> "hermes"
                            # "King Solomon" -> "solomon"
                            full_name = magus.get("name", "")
                            
                            if not full_name:
                                continue

                            # 1. Generate ID from First Name (Simple invoke)
                            first_word = full_name.split(' ')[0].lower()
                            
                            # Inject extra metadata (So we know where they came from)
                            magus["_category"] = cat_name
                            
                            # Store in memory by First Name (e.g., 'hermes')
                            # Note: If two magi have the same first name, the last one loaded wins.
                            # Ideally, we would handle collisions, but for v0.1 this is fine.
                            self.knowledge_base[first_word] = magus
                            
                            # 2. Also store by Full Slug (Precise invoke)
                            # "Hermes Trismegistus" -> "hermes_trismegistus"
                            full_slug = re.sub(r'[^a-zA-Z0-9]', '_', full_name.lower())
                            self.knowledge_base[full_slug] = magus

            # debug line (uncomment to see count)
            # print(f"📚 Ontology Loaded: {len(self.knowledge_base)} spirits ready.")
            
        except json.JSONDecodeError:
            print("❌ The Grimoire (JSON) is corrupted or invalid format.")
        except Exception as e:
            print(f"⚠️ Ontology Error: {e}")

    def resolve(self, entity_id: str) -> Optional[Dict[str, Any]]:
        """
        Queries the knowledge base.
        Usage: resolve("hermes") or resolve("tesla")
        """
        if not entity_id:
            return None
        return self.knowledge_base.get(entity_id.lower())

    def get_attribute(self, entity_id: str, attr: str) -> Any:
        entity = self.resolve(entity_id)
        if not entity:
            raise OntologyError(f"Entity '{entity_id}' is unknown.")
        
        # Check standard fields
        if attr in entity:
            return entity[attr]
            
        raise OntologyError(f"Entity '{entity_id}' does not possess attribute '{attr}'.")
