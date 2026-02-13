# Form Datepicker Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Form Datepicker component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/form_datepicker.html' with name="date" label="Select Date" picker_type="date" %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `aria_describedby` | string | Parameter description | None |
| `aria_label` | string | Parameter description | None |
| `conjunction` | string | Parameter description | None |
| `date_format` | string | Parameter description | None |
| `default_date` | string | Parameter description | None |
| `disable_dates` | string | Parameter description | None |
| `enable_time` | string | Parameter description | None |
| `form` | string | Parameter description | None |
| `group_class` | string | Parameter description | None |
| `help_text` | string | Parameter description | None |
| `id` | string | Parameter description | None |
| `inline` | string | Parameter description | None |
| `input_class` | string | Parameter description | None |
| `label` | string | Parameter description | None |
| `label_class` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/form_datepicker.html' with name="date" label="Select Date" picker_type="date" %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
