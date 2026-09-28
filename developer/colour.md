---
layout: default
title: Colour control · Foundry Developer
permalink: "/developer/colour.html"
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector</p>
<h1>Colour</h1>
<p class="lede">A colour picker that supplies a literal hexadecimal colour to templates.</p>


<figure class="control-screenshot">
    <img src="assets/screenshots/colour.png" width="348" height="234" alt="Literal colour wells showing opaque, opacity-enabled and indexed colour examples." />
    <figcaption>Colour wells support opacity and indexed arrays when declared.</figcaption>
</figure>

## Quick example

Add this dictionary to your part's `inspector` array:

```json
{
    "type" : "color",
    "id" : "textColor",
    "defaults" : {
        "base" : "#3366CC"
    }
}
```

Use it in the part's CSS template:

```css
:instance {
    color: {{ control.textColor }};
}
```

## Basic properties

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Identifies this item as Colour. Always use `color`.

```json
"type" : "color"
```

<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

The unique template name. It must start with a letter and may contain letters, numbers, underscores and hyphens.

<h3 class="property-heading"><code>label</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: empty</span></div>

Text shown to the left of the control, including when `count` is present.

<h3 class="property-heading"><code>tooltip</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: omitted</span></div>

Help text explaining what the control changes.

<h3 class="property-heading"><code>subtitle</code></h3>
<div class="property-meta"><span class="property-type">String or String array</span><span class="optional">Optional</span><span class="default">Default: empty</span></div>

Supporting text beneath the control. Use a String for one control or an indexed String array with `count`.

<h3 class="property-heading"><code>visibleWhen</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: shown</span></div>

Shows this control only when another control meets the declared condition.

<h3 class="property-heading"><code>valueAvailability</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: always</span></div>

Controls when this control's value is available to templates. `always` preserves the value when the control is hidden. `whenVisible` makes `control.<id>` and its qualified derived values unavailable while `visibleWhen` is false, without discarding the stored value. `whenVisible` requires `visibleWhen`. See [Conditional visibility](visible-when.html).

<h3 class="property-heading"><code>defaults</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="required">Required</span></div>

A dictionary containing the required `base` value and optional breakpoint values: `small`, `medium`, `large`, `extraLarge`, and `doubleExtraLarge`. Breakpoint entries require `responsive: true`. Every entry uses the complete value format described below; omitted breakpoints inherit the preceding enabled value. Disabled project breakpoints are skipped without discarding their declarations. A new part starts with each breakpoint entry already pinned, exactly as if the user had pinned it: its blue dot is set in the Inspector, and the user can edit or unpin it like any other pinned value.

<h3 class="property-heading"><code>defaults.base</code></h3>
<div class="property-meta"><span class="property-type">String or String array</span><span class="required">Required</span></div>

The initial colour. Use `#RRGGBB`, or `#RRGGBBAA` when `opacity` is true. With `count`, provide exactly one colour per picker.

```json
"defaults" : {
    "base" : "#3366CC"
}
```

<h3 class="property-heading"><code>responsive</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: false</span></div>

Allows a different colour at each responsive breakpoint.

## Colour options

<h3 class="property-heading"><code>count</code></h3>
<div class="property-meta"><span class="property-type">Integer</span><span class="optional">Optional</span><span class="default">Default: omitted</span></div>

Creates two to four colour pickers stored and returned as one indexed array.

<h3 class="property-heading"><code>opacity</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: false</span></div>

Allows alpha. Transparent selections may be returned using CSS functional colour syntax.

<h3 class="property-heading"><code>outputFormat</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: hex</span></div>

Controls how the colour is supplied to templates. The selected format applies to every value when `count` is present.

