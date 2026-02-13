# Spinner Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Spinner component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/spinner.html' with type="border" color="primary" size="sm" text="Loading..." align="center" in_button=True %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `button_color` | string | Parameter description | None |
| `classes` | string | Parameter description | None |
| `color` | string | Parameter description | None |
| `container_class` | string | Parameter description | None |
| `size` | string | Parameter description | None |
| `text` | string | Parameter description | None |
| `type` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/spinner.html' with type="border" color="primary" size="sm" text="Loading..." align="center" in_button=True %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
