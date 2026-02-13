"""
Context processors for the components app.
"""

def sidebar_menu_context(request):
    """
    Add default sidebar menu data to the context.
    This can be overridden by passing app_menu_items in the view context.
    """
    # Default menu structure - can be customized per application
    default_menu_items = [
        {
            'title': 'Main Menu',
            'items': [
                {
                    'title': 'Dashboard',
                    'url': '/components_app/',
                    'icon': 'mingcute:home-3-line'
                },
                {
                    'title': 'UI Components',
                    'url': '/components_app/all-components-demo/',
                    'icon': 'mingcute:box-line'
                },
                {
                    'title': 'Sidebar Demo',
                    'url': '/components_app/sidebar-demo/',
                    'icon': 'mingcute:menu-line'
                }
            ]
        }
    ]

    return {
        'default_menu_items': default_menu_items
    }