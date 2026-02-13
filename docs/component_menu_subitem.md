# Menu Subitem Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Menu Subitem component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/menu_subitem.html' %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `item.badge_color` | string | Parameter description | None |
| `item.badge_text` | string | Parameter description | None |
| `item.css_class` | string | Parameter description | None |
| `item.title` | string | Parameter description | None |
| `item.url` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/menu_subitem.html' %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
