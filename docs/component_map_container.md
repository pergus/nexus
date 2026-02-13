# Map Container Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Map Container component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/map_container.html' %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `map_class` | string | Parameter description | None |
| `map_height` | string | Parameter description | None |
| `map_id` | string | Parameter description | None |
| `placeholder_text` | string | Parameter description | None |
| `subtitle` | string | Parameter description | None |
| `title` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/map_container.html' %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
