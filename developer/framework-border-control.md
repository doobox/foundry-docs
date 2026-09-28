---
layout: default
title: Framework border control · Foundry Developer
permalink: /developer/framework-border-control.html
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector</p>
<h1>Framework border</h1>
<p class="lede">A four-edge width editor and an optional style picker.</p>


<figure class="control-screenshot">
    <img src="assets/screenshots/framework-border-control.png?v=2" width="377" height="202" alt="Foundry’s Framework border width editor in framework mode with all four edges set to None - 0 and both pairs unlinked, above a Style row set to Solid and a separate Colour row." />
    <figcaption>The four-edge width editor with the optional Style row. The Colour row shown below is a separate framework colour control.</figcaption>
</figure>

## Quick example

Add this dictionary to your part's `inspector` array:

```json
{
    "type" : "frameworkBorder",
    "id" : "border",
    "defaults" : {
        "base" : {
            "width" : "sm"
        }
    }
}
```

Use it in the part's CSS template:

```css
:instance {
    border-width: {{ control.border.width }};
    border-style: {{ control.border.style }};
}
```

## Properties

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Always `frameworkBorder`. The four width fields are always visible. The optional Style row appears below them. Does not accept `count`, `options`, `frameworkValues`, `minimum`, `maximum`, `step`, or `unit`.

<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Unique identifier starting with a letter and containing letters, numbers, underscores or hyphens. Examples use `border`.

<h3 class="property-heading"><code>label</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: Border</span></div>

Shown in the normal Inspector label column. Empty labels also fall back to Border. The four width fields are Top, Bottom, Left and Right; the optional additional row is Style.

<h3 class="property-heading"><code>defaults</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="required">Required</span></div>

A dictionary containing the required `base` value and optional breakpoint values: `small`, `medium`, `large`, `extraLarge`, and `doubleExtraLarge`. Breakpoint entries require `responsive: true`. Every entry uses the complete value format described below; omitted breakpoints inherit the preceding enabled value. Disabled project breakpoints are skipped without discarding their declarations. A new part starts with each breakpoint entry already pinned, exactly as if the user had pinned it: its blue dot is set in the Inspector, and the user can edit or unpin it like any other pinned value.

<h3 class="property-heading"><code>defaults.base</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="required">Required</span></div>

Contains required `width` and optional `style`. No other keys are accepted.

<h3 class="property-heading"><code>defaults.base.width</code></h3>
<div class="property-meta"><span class="property-type">String or Dictionary</span><span class="required">Required</span></div>

Accepts `none`, `xs`, `sm`, `md`, `lg`, or `xl`; a custom length dictionary with exactly `value` (finite, nonnegative Number) and `unit` (`px`, `rem`, or `em`); or a dictionary containing all four `top`, `right`, `bottom`, `left` selections. Each edge accepts a token or custom length. Percentages, negative lengths, `auto`, arrays and raw CSS strings are rejected.

Framework tokens use the border-width scale in pixels. None outputs `0`. A shared default, or a four-edge dictionary whose edges are all equal, starts with both pairs linked; any differing edge starts the control fully unlinked.

A single mode button switches the whole control between framework values and custom lengths; there is no per-edge Custom choice. Framework mode shows each edge as a picker of the framework's border widths, including user-created border widths from the active framework; portable manifest defaults use the predefined tokens only. Custom mode shows a number field and unit menu (`px`, `rem`, `em`) for each edge. Switching to custom starts each edge with its framework amount in pixels; switching back to framework selects the nearest framework value for each edge.

Two link buttons connect the edges: one links Top–Bottom using Top, the other links Left–Right using Left, regardless of which end was clicked. With both pairs linked, all four edges edit together, and completing the second link copies its own pair's leading edge — Top or Left — to all four. Unlinking preserves values. Linking shares the complete selection, token or amount and unit.

<h3 class="property-heading"><code>defaults.base.style</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: solid</span></div>

One of `solid`, `dashed`, `dotted`, `double`, `none`, `hidden`, `groove`, `ridge`, `inset`, or `outset`. Applies to all sides, including when the Style row is hidden. Choosing None preserves widths.

<h3 class="property-heading"><code>showsStyle</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: false</span></div>

Shows the Style picker below widths. Otherwise the declared style is still returned.

<h3 class="property-heading"><code>responsive</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: false</span></div>

Enables responsive overrides for widths and the visible Style row. Four widths and link state are stored together; Style has its own indicator. A hidden Style row follows its declared breakpoint defaults. Use outputs in a CSS template to generate responsive styles.

<h3 class="property-heading"><code>tooltip</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: Border</span></div>

Help for the width editor. Buttons retain action-specific help.

<h3 class="property-heading"><code>subtitle</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: empty</span></div>

Supporting text beneath the width editor.

<h3 class="property-heading"><code>visibleWhen</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: shown</span></div>

Controls visibility of the whole control. See [Conditional visibility](visible-when.html). The border is not a scalar comparison source.
<h3 class="property-heading"><code>valueAvailability</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: always</span></div>

Controls when this control's value is available to templates. `always` preserves the value when the control is hidden. `whenVisible` makes `control.<id>` and its qualified derived values unavailable while `visibleWhen` is false, without discarding the stored value. `whenVisible` requires `visibleWhen`. See [Conditional visibility](visible-when.html).


## Return value

Use qualified fields; the whole border is not a CSS shorthand string.

- `width`: four CSS lengths in top, right, bottom, left order.
- `width.top`, `width.right`, `width.bottom`, `width.left`: individual CSS lengths.
- `width.css`: the same width shorthand.
- `width.values.top` (and other edges): numeric amount.
- `width.units.top` (and other edges): corresponding unit.
- `style`: CSS border-style keyword.

Framework widths return CSS variables such as `var(--foundry-border-width-sm)`. Numeric framework amounts use `px`; custom values retain entered units. None and missing tokens return zero and an empty unit. Custom zero retains its unit. Missing tokens remain marked in the editor. Numeric amounts are not browser-computed measurements.

## Example

```json
{
    "type" : "frameworkBorder",
    "id" : "border",
    "label" : "Border",
    "showsStyle" : true,
    "responsive" : true,
    "defaults" : {
        "base" : {
            "width" : "sm",
            "style" : "solid"
        }
    }
}
```

```css
:instance {
    border-width: {{ control.border.width }};
    border-style: {{ control.border.style }};
}
```

Declaring the control does not apply the border automatically. Use its width and style outputs in the CSS template.
{% endraw %}
