import os
import sys

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
    return render(request, "plugins/{plugin_name}/index.html", {"plugin": plugin})
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

def main():
    if len(sys.argv) < 2:
        print("Usage: python create_plugin.py <plugin_name> [verbose_name] [description]")
        sys.exit(1)

    plugin_name = sys.argv[1].lower()
    verbose_name = sys.argv[2] if len(sys.argv) > 2 else plugin_name.title()
    description = sys.argv[3] if len(sys.argv) > 3 else f"{verbose_name} plugin"

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

    print(f"Plugin '{plugin_name}' created successfully at {base_dir}")

if __name__ == "__main__":
    main()

