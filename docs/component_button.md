# Button Component

## Purpose
The Button component provides a reusable, customizable button element that can be used throughout your application. It supports both button and anchor elements, allowing you to create action buttons or navigation links with consistent styling.

## When to Use
Use the Button component when you need to:

- Create action buttons for forms (submit, cancel, etc.)
- Create navigation links with button styling
- Provide consistent UI elements across your application
- Implement various button styles (primary, secondary, outline, etc.)

## Usage

```django
{% include 'components/button.html' with type="primary" text="Click me" size="lg" %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `type` | string | Button style variant (primary, secondary, success, danger, warning, info, light, dark) | primary |
| `text` | string | Button label text | None |
| `size` | string | Button size (sm for small, lg for large) | None |
| `outline` | boolean | Render as outline button instead of solid | False |
| `soft` | boolean | Render as soft style button | False |
| `rounded` | boolean | Apply rounded corners | False |
| `width` | string | Width class (xs, sm, md, lg, xl) | None |
| `block` | boolean | Make button full width | False |
| `disabled` | boolean | Disable the button | False |
| `href` | string | If provided, renders as anchor link instead of button | None |
| `icon` | string | CSS class for icon (e.g., "mdi mdi-plus") | None |
| `submit` | boolean | If true, creates a submit button | False |

## Examples

### Basic Primary Button
```django
{% include 'components/button.html' with type="primary" text="Submit" %}
```

### Large Outline Button with Icon
```django
{% include 'components/button.html' with type="success" text="Save Changes" size="lg" outline=True icon="mdi mdi-content-save" %}
```

### Link Button
```django
{% include 'components/button.html' with href="/dashboard" text="Go to Dashboard" type="secondary" %}
```

### Disabled Button
```django
{% include 'components/button.html' with type="primary" text="Disabled" disabled=True %}
```

## Customization
To customize the button styles, you can extend the CSS classes by passing additional classes through the `classes` parameter, or modify the template directly to add new variants.
