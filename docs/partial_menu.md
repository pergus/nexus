# Menu Partial

## Purpose
The Menu partial serves as the main layout wrapper that combines the top navigation bar with the sidebar navigation. It provides a flexible structure that allows switching between different sidebar implementations while maintaining consistent page layout.

## When to Use
Use the Menu partial when you need to:
- Create consistent page layouts across your application

- Implement a combination of topbar and sidebar navigation

- Provide flexibility in sidebar implementation

- Maintain a standardized application structure

## Usage

```django
{% include 'partials/menu.html' %}
```

Or with a custom sidebar:

```django
{% include 'partials/menu.html' with sidebar_template='partials/custom_sidebar.html' %}
```

## Structure Overview
The menu consists of two main components:

1. **Topbar** - Includes the `topbar.html` partial for header navigation
2. **Sidebar** - Dynamically includes either:
   - A custom sidebar specified by `sidebar_template` variable

- The default `flexible_sidebar.html` partial

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `sidebar_template` | string | Custom sidebar template to include | flexible_sidebar.html |
|-----------|------|-------------|---------|

## Creating Custom Menus

### Custom Sidebar Implementation
To use a custom sidebar, pass the `sidebar_template` variable:

```django
{% include 'partials/menu.html' with sidebar_template='partials/my_custom_sidebar.html' %}
```

### Custom Topbar
To modify the topbar, create your own `topbar.html` partial in the same directory, or modify the existing one.

### Complete Custom Menu
For entirely custom menu structures, create a new partial and include it instead of the default menu:

```django
<!-- In your base template -->
{% include 'partials/my_complete_menu.html' %}
```

## Customization Guide

### Modifying the Default Structure
The menu template is designed to be lightweight and flexible. To customize:

1. **Change sidebar behavior**: Modify the conditional logic in the template
2. **Add additional elements**: Insert new components between topbar and sidebar
3. **Modify layout classes**: Adjust CSS classes for responsive behavior

### Creating a Custom Sidebar Template
Create a new sidebar template by following this basic structure:

```html
<div class="app-sidebar">
    <div class="logo-box">
        <!-- Your logo -->
    </div>
    <div class="scrollbar" data-simplebar>
        <ul class="navbar-nav">
            <!-- Your navigation items -->
        </ul>
    </div>
</div>
```

Then use it:

```django
{% include 'partials/menu.html' with sidebar_template='partials/my_new_sidebar.html' %}
```

## Dependencies

- `topbar.html` partial for header navigation

- Sidebar templates (default is `flexible_sidebar.html`)
- Bootstrap for responsive behavior

- SimpleBar for custom scrollbars

## Best Practices
1. Maintain consistency in navigation patterns across the application
2. Ensure mobile responsiveness when creating custom menus
3. Use semantic HTML for accessibility
4. Test navigation flow with real user scenarios
5. Keep the menu structure lightweight to avoid performance issues
6. Document custom menu implementations for team members