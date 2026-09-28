---
layout: default
title: Slider control · Foundry Developer
permalink: "/developer/slider-control.html"
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector</p>
<h1>Slider</h1>
<p class="lede">A continuous or stepped numeric slider. Its current value is always shown beside it, either as a label or as an editable field, and you can add tick marks, tick labels, end labels and a neutral point.</p>


<figure class="control-screenshot">
    <img src="assets/screenshots/slider-control.png" width="348" height="41" alt="Slider control set to 50 percent with a numeric value field." />
    <figcaption>With <code>editableValue</code> set to true, the slider and number field edit the same value.</figcaption>
</figure>

## Quick example

Add this dictionary to your part's `inspector` array:

```json
{
    "type" : "slider",
    "id" : "intensity",
    "minimum" : 0.0,
    "maximum" : 100.0,
    "defaults" : {
        "base" : 100.0
    }
}
```

Use it in the part's CSS template:

```css
:instance {
    filter: brightness({{ control.intensity }}%);
}
```


## Basic properties

Each item in the `inspector` array defines one Inspector item. These keys set its name, initial value and responsive behaviour where applicable.

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Identifies this item as Slider. Always use `slider`.

```json
"type" : "slider"
```


<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

The unique name used to store this control and read it in templates. It must start with a letter and may contain letters, numbers, underscores and hyphens.

```json
"id" : "intensity"
```

<h3 class="property-heading"><code>label</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: empty</span></div>

Text shown to the left of the control in the Inspector, including when `count` is present.

