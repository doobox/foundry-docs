---
layout: default
title: Framework font size control · Foundry Developer
permalink: /developer/framework-font-size-control.html
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector</p>
<h1>Framework font size</h1>
<p class="lede">A picker of the framework's font sizes that resolves the selected size — and its paired line height — for templates.</p>

## Quick example

Add this dictionary to your part's `inspector` array:

```json
{
    "type" : "frameworkFontSize",
    "id" : "textSize",
    "label" : "Size",
    "defaults" : {
        "base" : "base"
    }
}
```

Use its resolved CSS values in your stylesheet:

```css
:instance {
    font-size: {{ control.textSize }};
    line-height: {{ control.textSize.lineHeight }};
}
```

## Choosing sizes

Authors pick from the active framework's font sizes: the predefined scale (XS through 9XL) followed by the project's custom sizes. Each size carries its own line height, edited together in the framework's Font Size section, so text set with this control follows the framework when its sizes change.

Use the separate `number` control when an arbitrary length is needed instead of a framework size.

## Properties

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Always `frameworkFontSize`. It does not accept `count`, `options`, `frameworkValues`, or `allowsCustom`.

```json
"type" : "frameworkFontSize"
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

A predefined size ID: `xs`, `sm`, `base`, `lg`, `xl`, `2xl`, `3xl`, `4xl`, `5xl`, `6xl`, `7xl`, `8xl`, or `9xl`. `base` is the framework's body size, shown as MD in the Inspector. Project custom sizes appear in the picker but are not portable manifest defaults.

<h3 class="property-heading"><code>responsive</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: false</span></div>

Allows a different size selection at each responsive breakpoint.

## Return value

- `{{ control.textSize }}`: the size's CSS variable, such as `var(--foundry-font-size-xl)`.
- `{{ control.textSize.lineHeight }}`: the paired line height variable, such as `var(--foundry-font-size-xl-line-height)`.

Both outputs are CSS variable references, so published pages follow later framework edits through the stylesheet without re-rendering. Line height values are unitless multiples of the font size. A selection that no longer exists in the framework falls back to the body size.
{% endraw %}
