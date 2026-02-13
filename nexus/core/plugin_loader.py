import inspect
import importlib
from django.conf import settings
from core.plugins.base import PluginConfig


def get_plugin_apps():
    return getattr(settings, "PLUGINS", [])


def get_plugin_configs_v1():
    configs = []

    for app in getattr(settings, "PLUGINS", []):
        try:
            module = importlib.import_module(f"{app}.plugin")
            for attr in dir(module):
                obj = getattr(module, attr)
                if hasattr(obj, "name"):
                    configs.append(obj())
        except Exception as e:
            print(f"Failed loading plugin config {app}: {e}")

    return configs

def get_plugin_configs():
    configs = []

    for app in getattr(settings, "PLUGINS", []):
        try:
            module = importlib.import_module(f"{app}.plugin")
            # inspect.getmembers returns (name, value) pairs
            for name, obj in inspect.getmembers(module, inspect.isclass):
                # Only include subclasses of PluginConfig defined in this module
                if issubclass(obj, PluginConfig) and obj is not PluginConfig:
                    configs.append(obj())
        except Exception as e:
            print(f"Failed loading plugin config {app}: {e}")

    return configs
