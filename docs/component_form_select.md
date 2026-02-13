# Form Select Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Form Select component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/form_select.html' with name="country" label="Country" options=country_options selected="S" %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `aria_describedby` | string | Parameter description | None |
| `aria_label` | string | Parameter description | None |
| `group_class` | string | Parameter description | None |
| `help_text` | string | Parameter description | None |
| `id` | string | Parameter description | None |
| `label` | string | Parameter description | None |
| `label_class` | string | Parameter description | None |
| `name` | string | Parameter description | None |
| `option.group` | string | Parameter description | None |
| `option.text` | string | Parameter description | None |
| `option.value` | string | Parameter description | None |
| `placeholder` | string | Parameter description | None |
| `select_class` | string | Parameter description | None |
| `size` | string | Parameter description | None |
| `size_attr` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/form_select.html' with name="country" label="Country" options=country_options selected="S" %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
