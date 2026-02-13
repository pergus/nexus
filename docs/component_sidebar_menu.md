# Sidebar Menu Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Sidebar Menu component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/sidebar_menu.html' %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `child.badge.color` | string | Parameter description | None |
| `child.badge.text` | string | Parameter description | None |
| `child.title` | string | Parameter description | None |
| `child.url` | string | Parameter description | None |
| `item.badge.color` | string | Parameter description | None |
| `item.badge.text` | string | Parameter description | None |
| `item.icon` | string | Parameter description | None |
| `item.id` | string | Parameter description | None |
| `item.title` | string | Parameter description | None |
| `item.url` | string | Parameter description | None |
| `logo_url` | string | Parameter description | None |
| `section.title` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/sidebar_menu.html' %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
