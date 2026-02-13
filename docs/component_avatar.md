# Avatar Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Avatar component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/avatar.html' with src="/path/to/image.jpg" alt="ser Name" size="md" rounded=True circle=True %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `alt` | string | Parameter description | None |
| `classes` | string | Parameter description | None |
| `height` | string | Parameter description | None |
| `size` | string | Parameter description | None |
| `src` | string | Parameter description | None |
| `width` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/avatar.html' with src="/path/to/image.jpg" alt="ser Name" size="md" rounded=True circle=True %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
