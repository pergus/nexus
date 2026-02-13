# Tabs Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Tabs component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/tabs.html' with tabs=tab_items active_tab="profile" type="tabs" justified=False vertical=False %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `id` | string | Parameter description | None |
| `tab.content` | string | Parameter description | None |
| `tab.icon` | string | Parameter description | None |
| `tab.id` | string | Parameter description | None |
| `tab.title` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/tabs.html' with tabs=tab_items active_tab="profile" type="tabs" justified=False vertical=False %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
