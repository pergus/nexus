# Chart Line Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Chart Line component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/chart_line.html' with chart_id="my-chart" series_data=series_data chart_title="My Chart" height=380 %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `chart_id` | string | Parameter description | None |
| `chart_title` | string | Parameter description | None |
| `height` | string | Parameter description | None |
| `series_data` | string | Parameter description | None |
| `xaxis_categories` | string | Parameter description | None |
| `xaxis_title` | string | Parameter description | None |
| `yaxis_max` | string | Parameter description | None |
| `yaxis_min` | string | Parameter description | None |
| `yaxis_title` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/chart_line.html' with chart_id="my-chart" series_data=series_data chart_title="My Chart" height=380 %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
