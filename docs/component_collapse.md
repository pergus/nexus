# Collapse Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Collapse component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/collapse.html' with id="collapseExample" content="Collapsed content" button_text="Toggle" horizontal=False multi_targets=False %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `btn_class` | string | Parameter description | None |
| `button_text` | string | Parameter description | None |
| `card_classes` | string | Parameter description | None |
| `card_style` | string | Parameter description | None |
| `classes` | string | Parameter description | None |
| `content` | string | Parameter description | None |
| `id` | string | Parameter description | None |
| `multi_controls` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/collapse.html' with id="collapseExample" content="Collapsed content" button_text="Toggle" horizontal=False multi_targets=False %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
