# Form Input Group Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Form Input Group component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/form_input_group.html' with name="username" label="sername" prepend_text="@" %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `append_button_class` | string | Parameter description | None |
| `append_button_text` | string | Parameter description | None |
| `append_text` | string | Parameter description | None |
| `aria_label` | string | Parameter description | None |
| `autocomplete` | string | Parameter description | None |
| `form` | string | Parameter description | None |
| `group_class` | string | Parameter description | None |
| `help_text` | string | Parameter description | None |
| `id` | string | Parameter description | None |
| `input_class` | string | Parameter description | None |
| `label` | string | Parameter description | None |
| `label_class` | string | Parameter description | None |
| `max` | string | Parameter description | None |
| `maxlength` | string | Parameter description | None |
| `min` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/form_input_group.html' with name="username" label="sername" prepend_text="@" %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
