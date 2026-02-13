# Dropdown Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Dropdown component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/dropdown.html' with button_text="Dropdown" items=dropdown_items color="primary" split=False direction="down" dark=False %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `auto_close` | string | Parameter description | None |
| `button_text` | string | Parameter description | None |
| `classes` | string | Parameter description | None |
| `color` | string | Parameter description | None |
| `form_content` | string | Parameter description | None |
| `item.href` | string | Parameter description | None |
| `item.text` | string | Parameter description | None |
| `offset` | string | Parameter description | None |
| `reference` | string | Parameter description | None |
| `size` | string | Parameter description | None |
| `text_content` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/dropdown.html' with button_text="Dropdown" items=dropdown_items color="primary" split=False direction="down" dark=False %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
