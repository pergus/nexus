# Button Link Component

## Purpose
This component provides reusable UI functionality for consistent design throughout your application.

## When to Use
Use the Button Link component when you need to:
- Implementing consistent UI patterns

- Reusing common interface elements

- Maintaining design system consistency

- Reducing code duplication

## Usage

```django
{% include 'components/button_link.html' with label="Click Me" url="/some-page" btn_class="btn-primary" %}
```



## Parameters

| Parameter      | Type    | Description                                                                          | Default                        |
| -------------- | ------- | ------------------------------------------------------------------------------------ | ------------------------------ |
| `aria_label`   | string  | Sets the `aria-label` attribute for accessibility.                                   | None                           |
| `btn_class`    | string  | Bootstrap button class to control style (e.g., `btn-primary`, `btn-danger`).         | `btn-primary` if not specified |
| `button_class` | string  | Additional custom CSS classes applied to the button.                                 | None                           |
| `icon`         | string  | Optional icon class (e.g., FontAwesome) to display inside the button.                | None                           |
| `label`        | string  | The text label displayed on the button.                                              | `"Button"`                     |
| `outline`      | string  | Adds an outline style variant, e.g., `primary` will result in `btn-outline-primary`. | None                           |
| `size`         | string  | Adjusts button size, e.g., `sm` or `lg` → `btn-sm` or `btn-lg`.                      | None                           |
| `full_width`   | boolean | Makes the button stretch to full container width.                                    | False                          |
| `target`       | string  | Sets the target attribute for links, e.g., `_blank` to open in a new tab.            | None                           |
| `url`          | string  | The URL the button links to.                                                         | `#`                            |


## Examples

Example usage:
```django
{% include 'components/button_link.html' with label="Click Me" url="/some-page" btn_class="btn-primary" %}
```

## Customization
This component can be customized through CSS classes or by modifying the template directly.
