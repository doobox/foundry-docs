---
layout: default
title: Framework radius control · Foundry Developer
permalink: "/developer/framework-radius-control.html"
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector</p>
<h1>Framework radius</h1>
<p class="lede">A four-corner box editor with framework radius, custom lengths, and coordinated linking.</p>


<figure class="control-screenshot">
    <img src="assets/screenshots/framework-radius-control.png?v=2" width="374" height="112" alt="Foundry’s Framework radius grid editor in framework mode with all four corners set to 2XL - 24px and the link ring unlinked." />
    <figcaption>Each corner's picker sits at its own corner, joined by the all-or-none link ring. The box button switches every corner between framework and custom values.</figcaption>
</figure>

## Quick example

Add this dictionary to your part's `inspector` array:

```json
{
    "type" : "frameworkRadius",
    "id" : "frameworkRadius",
    "defaults" : {
        "base" : "sm"
    }
}
```

Use it in the part's CSS template:

```css
:instance {
    border-radius: {{ control.frameworkRadius }};
}
```

## Properties

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Always `frameworkRadius`. This is a dedicated control, not a Select extension.

The control includes all four corners and built-in custom inputs. It does not accept `count`, `options`, `frameworkValues`, `allowsCustom`, `minimum`, `maximum`, `step`, or a top-level `unit`. Only the properties listed on this page are accepted.

<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Unique control identifier, starting with a letter and containing letters, numbers, underscores or hyphens. Templates access its fields through `{{ control.yourID.topLeft }}` or its complete shorthand through `{{ control.yourID }}`.

<h3 class="property-heading"><code>label</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: Radius</span></div>

The control's label in the Inspector's normal left-hand label column. An omitted, empty or whitespace-only label displays Radius. The four corner fields are Top Left, Top Right, Bottom Left and Bottom Right.

<h3 class="property-heading"><code>defaults</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="required">Required</span></div>

A dictionary containing the required `base` value and optional breakpoint values: `small`, `medium`, `large`, `extraLarge`, and `doubleExtraLarge`. Breakpoint entries require `responsive: true`. Every entry uses the complete value format described below; omitted breakpoints inherit the preceding enabled value. Disabled project breakpoints are skipped without discarding their declarations. A new part starts with each breakpoint entry already pinned, exactly as if the user had pinned it: its blue dot is set in the Inspector, and the user can edit or unpin it like any other pinned value.

<h3 class="property-heading"><code>defaults.base</code></h3>
<div class="property-meta"><span class="property-type">String or Dictionary</span><span class="required">Required</span></div>

Declare one value for every corner, or a dictionary containing all four keys: `topLeft`, `topRight`, `bottomRight` and `bottomLeft`. Each corner accepts either:

- A portable framework radius ID: `xs`, `sm`, `md`, `lg`, `xl`, `2xl`, or `full`.
- `none`, which produces zero radius.
- A custom length dictionary containing exactly `value` (a finite, nonnegative Number) and `unit` (String: `px`, `rem`, `em`, or `%`).

A single token or custom length dictionary applies to all four corners. Four-corner dictionaries must include every corner and no other keys. Arrays, raw CSS strings such as `"16px"`, negative lengths and `auto` are not accepted. Only the predefined radius token IDs are supported; the framework sets their pixel values. `full` is a framework token (9,999px in the standard framework), not a percentage. Elliptical radii with separate horizontal/vertical values are not supported.

```json
"defaults" : {
    "base" : "sm"
}
```

For different initial values:

```json
"defaults" : {
    "base" : {
        "topLeft" : "lg",
        "topRight" : "sm",
        "bottomRight" : "lg",
        "bottomLeft" : {
            "value" : 1.5,
            "unit" : "rem"
        }
    }
}
```

Each corner's field sits at its own corner of a two-by-two grid. A shared default, or a four-corner dictionary whose corners are all equal, starts linked; any differing corner starts the control unlinked. All four corner fields remain visible in every state.

A single mode button switches the whole control between framework values and custom lengths; there is no per-corner Custom choice. Framework mode shows each corner as a picker of the framework's radius values, including user-created radii from the active framework; portable manifest defaults use the predefined tokens only. Custom mode shows a number field and unit menu (`px`, `rem`, `em`, `%`) for each corner. Switching to custom starts each corner with its framework amount in pixels; switching back to framework selects the nearest framework value for each corner.

