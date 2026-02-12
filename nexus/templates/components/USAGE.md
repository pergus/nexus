# Component Usage Guide

This guide shows how to use all the reusable components in your Django templates.

## Badge Component

```django
{% include 'components/badge.html' with type="primary" text="New" pill=True outline=False soft=False %}
```

**Parameters:**
- `type`: Badge type (primary, secondary, success, danger, warning, info, light, dark)
- `text`: Badge text
- `pill`: Boolean, creates rounded pill badge
- `outline`: Boolean, creates outline badge
- `soft`: Boolean, creates soft badge
- `classes`: Additional CSS classes

## Breadcrumb Component

```django
{% include 'components/breadcrumb.html' with items=breadcrumb_items divider=">" %}
```

**Parameters:**
- `items`: List of breadcrumb items (each with `text`, `url`, and optionally `active`)
- `divider`: Divider character (default: "/")
- `classes`: Additional CSS classes

## Button Component

```django
{% include 'components/button.html' with type="primary" text="Click me" size="lg" outline=True %}
```

**Parameters:**
- `type`: Button type (primary, secondary, success, danger, warning, info, light, dark)
- `text`: Button text
- `href`: If provided, creates a link instead of a button
- `size`: Button size (sm, lg)
- `outline`: Boolean, creates outline button
- `soft`: Boolean, creates soft button
- `rounded`: Boolean, creates rounded button
- `width`: Button width (xs, sm, md, lg, xl)
- `block`: Boolean, creates block-level button
- `disabled`: Boolean, disables the button
- `icon`: Icon class to add to the button
- `submit`: Boolean, creates a submit button
- `classes`: Additional CSS classes

## Alert Component

```django
{% include 'components/alert.html' with type="success" title="Success!" message="Operation completed." dismissible=True icon="bx bx-check" %}
```

**Parameters:**
- `type`: Alert type (primary, secondary, success, danger, warning, info, light, dark)
- `title`: Alert title (optional)
- `message`: Alert message
- `dismissible`: Boolean, adds close button
- `icon`: Icon class to add to the alert
- `classes`: Additional CSS classes

## Card Component

```django
{% include 'components/card.html' with title="Card Title" subtitle="Card Subtitle" %}
    {% block card_content %}
        <p>Card content goes here</p>
    {% endblock %}
{% endinclude %}
```

**Parameters:**
- `title`: Card title (optional)
- `subtitle`: Card subtitle (optional)
- `classes`: Additional CSS classes
- `footer`: Card footer content (optional)

## Avatar Component

```django
{% include 'components/avatar.html' with src="/path/to/image.jpg" alt="User Name" size="md" rounded=True circle=False %}
```

**Parameters:**
- `src`: Image source path
- `alt`: Alternative text
- `size`: Avatar size (xs, sm, md, lg, xl)
- `rounded`: Boolean, adds rounded corners
- `circle`: Boolean, creates circular avatar
- `thumbnail`: Boolean, adds thumbnail styling
- `width`: Image width
- `height`: Image height
- `classes`: Additional CSS classes

## Progress Component

```django
{% include 'components/progress.html' with value=50 max=100 type="primary" striped=True animated=False show_label=True height="sm" %}
```

**Parameters:**
- `value`: Current progress value
- `max`: Maximum value (default: 100)
- `type`: Progress bar color (primary, secondary, success, danger, warning, info, light, dark)
- `striped`: Boolean, adds striped effect
- `animated`: Boolean, adds animation
- `show_label`: Boolean, shows percentage label
- `height`: Progress bar height (xs, sm, md, lg, xl)
- `classes`: Additional CSS classes

## Spinner Component

```django
{% include 'components/spinner.html' with type="border" color="primary" size="sm" text="Loading..." align="center" in_button=False %}
```

**Parameters:**
- `type`: Spinner type (border, grow)
- `color`: Spinner color (primary, secondary, success, danger, warning, info, light, dark)
- `size`: Spinner size (sm)
- `text`: Loading text
- `align`: Alignment (center, right, between)
- `text_position`: Text position when align="between" (before, after)
- `in_button`: Boolean, creates spinner inside button
- `button_color`: Button color when in_button=True
- `button_disabled`: Boolean, disables button when in_button=True
- `container_class`: Container CSS classes
- `classes`: Additional CSS classes

## Accordion Component

```django
{% include 'components/accordion.html' with id="accordionExample" items=accordion_items flush=False always_open=False %}
```

**Parameters:**
- `id`: Accordion container ID
- `items`: List of accordion items (each with `title`, `content`, `id`, `collapsed`, `show`)
- `flush`: Boolean, removes default background and rounded corners
- `always_open`: Boolean, allows multiple items to be open
- `classes`: Additional CSS classes

## Modal Component

```django
{% include 'components/modal.html' with id="myModal" title="Modal Title" body="Modal content" trigger_button_text="Open Modal" size="lg" centered=True %}
```

