# Progress Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Progress component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/progress.html' with value=25 max=100 type="primary" striped=True animated=True height="sm" show_label=True %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `classes` | string | Parameter description | None |
| `height` | string | Parameter description | None |
| `max` | string | Parameter description | None |
| `type` | string | Parameter description | None |
| `value` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/progress.html' with value=25 max=100 type="primary" striped=True animated=True height="sm" show_label=True %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