One link joins all four corners — there is no pair linking. It is drawn as a ring of segments between adjacent fields, and clicking any segment toggles it. Linked, every corner shares one selection, and completing the link copies Top Left to all four. Unlinking preserves values and makes every corner independent. Linking shares the complete selection, token or amount and unit; it does not merely copy the displayed number.

<h3 class="property-heading"><code>responsive</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: false</span></div>

Allows the whole four-corner value to override at a responsive breakpoint. There is one responsive indicator beside the main label, not one per corner. Editing at an overridden breakpoint stores all four selections and their link state together. Use the returned fields in the part's CSS template to generate responsive styles. Radius is shared between light and dark appearances.

<h3 class="property-heading"><code>tooltip</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: Radius</span></div>

Help text for the overall control. Individual buttons retain their action-specific help.

<h3 class="property-heading"><code>subtitle</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: empty</span></div>

Supporting text beneath the four-corner editor. Arrays are not accepted because this control does not support `count`.

<h3 class="property-heading"><code>visibleWhen</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: shown</span></div>

Shows the complete control when another control meets the declared condition. See [Conditional visibility](visible-when.html). Radius itself is a structured value, not a scalar comparison source.
<h3 class="property-heading"><code>valueAvailability</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: always</span></div>

Controls when this control's value is available to templates. `always` preserves the value when the control is hidden. `whenVisible` makes `control.<id>` and its qualified derived values unavailable while `visibleWhen` is false, without discarding the stored value. `whenVisible` requires `visibleWhen`. See [Conditional visibility](visible-when.html).


## Return value

Use `{{ control.frameworkRadius }}` directly to output the four CSS lengths in shorthand order: top left, top right, bottom right, bottom left. Qualified fields remain available:

- `topLeft`, `topRight`, `bottomRight`, `bottomLeft`: resolved CSS lengths.
- `css`: the four lengths in CSS shorthand order: top left, top right, bottom right, bottom left.
- `values`: an object containing the numeric amount for each corner (`topLeft`, `topRight`, `bottomRight`, `bottomLeft`).
- `units`: an object containing the corresponding unit String for each corner.

Framework choices resolve to CSS variable references, such as `var(--foundry-border-radius-sm)`, so framework edits continue to affect the part. Custom lengths include their units. None resolves to `0`. A missing framework radius choice remains marked as missing in the Inspector and resolves to `0` until replaced.

Do not append units to the CSS shorthand or individual CSS corner fields. Declaring the control does not apply radius automatically; the template chooses where to use it.

For calculations or JavaScript, use `values` together with `units`:

```text
{{ control.frameworkRadius.topLeft }}        → var(--foundry-border-radius-sm)
{{ control.frameworkRadius.values.topLeft }} → 4
{{ control.frameworkRadius.units.topLeft }}  → px
```

This example uses the standard framework's SM radius. Framework radius amounts resolve from the current framework in `px`; custom lengths retain their entered amount and unit (`px`, `rem`, `em`, or `%`). None and missing framework choices return numeric `0` and an empty unit String. A custom zero retains its chosen unit.

These amounts are not browser-computed pixel measurements: `1rem`, `1px`, and `1%` are different lengths. Framework amounts reflect the framework at rendering time, not later CSS variable overrides. Keep using the CSS fields for styles that should follow CSS variables.

## Example

Declare this item inside the `inspector` array in `manifest.json`:

```json
{
    "type" : "frameworkRadius",
    "id" : "frameworkRadius",
    "label" : "Content radius",
    "defaults" : {
        "base" : "sm"
    },
    "responsive" : true
}
```

Use it in the part's CSS template:

```css
:instance {
    border-radius: {{ control.frameworkRadius }};
}
```

Or apply individual corners:

```css
:instance {
    border-top-left-radius: {{ control.frameworkRadius.topLeft }};
    border-top-right-radius: {{ control.frameworkRadius.topRight }};
    border-bottom-right-radius: {{ control.frameworkRadius.bottomRight }};
    border-bottom-left-radius: {{ control.frameworkRadius.bottomLeft }};
}
```
{% endraw %}
