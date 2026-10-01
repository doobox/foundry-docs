---
layout: default
title: Transitions control group · Foundry Developer
permalink: /developer/transitions-control-group.html
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector · control groups</p>
<h1>Transitions</h1>
<p class="lede">Control how CSS properties change between states.</p>

## Quick example

Add this entry to the manifest's inspector:

```json
{
  "section": "Transitions",
  "systemImage": "circle.dotted.circle",
  "controls": [
    { "type": "transitions", "id": "transitions" }
  ]
}
```

Place the composed declarations on the element whose appearance changes, in its normal rule so both entering and leaving a state use the same timing:

```css
:instance { {{ control.transitions.css }} }
:instance:hover { background-color: #334155; }
```

The group starts disabled. Enabling it uses All, Ease-in-out, 300ms duration and zero delay. It does not create hover styles itself. Built-in visual parts expose the group on their root; Navigation also applies it to its links, underline indicators and menu-toggle bars. Nested parts retain their own transition settings.

Only browser-interpolable changes animate. Switching background images or gradients does not crossfade them; automatic heights and display changes are not made animatable by this group. Reveal entrance animations and video playback remain separate.

## Properties

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Always `transitions`.

<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

The group's namespace. It must start with a letter and contain only letters, numbers, underscores or hyphens. This page uses `transitions`; another ID changes every template prefix accordingly.

<h3 class="property-heading"><code>defaults</code></h3>
<div class="property-meta"><span class="property-type">Object</span><span>Optional</span><span class="default">Default: {}</span></div>

Overrides initial values by local control ID. For example:

```json
{
  "type": "transitions",
  "id": "transitions",
  "defaults": {
    "transitionsEnabled": true,
    "transitionProperty": "colors",
    "transitionDuration": 200
  }
}
```

<h3 class="property-heading"><code>visibleWhen</code></h3>
<div class="property-meta"><span class="property-type">Condition object</span><span>Optional</span><span class="default">Default: always visible</span></div>

Controls visibility of the entire group using the shared [visibility conditions](visible-when.html). Hiding the group does not disable its output.

<h3 class="property-heading"><code>excludeControls</code></h3>
<div class="property-meta"><span class="property-type">String array</span><span>Optional</span><span class="default">Default: []</span></div>

Removes named local controls and their visibility-dependent controls. Missing timing controls use the group's standard timing values. Without `transitionsEnabled`, the composed output is disabled.

<h3 class="property-heading"><code>allowedOptions</code></h3>
<div class="property-meta"><span class="property-type">Object of String arrays</span><span>Optional</span><span class="default">Default: {}</span></div>

Narrows select choices by local ID, such as `transitionProperty` or `transitionFunction`. Lists contain the permitted values in display order. See [control groups](control-groups.html) for shared configuration rules.

## Generated controls

All five controls are responsive. An Enable switch gates the other four.

<h3 class="property-heading"><code>control.transitions.transitionsEnabled</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="default">Default: false</span><span>Responsive</span></div>

Enables the transition. Disabled output explicitly emits `transition: none`, clearing an earlier breakpoint's transition.

<h3 class="property-heading"><code>control.transitions.transitionProperty</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: all</span><span>Responsive</span></div>

Apply to accepts `all`, `colors`, `opacity`, `transform`, `shadow`, `border` `size` or `filters`. All follows browser support for any changed property. Colours covers text, background, border, decoration, fill and stroke colours. Transform covers transform, translate, rotate and scale. Shadow covers box and text shadows. Border covers colour, width and radius. Size covers width, height and their minimums and maximums. Filters covers filter and backdrop-filter (including the prefixed variant). Prefer a narrower scope when layout changes should remain immediate.

<h3 class="property-heading"><code>control.transitions.transitionFunction</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: ease-in-out</span><span>Responsive</span></div>

Function accepts `ease`, `linear`, `ease-in`, `ease-out` or `ease-in-out`.

<h3 class="property-heading"><code>control.transitions.transitionDuration</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 300</span><span>Responsive</span></div>

Duration in milliseconds, from 0 through 10000. Zero makes the change immediate when delay is also zero. The inspector increments by 10ms.

<h3 class="property-heading"><code>control.transitions.transitionDelay</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 0</span><span>Responsive</span></div>

Delay before the transition starts, in milliseconds from 0 through 10000. The inspector increments by 10ms.

## Return value

<h3 class="property-heading"><code>control.transitions.css</code></h3>
<div class="property-meta"><span class="property-type">CSS declarations</span></div>

When enabled, supplies `transition-property`, `transition-duration`, `transition-timing-function` and `transition-delay`. Duration and delay automatically become zero under the visitor's reduced-motion preference through Foundry's shared stylesheet. When disabled, supplies `transition: none;`.

Use this output on explicitly chosen descendants too when a part's interactive elements need the same timing. Do not apply it indiscriminately to every descendant: that would also affect nested parts. Avoid adding CSS transitions to properties simultaneously driven frame-by-frame by JavaScript animation.

The raw controls remain available for custom composition; raw duration and delay are numbers in milliseconds and do not themselves apply reduced-motion protection.
{% endraw %}
