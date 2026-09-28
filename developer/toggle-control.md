---
layout: default
title: Toggle control · Foundry Developer
permalink: "/developer/toggle-control.html"
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector</p>
<h1>Toggle</h1>
<p class="lede">A Boolean switch.</p>


<figure class="control-screenshot">
    <img src="assets/screenshots/toggle-control.png" width="348" height="32" alt="Toggle checkbox in its enabled state." />
    <figcaption>A checkbox for a Boolean value.</figcaption>
</figure>

## Quick example

Add this dictionary to your part's `inspector` array:

```json
{
    "type" : "toggle",
    "id" : "featured",
    "defaults" : {
        "base" : false
    }
}
```

Use it in your HTML template:

```html
<div class="{{ if control.featured }}featured{{ endif }}">Content</div>
```


## Basic properties

Each item in the `inspector` array defines one Inspector item. These keys set its name, initial value and responsive behaviour where applicable.

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Identifies this item as Toggle. Always use `toggle`.

```json
"type" : "toggle"
```


<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

The unique name used to store this control and read it in templates. It must start with a letter and may contain letters, numbers, underscores and hyphens.

```json
"id" : "featured"
```

<h3 class="property-heading"><code>label</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: empty</span></div>

Text shown to the left of the control in the Inspector, including when `count` is present.

```json
"label" : "Toggle"
```

<h3 class="property-heading"><code>tooltip</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: omitted</span></div>

Help text that explains what the control changes.

```json
"tooltip" : "Choose a value."
```

<h3 class="property-heading"><code>subtitle</code></h3>
<div class="property-meta"><span class="property-type">String or String array</span><span class="optional">Optional</span><span class="default">Default: empty</span></div>

Supporting text shown beneath the control. Use a String for one control or a String array with `count`.

Single control

```json
"subtitle" : "Additional guidance"
```

Control array

```json
"subtitle" : [
    "First value",
    "Second value"
]
```

<h3 class="property-heading"><code>visibleWhen</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: shown</span></div>

Shows this control only when another control meets the stated condition.

```json
"visibleWhen" : {
    "id" : "showControl",
    "value" : true
}
```

<h3 class="property-heading"><code>valueAvailability</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: always</span></div>

Controls when this control's value is available to templates. `always` preserves the value when the control is hidden. `whenVisible` makes `control.<id>` and its qualified derived values unavailable while `visibleWhen` is false, without discarding the stored value. `whenVisible` requires `visibleWhen`. See [Conditional visibility](visible-when.html).

<h3 class="property-heading"><code>defaults</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="required">Required</span></div>

A dictionary containing the required `base` value and optional breakpoint values: `small`, `medium`, `large`, `extraLarge`, and `doubleExtraLarge`. Breakpoint entries require `responsive: true`. Every entry uses the complete value format described below; omitted breakpoints inherit the preceding enabled value. Disabled project breakpoints are skipped without discarding their declarations. A new part starts with each breakpoint entry already pinned, exactly as if the user had pinned it: its blue dot is set in the Inspector, and the user can edit or unpin it like any other pinned value.

<h3 class="property-heading"><code>defaults.base</code></h3>
<div class="property-meta"><span class="property-type">Boolean or Boolean array</span><span class="required">Required</span></div>

The value initially stored for this control. A control array needs one value for each member.

Single control

```json
"defaults" : {
    "base" : false
}
```

Control array

```json
"defaults" : {
    "base" : [
        false,
        false
    ]
}
```

<h3 class="property-heading"><code>responsive</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: false</span></div>

Set to true to allow a different value at each responsive breakpoint.

```json
"responsive" : false
```

## Toggle options

These keys sit directly in the same custom-item dictionary. Omitted optional keys use the defaults shown.

<h3 class="property-heading"><code>presentation</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: checkbox</span></div>

Chooses the Inspector control: `checkbox` (the default) or `switch` for a native macOS toggle switch. Purely presentational — the stored Boolean value and template output are identical either way.

```json
"presentation" : "switch"
```

<h3 class="property-heading"><code>count</code></h3>
<div class="property-meta"><span class="property-type">Integer</span><span class="optional">Optional</span><span class="default">Default: omitted</span></div>

Creates two to four controls that are stored as one array. Read each value with a zero-based index such as `{{ control.myControl[0] }}`.

Control array

```json
"count" : 2
```

## Return value

`{{ control.featured }}` resolves as **true or false**. Stored internally, its value is **Boolean**.

```text
{{ if control.featured }}featured{{ endif }}
```

## Complete example

### manifest.json

```json
"inspector" : [
    {
        "id" : "featured",
        "label" : "Toggle",
        "type" : "toggle",
        "defaults" : {
            "base" : false
        },
        "responsive" : false
    }
]
```

### Use it in a template

```text
{{ if control.featured }}featured{{ endif }}
```

{% endraw %}