**Parameters:**
- `id`: Modal ID
- `title`: Modal title
- `body`: Modal body content
- `trigger_button_text`: Text for the button that opens the modal
- `trigger_btn_class`: CSS classes for the trigger button
- `size`: Modal size (sm, lg, xl)
- `centered`: Boolean, vertically centers the modal
- `scrollable`: Boolean, makes modal body scrollable
- `fullscreen`: Boolean, creates fullscreen modal
- `static_backdrop`: Boolean, prevents closing by clicking outside
- `keyboard`: Boolean, prevents closing with ESC key
- `footer_content`: Custom footer content
- `modal_class`: Additional modal CSS classes
- `classes`: Additional CSS classes

## Pagination Component

```django
{% include 'components/pagination.html' with items=page_items current_page=1 alignment="center" size="lg" rounded=True %}
```

**Parameters:**
- `items`: List of pagination items (each with `number`, `url`, `active`, `disabled`)
- `current_page`: Current page number
- `alignment`: Alignment (center, end)
- `size`: Pagination size (sm, lg)
- `rounded`: Boolean, creates rounded pagination
- `show_previous`: Boolean, shows previous button
- `show_next`: Boolean, shows next button
- `previous_text`: Previous button text (default: "&laquo;")
- `next_text`: Next button text (default: "&raquo;")
- `has_previous`: Boolean, enables previous button
- `has_next`: Boolean, enables next button
- `previous_url`: Previous page URL
- `next_url`: Next page URL
- `classes`: Additional CSS classes

## Tabs Component

```django
{% include 'components/tabs.html' with tabs=tab_items active_tab="profile" type="tabs" justified=False vertical=False %}
```

**Parameters:**
- `tabs`: List of tabs (each with `id`, `title`, `content`, `icon`)
- `active_tab`: ID of the active tab
- `type`: Tab type (tabs, pills)
- `justified`: Boolean, makes tabs justified
- `vertical`: Boolean, creates vertical tabs
- `vertical_position`: Vertical tab position (left, right)
- `id`: Tabs container ID
- `classes`: Additional CSS classes

## Toast Component

```django
{% include 'components/toast.html' with id="myToast" title="Notification" message="This is a toast message" time="11 mins ago" show_close=True show_logo=True type="primary" %}
```

**Parameters:**
- `id`: Toast ID
- `title`: Toast title
- `message`: Toast message
- `time`: Time text
- `show_close`: Boolean, shows close button
- `show_logo`: Boolean, shows logo
- `logo_dark`: Dark logo path
- `logo_light`: Light logo path
- `type`: Toast type (primary, secondary, success, danger, warning, info, light, dark)
- `show`: Boolean, shows toast by default
- `autohide`: Boolean, auto-hides toast
- `delay`: Auto-hide delay in milliseconds
- `show_actions`: Boolean, shows action buttons
- `action_primary`: Primary action button text
- `action_secondary`: Secondary action button text
- `classes`: Additional CSS classes

## Popover Component

```django
{% include 'components/popover.html' with button_text="Click me" title="Popover Title" content="Popover content" placement="top" trigger="click" %}
```

**Parameters:**
- `button_text`: Popover trigger button text
- `title`: Popover title
- `content`: Popover content
- `placement`: Popover placement (top, right, bottom, left)
- `trigger`: Trigger event (click, hover, focus)
- `custom_class`: Custom CSS class
- `container`: Container element
- `btn_class`: Button CSS classes
- `disabled`: Boolean, disables the button

## Tooltip Component

```django
{% include 'components/tooltip.html' with text="Hover me" title="Tooltip Title" placement="top" custom_class="primary-tooltip" %}
```

**Parameters:**
- `text`: Tooltip trigger text
- `title`: Tooltip title
- `placement`: Tooltip placement (top, right, bottom, left)
- `custom_class`: Custom CSS class
- `element`: Element type (button, link)
- `href`: Link href when element="link"
- `btn_class`: Button CSS classes
- `link_class`: Link CSS classes

## Table Component

```django
{% include 'components/table.html' with headers=table_headers rows=table_rows striped=True hover=True bordered=True responsive=True %}
```

**Parameters:**
- `headers`: List of column headers
- `rows`: List of row data (each row is a list of cell values)
- `striped`: Boolean, adds striped rows
- `hover`: Boolean, adds hover effect
- `bordered`: Boolean, adds borders
- `borderless`: Boolean, removes borders
- `small`: Boolean, creates compact table
- `responsive`: Boolean, makes table responsive
- `dark`: Boolean, creates dark-themed table
- `classes`: Additional CSS classes

## Form Components

### Form Group Component

```django
{% include 'components/form_group.html' with label="Username" input_type="text" name="username" required=True %}
```

**Parameters:**
- `label`: Label text
- `input_type`: Input type (text, email, password, select, textarea, checkbox, radio)
- `name`: Field name
- `id`: Field ID (defaults to name)
- `value`: Field value
- `placeholder`: Placeholder text
- `required`: Boolean, marks field as required
- `disabled`: Boolean, disables the field
- `readonly`: Boolean, makes field read-only
- `size`: Field size (sm, lg)
- `validation_state`: Validation state (valid, invalid)
- `help_text`: Help text
- `validation_message`: Validation message
- `group_class`: Additional group CSS classes
- `label_class`: Additional label CSS classes
- `input_class`: Additional input CSS classes

