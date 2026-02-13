# Table Gridjs Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Table Gridjs component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/table_gridjs.html' with table_id="my-table" columns=grid_columns data=grid_data pagination=True search=True sort=True %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `columns` | string | Parameter description | None |
| `data` | string | Parameter description | None |
| `fixed_header` | string | Parameter description | None |
| `pagination_limit` | string | Parameter description | None |
| `pagination` | string | Parameter description | None |
| `resizable` | string | Parameter description | None |
| `search` | string | Parameter description | None |
| `sort` | string | Parameter description | None |
| `table_id` | string | Parameter description | None |
| `table_id` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/table_gridjs.html' with table_id="my-table" columns=grid_columns data=grid_data pagination=True search=True sort=True %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
