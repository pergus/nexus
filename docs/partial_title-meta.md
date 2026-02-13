# Title Meta Partial

## Purpose
The Title Meta partial handles page metadata including the HTML title tag and meta description. It ensures proper SEO setup and social sharing optimization for each page.

## When to Use
Use the Title Meta partial when you need to:
- Set proper HTML document titles for SEO

- Define meta descriptions for search engines

- Configure social media sharing metadata

- Implement consistent metadata across pages

## Usage

```django
{% include 'partials/title-meta.html' %}
```

## Structure Overview
The metadata section includes: 1) HTML title tag with page-specific content, 2) Meta description for search engines, 3) Open Graph tags for social sharing, 4) Twitter Card metadata, 5) Viewport and charset declarations

## Customization Guide
### Custom Page Titles
To set custom titles for specific pages:

### Adding Social Media Metadata
To include additional social sharing tags:

## Dependencies

- Django templating engine

- Static files for social sharing images

- SEO best practices

- Social media platform requirements

## Best Practices
1. Keep titles under 60 characters for search results
2. Write compelling meta descriptions under 160 characters
3. Use unique titles and descriptions for each page
4. Include relevant keywords naturally
5. Test social sharing previews before publishing
6. Update metadata when content changes significantly
