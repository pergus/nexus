# Toast Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Toast component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/toast.html' with id="myToast" title="Notification" message="This is a toast message" time="11 mins ago" show_close=True show_logo=True type="primary" placement="bottom-0 end-0" %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `action_primary` | string | Parameter description | None |
| `action_secondary` | string | Parameter description | None |
| `classes` | string | Parameter description | None |
| `delay` | string | Parameter description | None |
| `id` | string | Parameter description | None |
| `logo_dark` | string | Parameter description | None |
| `logo_light` | string | Parameter description | None |
| `message` | string | Parameter description | None |
| `time` | string | Parameter description | None |
| `title` | string | Parameter description | None |
| `type` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/toast.html' with id="myToast" title="Notification" message="This is a toast message" time="11 mins ago" show_close=True show_logo=True type="primary" placement="bottom-0 end-0" %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
