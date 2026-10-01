---
layout: default
title: Filters control group · Foundry Developer
permalink: /developer/filters-control-group.html
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector · control groups</p>
<h1>Filters</h1>
<p class="lede">Static and hovered visual effects, plus backdrop blur.</p>

## Quick example

Add the group to the manifest's inspector:

```json
{
  "section": "Filters",
  "systemImage": "camera.filters",
  "controls": [
    { "type": "filters", "id": "filters" }
  ]
}
```

Apply both outputs to the same element in instance-scoped CSS:

```css
:instance { {{ control.filters.css }} }
:instance:hover { {{ control.filters.hover.css }} }
```

Filters apply to the selected element's rendered appearance, including its contents. They are not background-only effects. Backdrop blur affects what is behind the element and is visible through transparent or translucent areas. The group adds no wrappers and does not force positioning or clipping.

For smooth hover changes, also declare a [Transitions group](transitions-control-group.html), apply its CSS to the normal rule, and enable it with Apply to set to All or Filters. Filter settings do not generate transitions themselves.

Non-neutral CSS filters create a stacking context and a containing block for positioned descendants, including fixed descendants. None and all-neutral settings emit `filter: none` to avoid introducing that behaviour unnecessarily. See the [CSS Filter Effects specification](https://www.w3.org/TR/filter-effects-1/). Do not apply filter animations and a JavaScript-driven filter animation such as Reveal Blur to the same element simultaneously.

## Properties

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Always `filters`.

<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Required namespace, starting with a letter and containing only letters, numbers, underscores or hyphens. This page uses `filters`; another ID changes all template prefixes.

<h3 class="property-heading"><code>defaults</code></h3>
<div class="property-meta"><span class="property-type">Object</span><span>Optional</span><span class="default">Default: {}</span></div>

Overrides initial values by local control ID. For example, start grayscale and restore colour on hover:

```json
{
  "type": "filters",
  "id": "filters",
  "defaults": {
    "filtersMode": "hover",
    "filtersGrayscale": 100,
    "filtersHoverGrayscale": 0
  }
}
```

<h3 class="property-heading"><code>visibleWhen</code></h3>
<div class="property-meta"><span class="property-type">Condition object</span><span>Optional</span><span class="default">Default: always visible</span></div>

Gates the whole group using [visibility conditions](visible-when.html). Hidden controls retain their values; visibility does not disable filtering.

<h3 class="property-heading"><code>excludeControls</code></h3>
<div class="property-meta"><span class="property-type">String array</span><span>Optional</span><span class="default">Default: []</span></div>

Removes local control IDs and visibility-dependent controls. Excluded effects do not contribute to the composed CSS. To remove an effect from both states, exclude its normal and hovered IDs.

<h3 class="property-heading"><code>allowedOptions</code></h3>
<div class="property-meta"><span class="property-type">Object of String arrays</span><span>Optional</span><span class="default">Default: {}</span></div>

Narrows the `filtersMode` and `filtersState` selects to permitted values in the specified display order. See [control groups](control-groups.html) for the shared configuration rules.

## Generated controls

<h3 class="property-heading"><code>control.filters.filtersMode</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: none</span><span>Not responsive</span></div>

Type accepts `none`, `static` or `hover`. None explicitly clears regular and backdrop filters in both outputs. Static uses normal values in both states. Hover uses separate normal and hovered values.

<h3 class="property-heading"><code>control.filters.filtersState</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: normal</span><span>Not responsive</span></div>

Inspector-only choice of `normal` or `hover`, labelled Normal and Hovered. Shown in Hover mode. It selects which settings are being edited; it does not change the exported hover behaviour.

<h3 class="property-heading"><code>control.filters.filtersBlur</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 0</span><span>Responsive</span></div>

Blur in pixels, from 0 through 100, with inspector increments of 1. The hovered counterpart is `control.filters.filtersHoverBlur`, with the same type, range and default. Normal controls appear in Static mode or while editing Normal; hovered controls appear while editing Hovered.

<h3 class="property-heading"><code>control.filters.filtersBrightness</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 100</span><span>Responsive</span></div>

Brightness in percent, from 0 through 200, with inspector increments of 1. The hovered counterpart is `control.filters.filtersHoverBrightness`, with the same type, range and default. Normal controls appear in Static mode or while editing Normal; hovered controls appear while editing Hovered.

<h3 class="property-heading"><code>control.filters.filtersContrast</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 100</span><span>Responsive</span></div>

Contrast in percent, from 0 through 200, with inspector increments of 1. The hovered counterpart is `control.filters.filtersHoverContrast`, with the same type, range and default. Normal controls appear in Static mode or while editing Normal; hovered controls appear while editing Hovered.

<h3 class="property-heading"><code>control.filters.filtersSaturate</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 100</span><span>Responsive</span></div>

Saturation in percent, from 0 through 200, with inspector increments of 1. The hovered counterpart is `control.filters.filtersHoverSaturate`, with the same type, range and default. Normal controls appear in Static mode or while editing Normal; hovered controls appear while editing Hovered.

<h3 class="property-heading"><code>control.filters.filtersGrayscale</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 0</span><span>Responsive</span></div>

Grayscale in percent, from 0 through 100, with inspector increments of 1. The hovered counterpart is `control.filters.filtersHoverGrayscale`, with the same type, range and default. Normal controls appear in Static mode or while editing Normal; hovered controls appear while editing Hovered.

<h3 class="property-heading"><code>control.filters.filtersSepia</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 0</span><span>Responsive</span></div>

Sepia in percent, from 0 through 100, with inspector increments of 1. The hovered counterpart is `control.filters.filtersHoverSepia`, with the same type, range and default. Normal controls appear in Static mode or while editing Normal; hovered controls appear while editing Hovered.

<h3 class="property-heading"><code>control.filters.filtersInvert</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 0</span><span>Responsive</span></div>

Invert in percent, from 0 through 100, with inspector increments of 1. The hovered counterpart is `control.filters.filtersHoverInvert`, with the same type, range and default. Normal controls appear in Static mode or while editing Normal; hovered controls appear while editing Hovered.

<h3 class="property-heading"><code>control.filters.filtersHueRotate</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 0</span><span>Responsive</span></div>

Hue rotation in degrees, from 0 through 360, with inspector increments of 1. The hovered counterpart is `control.filters.filtersHoverHueRotate`, with the same type, range and default. Normal controls appear in Static mode or while editing Normal; hovered controls appear while editing Hovered.

<h3 class="property-heading"><code>control.filters.filtersBackdropBlur</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 0</span><span>Responsive</span></div>

Backdrop blur in pixels, from 0 through 100, with inspector increments of 1. The hovered counterpart is `control.filters.filtersHoverBackdropBlur`, with the same type, range and default. Normal controls appear in Static mode or while editing Normal; hovered controls appear while editing Hovered. This blurs the backdrop, not the part's own content. An opaque background obscures the effect.

<h3 class="property-heading"><code>control.filters.filtersShadow</code></h3>
<div class="property-meta"><span class="property-type">Framework shadow</span><span class="default">Default: none</span><span>Responsive</span></div>

Drop shadow reuses the [Framework shadow control](framework-shadow-control.html). The hovered counterpart is `control.filters.filtersHoverShadow`, also defaulting to none. It follows the same state visibility as the numeric effects.

Unlike an Effects box shadow, this follows the rendered silhouette. Outer framework shadow layers become CSS `drop-shadow()` functions; inset layers are skipped and spread is ignored because CSS drop shadows do not support them. Blur radius is converted to the corresponding standard deviation. Multiple outer layers become successive filter functions, not independent box shadows. The resolved control value in this group is the function chain or `none`.

## Return value

<h3 class="property-heading"><code>control.filters.css</code></h3>
<div class="property-meta"><span class="property-type">CSS declarations</span></div>

Normal-state declarations for `filter`, `backdrop-filter` and `-webkit-backdrop-filter`. The regular filter order is blur, brightness, contrast, saturation, grayscale, sepia, invert, hue rotation, then drop shadow. Neutral chains resolve to `none`. Values are bounded to their control ranges.

<h3 class="property-heading"><code>control.filters.hover.css</code></h3>
<div class="property-meta"><span class="property-type">CSS declarations</span></div>

Hovered-state declarations for the same three properties. Mirrors normal output in Static mode and explicitly clears effects in None mode, so switching modes or breakpoints does not leave stale CSS.

Raw numeric controls remain available for custom composition. The group does not apply itself: use the composed declarations on the element you want to filter, without also applying them to its descendants unless compounded filtering is intended.
{% endraw %}
