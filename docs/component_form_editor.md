# Form Editor Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Form Editor component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/form_editor.html' with name="content" label="Content" editor_type="snow" height=300 %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `editor_class` | string | Parameter description | None |
| `editor_type` | string | Parameter description | None |
| `form` | string | Parameter description | None |
| `group_class` | string | Parameter description | None |
| `height` | string | Parameter description | None |
| `help_text` | string | Parameter description | None |
| `id` | string | Parameter description | None |
| `label` | string | Parameter description | None |
| `label_class` | string | Parameter description | None |
| `name` | string | Parameter description | None |
| `placeholder` | string | Parameter description | None |
| `value` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/form_editor.html' with name="content" label="Content" editor_type="snow" height=300 %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
