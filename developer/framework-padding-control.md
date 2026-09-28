---
layout: default
title: Framework padding control · Foundry Developer
permalink: "/developer/framework-padding-control.html"
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector</p>
<h1>Framework padding</h1>
<p class="lede">A four-edge box editor with framework spacing, custom lengths, and coordinated linking.</p>

<figure class="control-screenshot">
    <img src="assets/screenshots/framework-padding-control.png?v=2" width="372" height="140" alt="Foundry’s Framework padding box editor in framework mode with Top and Bottom set to XL - 3rem, Left and Right set to MD - 1.5rem, and both pairs unlinked." />
    <figcaption>All four edge fields stay visible in every state. Dashed lines link each pair, and the box button switches every edge between framework and custom values.</figcaption>
</figure>

## Quick example

Add this dictionary to your part's `inspector` array:

```json
{
    "type" : "frameworkPadding",
    "id" : "frameworkPadding",
    "defaults" : {
        "base" : "sm"
    }
}
```

Use it in the part's CSS template:

```css
:instance {
    padding: {{ control.frameworkPadding }};
}
```

## Properties

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Always `frameworkPadding`. This is a dedicated control, not a Select extension.

The control includes all four edges and built-in custom inputs. It does not accept `count`, `options`, `frameworkValues`, `allowsCustom`, `minimum`, `maximum`, `step`, or a top-level `unit`. Only the properties listed on this page are accepted.

<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Unique control identifier, starting with a letter and containing letters, numbers, underscores or hyphens. Templates access its fields through `{{ control.yourID.top }}` or its complete shorthand through `{{ control.yourID }}`.

<h3 class="property-heading"><code>label</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: Padding</span></div>

The control's label in the Inspector's normal left-hand label column. An omitted, empty or whitespace-only label displays Padding. The four edge fields are Top, Bottom, Left and Right.

<h3 class="property-heading"><code>defaults</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="required">Required</span></div>

A dictionary containing the required `base` value and optional breakpoint values: `small`, `medium`, `large`, `extraLarge`, and `doubleExtraLarge`. Breakpoint entries require `responsive: true`. Every entry uses the complete value format described below; omitted breakpoints inherit the preceding enabled value. Disabled project breakpoints are skipped without discarding their declarations. A new part starts with each breakpoint entry already pinned, exactly as if the user had pinned it: its blue dot is set in the Inspector, and the user can edit or unpin it like any other pinned value.

<h3 class="property-heading"><code>defaults.base</code></h3>
<div class="property-meta"><span class="property-type">String or Dictionary</span><span class="required">Required</span></div>

Declare one value for every edge, or a dictionary containing all four keys: `top`, `right`, `bottom` and `left`. Each edge accepts either:

- A portable framework spacing ID: `3xs`, `2xs`, `xs`, `sm`, `md`, `lg`, `xl`, `2xl`, `3xl`, or `4xl`.
- `none`, which produces zero padding.
- A custom length dictionary containing exactly `value` (a finite, nonnegative Number) and `unit` (String: `px`, `rem`, `em`, or `%`).

A single token or custom length dictionary applies to all four edges. Four-edge dictionaries must include every edge and no other keys. Arrays, raw CSS strings such as `"16px"`, negative lengths and `auto` are not accepted. Project-specific custom framework IDs cannot be declared as portable defaults; authors select them from the active framework in the Inspector.

```json
"defaults" : {
    "base" : "sm"
}
```

For different initial values:

```json
"defaults" : {
    "base" : {
        "top" : "lg",
        "right" : "sm",
        "bottom" : "lg",
        "left" : {
            "value" : 1.5,
            "unit" : "rem"
        }
    }
}
```

A shared default, or a four-edge dictionary whose edges are all equal, starts with both pairs linked; any differing edge starts the control fully unlinked. All four edge fields remain visible in every state.

A single mode button switches the whole control between framework values and custom lengths; there is no per-edge Custom choice. Framework mode shows each edge as a picker of the active framework's spacing values. Custom mode shows a number field and unit menu (`px`, `rem`, `em`, `%`) for each edge. Switching to custom starts each edge with its framework amount in rem; switching back to framework selects the nearest framework value for each edge.

