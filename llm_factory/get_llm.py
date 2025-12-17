from llama_index.llms.groq import Groq
from config.settings import Settings

settings = Settings()
GROQ_API_KEY = settings.GROQ_API_KEY

# Module-level cache for model and instance
_current_model_name = None
_current_llm_instance = None


def get_groq_llm(model_name: str):
    global _current_model_name, _current_llm_instance
    if _current_model_name == model_name and _current_llm_instance is not None:
        return _current_llm_instance
    llm = Groq(model=model_name, api_key=GROQ_API_KEY)
    _current_model_name = model_name
    _current_llm_instance = llm
    return llm


# Example usage
# check_llm = get_groq_llm(model_name="llama3-8b-8192")
# print(check_llm)
# print(type(check_llm))
