---
layout: default
title: Framework spacing control · Foundry Developer
permalink: /developer/framework-spacing-control.html
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector</p>
<h1>Framework spacing</h1>
<p class="lede">A single framework-aware spacing value with custom lengths. Label and apply it wherever a nonnegative spacing value is needed.</p>


<figure class="control-screenshot">
    <img src="assets/screenshots/framework-spacing-control.png?v=2" width="381" height="38" alt="Framework spacing picker labelled Row Gap with MD - 1.5rem selected, beside the framework/custom mode button." />
    <figcaption>Developers supply the label; this example uses the spacing value as a row gap. The box button switches between framework and custom values.</figcaption>
</figure>

## Quick example

Add this dictionary to your part's `inspector` array:

```json
{
    "type" : "frameworkSpacing",
    "id" : "gap",
    "defaults" : {
        "base" : "sm"
    }
}
```

Use it in the part's CSS template:

```css
:instance {
    display: flex;
    gap: {{ control.gap }};
}
```

## Properties

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Always `frameworkSpacing`. This is a single value, without edge rows or linking. It does not accept `count`, `options`, `frameworkValues`, `allowsCustom`, `minimum`, `maximum`, `step`, or a top-level `unit`.

<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Unique identifier starting with a letter and containing letters, numbers, underscores or hyphens. Examples use `gap`.

<h3 class="property-heading"><code>label</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: Spacing</span></div>

Developer-supplied label in the normal Inspector row grid. Empty or whitespace-only labels fall back to Spacing.

<h3 class="property-heading"><code>defaults</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="required">Required</span></div>

A dictionary containing the required `base` value and optional breakpoint values: `small`, `medium`, `large`, `extraLarge`, and `doubleExtraLarge`. Breakpoint entries require `responsive: true`. Every entry uses the complete value format described below; omitted breakpoints inherit the preceding enabled value. Disabled project breakpoints are skipped without discarding their declarations. A new part starts with each breakpoint entry already pinned, exactly as if the user had pinned it: its blue dot is set in the Inspector, and the user can edit or unpin it like any other pinned value.

<h3 class="property-heading"><code>defaults.base</code></h3>
<div class="property-meta"><span class="property-type">String or Dictionary</span><span class="required">Required</span></div>

A framework spacing token (`3xs`, `2xs`, `xs`, `sm`, `md`, `lg`, `xl`, `2xl`, `3xl`, `4xl`), `none`, or a custom length dictionary containing exactly `value` (finite, nonnegative Number) and `unit` (`px`, `rem`, `em`, `%`). Arrays, edge dictionaries, negative lengths, `auto`, and raw CSS strings such as `16px` are rejected.

The picker offers the current framework’s spacing choices, including user-created framework spacing values. Portable manifest defaults use the predefined tokens above.

A mode button beside the control switches between framework values and a custom length, matching the four-edge spacing controls. Framework mode shows the framework-value picker; custom mode shows a number field with a unit menu. Switching to custom starts with the selected framework amount in rem; switching back to framework selects the nearest framework value.

```json
"defaults" : {
    "base" : {
        "value" : 1.5,
        "unit" : "rem"
    }
}
```

<h3 class="property-heading"><code>responsive</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: false</span></div>

Allows the selection to override at a responsive breakpoint. Use the output in the part’s CSS template for responsive rules. The selection is shared between light and dark appearances.

<h3 class="property-heading"><code>noneValue</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: 0</span></div>

The CSS emitted when the user chooses None. Without it, None becomes `0`, which is right for a gap or a minimum. Properties whose "no constraint" is spelt differently need their own keyword: `none` for a maximum, `auto` for a width or flex basis, `normal` for a gap that should fall back to the browser's own value. The string is written into the CSS as given, so it must be a valid value for the property the template applies it to.

Only the CSS output changes. `{{ control.<id>.value }}` still returns `0` and `{{ control.<id>.unit }}` an empty string. Choosing None is a user action; `noneValue` does not make None the default, which stays whatever `defaults.base` says.

This lets a template interpolate the control unconditionally rather than guarding it. The built-in Sizing group uses it for its limits: minimums emit `0`, maximums emit `none`.

```json
{
    "type" : "frameworkSpacing",
    "id" : "maxWidth",
    "label" : "Max width",
    "noneValue" : "none",
    "defaults" : {
        "base" : "none"
    }
}
```

```css
:instance {
    max-width: {{ control.maxWidth }};
}
```

Only `frameworkSpacing` accepts `noneValue`. The four-edge padding and margin controls always emit `0` for None, and other control types reject the key.

<h3 class="property-heading"><code>tooltip</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: Spacing</span></div>

Help text for the control.

<h3 class="property-heading"><code>subtitle</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: empty</span></div>

Supporting text beneath the control.

<h3 class="property-heading"><code>visibleWhen</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: shown</span></div>

Shows the control when another control meets the condition. See [Conditional visibility](visible-when.html). Spacing itself is structured and is not a scalar comparison source.
<h3 class="property-heading"><code>valueAvailability</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: always</span></div>

Controls when this control's value is available to templates. `always` preserves the value when the control is hidden. `whenVisible` makes `control.<id>` and its qualified derived values unavailable while `visibleWhen` is false, without discarding the stored value. `whenVisible` requires `visibleWhen`. See [Conditional visibility](visible-when.html).


## Return value

- `{{ control.gap }}`: resolved CSS length, such as `var(--foundry-space-sm)`.
- `{{ control.gap.css }}`: the same CSS length.
- `{{ control.gap.value }}`: numeric amount.
- `{{ control.gap.unit }}`: corresponding unit.

Framework amounts resolve in `rem`; custom amounts retain their entered unit. None and missing framework choices resolve to CSS `0`, numeric `0`, and an empty unit; set `noneValue` to emit a different CSS keyword in that case. A custom zero retains its chosen unit. Missing choices remain marked in the Inspector until replaced.

Do not append units to the CSS output. Numeric amounts are not browser-computed pixels: use the unit alongside the number. Framework amounts reflect the framework at render time, not subsequent CSS variable overrides.

## Example

```json
{
    "type" : "frameworkSpacing",
    "id" : "gap",
    "label" : "Gap",
    "defaults" : {
        "base" : "sm"
    },
    "responsive" : true
}
```

```css
:instance {
    display: flex;
    gap: {{ control.gap }};
}
```

Declaring the control does not apply spacing automatically. The template chooses the CSS property. For independent row and column gaps, declare two controls with different IDs and labels.
{% endraw %}
