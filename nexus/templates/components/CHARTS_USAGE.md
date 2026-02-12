# Chart Components Usage Guide

This document explains how to use the reusable chart components in your Django templates.

## Line Chart Component

### Basic Usage

```django
{% include 'components/chart_line.html' with
    chart_id="sales-chart"
    chart_title="Sales Overview"
    height=400
%}
```

### Required Data Structure

For the line chart, you need to provide series data in the following format:

```python
# In your view
series_data = [
    {
        "name": "Series 1",
        "data": [28, 29, 33, 36, 32, 32, 33]
    },
    {
        "name": "Series 2",
        "data": [12, 11, 14, 18, 17, 13, 13]
    }
]

xaxis_categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]
```

### Complete Example

```django
{% include 'components/chart_line.html' with
    chart_id="sales-chart"
    chart_title="Monthly Sales"
    series_data=series_data
    xaxis_categories=xaxis_categories
    height=400
%}

<script>
// Initialize the chart after including the component
var options = {
  chart: {
    height: 400,
    type: 'line',
    zoom: { enabled: false },
    toolbar: { show: false }
  },
  colors: ['#6658dd', '#1abc9c'],
  dataLabels: { enabled: true },
  stroke: {
    width: 3,
    curve: 'smooth'
  },
  series: {{ series_data|safe }},
  title: {
    text: 'Monthly Sales',
    align: 'left'
  },
  grid: {
    borderColor: '#f1f3fa'
  },
  xaxis: {
    categories: {{ xaxis_categories|safe }}
  }
};

var chart = new ApexCharts(document.querySelector("#sales-chart"), options);
chart.render();
</script>
```

## Pie Chart Component

### Basic Usage

```django
{% include 'components/chart_pie.html' with
    chart_id="market-share-chart"
    chart_title="Market Share"
    height=350
%}
```

### Required Data Structure

For the pie chart, you need to provide series data and labels:

```python
# In your view
series_data = [44, 55, 41, 17, 15]
labels = ["Team A", "Team B", "Team C", "Team D", "Team E"]
colors = ["#6658dd", "#4fc6e1", "#4a81d4", "#00b19d", "#f1556c"]
```

### Complete Example

```django
{% include 'components/chart_pie.html' with
    chart_id="market-share-chart"
    chart_title="Market Share"
    series_data=series_data
    labels=labels
    colors=colors
    height=350
%}

<script>
// Initialize the chart after including the component
var options = {
  chart: {
    height: 350,
    type: 'pie'
  },
  series: {{ series_data|safe }},
  labels: {{ labels|safe }},
  colors: {{ colors|safe }},
  legend: {
    position: 'bottom'
  }
};

var chart = new ApexCharts(document.querySelector("#market-share-chart"), options);
chart.render();
</script>
```

## Required Assets

Make sure to include the ApexCharts library in your base template:

```django
{% block extra_javascript %}
<script src="{% static 'vendor/apexcharts/apexcharts.min.js' %}"></script>
{% endblock %}
```

## Customization Options

Both chart components accept the following parameters:

- `chart_id`: Unique identifier for the chart element
- `chart_title`: Title displayed above the chart
- `height`: Height of the chart in pixels
- `series_data`: Data series for the chart (passed as JSON)
- `xaxis_categories`: X-axis labels (for line charts)
- `labels`: Labels for data points (for pie charts)
- `colors`: Color scheme for the chart

Additional customization can be done by modifying the JavaScript initialization code as shown in the examples above.