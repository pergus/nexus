# Tooltip Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Tooltip component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/tooltip.html' with text="Hover me" title="Tooltip Title" placement="top" custom_class="primary-tooltip" %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `btn_class` | string | Parameter description | None |
| `custom_class` | string | Parameter description | None |
| `href` | string | Parameter description | None |
| `link_class` | string | Parameter description | None |
| `placement` | string | Parameter description | None |
| `text` | string | Parameter description | None |
| `text` | string | Parameter description | None |
| `title` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/tooltip.html' with text="Hover me" title="Tooltip Title" placement="top" custom_class="primary-tooltip" %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
