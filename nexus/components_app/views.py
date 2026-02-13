from django.shortcuts import render

def demo_components(request):
    # Sample data for button group
    button_groups = [
        {
            'buttons': [
                {'text': 'Left', 'type': 'light'},
                {'text': 'Middle', 'type': 'light'},
                {'text': 'Right', 'type': 'light'},
            ]
        },
        {
            'buttons': [
                {'text': '1', 'type': 'light'},
                {'text': '2', 'type': 'light'},
                {'text': '3', 'type': 'secondary'},
                {'text': '4', 'type': 'light'},
            ]
        }
    ]

    # Sample data for dropdown button group
    dropdown_group = [
        {
            'buttons': [
                {'text': '5', 'type': 'light'},
                {'text': '6', 'type': 'secondary'},
                {'text': '7', 'type': 'light'},
                {'text': 'Dropdown', 'type': 'light', 'dropdown': True, 'id': 'sampleDropdown',
                 'dropdown_items': [
                     {'text': 'Dropdown link 1', 'href': '#'},
                     {'text': 'Dropdown link 2', 'href': '#'},
                 ]},
            ]
        }
    ]

    context = {
        'button_groups': button_groups,
        'dropdown_group': dropdown_group,
    }

    return render(request, 'components_app/demo.html', context)


def dashboard(request):
    """Dashboard view - main landing page"""
    context = {
        'page_title': 'Dashboard',
    }
    return render(request, 'components_app/dashboard.html', context)


def all_components_demo(request):
    # Sample data for breadcrumb
    breadcrumb_items = [
        {'text': 'Home', 'url': '/components_app/'},
        {'text': 'Components', 'url': '/components_app/all-components-demo/'},
        {'text': 'UI Components', 'active': True}
    ]

    # Sample data for sidebar menu - using actual working URLs
    sidebar_menu_items = [
        {
            'title': 'Components',
            'items': [
                {
                    'title': 'Dashboard',
                    'url': '/components_app/',
                    'icon': 'mingcute:home-3-line'
                },
                {
                    'title': 'UI Components',
                    'url': '/components_app/all-components-demo/',
                    'icon': 'mingcute:box-line',
                    'is_active': True
                },
                {
                    'title': 'Sidebar Demo',
                    'url': '/components_app/sidebar-demo/',
                    'icon': 'mingcute:menu-line'
                },
                {
                    'title': 'Forms',
                    'id': 'forms-menu',
                    'icon': 'mingcute:form-line',
                    'children': [
                        {'title': 'Basic Forms', 'url': '/components_app/forms/basic/'},
                        {'title': 'Advanced Forms', 'url': '/components_app/forms/advanced/'},
                        {'title': 'Validation', 'url': '/components_app/forms/validation/'}
                    ]
                },
                {
                    'title': 'Charts',
                    'url': '/components_app/charts/',
                    'icon': 'mingcute:chart-line',
                    'badge_text': 'New',
                    'badge_color': 'primary'
                },
                {
                    'title': 'Tables',
                    'id': 'tables-menu',
                    'icon': 'mingcute:table-line',
                    'children': [
                        {'title': 'Basic Tables', 'url': '/components_app/tables/basic/'},
                        {'title': 'Data Tables', 'url': '/components_app/tables/data/'}
                    ]
                }
            ]
        },
        {
            'title': 'Maps',
            'items': [
                {
                    'title': 'Google Maps',
                    'url': '/components_app/maps/google/',
                    'icon': 'mingcute:map-pin-line'
                },
                {
                    'title': 'Vector Maps',
                    'url': '/components_app/maps/vector/',
                    'icon': 'mingcute:map-2-line'
                }
            ]
        }
    ]

    context = {
        'breadcrumb_items': breadcrumb_items,
        'app_menu_items': sidebar_menu_items,
    }

    return render(request, 'components_app/all_components_demo.html', context)


def sidebar_demo(request):
    # Sample data for sidebar menu
    sidebar_menu_items = [
        {
            'title': 'Demo Menu',
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
                    'title': 'Components',
                    'id': 'components-menu',
                    'icon': 'mingcute:box-line',
                    'is_expanded': True,
                    'children': [
                        {'title': 'Buttons', 'url': '/components_app/all-components-demo/'},
                        {'title': 'Cards', 'url': '/components_app/all-components-demo/'},
                        {'title': 'Forms', 'url': '/components_app/all-components-demo/'}
                    ]
                },
                {
                    'title': 'Pages',
                    'id': 'pages-menu',
                    'icon': 'mingcute:document-line',
                    'children': [
                        {'title': 'Profile', 'url': '/components_app/all-components-demo/'},
                        {'title': 'Settings', 'url': '/components_app/all-components-demo/'},
                        {'title': 'Help', 'url': '/components_app/all-components-demo/'}
                    ]
                },
                {
                    'title': 'External Link',
                    'url': 'https://example.com',
                    'icon': 'mingcute:external-link-line',
                    'badge_text': 'New',
                    'badge_color': 'success'
                }
            ]
        }
    ]

    context = {
        'app_menu_items': sidebar_menu_items,
    }

    return render(request, 'components_app/sidebar_demo.html', context)


def google_maps_demo(request):
    """Google Maps demo view"""
    context = {
        'page_title': 'Google Maps',
    }
    return render(request, 'components_app/maps_demo.html', context)


def vector_maps_demo(request):
    """Vector Maps demo view"""
    context = {
        'page_title': 'Vector Maps',
    }
    return render(request, 'components_app/maps_demo.html', context)


def charts_demo(request):
    """Charts demo view"""
    context = {
        'page_title': 'Charts',
    }
    return render(request, 'components_app/charts_demo.html', context)


def basic_tables_demo(request):
    """Basic Tables demo view"""
    context = {
        'page_title': 'Basic Tables',
    }
    return render(request, 'components_app/tables_demo.html', context)


def data_tables_demo(request):
    """Data Tables demo view"""
    context = {
        'page_title': 'Data Tables',
    }
    return render(request, 'components_app/tables_demo.html', context)


def basic_forms_demo(request):
    """Basic Forms demo view"""
    context = {
        'page_title': 'Basic Forms',
    }
    return render(request, 'components_app/forms_demo.html', context)


def advanced_forms_demo(request):
    """Advanced Forms demo view"""
    context = {
        'page_title': 'Advanced Forms',
    }
    return render(request, 'components_app/forms_demo.html', context)


def validation_forms_demo(request):
    """Validation Forms demo view"""
    context = {
        'page_title': 'Validation Forms',
    }
    return render(request, 'components_app/forms_demo.html', context)