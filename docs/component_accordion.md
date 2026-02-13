# Accordion Component

## Purpose
The Accordion component provides a vertically stacked list of collapsible sections. Each section can be expanded or collapsed to show or hide content, making it ideal for organizing large amounts of information in a compact space.

## When to Use
Use the Accordion component when you need to:
- Displaying FAQ sections with questions and answers

- Organizing related content into collapsible sections

- Saving screen space while keeping information accessible

- Creating step-by-step guides or tutorials

## Usage

```django
{% include 'components/accordion.html' with id="accordionExample" items=accordion_items flush=True %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `classes` | string | Parameter description | None |
| `id` | string | Parameter description | None |
| `item.content` | string | Parameter description | None |
| `item.id` | string | Parameter description | None |
| `item.title` | string | Parameter description | None |

## Examples

### Basic Usage
```django
{% include 'components/accordion.html' with id="accordionExample" items=accordion_items flush=True %}
```

## Customization
Accordions can be customized by modifying CSS classes, changing animation speeds, or adding custom icons for expanded/collapsed states. You can also modify the template to add new styling variants.
