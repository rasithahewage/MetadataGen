from yaml import load, CLoader
from .paths import FRAMEWORK_ROOT, SUGGESTION_ENGINE_CONF, LLM_CONF


def load_framework_conf(framework: str, group: str) -> dict:
    """
    Reads teh configuration file of a framework and returns the variables and values as a dictionary.

    :param framework: The framework the config is for.
    :type: str
    :param group: The group (attribute) the framework is for (e.g. teaches, educationalAlignment,...).
    :type group: str
    :return: The conf in the form of a dictionary.
    :rtype: dict
    """

    path = (
        FRAMEWORK_ROOT /
        group /
        framework /
        "conf.yml"
    )

    with open(path, 'r') as f:
        return load(f.read(), Loader=CLoader)


def load_suggestion_engine_conf() -> dict:
    with open(SUGGESTION_ENGINE_CONF, 'r') as f:
        return load(f.read(), Loader=CLoader)


def load_llm_config() -> dict:
    with open(LLM_CONF, 'r') as f:
        return load(f.read(), Loader=CLoader)
