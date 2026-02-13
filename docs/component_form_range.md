# Form Range Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Form Range component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/form_range.html' with name="volume" label="Volume" min=0 max=100 step=1 value=50 %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `aria_describedby` | string | Parameter description | None |
| `aria_label` | string | Parameter description | None |
| `form` | string | Parameter description | None |
| `group_class` | string | Parameter description | None |
| `help_text` | string | Parameter description | None |
| `id` | string | Parameter description | None |
| `input_class` | string | Parameter description | None |
| `label` | string | Parameter description | None |
| `label_class` | string | Parameter description | None |
| `max` | string | Parameter description | None |
| `min` | string | Parameter description | None |
| `name` | string | Parameter description | None |
| `step` | string | Parameter description | None |
| `valid_message` | string | Parameter description | None |
| `validation_message` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/form_range.html' with name="volume" label="Volume" min=0 max=100 step=1 value=50 %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