```json
"label" : "Slider"
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
<div class="property-meta"><span class="property-type">Number or Number array</span><span class="required">Required</span></div>

The value initially stored for this control. A value must be supplied explicitly and must be numeric and within the declared range. A control array needs one value for each member.

Single control

```json
"defaults" : {
    "base" : 50.0
}
```

Control array

```json
"defaults" : {
    "base" : [
        50.0,
        50.0
    ]
}
```

<h3 class="property-heading"><code>responsive</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: false</span></div>

Set to true to allow a different value at each responsive breakpoint.

```json
"responsive" : false
```

## Slider options

These keys sit directly in the same custom-item dictionary. Omitted optional keys use the defaults shown.

<h3 class="property-heading"><code>count</code></h3>
<div class="property-meta"><span class="property-type">Integer</span><span class="optional">Optional</span><span class="default">Default: omitted</span></div>

Creates two to four controls that are stored as one array. Read each value with a zero-based index such as `{{ control.myControl[0] }}`.

Control array

```json
"count" : 2
```

<h3 class="property-heading"><code>minimum</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="optional">Optional</span><span class="default">Default: 0</span></div>

Lower slider bound.

```json
"minimum" : 0.0
```

<h3 class="property-heading"><code>maximum</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="optional">Optional</span><span class="default">Default: 100</span></div>

Upper slider bound. It must be greater than `minimum`. Directly entered values are clamped to the resulting range.

```json
"maximum" : 100.0
```

<h3 class="property-heading"><code>step</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="optional">Optional</span><span class="default">Default: 0</span></div>

Selectable increment relative to `minimum`. It cannot be negative; zero means continuous. Directly entered values snap to a positive step.

```json
"step" : 1.0
```

<h3 class="property-heading"><code>ticks</code></h3>
<div class="property-meta"><span class="property-type">Integer</span><span class="optional">Optional</span><span class="default">Default: 0</span></div>

Exact number of evenly distributed visible marks, including both endpoints. Use zero for no marks or an integer of at least two. Ticks are visual only: `step` decides which values can be chosen. Values in `tickLabels` add their own marks, so you can use either key alone or both together.

```json
"ticks" : 11
```

<h3 class="property-heading"><code>editableValue</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: false</span></div>

How the current value is shown beside the slider. By default it is a read-only label that updates as the slider moves, shown with the unit and as many decimal places as `step` needs. Set to true to show an editable number field instead, so the user can type an exact value.

```json
"editableValue" : true
```

<h3 class="property-heading"><code>tickLabels</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: none</span></div>

Draws a labelled mark beneath the track at each listed value. Each key is a slider value written as a string, and each value is the text shown under that mark. Keys must lie within `minimum`…`maximum`. Keep labels short and few: three to five fit comfortably in the Inspector. Tick labels make the slider row taller.

```json
"tickLabels" : {
    "0" : "Auto",
    "6" : "6",
    "12" : "12"
}
```

<h3 class="property-heading"><code>valueLabels</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: none</span></div>

Replaces the read-only value beside the slider with text when the slider rests on one of the listed values. Use it when a value has a special meaning, such as 0 meaning "Auto". Templates still receive the number, so test for it with `{{ if }}`. Keys follow the same rules as `tickLabels`. It cannot be combined with `editableValue: true`, because an editable field always shows a number.

```json
"valueLabels" : {
    "0" : "Auto"
}
```

<h3 class="property-heading"><code>minimumLabel</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: none</span></div>

Shown at the left end of the track. Provide a `title`, an SF Symbol name in `systemImage`, or both. When both are present the symbol is shown, and the title becomes its tooltip and its VoiceOver label.

```json
"minimumLabel" : {
    "systemImage" : "sun.min",
    "title" : "Dim"
}
```

<h3 class="property-heading"><code>maximumLabel</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: none</span></div>

Shown at the right end of the track. It takes the same keys as `minimumLabel`.

```json
"maximumLabel" : {
    "systemImage" : "sun.max",
    "title" : "Bright"
}
```

<h3 class="property-heading"><code>neutralValue</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="optional">Optional</span><span class="default">Default: minimum</span></div>

The value the track's fill starts from. By default the fill runs from the left end to the thumb. For a value that can go either way, such as an offset from −100 to 100, set it to 0 so the fill grows outwards from the centre. It must lie within the range.

```json
"neutralValue" : 0.0
```

<h3 class="property-heading"><code>units</code></h3>
<div class="property-meta"><span class="property-type">String or Array</span><span class="optional">Optional</span><span class="default">Default: none</span></div>

Inspector-only unit label. Use a string for one slider or one array entry per multi slider. Each may contain at most three characters; units are not appended to template output.

Single control

```json
"units" : "px"
```

Control array

```json
"units" : [
    "px",
    "%"
]
```

<div class="guidance" markdown="1">
<h3>Steps and ticks are independent</h3>

`step` controls selectable values and is measured from `minimum`. Omit it or use zero for a continuous slider. `ticks` is purely visual and gives the exact number of marks, including both endpoints. For a 0–100 percentage slider in increments of 10, use a step of 10 and 11 marks.

```json
"minimum" : 0.0,
"maximum" : 100.0,
"step" : 10.0,
"ticks" : 11
```

For a 0–1000 integer slider without marks, use `step` 1 and omit `ticks`.
</div>

<div class="guidance" markdown="1">
<h3>A value that means "Auto"</h3>

To give a slider an off or automatic setting, start its range one step lower and label that value. This slider picks a row count from 1 to 12, with 0 meaning "size rows to their content":

```json
"minimum" : 0.0,
"maximum" : 12.0,
"step" : 1.0,
"tickLabels" : {
    "0" : "Auto",
    "12" : "12"
},
"valueLabels" : {
    "0" : "Auto"
}
```

The template receives 0, so test for it:

```css
{{ if control.rows > 0 }}grid-template-rows: repeat({{ control.rows }}, minmax(0, 1fr));{{ endif }}
```
</div>

## Return value

`{{ control.intensity }}` resolves as **Locale-independent numeric String**. Stored internally, its value is **Number (Double)**.

```css
filter: brightness({{ control.intensity }}%);
```

## Complete example

### manifest.json

```json
"inspector" : [
    {
        "id" : "intensity",
        "label" : "Slider",
        "type" : "slider",
        "minimum" : 0.0,
        "maximum" : 100.0,
        "step" : 10.0,
        "ticks" : 11,
        "editableValue" : true,
        "units" : "%",
        "defaults" : {
            "base" : 100.0
        },
        "responsive" : false
    }
]
```

### Use it in a template

```css
filter: brightness({{ control.intensity }}%);
```

{% endraw %}
