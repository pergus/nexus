from django.shortcuts import render
from core.plugin_loader import get_plugin_configs

def index(request):
    plugin = next(p for p in get_plugin_configs() if p.base_url == "demo1")
    return render(request, "demo1/index.html", {"plugin": plugin})
