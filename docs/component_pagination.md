# Pagination Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Pagination component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/pagination.html' with items=page_items current_page=1 alignment="center" size="lg" rounded=True %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `classes` | string | Parameter description | None |
| `item.number` | string | Parameter description | None |
| `item.url` | string | Parameter description | None |
| `next_text` | string | Parameter description | None |
| `next_url` | string | Parameter description | None |
| `previous_text` | string | Parameter description | None |
| `previous_url` | string | Parameter description | None |
| `size` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/pagination.html' with items=page_items current_page=1 alignment="center" size="lg" rounded=True %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
