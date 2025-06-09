import os
import importlib.util
from modules.language_model.language_grounding import local_semantic_search

# Statuscaching für Module
_availability = {}

def is_module_available(module_name):
    if module_name in _availability:
        return _availability[module_name]
    try:
        spec = importlib.util.find_spec(module_name)
        _availability[module_name] = spec is not None
        return spec is not None
    except Exception:
        _availability[module_name] = False
        return False

def get_active_semantic_backend() -> str:
    # 1. Mistral-API erreichbar?
    if is_module_available("modules.language_model.language_mistral_interface"):
        try:
            from modules.language_model.language_mistral_interface import test_mistral_connection
            if test_mistral_connection():
                return "mistral"
        except Exception:
            pass

    # 2. OpenAI-Key gesetzt?
    if os.getenv("OPENAI_API_KEY"):
        try:
            import openai
            openai.Model.list()  # Testverbindung
            return "openai"
        except Exception:
            pass

    # 3. Fallback: Lokale Embeddings
    return "local"
