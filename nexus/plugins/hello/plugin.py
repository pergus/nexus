from core.plugins.base import PluginConfig


class HelloPluginConfig(PluginConfig):
    name = "plugins.hello"
    verbose_name = "Hello Plugin"
    description = "Example plugin"
    version = "1.0"
    base_url = "hello"
    group = "Utilities"



