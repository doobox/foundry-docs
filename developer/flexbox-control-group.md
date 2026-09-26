---
layout: default
title: Flexbox control group · Foundry Developer
permalink: /developer/flexbox-control-group.html
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector · control groups</p>
<h1>Flexbox</h1>
<p class="lede">Adds the complete responsive Flexbox container vocabulary — direction, wrapping, gaps, alignment and distribution — for parts that arrange their children with <code>display: flex</code>.</p>

## Quick example

```json
{
    "section" : "Layout",
    "systemImage" : "rectangle.3.group",
    "controls" : [
        {
            "type" : "flexbox",
            "defaultOverrides" : {
                "wrap" : "wrap"
            }
        }
    ]
}
```

The section is yours: any name and icon work, other controls can share it, and a group left at the top level of the `inspector` joins `Settings` instead.

```css
:instance {
    display: flex;
    flex-direction: {{ control.direction }};
    flex-wrap: {{ control.wrap }};
    column-gap: {{ control.columnGap }};
    row-gap: {{ control.rowGap }};
    align-items: {{ control.alignItems }};
    align-content: {{ control.alignContent }};
    justify-content: {{ control.justifyContent }};
}
```

## Properties

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Always `flexbox`. The group does not accept `id`, `label`, `group`, `responsive`, `styles`, or `states`.

<h3 class="property-heading"><code>defaultOverrides</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: generated defaults</span></div>

Replaces complete base defaults using any generated ID below. The generated defaults are column-first and start-aligned: intrinsic-width children like buttons keep their natural size instead of stretching. Parts whose children should fill the container regardless declare their own `width: 100%`, as Foundry's text parts do.

<h3 class="property-heading"><code>visibleWhen</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span></div>

Gates the whole group behind one of the part's own controls, using the standard <a href="visible-when.html">visibility condition</a> syntax. Every generated control inherits the condition, combined with any condition it already carries. Available on every grouped-control reference except `advanced`.

```json
{
    "type" : "flexbox",
    "visibleWhen" : {
        "id" : "layout",
        "value" : "flex"
    }
}
```

## Generated controls

<h3 class="property-heading"><code>control.direction</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: column</span><span>Responsive</span></div>

One of `column`, `row`, `column-reverse`, or `row-reverse` — the direction of flow. Justify Content distributes along it; Align Items and Align Content work across it. The default is `column`, matching how page sections most often stack; use `defaultOverrides` for row-first parts.

<h3 class="property-heading"><code>control.wrap</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: nowrap</span><span>Responsive</span></div>

One of `nowrap`, `wrap`, or `wrap-reverse`. Wrapping creates the multiple lines that `alignContent` spaces.

<h3 class="property-heading"><code>control.columnGap</code></h3>
<div class="property-meta"><span class="property-type">Framework spacing</span><span class="default">Default: md</span><span>Responsive</span></div>

The horizontal gap between items, as a framework spacing token or custom length. Shown only while it can apply: in a row direction, or whenever wrapping is on.

<h3 class="property-heading"><code>control.rowGap</code></h3>
<div class="property-meta"><span class="property-type">Framework spacing</span><span class="default">Default: md</span><span>Responsive</span></div>

The vertical gap between items and wrapped lines, as a framework spacing token or custom length. Shown only while it can apply: in a column direction, or whenever wrapping is on.

<h3 class="property-heading"><code>control.alignItems</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: flex-start</span><span>Responsive</span></div>

One of `flex-start`, `center`, `flex-end`, `stretch`, or `baseline` — how each item sits across the direction of flow. `stretch` gives items matching cross-axis sizes, such as equal-height cards in a row.

<h3 class="property-heading"><code>control.alignContent</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: flex-start</span><span>Responsive</span></div>

One of `flex-start`, `center`, `flex-end`, `stretch`, `space-between`, `space-around`, or `space-evenly` — how wrapped lines share the cross-axis space. Shown only while Wrap Items is on, because single-line layouts are unaffected.

<h3 class="property-heading"><code>control.justifyContent</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: flex-start</span><span>Responsive</span></div>

One of `flex-start`, `center`, `flex-end`, `space-between`, `space-around`, or `space-evenly` — how the items are distributed along the direction of flow.

## Template behavior

The group generates no CSS or HTML: your templates decide where the values land, and the part must set `display: flex` itself. Foundry deliberately omits `justify-items` — the CSS specification defines it as having no effect in flex layout — and the alignment menus omit `normal`, which is only an alias of the defaults above.
{% endraw %}
