# Table Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Table component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/table.html' with headers=table_headers rows=table_rows striped=True hover=True bordered=False responsive=True caption="List of users" %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `body_class` | string | Parameter description | None |
| `caption` | string | Parameter description | None |
| `cell.class` | string | Parameter description | None |
| `cell.colspan` | string | Parameter description | None |
| `cell.content` | string | Parameter description | None |
| `cell.rowspan` | string | Parameter description | None |
| `classes` | string | Parameter description | None |
| `header.class` | string | Parameter description | None |
| `header.style` | string | Parameter description | None |
| `header.text` | string | Parameter description | None |
| `header_variant` | string | Parameter description | None |
| `responsive_size` | string | Parameter description | None |
| `row.class` | string | Parameter description | None |
| `variant` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/table.html' with headers=table_headers rows=table_rows striped=True hover=True bordered=False responsive=True caption="List of users" %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
