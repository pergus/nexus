# Button Link Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Button Link component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/button_link.html' with label="Click Me" url="/some-page" btn_class="btn-primary" %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `aria_label` | string | Parameter description | None |
| `btn_class` | string | Parameter description | None |
| `button_class` | string | Parameter description | None |
| `icon` | string | Parameter description | None |
| `label` | string | Parameter description | None |
| `outline` | string | Parameter description | None |
| `size` | string | Parameter description | None |
| `target` | string | Parameter description | None |
| `url` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/button_link.html' with label="Click Me" url="/some-page" btn_class="btn-primary" %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
