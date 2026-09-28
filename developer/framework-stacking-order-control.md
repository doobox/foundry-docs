---
layout: default
title: Framework stacking order control · Foundry Developer
permalink: /developer/framework-stacking-order-control.html
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector</p>
<h1>Framework stacking order</h1>
<p class="lede">A picker of the framework's stacking-order tokens that resolves the selected z-index for templates.</p>

## Quick example

Add this dictionary to your part's `inspector` array:

```json
{
    "type" : "frameworkStackingOrder",
    "id" : "layer",
    "label" : "Layer",
    "defaults" : {
        "base" : "base"
    }
}
```

Use its resolved CSS value in your stylesheet:

```css
:instance {
    position: relative;
    z-index: {{ control.layer }};
}
```

## Choosing values

Authors pick from the active framework's stacking order: the project's custom values first, then the predefined tokens (Base through Toast). The values are edited in the framework's Stacking Order section, so parts using this control follow the framework when its values change.

A mode button beside the control switches between framework values and a custom number, matching the framework spacing controls. Framework mode shows the token picker; custom mode shows an integer field. Switching to custom starts with the selected token's own value; switching back to framework selects the nearest token.

## Properties

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Always `frameworkStackingOrder`. It does not accept `count`, `options`, `frameworkValues`, or `allowsCustom`.

```json
"type" : "frameworkStackingOrder"
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

Shows this control only when another control meets the declared condition. See [Conditional visibility](visible-when.html).

<h3 class="property-heading"><code>valueAvailability</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: always</span></div>

Controls when this control's value is available to templates. `always` preserves the value when the control is hidden. `whenVisible` makes `control.<id>` and its qualified derived values unavailable while `visibleWhen` is false, without discarding the stored value. `whenVisible` requires `visibleWhen`. See [Conditional visibility](visible-when.html).

<h3 class="property-heading"><code>defaults</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="required">Required</span></div>

A dictionary containing the required `base` value and optional breakpoint values: `small`, `medium`, `large`, `extraLarge`, and `doubleExtraLarge`. Breakpoint entries require `responsive: true`; omitted breakpoints inherit the preceding enabled value. Disabled project breakpoints are skipped without discarding their declarations. A new part starts with each breakpoint entry already pinned, exactly as if the user had pinned it: its blue dot is set in the Inspector, and the user can edit or unpin it like any other pinned value.

<h3 class="property-heading"><code>defaults.base</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

A predefined stacking ID: `base`, `dropdown`, `sticky`, `overlay`, `modal`, `tooltip`, or `toast`. Project custom values appear in the picker but are not portable manifest defaults.

<h3 class="property-heading"><code>responsive</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: false</span></div>

Allows a different selection at each responsive breakpoint.

## Return value

`{{ control.layer }}` resolves to the token's CSS variable, such as `var(--foundry-z-index-modal)`, so published pages follow later framework edits through the stylesheet without re-rendering. A custom number resolves to the entered integer. A selection that no longer exists in the framework falls back to the Base token.
{% endraw %}
