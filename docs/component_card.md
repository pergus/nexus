# Card Component

## Purpose
The Card component provides a flexible container for displaying content with optional header and footer sections. Cards are commonly used to organize information into digestible chunks, such as dashboards, product listings, user profiles, and content summaries.

## When to Use
Use the Card component when you need to:
- Group related content in a visually distinct container

- Create dashboard widgets or panels

- Display user profiles or product information

- Organize content with clear visual boundaries

## Usage

```django
{% include 'components/card.html' with title="Card Title" subtitle="Card Subtitle" %}
{% endinclude %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `title` | string | Card header title | None |
| `subtitle` | string | Card header subtitle | None |
| `footer` | string | Content for card footer | None |
| `classes` | string | Additional CSS classes for the card | None |
| `card_content` | string | Direct content for card body (alternative to block) | None |

## Examples

### Simple Card with Title
```django
{% include 'components/card.html' with title="Welcome" %}
    {% block card_content %}
        <p>Welcome to our application! This is a simple card with just a title.</p>
    {% endblock %}
{% endinclude %}
```

### Card with Header and Footer
```django
{% include 'components/card.html' with title="User Profile" subtitle="John Doe" footer="<small>Last updated: Today</small>" %}
    {% block card_content %}
        <div class="d-flex align-items-center">
            <img src="/path/to/avatar.jpg" class="rounded-circle me-3" width="50" alt="Avatar">
            <div>
                <h5 class="mb-1">John Doe</h5>
                <p class="mb-0">Software Developer</p>
            </div>
        </div>
    {% endblock %}
{% endinclude %}
```

### Card with Custom Classes
```django
{% include 'components/card.html' with title="Statistics" classes="border-primary shadow" %}
    {% block card_content %}
        <div class="row">
            <div class="col-md-4">
                <h3>125</h3>
                <p>Users</p>
            </div>
            <div class="col-md-4">
                <h3>42</h3>
                <p>Projects</p>
            </div>
            <div class="col-md-4">
                <h3>8</h3>
                <p>Teams</p>
            </div>
        </div>
    {% endblock %}
{% endinclude %}
```

## Customization
Cards can be customized through CSS classes passed via the `classes` parameter. You can also modify the template directly to add new styling variants or structural elements. For complex content, use the `card_content` block to provide rich HTML content.
