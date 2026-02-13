# Chart Radialbar Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Chart Radialbar component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/chart_radialbar.html' with chart_id="my-radialbar-chart" series_data=series_data chart_title="My Radialbar Chart" height=380 %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `chart_id` | string | Parameter description | None |
| `chart_title` | string | Parameter description | None |
| `colors` | string | Parameter description | None |
| `end_angle` | string | Parameter description | None |
| `fill_type` | string | Parameter description | None |
| `gradient_shade_intensity` | string | Parameter description | None |
| `gradient_shade` | string | Parameter description | None |
| `gradient_stops` | string | Parameter description | None |
| `gradient_to_colors` | string | Parameter description | None |
| `gradient_type` | string | Parameter description | None |
| `grid_padding_bottom` | string | Parameter description | None |
| `height` | string | Parameter description | None |
| `inverse_colors` | string | Parameter description | None |
| `labels` | string | Parameter description | None |
| `legend_align` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/chart_radialbar.html' with chart_id="my-radialbar-chart" series_data=series_data chart_title="My Radialbar Chart" height=380 %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
