---
layout: default
title: Collection control · Foundry Developer
permalink: "/developer/collection-control.html"
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector</p>
<h1>Collection</h1>
<p class="lede">Let someone manage an ordered set of records, with a declared group of controls for every item.</p>

## Quick example

This collection gives every card its own image, title and description:

```json
{
    "type" : "collection",
    "id" : "cards",
    "label" : "Cards",
    "itemLabel" : "Card",
    "controls" : [
        {
            "type" : "image",
            "id" : "image",
            "label" : "Image",
            "responsive" : true
        },
        {
            "type" : "text",
            "id" : "title",
            "label" : "Title",
            "responsive" : true,
            "defaults" : {
                "base" : "Gallery item"
            }
        },
        {
            "type" : "textArea",
            "id" : "description",
            "label" : "Description",
            "defaults" : {
                "base" : "Describe this item."
            }
        },
        {
            "type" : "link",
            "id" : "link",
            "label" : "Link",
            "defaults" : {
                "base" : ""
            }
        }
    ],
    "defaults" : {
        "base" : []
    }
}
```

Loop over the records and read each field by its declared id:

```html
<div class="gallery">
    {{ loop control.cards as card }}
    <article {{ loop.attributes }}>
        {{ if card.image }}<img src="{{ card.image }}" alt="{{ card.image.alt }}">{{ endif }}
        <h2>{{ card.title }}</h2>
        <p>{{ card.description }}</p>
        {{ if card.link }}<a href="{{ card.link }}" target="{{ card.link.target }}" {{ card.link.attributes }}>View</a>{{ endif }}
    </article>
    {{ endloop }}
</div>
```

The Inspector keeps the collection and its selected item together. The Collection row has previous and next arrows, an item menu, an add button and an actions menu. The selected item's declared controls appear directly beneath it using the same Inspector UI as ordinary controls.

Add `{{ loop.attributes }}` to the repeated item's outer element. It produces no published markup, but on the editing canvas it lets Foundry activate the corresponding item in the Inspector when someone clicks that rendered item.

## Properties

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span><span class="default">Value: collection</span></div>

Declares an ordered collection. Collections do not support `responsive` or `count`.

```json
"type" : "collection"
```

<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

The unique control and template value name.

```json
"id" : "cards"
```

Read the array as `control.cards` and normally use it with a template loop.

<h3 class="property-heading"><code>label</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: empty</span></div>

The text shown for the Collection navigator row in the Inspector.

```json
"label" : "Cards"
```

<h3 class="property-heading"><code>subtitle</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: empty</span></div>

Supporting text shown beneath the Collection row.

```json
"subtitle" : "Add and arrange the cards shown in this gallery."
```

<h3 class="property-heading"><code>itemLabel</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: Item</span></div>

The singular name used by the navigator for each record and its actions.

```json
"itemLabel" : "Card"
```

<h3 class="property-heading"><code>controls</code></h3>
<div class="property-meta"><span class="property-type">Array of Dictionaries</span><span class="required">Required</span></div>

Declares the controls repeated for every record. The array must not be empty and every control needs a unique id. Ordinary controls use the same Inspector presentation, value resolution and responsive behavior as their standalone equivalents. A collection cannot contain another `collection`, a `childPicker`, or the derived `math` control.

Nested controls use their normal declarations, including `label`, `subtitle`, `defaults`, `responsive`, `count`, `visibleWhen` and `valueAvailability`. Responsive values belong to the selected item and use the ordinary breakpoint indicator and inheritance behavior. The collection's item order and membership remain global rather than changing by breakpoint.

```json
"controls" : [
    {
        "type" : "text",
        "id" : "caption",
        "label" : "Caption",
        "defaults" : {
            "base" : ""
        }
    },
    {
        "type" : "image",
        "id" : "image",
        "label" : "Image"
    }
]
```

<h3 class="property-heading"><code>defaults</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="required">Required</span></div>

Contains a `base` array of initial records. Use an empty array to start with no items. Each record is a dictionary whose keys match the nested control ids. Omitted fields receive their declared control defaults.

```json
"defaults" : {
    "base" : [
        {
            "title" : "First card",
            "description" : "The first item in the collection."
        },
        {
            "title" : "Second card",
            "description" : "Items retain their values when reordered."
        }
    ]
}
```

Media defaults must use declared package asset paths, just as they do for standalone image, SVG and video controls.

<h3 class="property-heading"><code>tooltip</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: omitted</span></div>

Help text shown when the pointer rests on the Collection row.

<h3 class="property-heading"><code>visibleWhen</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: shown</span></div>

Conditionally shows the complete Collection row. A hidden collection retains its records.

<h3 class="property-heading"><code>valueAvailability</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: always</span></div>

Use `always` to keep the collection available to templates while its row is hidden, or `whenVisible` to make the value unavailable while `visibleWhen` is false. The stored records are preserved. `whenVisible` requires `visibleWhen`.

## Template values

`control.cards` is an ordered array. A loop alias represents the current record, and each declared field is available as a member of that alias:

```html
{{ loop control.cards as card }}
    {{ card.image }}
    {{ card.title }}
    {{ card.description }}
{{ endloop }}
```

Image, SVG and video fields produce the selected resource path. Foundry resolves imported resources for both the editing canvas and published output.

Link fields expose the same values as a standalone link: the resolved destination at `card.link`, the target at `card.link.target`, and custom attributes at `card.link.attributes`.

Image and SVG fields also expose their normal alternative text as `<field>.alt`. For example, an image field named `image` is available as `card.image`, with its alternative text at `card.image.alt`. When focal-point editing is enabled, `card.image.focalPointX` and `card.image.focalPointY` contain percentages.

Collection items have stable internal identities, so their values stay attached to the correct record when items are moved or duplicated. Those identities are managed by Foundry and are not part of the template API.
{% endraw %}
