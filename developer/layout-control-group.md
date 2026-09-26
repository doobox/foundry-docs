---
layout: default
title: Layout control group · Foundry Developer
permalink: /developer/layout-control-group.html
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector · control groups</p>
<h1>Layout</h1>
<p class="lede">Adds responsive positioning and display controls — position, z-index, offsets, visibility, overflow and isolation — to the Inspector section of your choice.</p>

## Quick example

```json
{
    "section" : "Layout",
    "systemImage" : "square.on.square",
    "controls" : [
        {
            "type" : "layout"
        }
    ]
}
```

The section is yours: any name and icon work, other controls can share it, and a group left at the top level of the `inspector` joins `Settings` instead.

```css
:instance {
    {{ if control.position != "none" }}position: {{ control.position }};{{ endif }}
    {{ if control.zIndexMode == "auto" }}z-index: auto;{{ elseif control.zIndexMode == "custom" }}z-index: {{ control.zIndex }};{{ endif }}
    {{ if control.offsets != "none" }}inset: {{ control.offset }}{{ control.offsetEdges }};{{ endif }}
    {{ if control.hidden }}display: none;{{ endif }}
    {{ if control.visibility != "default" }}visibility: {{ control.visibility }};{{ endif }}
    {{ if control.overflow != "none" }}overflow: {{ control.overflow }};{{ endif }}
    {{ if control.isolation != "none" }}isolation: {{ control.isolation }};{{ endif }}
}
```

The two offset values declare `valueAvailability: whenVisible`, so exactly one of them exists at a time — the `inset` line interpolates both and renders whichever mode is active. The remaining conditions are value semantics, not visibility: `none` and `default` are the author's explicit "emit nothing" choices on always-visible controls, which only a condition can express.

## Properties

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Always `layout`. The group does not accept `id`, `label`, `group`, `responsive`, `styles`, or `states`.

<h3 class="property-heading"><code>defaultOverrides</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: generated defaults</span></div>

Replaces complete base defaults using any generated ID below.

<h3 class="property-heading"><code>visibleWhen</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span></div>

Gates the whole group behind one of the part's own controls, using the standard <a href="visible-when.html">visibility condition</a> syntax. Every generated control inherits the condition, combined with any condition it already carries.

## Generated controls

<h3 class="property-heading"><code>control.position</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: none</span><span>Responsive</span></div>

One of `none`, `static`, `relative`, `absolute`, `fixed`, or `sticky`. `none` means the template should emit no <code>position</code>; `static` is the explicit CSS value — normal flow, offsets and z-index inert — useful for overriding positioning set elsewhere.

<h3 class="property-heading"><code>control.zIndexMode</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: none</span><span>Responsive</span></div>

One of `none`, `auto`, or `custom`, shown as a segmented control. `none` means the template should emit no <code>z-index</code>; `custom` reveals the numeric value below.

<h3 class="property-heading"><code>control.zIndex</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 0</span><span>Responsive</span></div>

The custom stacking value, −9999 through 9999. Shown only while <code>zIndexMode</code> is <code>custom</code>, and unavailable to templates otherwise (<code>valueAvailability: whenVisible</code>).

<h3 class="property-heading"><code>control.offsets</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: none</span><span>Responsive</span></div>

One of `none`, `uniform`, or `individual`, shown as a segmented control — how the top/right/bottom/left offsets are edited. `uniform` reveals one shared length; `individual` reveals the four-edge control.

<h3 class="property-heading"><code>control.offset</code></h3>
<div class="property-meta"><span class="property-type">Framework spacing</span><span class="default">Default: none</span><span>Responsive</span></div>

The shared offset applied to every edge, as a framework spacing token or custom length — the CSS <code>inset</code> shorthand with one value. Shown only while <code>offsets</code> is <code>uniform</code>, and unavailable to templates otherwise (<code>valueAvailability: whenVisible</code>).

<h3 class="property-heading"><code>control.offsetEdges</code></h3>
<div class="property-meta"><span class="property-type">Edges</span><span class="default">Default: 0px each edge</span><span>Responsive</span></div>

Independent top/right/bottom/left offsets as raw lengths in `px`, `%`, `rem`, or `em`. Shown only while <code>offsets</code> is <code>individual</code>, and unavailable to templates otherwise (<code>valueAvailability: whenVisible</code>). The direct value renders the four-value <code>inset</code> shorthand; qualified values such as <code>control.offsetEdges.top</code> remain available.

<h3 class="property-heading"><code>control.hidden</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="default">Default: false</span><span>Responsive</span></div>

A switch for removing the part from the flow at a breakpoint — templates typically emit <code>display: none</code> while it is on.

<h3 class="property-heading"><code>control.visibility</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: default</span><span>Responsive</span></div>

One of `default`, `visible`, or `hidden`. `default` means the template should emit no <code>visibility</code> — CSS visibility has no `auto` keyword, so the sentinel is named honestly. Unlike <code>hidden</code> above, CSS visibility keeps the part's space in the flow.

<h3 class="property-heading"><code>control.overflow</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: none</span><span>Responsive</span></div>

One of `none`, `visible`, `hidden`, `scroll`, or `auto`. `none` means the template should emit no <code>overflow</code>.

<h3 class="property-heading"><code>control.isolation</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: none</span><span>Responsive</span></div>

One of `none`, `isolate`, or `auto`, shown as a segmented control. `isolate` creates a new stacking context without any other visual effect; `none` means the template should emit no <code>isolation</code>.

## Template behavior

The group generates no CSS or HTML: your templates decide where the values land. The `none` and `default` base values are deliberate "emit nothing" choices — guard each declaration as the quick example does, so an untouched part contributes no positioning CSS at all.
{% endraw %}