- `hex` returns `#FF3366`, or `#FF336680` when `opacity` is true.
- `hexValue` returns `FF3366`, or `FF336680` when `opacity` is true.
- `rgb` returns `rgb(255 51 102)`, or `rgb(255 51 102 / 0.502)` when `opacity` is true.
- `rgba` returns `rgba(255, 51, 102, 0.502)`.
- `rgbValues` returns `255, 51, 102`.
- `rgbaValues` returns `255, 51, 102, 0.502`.
- `hsl` returns `hsl(345 100% 60%)`, or `hsl(345 100% 60% / 0.502)` when `opacity` is true.
- `hsla` returns `hsla(345, 100%, 60%, 0.502)`.
- `hslValues` returns `345, 100%, 60%`.
- `hslaValues` returns `345, 100%, 60%, 0.502`.

The explicitly alpha-bearing `rgba`, `rgbaValues`, `hsla` and `hslaValues` formats return alpha `1` when `opacity` is false. `rgbValues` and `hslValues` intentionally omit alpha so they can be embedded in custom CSS expressions.

```json
"outputFormat" : "rgbValues"
```

```css
:root {
    --brand-rgb: {{ control.brandColor }};
}

.example {
    background: rgba(var(--brand-rgb), 0.6);
}
```

## Individual colour channels

Named channel values are available regardless of `outputFormat`:

- `red`, `green` and `blue` return numbers from 0 through 255.
- `alpha` returns a number from 0 through 1.
- `hue` returns degrees from 0 up to 360.
- `saturation` and `lightness` return percentages as numbers from 0 through 100.

```text
{{ control.brandColor.red }}
{{ control.brandColor.green }}
{{ control.brandColor.blue }}
{{ control.brandColor.alpha }}
{{ control.brandColor.hue }}
{{ control.brandColor.saturation }}
{{ control.brandColor.lightness }}
```

With `count`, place the colour index before the named channel:

```text
{{ control.palette[0].red }}
{{ control.palette[1].alpha }}
{{ control.palette[2].hue }}
```

Channels are numeric, so they can also be used in template expressions.

## Accessibility values

Each colour also provides values that help choose readable foreground colours:

- `relativeLuminance` returns the WCAG relative luminance from 0 through 1.
- `contrastColor` returns `#FFFFFF` when white meets WCAG's 3:1 large-text contrast against the colour, and `#000000` otherwise. This matches the text colour designers choose in practice: the raw ratio comparison would pick black on saturated mid colours where white is the everyday choice.
- `contrastRatioWithBlack` and `contrastRatioWithWhite` return the corresponding WCAG contrast ratios.

```html
<div style="background: {{ control.brandColor }}; color: {{ control.brandColor.contrastColor }}">
    Readable text
</div>
```

For an array, put the index before the named value, such as `control.palette[0].contrastColor`.

## Colour filters

Colour filters derive a colour in the template without adding another Inspector control. They preserve the control's `outputFormat` and may be chained from left to right.

- `lighten(percentage)` mixes the colour with white.
- `darken(percentage)` mixes the colour with black.
- `withAlpha(value)` replaces its alpha with a value from 0 through 1.
- `mix("#RRGGBB", percentage)` mixes towards another colour. The target may also use `#RRGGBBAA`.

Arguments may be literals or compatible control values. Use a Number control for percentages and alpha, and a Colour control for `mix`'s target colour.

```css
.card {
    background: {{ control.brandColor | lighten(15) }};
    border-color: {{ control.brandColor | darken(20) }};
    box-shadow: 0 8px 24px {{ control.brandColor | withAlpha(0.25) }};
}

.card:hover {
    background: {{ control.brandColor | mix(control.hoverColor, control.mixAmount) }};
}
```

Filters are calculated only where they appear in a template. They do not change the value stored by the Inspector.

## Return value

Returns the selected colour string using `outputFormat`. With `count`, it returns an indexed array in the selected format.

```css
color: {{ control.textColor }};
```

## Complete example

```json
{
    "type" : "color",
    "id" : "textColor",
    "label" : "Text colour",
    "opacity" : true,
    "defaults" : {
        "base" : "#3366CC"
    }
}
```

{% endraw %}
