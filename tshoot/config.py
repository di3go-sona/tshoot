import os

from dynaconf import Dynaconf, loaders
from dynaconf.utils.boxing import DynaBox
from InquirerPy import prompt

from .config_helper import get_settings_fields

SETTINGS_PATH = os.path.expanduser("~/.tshoot/settings.toml")
DEFAULT_SETTINGS_PATH = os.path.dirname(__file__) + "/settings.toml"


def write_settings(settings):
    """Write settings to disk."""
    os.makedirs(os.path.dirname(SETTINGS_PATH), exist_ok=True)
    open(SETTINGS_PATH, "a").close()
    os.chmod(SETTINGS_PATH, 0o600)
    loaders.write(SETTINGS_PATH, DynaBox(settings.as_dict()).to_dict())


def ask_settings(write=True):
    settings = Dynaconf(
        envvar_prefix="TSHOOT",
        # root_path=os.path.dirname(__file__),
        settings_files=[DEFAULT_SETTINGS_PATH, SETTINGS_PATH],
    )
    questions = get_settings_fields(settings)
    configuration = prompt(questions)

    settings.update(configuration)
    if write:
        write_settings(settings)
    return settings


def load_settings(ask=None):
    """Get the settings."""
    settings = Dynaconf(
        envvar_prefix="TSHOOT",
        # root_path=os.path.dirname(__file__),
        settings_files=[SETTINGS_PATH],
        DEFAULT_SETTINGS_PATH
    )

    required_settings_fields = [f["name"] for f in get_settings_fields()]
    present_settings_field = [settings.exists(f) for f in required_settings_fields]

    if ask or not all(present_settings_field):
        settings = ask_settings(write=True)

    return settings
