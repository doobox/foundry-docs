---
layout: default
title: Icon control · Foundry Developer
permalink: "/developer/icon-control.html"
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector</p>
<h1>Icon</h1>
<p class="lede">A searchable visual picker containing every icon in Foundry’s built-in icon library.</p>


<figure class="control-screenshot">
    <img src="assets/screenshots/icon-control.png" width="348" height="41" alt="Icon picker with Stars selected." />
    <figcaption>The picker shows the selected icon beside its name.</figcaption>
</figure>

## Quick example

Add this dictionary to your part's `inspector` array:

```json
{
    "type" : "icon",
    "id" : "symbol",
    "defaults" : {
        "base" : "stars"
    }
}
```

Use it in your HTML template:

```html
<i class="bi bi-{{ control.symbol }}" aria-hidden="true"></i>
```


## Basic properties

Each item in the `inspector` array defines one Inspector item. These keys set its name, initial value and responsive behaviour.

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Identifies this item as an Icon control. Always use `icon`.

```json
"type" : "icon"
```


<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

The unique name used to store this control and read it in templates. It must start with a letter and may contain letters, numbers, underscores and hyphens.

```json
"id" : "symbol"
```

<h3 class="property-heading"><code>label</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: empty</span></div>

Text shown to the left of the control in the Inspector, including when `count` is present.

```json
"label" : "Icon"
```

<h3 class="property-heading"><code>tooltip</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: omitted</span></div>

Help text that explains what the control changes.

```json
"tooltip" : "Choose an icon."
```

<h3 class="property-heading"><code>subtitle</code></h3>
<div class="property-meta"><span class="property-type">String or String array</span><span class="optional">Optional</span><span class="default">Default: empty</span></div>

Supporting text shown beneath the picker. With `count`, use an array containing no more than one subtitle for each picker; entries correspond by zero-based index.

```json
"subtitle" : "Additional guidance"
```

<h3 class="property-heading"><code>visibleWhen</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: shown</span></div>

Shows this control only when another control meets the stated condition. See [Conditional visibility](visible-when.html).

<h3 class="property-heading"><code>valueAvailability</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: always</span></div>

Controls when this control's value is available to templates. `always` preserves the value when the control is hidden. `whenVisible` makes `control.<id>` and its qualified derived values unavailable while `visibleWhen` is false, without discarding the stored value. `whenVisible` requires `visibleWhen`. See [Conditional visibility](visible-when.html).

<h3 class="property-heading"><code>defaults</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="required">Required</span></div>

A dictionary containing the required `base` value and optional breakpoint values: `small`, `medium`, `large`, `extraLarge`, and `doubleExtraLarge`. Breakpoint entries require `responsive: true`. Every entry uses the complete value format described below; omitted breakpoints inherit the preceding enabled value. Disabled project breakpoints are skipped without discarding their declarations. A new part starts with each breakpoint entry already pinned, exactly as if the user had pinned it: its blue dot is set in the Inspector, and the user can edit or unpin it like any other pinned value.

<h3 class="property-heading"><code>defaults.base</code></h3>
<div class="property-meta"><span class="property-type">String or String array</span><span class="required">Required</span></div>

An icon name from Foundry’s built-in catalogue, without the `bi-` prefix. A control array needs one value for each member.

```json
"defaults" : {
    "base" : "stars"
}
```

<h3 class="property-heading"><code>responsive</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: false</span></div>

Set to true to allow a different icon at each responsive breakpoint.

```json
"responsive" : false
```

## Icon options

<h3 class="property-heading"><code>count</code></h3>
<div class="property-meta"><span class="property-type">Integer</span><span class="optional">Optional</span><span class="default">Default: omitted</span></div>

Creates two to four icon controls stored as one array. Read each value using a zero-based index.

When `count` is present, `defaults.base` must be an array containing exactly `count` valid icon names.

```json
"count" : 2,
"subtitle" : [
    "Previous",
    "Next"
],
"defaults" : {
    "base" : [
        "arrow-left",
        "arrow-right"
    ]
}
```

## Built-in icon library

An Icon control automatically includes Foundry’s bundled Bootstrap Icons CSS and font in preview and published output. Do not add a `libraries` declaration for it. Foundry includes the library once even when a part declares several Icon controls or a page uses several parts containing them.

## Return value

`{{ control.symbol }}` resolves as an **HTML-escaped icon name without the `bi-` prefix**. A single Icon stores a **String**; a multi Icon stores a **String array**.

```html
<i class="bi bi-{{ control.symbol }}" aria-hidden="true"></i>
```

For a multi Icon, read each name by zero-based index.

```html
<i class="bi bi-{{ control.directions[0] }}" aria-hidden="true"></i>
<i class="bi bi-{{ control.directions[1] }}" aria-hidden="true"></i>
```

## Complete example

### manifest.json

```json
"inspector" : [
    {
        "type" : "icon",
        "id" : "symbol",
        "label" : "Icon",
        "defaults" : {
            "base" : "stars"
        }
    }
]
```

### Use it in a template

```html
<i class="bi bi-{{ control.symbol }}" aria-hidden="true"></i>
```

{% endraw %}
