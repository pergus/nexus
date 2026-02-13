# Popover Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Popover component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/popover.html' with button_text="Click me" title="Popover Title" content="Popover content" placement="top" trigger="click" %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `btn_class` | string | Parameter description | None |
| `button_text` | string | Parameter description | None |
| `container` | string | Parameter description | None |
| `content` | string | Parameter description | None |
| `custom_class` | string | Parameter description | None |
| `placement` | string | Parameter description | None |
| `title` | string | Parameter description | None |
| `trigger` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/popover.html' with button_text="Click me" title="Popover Title" content="Popover content" placement="top" trigger="click" %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
