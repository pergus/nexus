# Flexible Sidebar Partial

## Purpose
The Flexible Sidebar partial provides a dynamic, collapsible sidebar navigation that adapts to different screen sizes. It includes scrollable navigation menus with support for nested items, icons, and responsive behavior that automatically collapses on smaller screens.

## When to Use
Use the Flexible Sidebar partial when you need to:
- Create responsive sidebar navigation for dashboard applications

- Implement collapsible menu systems

- Support nested navigation hierarchies

- Provide consistent navigation across application pages

## Usage

```django
{% include 'partials/flexible_sidebar.html' %}
```

## Structure Overview
The sidebar consists of: 1) Main container with class 'app-sidebar', 2) Logo box section for branding, 3) Scrollable navigation area using SimpleBar, 4) Navigation menu with collapsible sections, 5) Toggle button for collapsing/expanding on desktop

## Customization Guide
### Adding New Menu Items
To add new navigation items to the sidebar:

### Customizing Sidebar Colors
To modify sidebar colors, override the CSS variables in your custom stylesheet:

## Dependencies

- Bootstrap for responsive behavior

- SimpleBar library for custom scrollbars

- Material Design Icons for navigation icons

- App CSS for sidebar styling

- JavaScript for collapse/hover behavior

## Best Practices
1. Limit navigation depth to improve usability
2. Use clear, descriptive labels for menu items
3. Group related items under logical sections
4. Ensure icons are meaningful and consistent
5. Test responsive behavior on all device sizes
6. Optimize for keyboard navigation accessibility
