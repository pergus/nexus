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


def all_components_demo(request):
    # Sample data for breadcrumb
    breadcrumb_items = [
        {'text': 'Home', 'url': '/'},
        {'text': 'Library', 'url': '/library/'},
        {'text': 'Data', 'active': True}
    ]

    context = {
        'breadcrumb_items': breadcrumb_items,
    }

    return render(request, 'components_app/all_components_demo.html', context)