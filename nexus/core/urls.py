from django.conf import settings
from django.urls import include, path
from core.plugin_loader import get_plugin_configs
from core import views


urlpatterns = [
    path("portal/", views.portal, name="portal"),
]


# Load Plugins
for plugin in get_plugin_configs():
    if plugin.base_url:
        try:
            urlpatterns.append(
                path(
                    f"plugins/{plugin.base_url}/",
                    include(f"{plugin.name}.urls")
                )
            )
        except ModuleNotFoundError:
            pass

