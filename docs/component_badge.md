# Badge Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Badge component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/badge.html' with type="primary" text="New" pill=True %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `classes` | string | Parameter description | None |
| `text` | string | Parameter description | None |
| `type` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/badge.html' with type="primary" text="New" pill=True %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
