---
layout: default
title: Framework colour control · Foundry Developer
permalink: "/developer/framework-colour-control.html"
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector</p>
<h1>Framework colour</h1>
<p class="lede">A palette and shade selector that resolves the selected colour for templates.</p>

<figure class="control-screenshot">
    <img src="assets/screenshots/framework-colour-control.png" width="348" height="45" alt="Framework colour ribbon with an Accent shade selected, a default-shade button and a palette menu." />
    <figcaption>The shade ribbon follows the selected palette; the star selects its default shade.</figcaption>
</figure>

## Quick example

Add this dictionary to your part's `inspector` array:

```json
{
    "type" : "frameworkColor",
    "id" : "textColour",
    "label" : "Colour",
    "defaults" : {
        "base" : {
            "palette" : "text"
        }
    }
}
```

Use its resolved CSS value in your stylesheet:

```css
:instance {
    color: {{ control.textColour }};
}
```

## Choosing colours

Authors can choose from the project's custom, framework and standard colour palettes using a searchable menu. The ribbon selects a shade from 1–11; Black and White each have one colour.

Palettes resolve by identity, not display name. Custom palettes never override framework or standard palettes, even when their names match. Duplicating a palette creates an independent custom colour with a unique name. Framework palette names remain fixed; their shades are editable in user-created and imported frameworks. Built-in frameworks and standard palettes are read-only.

A part stores one palette identity and separate fixed light and dark shade numbers. Choosing a palette captures its two current defaults. Changing either palette default later does not move existing part selections. The canvas sun/moon buttons select which appearance the Inspector edits, independently of macOS appearance. The Inspector star refers to that appearance's default; clicking it selects the default without creating a live link. Edits to the selected swatch colour still update the part.

Use the separate `color` control when only a literal colour picker is needed.

## Basic properties

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Identifies this item as Framework colour. Always use `frameworkColor`. This control does not support `count`.

```json
"type" : "frameworkColor"
```

<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

The unique template name. It must start with a letter and may contain letters, numbers, underscores and hyphens.

<h3 class="property-heading"><code>label</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: empty</span></div>

Text shown to the left of the control.

<h3 class="property-heading"><code>tooltip</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: omitted</span></div>

Help text explaining what the control changes.

<h3 class="property-heading"><code>subtitle</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: empty</span></div>

Supporting text shown beneath the control.

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
<div class="property-meta"><span class="property-type">Dictionary</span><span class="required">Required</span></div>

Groups the initial palette, optional appearance-specific shades and initial opacity. The accepted keys are `palette`, `lightShade`, `darkShade`, and `opacity`. A string or array is not accepted; shade keys belong inside this dictionary, not alongside `defaults.base`. The nested numeric `opacity` requires the control-level Boolean `opacity` to be true.

<h3 class="property-heading"><code>defaults.base.palette</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

The initially selected palette. Framework roles are: `page`, `surface`, `text`, `muted`, `brand`, `accent`, or `links`. New parts capture that palette's light and dark defaults unless the corresponding shade key is supplied. `page` also supplies the page's outer background; `surface` is the raised-card layer, `brand` carries the site's identity colour and `accent` its interactive highlight. `custom` is valid only when `allowsCustom` is true, requires the control's `customColor`, and prohibits both shade keys. Standard palettes are also accepted using these stable IDs: `standard.black`, `standard.white`, `standard.red`, `standard.orange`, `standard.amber`, `standard.yellow`, `standard.lime`, `standard.green`, `standard.emerald`, `standard.teal`, `standard.cyan`, `standard.sky`, `standard.blue`, `standard.indigo`, `standard.violet`, `standard.purple`, `standard.fuchsia`, `standard.pink`, `standard.rose`, `standard.slate`, `standard.grey`, `standard.zinc`, `standard.neutral`, and `standard.stone`.

Use the exact ID, not the display name. Project-specific custom palette IDs are not accepted as portable defaults. Standard palettes do not require `allowsCustom`. Black and White have only one colour, so shade numbers do not change their rendered colour.

For example, start with Lime:

```json
"defaults" : {
    "base" : {
        "palette" : "standard.lime",
        "lightShade" : 8,
        "darkShade" : 3
    }
}
```

<h3 class="property-heading"><code>defaults.base.lightShade</code></h3>
<div class="property-meta"><span class="property-type">Integer</span><span class="optional">Optional</span><span class="default">Default: palette's light default shade</span></div>

The initial light-appearance shade number, from `1` to `11` inclusive. Omit it to capture the palette's light default when the part is created. The stored shade number does not follow subsequent default changes.

Available only inside a `frameworkColor` default dictionary with a framework-role or standard `palette`; it cannot be combined with `palette: custom`. This setting controls initial creation, not subsequent palette choices in the Inspector.

```json
"defaults" : {
    "base" : {
        "palette" : "accent",
        "lightShade" : 8,
        "darkShade" : 3
    }
}
```

<h3 class="property-heading"><code>defaults.base.darkShade</code></h3>
<div class="property-meta"><span class="property-type">Integer</span><span class="optional">Optional</span><span class="default">Default: palette's dark default shade</span></div>

The initial dark-appearance shade number, from `1` to `11` inclusive. Omit it to capture the palette's dark default when the part is created. It uses the same palette and ribbon as `lightShade`, but stores an independent fixed shade number. Available only inside a `frameworkColor` default dictionary with a framework-role or standard `palette`; it cannot be combined with `palette: custom`. It affects initial creation, not subsequent palette choices in the Inspector.