### Form Input Component

```django
{% include 'components/form_input.html' with type="email" name="email" placeholder="Enter your email" required=True %}
```

**Parameters:**
- `type`: Input type (text, email, password, number, etc.)
- `name`: Field name
- `id`: Field ID (defaults to name)
- `value`: Field value
- `placeholder`: Placeholder text
- `required`: Boolean, marks field as required
- `disabled`: Boolean, disables the field
- `readonly`: Boolean, makes field read-only
- `size`: Field size (sm, lg)
- `validation_state`: Validation state (valid, invalid)
- `help_text`: Help text
- `validation_message`: Validation message
- `valid_message`: Valid message
- `group_class`: Additional group CSS classes
- `label_class`: Additional label CSS classes
- `input_class`: Additional input CSS classes

### Form Select Component

```django
{% include 'components/form_select.html' with name="country" label="Country" options=country_options selected="US" %}
```

**Parameters:**
- `name`: Field name
- `label`: Label text
- `options`: List of options (each with `value`, `text`, and optionally `selected`, `disabled`)
- `selected`: Selected value
- `placeholder`: Placeholder option text
- `required`: Boolean, marks field as required
- `disabled`: Boolean, disables the field
- `multiple`: Boolean, allows multiple selections
- `size_attr`: Size attribute for multiple select
- `size`: Field size (sm, lg)
- `validation_state`: Validation state (valid, invalid)
- `help_text`: Help text
- `validation_message`: Validation message
- `valid_message`: Valid message
- `group_class`: Additional group CSS classes
- `label_class`: Additional label CSS classes
- `select_class`: Additional select CSS classes

### Form Checkbox Component

```django
{% include 'components/form_checkbox.html' with name="agree" label="I agree to the terms" checked=True %}
```

**Parameters:**
- `name`: Field name
- `label`: Label text
- `value`: Field value
- `checked`: Boolean, marks checkbox as checked
- `required`: Boolean, marks field as required
- `disabled`: Boolean, disables the field
- `inline`: Boolean, displays checkbox inline
- `switch`: Boolean, creates switch-style checkbox
- `color`: Color variant (primary, secondary, success, danger, warning, info, light, dark)
- `validation_state`: Validation state (valid, invalid)
- `help_text`: Help text
- `validation_message`: Validation message
- `valid_message`: Valid message
- `group_class`: Additional group CSS classes
- `label_class`: Additional label CSS classes
- `input_class`: Additional input CSS classes

### Form Textarea Component

```django
{% include 'components/form_textarea.html' with name="message" label="Message" rows=5 placeholder="Enter your message" required=True %}
```

**Parameters:**
- `name`: Field name
- `label`: Label text
- `value`: Field value
- `placeholder`: Placeholder text
- `rows`: Number of rows
- `cols`: Number of columns
- `required`: Boolean, marks field as required
- `disabled`: Boolean, disables the field
- `readonly`: Boolean, makes field read-only
- `minlength`: Minimum length
- `maxlength`: Maximum length
- `size`: Field size (sm, lg)
- `validation_state`: Validation state (valid, invalid)
- `help_text`: Help text
- `validation_message`: Validation message
- `valid_message`: Valid message
- `group_class`: Additional group CSS classes
- `label_class`: Additional label CSS classes
- `textarea_class`: Additional textarea CSS classes

## Chart Components

### Line Chart Component

```django
{% include 'components/chart_line.html' with chart_id="sales-chart" chart_title="Sales Overview" height=400 %}
```

**Parameters:**
- `chart_id`: Unique identifier for the chart element
- `chart_title`: Title displayed above the chart
- `height`: Height of the chart in pixels

**JavaScript Initialization:**
```javascript
var options = {
  chart: {
    height: 400,
    type: 'line'
  },
  series: [{name: "Sales", data: [28, 29, 33, 36, 32, 32, 33]}],
  xaxis: {categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]}
};

var chart = new ApexCharts(document.querySelector("#sales-chart"), options);
chart.render();
```

### Pie Chart Component

```django
{% include 'components/chart_pie.html' with chart_id="market-share-chart" chart_title="Market Share" height=350 %}
```

**Parameters:**
- `chart_id`: Unique identifier for the chart element
- `chart_title`: Title displayed above the chart
- `height`: Height of the chart in pixels

**JavaScript Initialization:**
```javascript
var options = {
  chart: {
    height: 350,
    type: 'pie'
  },
  series: [44, 55, 41, 17, 15],
  labels: ["Team A", "Team B", "Team C", "Team D", "Team E"]
};

var chart = new ApexCharts(document.querySelector("#market-share-chart"), options);
chart.render();
```

For detailed usage instructions for form and chart components, see:
- `FORMS_USAGE.md` for comprehensive form component documentation
- `CHARTS_USAGE.md` for comprehensive chart component documentation