---
layout: default
title: Transforms control group · Foundry Developer
permalink: /developer/transforms-control-group.html
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector · control groups</p>
<h1>Transforms</h1>
<p class="lede">Scale, rotate, translate and skew, with independent normal and hovered states.</p>

## Quick example

Add the group to the manifest's inspector:

```json
{
  "section": "Transforms",
  "systemImage": "move.3d",
  "controls": [
    { "type": "transforms", "id": "transforms" }
  ]
}
```

Apply both outputs to the same element in instance-scoped CSS:

```css
:instance { {{ control.transforms.css }} }
:instance:hover { {{ control.transforms.hover.css }} }
```

Transforms apply to the selected element and its contents, without adding wrappers or forcing positioning. Use a block, inline-block, flex or grid element; ordinary non-replaced inline elements cannot be transformed.

For smooth hover changes, declare a [Transitions group](transitions-control-group.html), apply its CSS to the normal rule, and enable All or Transform. Transforms do not generate transitions themselves.

Non-neutral transforms establish a stacking context and a containing block for positioned descendants, including fixed descendants. Neutral settings emit `transform: none`. Avoid applying JavaScript-driven transform animations such as Reveal to the same element: inline animation styles can override these rules.

## Properties

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Always `transforms`.

<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Required namespace, starting with a letter and containing only letters, numbers, underscores or hyphens. This page uses `transforms`; another ID changes all template prefixes.

<h3 class="property-heading"><code>defaults</code></h3>
<div class="property-meta"><span class="property-type">Object</span><span>Optional</span><span class="default">Default: {}</span></div>

Overrides initial values by local control ID. For example, scale up on hover:

```json
{
  "type": "transforms",
  "id": "transforms",
  "defaults": {
    "transformsMode": "hover",
    "transformsScale": 100,
    "transformsHoverScale": 110
  }
}
```

<h3 class="property-heading"><code>visibleWhen</code></h3>
<div class="property-meta"><span class="property-type">Condition object</span><span>Optional</span><span class="default">Default: always visible</span></div>

Gates the whole group using [visibility conditions](visible-when.html). Hidden controls retain their values; visibility does not disable transforms.

<h3 class="property-heading"><code>excludeControls</code></h3>
<div class="property-meta"><span class="property-type">String array</span><span>Optional</span><span class="default">Default: []</span></div>

Removes local control IDs and visibility-dependent controls. Excluded effects do not contribute to the composed CSS. To remove an effect from both states, exclude its normal and hovered IDs.

<h3 class="property-heading"><code>allowedOptions</code></h3>
<div class="property-meta"><span class="property-type">Object of String arrays</span><span>Optional</span><span class="default">Default: {}</span></div>

Narrows the `transformsMode`, `transformsState` and origin selects to permitted values in the specified display order. See [control groups](control-groups.html) for the shared configuration rules.

## Generated controls

<h3 class="property-heading"><code>control.transforms.transformsMode</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: none</span><span>Not responsive</span></div>

Type accepts `none`, `static` or `hover`. None explicitly resets transform and transform origin in both outputs. Static uses normal values in both states. Hover uses separate normal and hovered values.

<h3 class="property-heading"><code>control.transforms.transformsState</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: normal</span><span>Not responsive</span></div>

Inspector-only choice of `normal` or `hover`, labelled Normal and Hovered. Shown in Hover mode. It selects which settings are being edited; it does not change the exported hover behaviour.

<h3 class="property-heading"><code>control.transforms.transformsOrigin</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: center</span><span>Responsive</span></div>

Accepts `center`, `top left`, `top`, `top right`, `left`, `right`, `bottom left`, `bottom` or `bottom right`. The hovered counterpart is `control.transforms.transformsHoverOrigin`, with the same type, constraints and default. Normal controls appear in Static mode or while editing Normal; hovered controls appear while editing Hovered.

<h3 class="property-heading"><code>control.transforms.transformsScale</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 100</span><span>Responsive</span></div>

Uniform scale in percent, from 0 through 1000, in increments of 1. The hovered counterpart is `control.transforms.transformsHoverScale`, with the same type, constraints and default. Normal controls appear in Static mode or while editing Normal; hovered controls appear while editing Hovered.

<h3 class="property-heading"><code>control.transforms.transformsRotate</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 0</span><span>Responsive</span></div>

Rotation in degrees, from -360 through 360, in increments of 1. The hovered counterpart is `control.transforms.transformsHoverRotate`, with the same type, constraints and default. Normal controls appear in Static mode or while editing Normal; hovered controls appear while editing Hovered.

<h3 class="property-heading"><code>control.transforms.transformsTranslateX</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: 0px</span><span>Responsive</span></div>

Horizontal translation. The hovered counterpart is `control.transforms.transformsHoverTranslateX`, with the same type, constraints and default. Normal controls appear in Static mode or while editing Normal; hovered controls appear while editing Hovered.

Accepts a signed decimal followed by `px`, `%`, `em`, `rem`, `vw`, `vh`, `vmin`, `vmax`, `svw`, `svh`, `lvw`, `lvh`, `dvw`, `dvh`, `ch`, `ex`, `cm`, `mm`, `in`, `pt` or `pc`. Unitless zero is accepted. Functions such as `calc()` and `var()` are not supported; invalid values resolve to `0px`.

<h3 class="property-heading"><code>control.transforms.transformsTranslateY</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: 0px</span><span>Responsive</span></div>

Vertical translation. The hovered counterpart is `control.transforms.transformsHoverTranslateY`, with the same type, constraints and default. Normal controls appear in Static mode or while editing Normal; hovered controls appear while editing Hovered.

Accepts a signed decimal followed by `px`, `%`, `em`, `rem`, `vw`, `vh`, `vmin`, `vmax`, `svw`, `svh`, `lvw`, `lvh`, `dvw`, `dvh`, `ch`, `ex`, `cm`, `mm`, `in`, `pt` or `pc`. Unitless zero is accepted. Functions such as `calc()` and `var()` are not supported; invalid values resolve to `0px`.

<h3 class="property-heading"><code>control.transforms.transformsSkewX</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 0</span><span>Responsive</span></div>

Horizontal skew in degrees, from -89 through 89, in increments of 1. The hovered counterpart is `control.transforms.transformsHoverSkewX`, with the same type, constraints and default. Normal controls appear in Static mode or while editing Normal; hovered controls appear while editing Hovered.

<h3 class="property-heading"><code>control.transforms.transformsSkewY</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 0</span><span>Responsive</span></div>

Vertical skew in degrees, from -89 through 89, in increments of 1. The hovered counterpart is `control.transforms.transformsHoverSkewY`, with the same type, constraints and default. Normal controls appear in Static mode or while editing Normal; hovered controls appear while editing Hovered.

## Return value

<h3 class="property-heading"><code>control.transforms.css</code></h3>
<div class="property-meta"><span class="property-type">CSS declarations</span></div>

Normal-state `transform` and `transform-origin` declarations. The transform list is translate, rotate, skew, then scale (CSS applies the rightmost operation first). Numeric values are bounded to their control ranges. Neutral values emit `transform: none`.

<h3 class="property-heading"><code>control.transforms.hover.css</code></h3>
<div class="property-meta"><span class="property-type">CSS declarations</span></div>

Hovered-state declarations for the same properties. Mirrors the normal output in Static mode and resets both properties in None mode. Inspector state selection does not affect this output.

Individual controls remain available for custom composition. The group does not apply itself: place both outputs on the intended element.
{% endraw %}
