# Button Group Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Button Group component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/button_group.html' with buttons=button_list vertical=True %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `button.id` | string | Parameter description | None |
| `button.text` | string | Parameter description | None |
| `button.type` | string | Parameter description | None |
| `classes` | string | Parameter description | None |
| `item.href` | string | Parameter description | None |
| `item.text` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/button_group.html' with buttons=button_list vertical=True %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
