from django.shortcuts import render
from core.plugin_loader import get_plugin_configs


def portal(request):
    plugins = get_plugin_configs()
    return render(request, "core/portal.html", { "plugins": plugins })

