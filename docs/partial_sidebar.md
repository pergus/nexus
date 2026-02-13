# Sidebar Partial

## Purpose
The Sidebar partial provides the main navigation structure for the application. It includes the application logo, scrollable navigation menu with collapsible sections, and various menu items organized into logical groups. The sidebar supports icons, badges, and multi-level navigation.

## When to Use
Use the Sidebar partial when you need to:
- Implement the main application navigation

- Provide organized access to different sections of your application

- Create a consistent navigation experience across pages

- Implement collapsible menu sections for better organization

## Usage

```django
{% include 'partials/sidebar.html' %}
```

## Structure Overview
The sidebar is organized into several key sections:

1. **Logo Area** - Displays application branding with light/dark variants
2. **Scrollable Navigation** - Main menu with SimpleBar scrolling
3. **Menu Sections** - Logically grouped navigation items
4. **Navigation Items** - Individual links with icons and badges
5. **Collapsible Groups** - Multi-level menu sections
6. **Visual Elements** - Icons, badges, and decorative elements

## Menu Organization
The navigation is structured as follows:
- Dashboard

- Authentication (Sign In, Sign Up, Password Reset, Lock Screen)
- Error Pages (404 variants)
- UI Kit (Accordion, Alerts, Buttons, Cards, etc.)
- Charts (Apex Charts)
- Forms (Basic, Validation, File Upload, Editors)
- Tables (Basic, GridJS)
- Icons (Boxicons, Solar)
- Maps (Google, Vector)
- Layouts (Different theme variations)
- Multi-level demo menus

## Customization Guide

### Adding New Menu Items
To add new menu items, modify the template directly by adding new `<li>` elements within the appropriate section:

```html
<li class="nav-item">
    <a class="nav-link" href="/your-page">
        <span class="nav-icon">
            <iconify-icon icon="your-icon-class"></iconify-icon>
        </span>
        <span class="nav-text"> Your Menu Item </span>
    </a>
</li>
```

### Adding Collapsible Sections
To create a new collapsible menu section:

```html
<li class="nav-item">
    <a class="nav-link menu-arrow" href="#yourSectionId" data-bs-toggle="collapse" role="button" aria-expanded="false" aria-controls="yourSectionId">
        <span class="nav-icon">
            <iconify-icon icon="your-icon-class"></iconify-icon>
        </span>
        <span class="nav-text"> Section Title </span>
    </a>
    <div class="collapse" id="yourSectionId">
        <ul class="nav sub-navbar-nav">
            <li class="sub-nav-item">
                <a class="sub-nav-link" href="/sub-item-url">Sub Item</a>
            </li>
        </ul>
    </div>
</li>
```

### Customizing Logo
Modify the logo section to change branding:

```html
<div class="logo-box">
    <a href="/" class="logo-dark">
        <img src="{% static '/images/your-logo-sm.png' %}" class="logo-sm" alt="logo sm">
        <img src="{% static '/images/your-logo-dark.png' %}" class="logo-lg" alt="logo dark">
    </a>
    <!-- Light variant -->
</div>
```

## Dependencies

- Iconify library for vector icons

- Bootstrap for collapse functionality

- SimpleBar for custom scrollbars

- Static image assets for logos

## Best Practices
1. Keep menu hierarchies shallow (maximum 2-3 levels)
2. Use descriptive, concise menu item labels
3. Group related functionality together
4. Use appropriate icons to enhance recognition
5. Consider mobile responsiveness when adding new items
6. Test navigation flow with real user scenarios