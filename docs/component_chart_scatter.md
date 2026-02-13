# Chart Scatter Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Chart Scatter component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/chart_scatter.html' with chart_id="my-scatter-chart" series_data=series_data chart_title="My Scatter Chart" height=380 %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `chart_id` | string | Parameter description | None |
| `chart_title` | string | Parameter description | None |
| `colors` | string | Parameter description | None |
| `height` | string | Parameter description | None |
| `legend_align` | string | Parameter description | None |
| `legend_offset_x` | string | Parameter description | None |
| `legend_offset_y` | string | Parameter description | None |
| `legend_position` | string | Parameter description | None |
| `marker_hover_size` | string | Parameter description | None |
| `marker_size` | string | Parameter description | None |
| `series_data` | string | Parameter description | None |
| `tooltip_x_unit` | string | Parameter description | None |
| `tooltip_y_unit` | string | Parameter description | None |
| `xaxis_tick_amount` | string | Parameter description | None |
| `xaxis_title` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/chart_scatter.html' with chart_id="my-scatter-chart" series_data=series_data chart_title="My Scatter Chart" height=380 %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
