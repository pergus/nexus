# Footer Partial

## Purpose
The Footer partial provides a consistent footer section across all pages in your application. It typically contains copyright information, links to legal pages, contact information, and other global navigation elements that appear at the bottom of every page.

## When to Use
Use the Footer partial when you need to:
- Include consistent footer content across all application pages

- Display copyright and legal information

- Provide global navigation links in the footer

- Maintain branding consistency throughout the site

## Usage

```django
{% include 'partials/footer.html' %}
```

## Structure Overview
The footer consists of a container div with class 'footer' that typically
includes: 1) Copyright information with current year, 2) Links to legal pages
(Privacy Policy, Terms of Service), 3) Contact information or social media
links, 4) Additional navigation elements as needed

## Customization Guide
### Modifying Footer Content
To customize the footer content, modify the template directly:

### Adding Social Media Links
To add social media icons to the footer:

## Dependencies

- Bootstrap CSS for styling

- App CSS for custom footer styles

- Container utility classes

## Best Practices
1. Keep footer content concise and relevant
2. Ensure footer links are accessible and functional
3. Use semantic HTML for better accessibility
4. Make footer responsive for all device sizes
5. Include important legal links as required
6. Update copyright year automatically or regularly
