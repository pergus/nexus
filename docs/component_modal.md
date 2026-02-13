# Modal Component

## Purpose
The Modal component creates dialog overlays that appear on top of the main content. Modals are useful for drawing attention to important information, confirming actions, or collecting user input without navigating away from the current page.

## When to Use
Use the Modal component when you need to:
- Displaying important notifications or confirmations

- Collecting user input in a focused context

- Showing detailed information without leaving the current page

- Creating wizards or multi-step processes

## Usage

```django
{% include 'components/modal.html' with id="myModal" title="Modal Title" body="Modal content" size="lg" centered=True %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `body` | string | Parameter description | None |
| `footer_content` | string | Parameter description | None |
| `id` | string | Parameter description | None |
| `modal_class` | string | Parameter description | None |
| `size` | string | Parameter description | None |
| `title` | string | Parameter description | None |
| `trigger_btn_class` | string | Parameter description | None |
| `trigger_button_text` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/modal.html' with id="myModal" title="Modal Title" body="Modal content" size="lg" centered=True %}
```

## Customization
Modals can be customized by modifying CSS classes, changing sizes, or adding new footer configurations. You can also extend the template to include additional styling options or behaviors.
