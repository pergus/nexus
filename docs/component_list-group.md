# List-group Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the List-group component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/list-group.html' with items=list_items type="basic" flush=False numbered=False horizontal=False classes="w-50" %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `classes` | string | Parameter description | None |
| `forloop.counter` | string | Parameter description | None |
| `item.badge` | string | Parameter description | None |
| `item.color` | string | Parameter description | None |
| `item.content` | string | Parameter description | None |
| `item.href` | string | Parameter description | None |
| `item.id` | string | Parameter description | None |
| `item.label` | string | Parameter description | None |
| `item.small_text` | string | Parameter description | None |
| `item.text` | string | Parameter description | None |
| `item.title` | string | Parameter description | None |
| `item.value` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/list-group.html' with items=list_items type="basic" flush=False numbered=False horizontal=False classes="w-50" %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
