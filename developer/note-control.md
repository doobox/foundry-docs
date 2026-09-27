---
layout: default
title: Note control · Foundry Developer
permalink: "/developer/note-control.html"
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector</p>
<h1>Note</h1>
<p class="lede">Presentation-only explanatory text in an Inspector section.</p>


<figure class="control-screenshot">
    <img src="assets/screenshots/note-control.png" width="348" height="63" alt="Informational Note with an icon, title and explanatory text." />
    <figcaption>Notes display developer-supplied information rather than an editable value.</figcaption>
</figure>

## Quick example

Add this dictionary to your part's `inspector` array:

```json
{
    "type" : "note",
    "title" : "Layout",
    "body" : "Choose the spacing for this part."
}
```

This item displays guidance in the Inspector; it produces no template value.


## Basic properties

Each item in the `inspector` array defines one Inspector item. These keys set its identity and content.

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Identifies this item as Note. Always use `note`.

```json
"type" : "note"
```


<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: generated</span></div>

A note holds no value and nothing can refer to one, so you can leave `id` out and Foundry names it for you. If you do supply one, it must be unique within the part, start with a letter, and contain only letters, numbers, underscores and hyphens. It is never available as a template value.

```json
"id" : "guidance"
```

<h3 class="property-heading"><code>title</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: none</span></div>

An optional heading shown above the explanatory text. Omit this key to show the text without a heading.

```json
"title" : "About responsive settings"
```

<h3 class="property-heading"><code>body</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

The explanatory text shown across the full width of the Inspector.

```json
"body" : "Changes here affect every breakpoint."
```

<h3 class="property-heading"><code>systemImage</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: none</span></div>

The name of an SF Symbol shown in secondary colour to the left of the title. Omit this key to show no symbol.

```json
"systemImage" : "info.circle"
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

## Note options

These keys sit directly in the same custom-item dictionary. Omitted optional keys use the defaults shown.

<div class="guidance" markdown="1">
<h3>Supplying the message</h3>

Use `body` for the required explanatory copy, optionally add `title` as a heading, and use `systemImage` when the message benefits from an SF Symbol. Note content occupies the full Inspector width rather than using the standard label and value columns.

```json
"body" : "Changes here affect every breakpoint."
```

> **Important:** Note does not use `label` or `subtitle`. It is a single, presentation-only item and does not support `count` or `responsive`.
</div>

## Return value

Note is an Inspector-only item. It stores nothing and produces no template value, so templates cannot refer to it.

```text
No template value
```

## Complete example

### manifest.json

```json
"inspector" : [
    {
        "title" : "About responsive settings",
        "body" : "Changes here affect every breakpoint.",
        "systemImage" : "info.circle",
        "type" : "note"
    }
]
```

### Use it in a template

```text
No template value
```

{% endraw %}
