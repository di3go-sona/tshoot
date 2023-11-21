import os

from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="TSHOOT",
    root_path=os.path.dirname(__file__),
    settings_files=['settings.toml', '.secrets.toml'],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
