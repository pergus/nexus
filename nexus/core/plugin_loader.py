import os
import importlib
import inspect
from django.conf import settings
from core.plugins.base import PluginConfig

PLUGINS_DIR = settings.BASE_DIR / "plugins"

def get_plugin_configs():
    configs = []

    if not os.path.exists(PLUGINS_DIR):
        return configs

    # Scan each subfolder in plugins/
    for plugin_name in os.listdir(PLUGINS_DIR):
        plugin_path = PLUGINS_DIR / plugin_name

        if not plugin_path.is_dir():
            continue

        # Skip special folders
        if plugin_name.startswith("_"):
            continue

        # Only load folders containing plugin.py
        if not (plugin_path / "plugin.py").exists():
            continue

        try:
            module = importlib.import_module(f"plugins.{plugin_name}.plugin")

            for name, obj in inspect.getmembers(module, inspect.isclass):
                if issubclass(obj, PluginConfig) and obj is not PluginConfig:
                    configs.append(obj())

        except Exception as e:
            print(f"Failed loading plugin {plugin_name}: {e}")

    return configs