<h3 class="property-heading"><code>defaults.base.opacity</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="optional">Optional</span><span class="default">Default: 1</span></div>

Initial opacity for both appearances, from `0` (transparent) to `1` (opaque). Requires `opacity: true` on the control. Applies to framework palettes, standard palettes and custom colours. Authors can subsequently adjust light and dark opacity independently using the canvas appearance buttons. Responsive default dictionaries may also supply this value.

For a black tint starting at 20% opacity:

```json
{
    "type": "frameworkColor",
    "id": "overlayColor",
    "label": "Overlay colour",
    "allowsCustom": true,
    "opacity": true,
    "defaults": { "base": { "palette": "standard.black", "opacity": 0.2 } }
}
```

<h3 class="property-heading"><code>responsive</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: false</span></div>

Allows a different selection at each responsive breakpoint. Each breakpoint value contains one palette choice and its light and dark shade selections.

## Framework colour options

<h3 class="property-heading"><code>allowsCustom</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: false</span></div>

Adds a shippingbox mode button on the control that switches between framework palettes and a literal colour picker, matching the framework spacing and shadow controls. This permits `defaults.base.palette` to be `custom`, which also requires `customColor`. It does not control access to the project's custom palettes; those are available alongside framework and standard palettes.

<h3 class="property-heading"><code>customColor</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: #000000</span></div>

The initial literal colour for both appearances. It must be `#RRGGBB`, requires `allowsCustom` to be true, and is required when `defaults.base.palette` is `custom`. This key remains at control level, outside the `defaults.base` dictionary. Authors can subsequently edit separate light and dark literal colours using the canvas appearance buttons.

<h3 class="property-heading"><code>opacity</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: false</span></div>

Adds a 0–100% opacity slider beneath the colour control for both palette selections and Custom Colour. Also enables alpha in the custom colour picker; the picker and slider edit the same appearance-specific value. When omitted or false, no slider is shown and stored opacity is not applied to output. Use `defaults.base.opacity` to choose the initial opacity; otherwise it starts at 100%.

<h3 class="property-heading"><code>outputFormat</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: hex</span></div>

Controls how the resolved colour is supplied to templates. Only the complete-colour formats are accepted: `hex`, `rgb`, `rgba`, `hsl`, or `hsla`, with the same output shapes as the [Colour control](colour.html). The fragment formats (`hexValue`, `rgbValues`, `rgbaValues`, `hslValues`, `hslaValues`) are rejected — a framework colour must stay a complete CSS colour so it can adapt between light and dark; use the qualified `light`/`dark` fields below for embeddable fragments.

## Return value

Returns a CSS colour, not a palette ID or shade number. The canvas resolves the appearance being edited. Light-only and dark-only sites export the corresponding colour. Sites supporting both export a CSS `light-dark(light, dark)` colour, following the browser's system preference unless explicitly overridden. Palette and Custom Colour selections include their appearance-specific opacity when enabled, including in the qualified channel values. Use the result directly in CSS rather than treating it as a hexadecimal string.

For sites supporting both appearances, a part can call `window.foundryAppearance.set('light')`, `.set('dark')`, or `.set('system')` in its browser script. The visitor's choice is remembered for that site. This interface is not installed in the editing canvas or on single-appearance sites.

## Derived values

A framework colour is a light/dark pair, so its derived values come in two kinds. Colour-valued outputs stay unqualified and adapt between appearances automatically, exactly like the main value. Numeric outputs are fixed numbers baked into the published file, so they are qualified with `light` or `dark` — both are always available and always truthful, whatever the site's appearance setting.

Unqualified, appearance-aware:

- `contrastColor` returns `#FFFFFF` when white meets WCAG's 3:1 large-text contrast against that appearance's colour and `#000000` otherwise, combined into `light-dark(…)` on sites supporting both.
- The [colour filters](colour.html#colour-filters) — `lighten`, `darken`, `withAlpha`, and `mix` — apply to each appearance's colour independently and return one appearance-aware colour. `mix` with another framework colour mixes light with light and dark with dark.

```css
.card {
    background: {{ control.backgroundColor }};
    color: {{ control.backgroundColor.contrastColor }};
    border-color: {{ control.backgroundColor | darken(20) }};
}
```

Qualified with `light` or `dark`:

- `red`, `green` and `blue` return numbers from 0 through 255; `alpha` returns 0 through 1; `hue` returns degrees; `saturation` and `lightness` return percentages as numbers.
- `relativeLuminance`, `contrastColor`, `contrastRatioWithBlack` and `contrastRatioWithWhite` return that appearance's accessibility values.
- `hexValue`, `rgbValues`, `rgbaValues`, `hslValues` and `hslaValues` return embeddable fragments.
- The colour filters also chain from a qualified colour, returning that one appearance's result.

```css
:root {
    --brand-rgb: {{ control.backgroundColor.light.rgbValues }};
    --brand-rgb-dark: {{ control.backgroundColor.dark.rgbValues }};
}
```

Qualified numbers never change with the site's appearance setting: `light.red` always means "the red channel of the light selection", including while the canvas shows dark. Numeric values are usable in template expressions.

## Complete example

```json
{
    "type" : "frameworkColor",
    "id" : "backgroundColor",
    "label" : "Background",
    "allowsCustom" : true,
    "customColor" : "#3366CC",
    "opacity" : true,
    "defaults" : {
        "base" : {
            "palette" : "accent"
        }
    }
}
```

```css
background-color: {{ control.backgroundColor }};
```

{% endraw %}
