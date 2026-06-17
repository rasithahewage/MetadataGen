from app.llm_support import gemini_chain, claude_chain
from app.helper.load_config import load_llm_config


def get_chain_by_config():
    model_family = load_llm_config()["ACTIVE"]

    chains = {
        "GEMINI": gemini_chain,
        "CLAUDE": claude_chain
    }

    return chains[model_family]