Two link buttons connect the edges: one links Top–Bottom using Top, the other links Left–Right using Left, regardless of which end was clicked. With both pairs linked, all four edges edit together, and completing the second link copies its own pair's leading edge — Top or Left — to all four. Unlinking preserves values. Linking shares the complete selection, token or amount and unit; it does not merely copy the displayed number.

<h3 class="property-heading"><code>responsive</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: false</span></div>

Allows the whole four-edge value to override at a responsive breakpoint. There is one responsive indicator beside the main label, not one per edge. Editing at an overridden breakpoint stores all four selections and their link state together. Use the returned fields in the part's CSS template to generate responsive styles. Padding is shared between light and dark appearances.

<h3 class="property-heading"><code>tooltip</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: Padding</span></div>

Help text for the overall control. Individual buttons retain their action-specific help.

<h3 class="property-heading"><code>subtitle</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: empty</span></div>

Supporting text beneath the four-edge editor. Arrays are not accepted because this control does not support `count`.

<h3 class="property-heading"><code>visibleWhen</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: shown</span></div>

Shows the complete control when another control meets the declared condition. See [Conditional visibility](visible-when.html). Padding itself is a structured value, not a scalar comparison source.
<h3 class="property-heading"><code>valueAvailability</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: always</span></div>

Controls when this control's value is available to templates. `always` preserves the value when the control is hidden. `whenVisible` makes `control.<id>` and its qualified derived values unavailable while `visibleWhen` is false, without discarding the stored value. `whenVisible` requires `visibleWhen`. See [Conditional visibility](visible-when.html).


## Return value

Use `{{ control.frameworkPadding }}` directly to output the four CSS lengths in shorthand order: top, right, bottom, left. Qualified fields remain available:

- `top`, `right`, `bottom`, `left`: resolved CSS lengths.
- `css`: the four lengths in CSS shorthand order: top, right, bottom, left.
- `values`: an object containing the numeric amount for each edge (`top`, `right`, `bottom`, `left`).
- `units`: an object containing the corresponding unit String for each edge.

Framework choices resolve to CSS variable references, such as `var(--foundry-space-sm)`, so framework edits continue to affect the part. Custom lengths include their units. None resolves to `0`. A removed custom framework spacing choice remains marked as missing in the Inspector and resolves to `0` until replaced.

Do not append units to the CSS shorthand or individual CSS edge fields. Declaring the control does not apply padding automatically; the template chooses where to use it.

For calculations or JavaScript, use `values` together with `units`:

```text
{{ control.frameworkPadding.top }}        → var(--foundry-space-sm)
{{ control.frameworkPadding.values.top }} → 1
{{ control.frameworkPadding.units.top }}  → rem
```

This example uses the standard framework's SM spacing. Framework spacing amounts resolve from the current framework in `rem`; custom lengths retain their entered amount and unit (`px`, `rem`, `em`, or `%`). None and missing framework choices return numeric `0` and an empty unit String. A custom zero retains its chosen unit.

These amounts are not browser-computed pixel measurements: `1rem`, `1px`, and `1%` are different lengths. Framework amounts reflect the framework at rendering time, not later CSS variable overrides. Keep using the CSS fields for styles that should follow CSS variables.

## Example

Declare this item inside the `inspector` array in `manifest.json`:

```json
{
    "type" : "frameworkPadding",
    "id" : "frameworkPadding",
    "label" : "Content padding",
    "defaults" : {
        "base" : "sm"
    },
    "responsive" : true
}
```

Use it in the part's CSS template:

```css
:instance {
    padding: {{ control.frameworkPadding }};
}
```

Or apply individual edges:

```css
:instance {
    padding-top: {{ control.frameworkPadding.top }};
    padding-right: {{ control.frameworkPadding.right }};
    padding-bottom: {{ control.frameworkPadding.bottom }};
    padding-left: {{ control.frameworkPadding.left }};
}
```
{% endraw %}
