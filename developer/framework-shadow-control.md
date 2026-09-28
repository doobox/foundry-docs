---
layout: default
title: Framework shadow control · Foundry Developer
permalink: "/developer/framework-shadow-control.html"
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector</p>
<h1>Framework shadow</h1>
<p class="lede">A framework shadow picker with an optional author-editable stack of outer or inset shadow layers behind the framework-mode toggle.</p>


<figure class="control-screenshot">
    <img src="assets/screenshots/shadow-control.png" width="348" height="38" alt="Shadow picker with MD selected." />
    <figcaption>A compact picker for the selected shadow preset.</figcaption>
</figure>

## Quick example

Add this dictionary to your part's `inspector` array:

```json
{
    "type" : "frameworkShadow",
    "id" : "cardShadow",
    "defaults" : {
        "base" : "md"
    }
}
```

Use it in the part's CSS template:

```css
:instance {
    box-shadow: {{ control.cardShadow }};
}
```


## Basic properties

Each item in the `inspector` array defines one Inspector item. These keys set its name, initial value and responsive behaviour where applicable.

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Identifies this item as a Framework shadow control. Always use `frameworkShadow`.

```json
"type" : "frameworkShadow"
```


<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

The unique name used to store this control and read it in templates. It must start with a letter and may contain letters, numbers, underscores and hyphens.

```json
"id" : "cardShadow"
```

<h3 class="property-heading"><code>label</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: empty</span></div>

Text shown beside the Framework shadow control in the Inspector.

```json
"label" : "Shadow"
```

<h3 class="property-heading"><code>tooltip</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: omitted</span></div>

Help text that explains what the control changes.

```json
"tooltip" : "Choose a value."
```

<h3 class="property-heading"><code>subtitle</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: empty</span></div>

Supporting text shown beneath the control.

```json
"subtitle" : "Additional guidance"
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
<div class="property-meta"><span class="property-type">Value</span><span class="required">Required</span></div>

The initially selected portable framework shadow. Use `none`, `inner`, `xs`, `sm`, `md`, `lg`, `xl` or `2xl`; use `custom` only when Custom is enabled. `sm` is the standard default-sized shadow.

```json
"defaults" : {
    "base" : "md"
}
```

> Use a portable predefined shadow ID. Use `custom` only when `allowsCustom` is true. Project-specific custom shadow IDs can be selected by an author but are not portable manifest defaults.

<h3 class="property-heading"><code>responsive</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: false</span></div>

Set to true to allow the selected framework shadow or custom layer stack to vary at each responsive breakpoint.

```json
"responsive" : false
```

## Shadow options

These keys sit directly in the same custom-item dictionary. Omitted optional keys use the defaults shown. Do not declare `frameworkValues` or `count`: Framework shadow uses the active framework automatically and edits one shadow value.

<h3 class="property-heading"><code>allowsCustom</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: false</span></div>

Enables custom mode. The control shows the framework-mode toggle to the picker's right; switching it off replaces the picker with the editable shadow-layer stack, exactly as the framework spacing controls switch between tokens and custom values.

```json
"allowsCustom" : true
```

> Custom layers are author-owned. The manifest enables the editor but does not declare initial layer values; Foundry supplies the initial editable layer.

<div class="guidance" markdown="1">
<h3>Framework and custom shadows</h3>

The popup lists custom shadows from the active project framework followed by the predefined scale. Portable predefined IDs are `none`, `inner`, `xs`, `sm`, `md`, `lg`, `xl` and `2xl`. Do not declare `frameworkValues`; this control loads framework shadows automatically.

The framework-mode toggle beside the picker switches to a custom layer editor. Each layer has horizontal and vertical offsets, blur, spread, colour, opacity and an outer or inset position. Multiple layers produce a comma-separated CSS value; no layers produce `none`.

> **Important:** Framework selections resolve through the active project framework. Custom layers store horizontal and vertical offsets, blur, spread, colour, opacity and outer or inset position together under this property ID.
</div>

## Return value

`{{ control.cardShadow }}` resolves as **CSS-ready box-shadow String**. Stored internally, its value is **One structured shadow value**.

```css
box-shadow: {{ control.cardShadow }};
```

## Complete example

### manifest.json

```json
"inspector" : [
    {
        "id" : "cardShadow",
        "label" : "Shadow",
        "type" : "frameworkShadow",
        "allowsCustom" : true,
        "defaults" : {
            "base" : "md"
        },
        "responsive" : false
    }
]
```

### Use it in a template

```css
box-shadow: {{ control.cardShadow }};
```

{% endraw %}
