---
layout: default
title: Sizing control group · Foundry Developer
permalink: /developer/sizing-control-group.html
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector · control groups</p>
<h1>Sizing</h1>
<p class="lede">Adds responsive width, maximum-width, minimum-height and height controls to the Inspector section of your choice.</p>

## Quick example

```json
{
    "section" : "Sizing",
    "systemImage" : "arrow.up.left.and.arrow.down.right",
    "controls" : [
        {
            "type" : "sizing"
        }
    ]
}
```

The section is yours: any name and icon work, other controls can share it, and a group left at the top level of the `inspector` joins `Settings` instead.

```css
:instance {
    width: auto;
    {{ if control.widthMode == "full" }}width: 100%;{{ endif }}
    {{ if control.widthMode == "fit" }}width: fit-content;{{ endif }}
    {{ if control.widthMode == "screen" }}width: 100svw;{{ endif }}
    {{ if control.widthMode == "breakpoint" }}width: min(100%, var(--foundry-container-width));{{ endif }}
    {{ if control.widthMode == "custom" }}width: min(100%, {{ control.customWidth }}px);{{ endif }}
    height: {{ if control.heightMode == "viewport" }}100svh{{ elseif control.heightMode == "custom" }}{{ control.customHeight }}px{{ else }}auto{{ endif }};
    min-width: {{ control.minWidth }};
    max-width: {{ control.maxWidth }};
    min-height: {{ control.minHeight }};
    max-height: {{ control.maxHeight }};
}
```

The four minimum and maximum controls need no guards: each declares the CSS its `none` token emits — `0` for a minimum, `none` for a maximum — so an unconstrained value interpolates to a harmless no-op.

<div class="callout warning" markdown="1">
**Guard the maximum when your part has a width rail.** `none` is a real declaration, and an instance rule outranks a global one, so an unset Max width would wipe out a `max-width: 100%` the part relies on. Keep the rail and guard the override using the numeric `.value`:

```css
max-width: 100%;
{{ if control.maxWidth.value > 0 }}max-width: min(100%, {{ control.maxWidth }});{{ endif }}
```

Interpolate `control.maxWidth` unguarded only when the part has no rail to protect — as the quick example above does.
</div>

## Properties

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Always `sizing`. The group does not accept `id`, `label`, `group`, `responsive`, `styles`, or `states`.

<h3 class="property-heading"><code>defaultOverrides</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: generated defaults</span></div>

Replaces complete base defaults using the generated IDs below.

## Generated controls

<h3 class="property-heading"><code>control.widthMode</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: auto</span><span>Responsive</span></div>

One of `auto`, `full`, `fit`, `screen`, `breakpoint`, or `custom`.

<ul>
<li><code>auto</code> — CSS's initial width. A block-level part fills its parent <em>after</em> margins, padding and borders are subtracted, so it never overflows the way a percentage does. This is the default for that reason.</li>
<li><code>full</code> — the parent's full content width (<code>100%</code>). Margins are added on top of it, so combine it with horizontal margins only deliberately; it is the right choice for a flex item, where <code>auto</code> sizes to content instead.</li>
<li><code>fit</code> — shrink-wraps the content (<code>fit-content</code>).</li>
<li><code>screen</code> — the viewport width (<code>100svw</code>), regardless of the parent.</li>
<li><code>breakpoint</code> — the framework's container width for the current breakpoint, via <code>var(--foundry-container-width)</code>.</li>
<li><code>custom</code> — the pixel value from <code>customWidth</code> below.</li>
</ul>

<h3 class="property-heading"><code>control.customWidth</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 320</span><span>Responsive</span></div>

A pixel width from 0 through 10,000. Shown when `widthMode` is `custom`.

<h3 class="property-heading"><code>control.heightMode</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: auto</span><span>Responsive</span></div>

One of `auto`, `fill`, `viewport`, or `custom`, displayed as Fit content, Fill Remaining Space, Fill viewport, and Custom. `fill` grows the part into the viewport space its siblings leave free — the page body is a minimum-height flex column, so `flex: 1 1 auto` on the part is all it takes.

<h3 class="property-heading"><code>control.customHeight</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 400</span><span>Responsive</span></div>

A pixel height from 0 through 10,000. Shown when `heightMode` is `custom`.

<h3 class="property-heading"><code>control.minWidth</code></h3>
<div class="property-meta"><span class="property-type">Framework spacing</span><span class="default">Default: none</span><span>Responsive</span></div>

The smallest width, as a framework spacing token or custom length. `none` emits `0` — CSS's own "no constraint" for this property.

<h3 class="property-heading"><code>control.maxWidth</code></h3>
<div class="property-meta"><span class="property-type">Framework spacing</span><span class="default">Default: none</span><span>Responsive</span></div>

The largest width, as a framework spacing token or custom length. `none` emits `none` — CSS's own "no constraint" for this property. Templates should ensure the result never exceeds the available parent width — the quick example wraps it in `min(100%, …)`.

<h3 class="property-heading"><code>control.minHeight</code></h3>
<div class="property-meta"><span class="property-type">Framework spacing</span><span class="default">Default: none</span><span>Responsive</span></div>

The smallest height, as a framework spacing token or custom length. `none` emits `0` — CSS's own "no constraint" for this property.

<h3 class="property-heading"><code>control.maxHeight</code></h3>
<div class="property-meta"><span class="property-type">Framework spacing</span><span class="default">Default: none</span><span>Responsive</span></div>

The largest height, as a framework spacing token or custom length. `none` emits `none` — CSS's own "no constraint" for this property.

## Template behavior

The group generates no CSS or HTML. The mode values are semantic choices whose CSS mapping belongs to the part template, and `customWidth`/`customHeight` are plain numbers — append `px` when producing CSS. The four minimum and maximum values are framework spacing values: interpolate them directly for a ready-made length, or read `.value` and `.unit` for their parts.
{% endraw %}
