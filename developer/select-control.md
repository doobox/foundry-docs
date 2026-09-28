---
layout: default
title: Select control · Foundry Developer
permalink: "/developer/select-control.html"
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector</p>
<h1>Select</h1>
<p class="lede">A native popup containing explicitly declared options.</p>


<figure class="control-screenshot">
    <img src="assets/screenshots/select-control.png" width="348" height="39" alt="Select control with One selected." />
    <figcaption>The selected option is shown in a compact menu picker.</figcaption>
</figure>

## Quick example

Add this dictionary to your part's `inspector` array:

```json
{
    "type" : "select",
    "id" : "layout",
    "options" : [
        {
            "value" : "block",
            "title" : "Block"
        },
        {
            "value" : "flex",
            "title" : "Flex"
        }
    ],
    "defaults" : {
        "base" : "block"
    }
}
```

Use it in the part's CSS template:

```css
:instance {
    display: {{ control.layout }};
}
```


## Basic properties

Each item in the `inspector` array defines one Inspector item. These keys set its name, initial value and responsive behaviour where applicable.

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Identifies this item as a Select. Always use `select`.

```json
"type" : "select"
```


<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

The unique name used to store this Select and read it in templates. It must start with a letter and may contain letters, numbers, underscores and hyphens.

```json
"id" : "mySelect"
```

> Replace `mySelect` with your own identifier. The name is not predefined, but it must be unique in the part and follow the identifier rules above.

<h3 class="property-heading"><code>label</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: empty</span></div>

Text shown to the left of the Select in the Inspector, including for a [Multi Select](#count).

```json
"label" : "Font Size"
```

<h3 class="property-heading"><code>tooltip</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: omitted</span></div>

Help text that explains what the Select changes.

```json
"tooltip" : "Choose the text size."
```

<h3 class="property-heading"><code>subtitle</code></h3>
<div class="property-meta"><span class="property-type">String or String array</span><span class="optional">Optional</span><span class="default">Default: empty</span></div>

Supporting text shown beneath the control. Use a String for one control or a String array with `count`.

Single control

```json
"subtitle" : "Additional guidance"
```

Multi Select

```json
"subtitle" : [
    "Small screen",
    "Large screen"
]
```

<h3 class="property-heading"><code>visibleWhen</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: shown</span></div>

Shows this Select only when another control meets the stated condition.

```json
"visibleWhen" : {
    "id" : "showTypography",
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
<div class="property-meta"><span class="property-type">String or String array</span><span class="required">Required</span></div>

The initially selected value. Use a declared option value. A Multi Select needs one value per popup.

Single Select

```json
"defaults" : {
    "base" : "base"
}
```

Multi Select

```json
"defaults" : {
    "base" : [
        "compact",
        "comfortable"
    ]
}
```

> Use the `value` of a declared option.

<h3 class="property-heading"><code>responsive</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: false</span></div>

Set to true to allow a different selected value at each responsive breakpoint.

```json
"responsive" : false
```

## Select options

These keys sit directly in the same custom-item dictionary. Omitted optional keys use the defaults shown.

<h3 class="property-heading"><code>presentation</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: menu</span></div>

Use <code>menu</code> for the standard popup or <code>segmented</code> for an inline segmented picker.

```json
"presentation" : "segmented"
```

<h3 class="property-heading"><code>count</code></h3>
<div class="property-meta"><span class="property-type">Integer</span><span class="optional">Optional</span><span class="default">Default: omitted</span></div>

Creates two to four popups that share the same declared options. Their values are stored as an array and read in templates using a zero-based index.

Multi Select

```json
"count" : 2
```

Template access

```text
{{ control.mySelect[0] }}
{{ control.mySelect[1] }}
```

> **Template access uses a zero-based index.** Use `{{ control.mySelect[0] }}` for the first value and `{{ control.mySelect[1] }}` for the second.

<h3 class="property-heading"><code>options</code></h3>
<div class="property-meta"><span class="property-type">Array of dictionaries</span><span class="optional">Optional</span><span class="default">Default: \[\]</span></div>

Lists choices supplied by the part. Each dictionary needs a value to store and a title to show in the popup.

```json
"options" : [
    {
        "value" : "compact",
        "title" : "Compact"
    },
    {
        "value" : "comfortable",
        "title" : "Comfortable"
    }
]
```

Each option may include a <code>systemImage</code> String containing an SF Symbol name. Segmented controls display the symbol in place of the visible title while retaining <code>title</code> as the accessible label and help text.

```json
{
    "value" : "image",
    "title" : "Image",
    "systemImage" : "photo"
}
```

Select offers only the options declared here. It does not populate choices from the framework. Use a dedicated framework control for framework-aware editing.

## Return value

`{{ control.layout }}` returns the selected option's String value unchanged. With `count`, it returns an array of those strings, accessed by zero-based index.

## Complete example

### manifest.json

```json
"inspector" : [
    {
        "type" : "select",
        "id" : "layout",
        "label" : "Layout",
        "options" : [
            {
                "value" : "block",
                "title" : "Block"
            },
            {
                "value" : "flex",
                "title" : "Flex"
            }
        ],
        "defaults" : {
            "base" : "block"
        },
        "responsive" : false
    }
]
```

### Use it in a template

```css
display: {{ control.layout }};
```

{% endraw %}
