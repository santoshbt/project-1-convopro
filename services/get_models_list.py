from config.settings import Settings

settings = Settings()

def get_groq_models_list():
    models_list = settings.GROQ_MODELS  # str data type from .env file
    groq_models = [model.strip() for model in models_list.split(",") if model.strip()]
    return groq_models


# Example usage
# check_groq_models = get_groq_models_list()
# print(type(check_groq_models))
# print(check_groq_models)
