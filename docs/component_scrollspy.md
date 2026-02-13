# Scrollspy Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Scrollspy component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/scrollspy.html' with id="scrollspyExample" navbar_id="navbarExample" items=scrollspy_items root_margin="0px 0px -40%" smooth_scroll=True %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `classes` | string | Parameter description | None |
| `item.content` | string | Parameter description | None |
| `item.id` | string | Parameter description | None |
| `item.title` | string | Parameter description | None |
| `navbar_brand` | string | Parameter description | None |
| `navbar_id` | string | Parameter description | None |
| `root_margin` | string | Parameter description | None |
| `smooth_scroll` | string | Parameter description | None |
| `subitem.id` | string | Parameter description | None |
| `subitem.title` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/scrollspy.html' with id="scrollspyExample" navbar_id="navbarExample" items=scrollspy_items root_margin="0px 0px -40%" smooth_scroll=True %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
