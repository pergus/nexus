# Breadcrumb Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Breadcrumb component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/breadcrumb.html' with items=breadcrumb_items divider=">" %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `classes` | string | Parameter description | None |
| `divider` | string | Parameter description | None |
| `item.text` | string | Parameter description | None |
| `item.url` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/breadcrumb.html' with items=breadcrumb_items divider=">" %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
