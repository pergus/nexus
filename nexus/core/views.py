from django.shortcuts import render
from core.plugin_loader import get_plugin_configs

def portal(request):
    plugins = get_plugin_configs()
    return render(request, "core/portal.html", { "plugins": plugins })


from django.urls import URLResolver, URLPattern, resolve
from django.http import Http404
from importlib import import_module
from django.conf import settings
from django.template import engines

def plugin_dispatch(request, plugin_name, path):
    try:
        module_urls = import_module(f"plugins.{plugin_name}.urls")
        urlpatterns = getattr(module_urls, "urlpatterns", [])
    except ModuleNotFoundError:
        raise Http404(f"No such plugin: {plugin_name}")

    # Dynamically add the plugin's templates folder to Django engines
    plugin_templates_dir = settings.BASE_DIR / "plugins" / plugin_name / "templates"
    str_dir = str(plugin_templates_dir)
    for engine in engines.all():
        if str_dir not in engine.dirs:
            engine.dirs.insert(0, str_dir)

    # Find the first matching view for the remaining path
    for pattern in urlpatterns:
        if isinstance(pattern, URLPattern):
            match = pattern.resolve(path)
            if match:
                return pattern.callback(request, **match.kwargs)
        elif isinstance(pattern, URLResolver):
            match = pattern.resolve(path)
            if match:
                return match.func(request, **match.kwargs)

    raise Http404(f"No view matches {path} in plugin {plugin_name}")
