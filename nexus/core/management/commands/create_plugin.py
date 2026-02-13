import os
from django.core.management.base import BaseCommand

TEMPLATE_PLUGIN = """\
from core.plugins.base import PluginConfig

class {PluginClass}PluginConfig(PluginConfig):
    name = "plugins.{plugin_name}"
    base_url = "{plugin_name}"
    verbose_name = "{plugin_verbose_name}"
    description = "{plugin_description}"
"""

TEMPLATE_URLS = """\
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="{plugin_name}_index"),
]
"""

TEMPLATE_VIEWS = """\
from django.shortcuts import render
from core.plugin_loader import get_plugin_configs

def index(request):
    plugin = next(p for p in get_plugin_configs() if p.base_url == "{plugin_name}")
    return render(request, "{plugin_name}/index.html", {{"plugin": plugin}})
"""

TEMPLATE_INDEX_HTML = """\
{% extends "base.html" %}

{% block title %}{{ plugin.verbose_name }}{% endblock %}

{% block content %}
<h1>{{ plugin.verbose_name }}</h1>
<p>{{ plugin.description }}</p>
{% endblock %}
"""

TEMPLATE_INIT = ""

class Command(BaseCommand):
    help = "Create a new plugin scaffold"

    def add_arguments(self, parser):
        parser.add_argument("plugin_name", type=str, help="Plugin folder name")
        parser.add_argument("verbose_name", nargs="?", type=str, help="Plugin verbose name")
        parser.add_argument("description", nargs="?", type=str, help="Plugin description")

    def handle(self, *args, **options):
        plugin_name = options["plugin_name"].lower()
        verbose_name = options.get("verbose_name") or plugin_name.title()
        description = options.get("description") or f"{verbose_name} plugin"

        base_dir = os.path.join(os.getcwd(), "plugins", plugin_name)
        os.makedirs(base_dir, exist_ok=True)

        # Create files
        files = {
            "__init__.py": TEMPLATE_INIT,
            "plugin.py": TEMPLATE_PLUGIN.format(
                PluginClass=plugin_name.title().replace("_", ""),
                plugin_name=plugin_name,
                plugin_verbose_name=verbose_name,
                plugin_description=description
            ),
            "urls.py": TEMPLATE_URLS.format(plugin_name=plugin_name),
            "views.py": TEMPLATE_VIEWS.format(plugin_name=plugin_name),
        }

        # Create templates folder
        templates_dir = os.path.join(base_dir, "templates", plugin_name)
        os.makedirs(templates_dir, exist_ok=True)
        with open(os.path.join(templates_dir, "index.html"), "w") as f:
            f.write(TEMPLATE_INDEX_HTML)

        # Write files
        for filename, content in files.items():
            path = os.path.join(base_dir, filename)
            with open(path, "w") as f:
                f.write(content)

        self.stdout.write(self.style.SUCCESS(f"Plugin '{plugin_name}' created successfully at {base_dir}"))

