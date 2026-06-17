from pathlib import Path


APP_ROOT = Path(__file__).resolve().parent.parent

FRAMEWORK_ROOT = (
        APP_ROOT /
        "frameworks"
)

EMBEDDINGS_ROOT = (
    APP_ROOT /
    "embedding_models"
)

SUGGESTION_ENGINE_ROOT = (
    APP_ROOT /
    "suggestion_engine"
)

SUGGESTION_ENGINE_CONF = (
    SUGGESTION_ENGINE_ROOT /
    "conf.yml"
)

LLM_CONF = (
    APP_ROOT /
    "llm_support" /
    "conf.yml"
)
