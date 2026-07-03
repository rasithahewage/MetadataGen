from langchain_ollama import ChatOllama
from app.llm_support.template_builder import create_template
from langchain_core.output_parsers import StrOutputParser
from app.helper.load_config import load_llm_config


def execute_chain(query: str, framework: str) -> str | None:
    """
    Executes a langchain to generate suggestions for keywords and an educational level
    of a given course. The basis for the suggestion are the course title and description.
    This is the integration for local models served via Ollama.

    :param query: The title and the description of the course combined into a single string.
    :type query: str
    :param framework: The framework for which the educational level suggestion is made.
    :type framework: str
    :return: The suggested educational level and keywords for the course.
    :rtype: str
    """
    prompt_template = create_template(framework)

    model_name = load_llm_config()["OLLAMA"]
    base_url = load_llm_config().get("OLLAMA_BASE_URL", "http://localhost:11434")

    try:
        model = ChatOllama(
            model=model_name,
            base_url=base_url,
            temperature=0,
            think=False,  # avoid <think>...</think> reasoning traces polluting parsed output
        )

        chain = prompt_template | model | StrOutputParser()

        return chain.invoke({"query": query})
    except Exception as e:
        print(e)
        print("Ollama request failed! Skipping keywords and educational level suggestion...")
        return None
