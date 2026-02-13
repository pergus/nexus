# Alert Component

## Purpose
The Alert component displays contextual feedback messages for typical user actions. Alerts provide important information through colored backgrounds and icons that indicate the severity or type of message.

## When to Use
Use the Alert component when you need to:
- Notifying users of successful operations

- Warning users about potential issues

- Informing users of errors or problems

- Providing informational messages

## Usage

```django
{% include 'components/alert.html' with type="primary" title="Title" message="Message" dismissible=True icon="bx bx-info-circle" %}
```

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| --------- | ---- | ----------- | ------- |
| `content` | string | Parameter description | None |
| `icon` | string | Parameter description | None |
| `message` | string | Parameter description | None |
| `title` | string | Parameter description | None |
| `type` | string | Parameter description | None |

## Examples

Example usage:
```django
{% include 'components/alert.html' with type="primary" title="Title" message="Message" dismissible=True icon="bx bx-info-circle" %}
```

## Customization
Alerts can be customized by modifying CSS classes, changing icons, or adding new color variants. You can also extend the template to include additional styling options.
