# Reusable UI Components

This directory contains reusable Django template components that can be used across different applications in the project.

## Available Components

### Button (`button.html`)

A flexible button component that can be used as a button or link.

**Usage:**
```django
{% include 'components/button.html' with type="primary" text="Click me" %}
```

**Parameters:**
- `type`: Button type (primary, secondary, success, danger, warning, info, light, dark) - default: primary
- `text`: Button text
- `href`: If provided, creates a link instead of a button
- `size`: Button size (sm, lg)
- `outline`: If True, creates an outline button
- `soft`: If True, creates a soft button
- `rounded`: If True, creates a rounded button
- `width`: Button width (xs, sm, md, lg, xl)
- `block`: If True, creates a block-level button
- `disabled`: If True, disables the button
- `icon`: Icon class to add to the button
- `submit`: If True, creates a submit button (only for button type)

### Alert (`alert.html`)

A flexible alert component with various styles and options.

**Usage:**
```django
{% include 'components/alert.html' with type="success" message="Operation completed!" dismissible=True %}
```

**Parameters:**
- `type`: Alert type (primary, secondary, success, danger, warning, info, light, dark) - default: primary
- `title`: Alert title (optional)
- `message`: Alert message
- `dismissible`: If True, adds a close button
- `icon`: Icon class to add to the alert

### Card (`card.html`)

A flexible card component with header, body, and footer.

**Usage:**
```django
{% include 'components/card.html' with title="Card Title" subtitle="Card Subtitle" %}
    {% block card_content %}
        <p>Card content goes here</p>
    {% endblock %}
{% endinclude %}
```

**Parameters:**
- `title`: Card title (optional)
- `subtitle`: Card subtitle (optional)
- `classes`: Additional CSS classes to add to the card
- `footer`: Card footer content (optional)

### Button Group (`button_group.html`)

A button group component for grouping buttons together.

**Usage:**
```django
{% include 'components/button_group.html' with buttons=button_list %}
```

**Parameters:**
- `buttons`: List of button dictionaries
- `vertical`: If True, creates a vertical button group
- `classes`: Additional CSS classes to add to the button group

## How to Use These Components

1. Include the component in your template:
   ```django
   {% include 'components/component_name.html' with parameter1=value1 parameter2=value2 %}
   ```

2. For components that accept content blocks (like card), use:
   ```django
   {% include 'components/card.html' with title="Card Title" %}
       {% block card_content %}
           <p>Your content here</p>
       {% endblock %}
   {% endinclude %}
   ```

## Creating New Components

When creating new components, follow these guidelines:

1. Place the component in the `templates/components/` directory
2. Use descriptive names for the component files
3. Document all parameters in comments at the top of the file
4. Provide usage examples in comments
5. Use default values where appropriate
6. Make components as flexible as possible
7. Follow the existing naming conventions

## Best Practices

1. Always use the `|default` filter for optional parameters
2. Use meaningful parameter names
3. Keep components focused on a single responsibility
4. Use Bootstrap classes for styling to maintain consistency
5. Document any required CSS or JavaScript dependencies