# Chart Bar Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Chart Bar component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/chart_bar.html' with chart_id="my-bar-chart" series_data=series_data chart_title="My Bar Chart" height=380 %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `bar_height` | string | Parameter description | None |
| `chart_id` | string | Parameter description | None |
| `chart_title` | string | Parameter description | None |
| `colors` | string | Parameter description | None |
| `data_labels` | string | Parameter description | None |
| `ending_shape` | string | Parameter description | None |
| `fill_opacity` | string | Parameter description | None |
| `height` | string | Parameter description | None |
| `legend_align` | string | Parameter description | None |
| `legend_offset_x` | string | Parameter description | None |
| `legend_offset_y` | string | Parameter description | None |
| `legend_position` | string | Parameter description | None |
| `series_data` | string | Parameter description | None |
| `stroke_width` | string | Parameter description | None |
| `tooltip_unit` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/chart_bar.html' with chart_id="my-bar-chart" series_data=series_data chart_title="My Bar Chart" height=380 %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
