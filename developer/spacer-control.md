---
layout: default
title: Spacer control · Foundry Developer
permalink: "/developer/spacer-control.html"
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector</p>
<h1>Spacer</h1>
<p class="lede">Presentation-only vertical space between inspector controls.</p>

## Quick example

Add this dictionary to your part's `inspector` array:

```json
{
    "type" : "spacer"
}
```

This item only adds space between Inspector controls; it produces no template value.


## Basic properties

Each item in the `inspector` array defines one Inspector item. A Spacer has no editable value and is used only to separate nearby controls.

Foundry spaces every control evenly, the same distance apart as the rows inside a multi-part control. Use a spacer wherever you want a clearer break, and a [divider](divider-control.html) when the break should also draw a line.

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Identifies this item as Spacer. Always use `spacer`.

```json
"type" : "spacer"
```

> **Important:** Spacer supports only `type`, an optional `height`, an optional `id`, and an optional `visibleWhen`. It has no author-editable state or template value.


<h3 class="property-heading"><code>height</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="optional">Optional</span><span class="default">Default: 10</span></div>

The height of the space in points, from 1 to 30.

```json
"height" : 20
```

<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: generated</span></div>

A spacer holds no value and nothing can refer to one, so you can leave `id` out and Foundry names it for you. If you do supply one, it must be unique within the part, start with a letter, and contain only letters, numbers, underscores and hyphens.

```json
"id" : "gap"
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

Spacer does not support `label`, `subtitle`, `tooltip`, `defaults`, `responsive`, or `count`.

## Return value

Spacer is an Inspector-only layout item. It does not produce a template value.

```text
No template value
```

## Complete example

### manifest.json

```json
"inspector" : [
    {
        "type" : "spacer",
        "height" : 20
    }
]
```

### Use it in a template

```text
No template value
```

{% endraw %}
