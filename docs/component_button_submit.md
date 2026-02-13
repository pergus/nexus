# Button Submit Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Button Submit component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/button_submit.html' with label="Submit" btn_class="btn-primary" full_width=True %}
```

## Parameters

| Parameter      | Type    | Description                                                                    | Default                        |
| -------------- | ------- | ------------------------------------------------------------------------------ | ------------------------------ |
| `aria_label`   | string  | Sets the `aria-label` attribute for accessibility.                             | None                           |
| `btn_class`    | string  | Bootstrap button class to control style (e.g., `btn-primary`, `btn-danger`).   | `btn-primary` if not specified |
| `button_class` | string  | Additional custom CSS classes applied to the button.                           | None                           |
| `form`         | string  | Specifies the HTML `form` attribute to associate the button with a form by ID. | None                           |
| `icon`         | string  | Optional icon class (e.g., FontAwesome) to display inside the button.          | None                           |
| `label`        | string  | The text label displayed on the button.                                        | `"Submit"`                     |
| `name`         | string  | Sets the `name` attribute for the button element.                              | None                           |
| `outline`      | string  | Adds an outline style variant, e.g., `primary` → `btn-outline-primary`.        | None                           |
| `size`         | string  | Adjusts button size, e.g., `sm` or `lg` → `btn-sm` or `btn-lg`.                | None                           |
| `full_width`   | boolean | Makes the button stretch to full container width.                              | False                          |
| `value`        | string  | Sets the HTML `value` attribute of the button.                                 | None                           |


## Examples

Example usage:
```django
{% include 'components/button_submit.html' with label="Submit" btn_class="btn-primary" full_width=True %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
