---
layout: default
title: Divider control · Foundry Developer
permalink: "/developer/divider-control.html"
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector</p>
<h1>Divider</h1>
<p class="lede">A presentation-only visual separator between inspector controls.</p>


<figure class="control-screenshot">
    <img src="assets/screenshots/divider-control.png" width="348" height="82" alt="An expanded Inspector section containing a thin horizontal divider." />
    <figcaption>A Divider adds a visual separator, not an editable value.</figcaption>
</figure>

## Quick example

Add this dictionary to your part's `inspector` array:

```json
{
    "type" : "divider"
}
```

This item only separates Inspector controls; it produces no template value.


## Basic properties

Each item in the `inspector` array defines one Inspector item. A Divider has no editable value and is used only to separate nearby controls visually.

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Identifies this item as Divider. Always use `divider`.

```json
"type" : "divider"
```

> **Important:** Divider supports only `type`, an optional `id`, and an optional `visibleWhen`. It has no author-editable state or template value.


<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: generated</span></div>

A divider holds no value and nothing can refer to one, so you can leave `id` out and Foundry names it for you. If you do supply one, it must be unique within the part, start with a letter, and contain only letters, numbers, underscores and hyphens.

```json
"id" : "separator"
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

Divider does not support `label`, `subtitle`, `tooltip`, `defaults`, `responsive`, or `count`.

Foundry displays 5 points of space above and below the divider, on top of the normal spacing between controls. To add space without a line, use a [spacer](spacer-control.html).

## Return value

Divider is an Inspector-only layout item. It does not produce a template value.

```text
No template value
```

## Complete example

### manifest.json

```json
"inspector" : [
    {
        "type" : "divider"
    }
]
```

### Use it in a template

```text
No template value
```

{% endraw %}
