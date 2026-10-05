---
layout: default
title: SVG control · Foundry Developer
permalink: "/developer/svg-control.html"
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector</p>
<h1>SVG</h1>
<p class="lede">Choose an SVG file and render its artwork inline, ready for your part's CSS.</p>

## Quick example

```json
{
    "type": "svg",
    "id": "artwork",
    "label": "SVG"
}
```

```html
<div class="artwork">{{ control.artwork }}</div>
```

```css
:instance .artwork svg { display: block; width: 100%; height: auto; }
```

The Inspector supplies Pick, Clear, a preview well and Alt text. Finder and Resources SVG files can be dropped into the well. The template value is **sanitised inline SVG markup, not an image URL**: place it in element content, never an attribute or stylesheet. Do not wrap it in another `svg` element.

The canvas supplies a replaceable SVG drop target, including an empty placeholder. Preview and published output contain the inline artwork only; an empty selection produces no markup. SVGs are imported into the project, not linked to a remote server.

## Properties

<h3 class="property-heading"><code>type</code></h3>
<p class="property-meta">String · Required · <code>svg</code></p>

One named SVG control. `count`, `focalPoint` and `renditions` are not supported. Vector artwork scales directly without image renditions.

<h3 class="property-heading"><code>id</code></h3>
<p class="property-meta">String · Required</p>

The unique control name, read as `control.artwork` in the example.

<h3 class="property-heading"><code>label</code></h3>
<p class="property-meta">String · Optional · Defaults to the control ID</p>

The Inspector's left-hand label.

<h3 class="property-heading"><code>subtitle</code></h3>
<p class="property-meta">String · Optional · No default</p>

Supporting text beneath the control.

<h3 class="property-heading"><code>defaults</code></h3>
<p class="property-meta">Dictionary · Optional · Empty selection</p>

`base` accepts an empty String or a declared package asset path. The asset must contain a supported SVG document. With `responsive: true`, breakpoint keys can select different SVG assets.

<h3 class="property-heading"><code>alt</code></h3>
<p class="property-meta">String · Optional · Empty String</p>

The initial alternative description. A nonempty description becomes the inline SVG's accessible name. Without one, an existing SVG title is retained; artwork without either is hidden from assistive technology.

<h3 class="property-heading"><code>responsive</code></h3>
<p class="property-meta">Boolean · Optional · Default: false</p>

Allows breakpoint-specific selections in the editor. Alt text is shared. As with other HTML values, the exported markup does not automatically change when the browser resizes; use CSS for responsive presentation.

<h3 class="property-heading"><code>tooltip</code></h3>
<p class="property-meta">String · Optional · No default</p>

Help text shown over the control.

<h3 class="property-heading"><code>visibleWhen</code></h3>
<p class="property-meta">Dictionary · Optional · Always visible</p>

A standard visibility condition. Hiding the control preserves its stored selection.

<h3 class="property-heading"><code>valueAvailability</code></h3>
<p class="property-meta">String · Optional · Default: always</p>

`always` keeps the template value available when hidden. `whenVisible` suppresses it while `visibleWhen` is false and requires that condition.

## Template drop zone

For editable artwork without a declared Inspector control, use a permanent, unique name:

```html
<div class="artwork">{{ svg("illustration") }}</div>
```

Do not reuse an Inspector control ID as the primitive name. Inside a template loop each instance stores its own SVG selection, like the image primitive.

## Inline SVG safety and appearance

Foundry accepts UTF-8 SVG files up to 5 MB. Static shapes, text, groups, gradients, clip paths, masks and safe inline presentation styles are retained. IDs and local paint references are namespaced per part and repeated instance so separate artwork does not collide.

Scripts, event attributes, embedded HTML, external resources, animation and embedded stylesheets are removed. Standard SVG DOCTYPE declarations are removed without loading their external DTD; entity declarations and internal DTD subsets are rejected. Export artwork using presentation attributes or inline styles; stylesheet-based or unsupported SVG features can change appearance. Use an Image control when you need to display such artwork without inline styling.

Original fills and strokes are retained unless your CSS overrides them. The built-in SVG part provides optional framework-colour fill and stroke overrides and a stroke-width override, plus the usual shared control groups. Custom parts can expose their own controls and target their inline SVG with CSS.

The built-in overrides change existing paint only: `fill:none` stays unfilled, and artwork without strokes does not acquire an outline. Clipping and mask geometry are excluded. For the same behaviour in custom parts, target `[data-foundry-svg-fill]` or `[data-foundry-svg-stroke]` inside your SVG. Foundry marks eligible shapes after resolving presentation attributes, inline styles and inherited fill/stroke values.
{% endraw %}
