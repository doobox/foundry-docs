---
layout: default
title: Lightbox control group · Foundry Developer
permalink: /developer/lightbox-control-group.html
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector · control groups</p>
<h1>Lightbox</h1>
<p class="lede">A reusable lightbox settings control, with automatic opening for a part's own media.</p>

## Quick example

```json
{
    "section": "Lightbox",
    "systemImage": "rectangle.on.rectangle",
    "controls": [
        { "type": "lightbox", "id": "lightbox" }
    ]
}
```

The compound control can also be declared directly in an existing inspector section. The section supplies the heading; the control supplies Enable, backdrop colour with opacity, and blur. Foundry supplies the shared runtime and styles.

Offer this capability only when the part has a clear lightbox action. Built-in Image, SVG and Video parts use it to open their own media. Layout parts and Button do not offer it.

## Properties

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Always `lightbox`. This is a compound control: it expands into ordinary inspector controls and provides behaviour rather than a `.css` expression.

<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

A unique identifier, starting with a letter and using letters, numbers, underscores or hyphens. No default. The example exposes values under `control.lightbox.`. Declare one Lightbox control per part, and use a flow-content container root such as `div`, `section` or `figure`, with the normal `part.class` and `part.attributes` expressions.

<h3 class="property-heading"><code>defaults</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: control defaults below</span></div>

Override initial values by local control ID. For a dedicated Lightbox part, enable it initially:

```json
{ "type": "lightbox", "id": "lightbox", "defaults": { "enabled": true } }
```

## Inspector controls

- `enabled`: Boolean, default `false`. Enable switch.
- `backdropColor`: Framework Colour with opacity enabled. Default: `standard.black` at `0.5` opacity. Supports framework colours and custom colours.
- `backdropBlur`: Number, default `0`, range `0–40` pixels.

Colour and blur appear only while enabled. There is no content picker, content type, trigger selector or size selector in the control. Ordinary shared control-group visibility and default overrides apply.

## Media behaviour

Without custom-content hooks, Lightbox opens media owned by the part, not a nested child part. An image uses its source image, an inline SVG opens as a vector, and native video or YouTube opens a player. The enabled control suppresses the shared Link group's navigation without deleting its destination.

Use a single, unambiguous media target. A root containing competing interactive descendants is not made clickable. Arbitrary external iframe URLs are not accepted as automatic media sources.

Canvas clicks continue to edit the part. Lightboxes open only in preview and published pages.

## Standalone parts and custom content

The built-in Lightbox part has separate Trigger and Content areas. These are ordinary child-picker slots belonging to the part, not to the Lightbox control. Third-party developers use the same public hooks:

```html
<div class="{{ part.class }}" {{ part.attributes }}>
    <div data-foundry-lightbox-trigger>{{ childArea("trigger") }}</div>
    <div {{ if !canvas }}hidden{{ endif }}>
        <div data-foundry-lightbox-content aria-label="More information">
            {{ childArea("content") }}
        </div>
    </div>
</div>
```

Declare the corresponding `trigger` and `content` child-picker controls in the manifest. Keep the hook elements owned by the part, outside nested part roots. The content's accessible label names the dialog.

The trigger area may contain one button or link, or a simple non-interactive image/card. A trigger containing multiple actions or form fields is not activated. A single button or link becomes the lightbox action instead of navigating. Content inside the dialog may contain interactive parts normally.

Custom content is editable in the canvas and hidden on the published page until opened. Opening moves the content into the dialog; closing restores it, preserving input values and event handlers. Nested parts should use their own instance selectors: CSS depending on the original ancestor does not match while content is in the dialog.

## Presentation and interaction

The lightbox uses a viewport-constrained, transparent surface, so media does not acquire a white panel or padding. Custom content keeps its own background and styling. A short fade and subtle scale animate opening and closing; reduced-motion preferences disable these animations.

Close button, Escape, backdrop dismissal, modal focus handling, scroll locking and focus restoration are standard behaviour, not inspector settings. Closing pauses native media and unloads iframe content. Only one lightbox is shown at once. Video playback is requested when opened, subject to browser playback restrictions.

JavaScript is required. The lightbox runtime is supplied only when enabled in preview or published output.
{% endraw %}
