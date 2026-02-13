# Form Textarea Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Form Textarea component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/form_textarea.html' with name="message" label="Message" rows=5 placeholder="Enter your message" required=True %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `aria_describedby` | string | Parameter description | None |
| `aria_label` | string | Parameter description | None |
| `cols` | string | Parameter description | None |
| `group_class` | string | Parameter description | None |
| `help_text` | string | Parameter description | None |
| `id` | string | Parameter description | None |
| `label` | string | Parameter description | None |
| `label_class` | string | Parameter description | None |
| `maxlength` | string | Parameter description | None |
| `minlength` | string | Parameter description | None |
| `name` | string | Parameter description | None |
| `placeholder` | string | Parameter description | None |
| `rows` | string | Parameter description | None |
| `size` | string | Parameter description | None |
| `textarea_class` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/form_textarea.html' with name="message" label="Message" rows=5 placeholder="Enter your message" required=True %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
