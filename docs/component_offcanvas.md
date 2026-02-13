# Offcanvas Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Offcanvas component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/offcanvas.html' with id="offcanvasExample" title="Offcanvas Title" body="Content" position="start" scroll=True backdrop=False %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `backdrop` | string | Parameter description | None |
| `body` | string | Parameter description | None |
| `classes` | string | Parameter description | None |
| `dropdown_text` | string | Parameter description | None |
| `id` | string | Parameter description | None |
| `item.href` | string | Parameter description | None |
| `item.text` | string | Parameter description | None |
| `position` | string | Parameter description | None |
| `scroll` | string | Parameter description | None |
| `title` | string | Parameter description | None |
| `trigger_btn_class` | string | Parameter description | None |
| `trigger_text` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/offcanvas.html' with id="offcanvasExample" title="Offcanvas Title" body="Content" position="start" scroll=True backdrop=False %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
