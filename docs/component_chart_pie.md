# Chart Pie Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Chart Pie component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/chart_pie.html' with chart_id="my-pie-chart" series_data=series_data chart_title="My Pie Chart" height=320 %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `chart_id` | string | Parameter description | None |
| `chart_title` | string | Parameter description | None |
| `colors` | string | Parameter description | None |
| `height` | string | Parameter description | None |
| `labels` | string | Parameter description | None |
| `legend_align` | string | Parameter description | None |
| `legend_position` | string | Parameter description | None |
| `legend_vertical_align` | string | Parameter description | None |
| `series_data` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/chart_pie.html' with chart_id="my-pie-chart" series_data=series_data chart_title="My Pie Chart" height=320 %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
