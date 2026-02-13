# Form Dropzone Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Form Dropzone component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/form_dropzone.html' with name="files" label="pload Files" multiple=True %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `accept` | string | Parameter description | None |
| `accept` | string | Parameter description | None |
| `add_remove_links` | string | Parameter description | None |
| `auto_process` | string | Parameter description | None |
| `cancel_upload_text` | string | Parameter description | None |
| `dropzone_class` | string | Parameter description | None |
| `dropzone_description` | string | Parameter description | None |
| `dropzone_title` | string | Parameter description | None |
| `group_class` | string | Parameter description | None |
| `help_text` | string | Parameter description | None |
| `id` | string | Parameter description | None |
| `label` | string | Parameter description | None |
| `label_class` | string | Parameter description | None |
| `max_files` | string | Parameter description | None |
| `max_filesize` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/form_dropzone.html' with name="files" label="pload Files" multiple=True %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
