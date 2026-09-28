---
layout: default
title: Image control · Foundry Developer
permalink: "/developer/image-control.html"
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector</p>
<h1>Image</h1>
<p class="lede">Let someone choose, import, replace or clear a project image using the standard media well.</p>

## Quick example

```json
{
    "type" : "image",
    "id" : "hero",
    "label" : "Image"
}
```

```html
<img src="{{ control.hero }}" alt="{{ control.hero.alt }}">
```

<p>The direct value is the selected image path, and it is empty until an image is chosen. The Inspector shows a preview well with Pick and Clear buttons, accepts an image dropped from Finder, Resources or a browser, and always includes an Alt text field. Imported files are added to Resources. Other media types are rejected.</p>

<p>Pick's menu also offers <strong>From URL…</strong> for an image on the web. <strong>Import Copy</strong> downloads it into Resources like any other import. <strong>Link</strong> keeps the address as the value instead, so visitors load the image from that server: the direct value and <code>href</code> are then the address, every rendition returns that same address, and the dimensions and file metadata are empty because Foundry never holds the bytes. Guard anything that needs them, as the complete example below does with <code>width</code>.</p>

<p>When the primary template binds an <code>img</code> element's <code>src</code> to the control — as <code>{{ control.hero }}</code>, <code>{{ control.hero.href }}</code> or a declared rendition — Foundry recognises the element. In the editing canvas it becomes a drop target and shows a placeholder while no image is selected. In preview and published output an <code>img</code> whose control has no image is removed. An <code>img src</code> control binding must reference an image control; the pack fails validation otherwise.</p>

## Properties

<section class="key-reference"><h3><code>type</code></h3><div class="key-meta"><span>String</span><strong>Required</strong><span><code>image</code></span></div><p>This control does not support <code>count</code>: an image control represents one named image. Declare each image property explicitly.</p></section>

```json
"type" : "image"
```

<section class="key-reference"><h3><code>id</code></h3><div class="key-meta"><span>String</span><strong>Required</strong></div><p>The unique control and template value name.</p></section>

```json
"id" : "hero"
```

Read it in the template as `control.hero`:

```html
<img src="{{ control.hero }}" alt="{{ control.hero.alt }}">
```

<section class="key-reference"><h3><code>label</code></h3><div class="key-meta"><span>String</span><span>Optional</span></div></section>

The text shown beside the media well in the Inspector.

```json
"label" : "Hero image"
```

<section class="key-reference"><h3><code>defaults</code></h3><div class="key-meta"><span>Dictionary</span><span>Optional</span></div><p>Omit <code>defaults</code> to start empty. A non-empty <code>base</code> is a package-relative path and must reference a declared package asset, which is used until someone chooses their own image. Image asset defaults support <code>base</code> only; breakpoints apply to responsive selections, not defaults.</p></section>

Declare the placeholder as a package asset, then use its path as the default:

```json
"assets" : [
    {
        "path" : "images/placeholder.jpg"
    }
]
```

```json
"defaults" : {
    "base" : "images/placeholder.jpg"
}
```

<section class="key-reference"><h3><code>alt</code></h3><div class="key-meta"><span>String</span><span>Optional</span><span>Default: empty</span></div><p>The initial alternative text. Site authors edit the final text in the Inspector's Alt field. Only image controls accept <code>alt</code>.</p></section>

```json
"alt" : "A view across the harbour at sunset"
```

```html
<img src="{{ control.hero }}" alt="{{ control.hero.alt }}">
```

<section class="key-reference"><h3><code>focalPoint</code></h3><div class="key-meta"><span>Boolean</span><span>Optional</span><span>Default: false</span></div><p>Declares that the part uses a focal point and provides the <code>position</code>, <code>focalPointX</code> and <code>focalPointY</code> template values. The Inspector adds a <strong>Focal Point</strong> button beneath Pick and Clear: turning it on shows a draggable marker over the preview, and turning it off hides the marker and returns the image to its centre, <code>50% 50%</code>. Only declare <code>focalPoint</code> when your template uses one of these values, so the button always has a visible effect. Declaring <code>focalPoint</code> makes the control responsive so the focal point can differ at each breakpoint. Only image controls accept <code>focalPoint</code>.</p></section>

```json
"focalPoint" : true
```

Crop around the chosen point with `object-position`:

```css
:instance img {
    width: 100%;
    height: 400px;
    object-fit: cover;
    object-position: {{ control.hero.position }};
}
```

<section class="key-reference"><h3><code>renditions</code></h3><div class="key-meta"><span>Array of Dictionaries</span><span>Optional</span></div><p>Declares named scaled variants for templates that want smaller sources. Each dictionary requires a String <code>id</code> — starting with a letter, containing letters, digits, hyphens or underscores, and unique within the control — and an Integer <code>maximumDimension</code> greater than zero. Values above 3,840 are clamped to 3,840, Foundry's maximum stored image dimension. Only image controls accept <code>renditions</code>.</p></section>

```json
"renditions" : [
    {
        "id" : "small",
        "maximumDimension" : 800
    },
    {
        "id" : "medium",
        "maximumDimension" : 1600
    }
]
```

Offer them to the browser with `srcset`. Each rendition reports its own pixel size, so the width descriptors are right for portrait images too, and for images that were already smaller than a rendition:

```html
<img src="{{ control.hero }}"
     srcset="{{ control.hero.rendition.small }} {{ control.hero.rendition.small.width }}w, {{ control.hero.rendition.medium }} {{ control.hero.rendition.medium.width }}w, {{ control.hero }} {{ control.hero.width }}w"
     sizes="100vw"
     alt="{{ control.hero.alt }}">
```

<section class="key-reference"><h3><code>responsive</code></h3><div class="key-meta"><span>Boolean</span><span>Optional</span><span>Default: false</span></div><p>A responsive image control lets each breakpoint override the selected image and its focal point. Always <code>true</code> when <code>focalPoint</code> is declared.</p></section>

```json
"responsive" : true
```

<section class="key-reference"><h3><code>tooltip</code></h3><div class="key-meta"><span>String</span><span>Optional</span></div></section>

Help text shown when the pointer rests on the control.

```json
"tooltip" : "The large image at the top of the section."
```

<section class="key-reference"><h3><code>visibleWhen</code></h3><div class="key-meta"><span>Dictionary</span><span>Optional</span></div><p>Conditionally shows the complete image row. A hidden row retains its selected value.</p></section>

Show the image only when a toggle is on:

```json
"visibleWhen" : {
    "id" : "showImage",
    "value" : true
}
```

<section class="key-reference"><h3><code>valueAvailability</code></h3><div class="key-meta"><span>String</span><span>Optional</span><span>Default: always</span></div><p>Use <code>always</code> to keep this control's template value available while hidden, or <code>whenVisible</code> to make the value and its qualified derived values unavailable while <code>visibleWhen</code> is false. The stored value is preserved. <code>whenVisible</code> requires <code>visibleWhen</code>.</p></section>

```json
"valueAvailability" : "whenVisible"
```

With `whenVisible`, test the value before writing the element:

```html
{{ if control.hero }}<img src="{{ control.hero }}" alt="{{ control.hero.alt }}">{{ endif }}
```


## Template values

<p><code>control.hero</code> is the image path. Use the structured values when the part needs alternative text, focal-point styling or file metadata:</p>

```text
control.hero.href
control.hero.alt
control.hero.position
control.hero.focalPointX
control.hero.focalPointY
control.hero.rendition.myRendition
control.hero.rendition.myRendition.width
control.hero.rendition.myRendition.height
control.hero.filename
control.hero.extension
control.hero.mimeType
control.hero.byteCount
control.hero.width
control.hero.height
control.hero.aspectRatio
```

<p><code>control.hero.href</code> returns the same path as the direct value: the exported image path in preview and published output, and both are empty when no image is selected. <code>control.hero.position</code> returns the focal point as a CSS position such as <code>50% 50%</code>, ready for <code>object-position</code> or <code>background-position</code>; <code>focalPointX</code> and <code>focalPointY</code> are the same coordinates as numbers from 0 to 100. <code>control.hero.rendition.myRendition</code> returns the path of that declared rendition — a copy whose longest side does not exceed the rendition's <code>maximumDimension</code>, or the original image when it is already small enough. Its <code>width</code> and <code>height</code> are that copy's pixel size, or the original's when no copy is needed, and are empty when the image's size is unknown. The editing canvas always uses the full-size image but reports the same rendition sizes.</p>

<p><code>width</code> and <code>height</code> are the stored pixel dimensions. Dimensions, aspect ratio and file metadata are empty when that metadata is unavailable. Imported images are stored with a longest side of at most 3,840 pixels.</p>

### Examples

The path, as an image or a link:

```html
<img src="{{ control.hero.href }}" alt="{{ control.hero.alt }}">
<a href="{{ control.hero.href }}" download>Download the full image</a>
```

The image as a CSS background, placed at its focal point:

```css
:instance {
    background-image: url("{{ control.hero }}");
    background-size: cover;
    background-position: {{ control.hero.position }};
}
```

The focal point as numbers, for example to feed your own CSS variables:

```css
:instance {
    --focus-x: {{ control.hero.focalPointX }}%;
    --focus-y: {{ control.hero.focalPointY }}%;
}
```

Width and height stop the page jumping while the image loads, and the aspect ratio reserves space for a box sized by CSS:

```html
<img src="{{ control.hero }}" width="{{ control.hero.width }}" height="{{ control.hero.height }}" alt="{{ control.hero.alt }}">
```

```css
:instance .frame {
    aspect-ratio: {{ control.hero.aspectRatio }};
}
```

File details, for a caption or a download label:

```html
<figcaption>{{ control.hero.filename }} · {{ control.hero.extension }} · {{ control.hero.mimeType }} · {{ control.hero.byteCount }} bytes</figcaption>
```

## Complete example

### manifest.json

```json
{
    "type" : "image",
    "id" : "hero",
    "label" : "Hero image",
    "alt" : "A view across the harbour at sunset",
    "focalPoint" : true,
    "renditions" : [
        {
            "id" : "small",
            "maximumDimension" : 800
        }
    ],
    "tooltip" : "The large image at the top of the section."
}
```

### part.html

```html
<figure class="{{ part.class }}" {{ part.attributes }}>
    <img src="{{ control.hero }}"
         {{ if control.hero.width }}srcset="{{ control.hero.rendition.small }} {{ control.hero.rendition.small.width }}w, {{ control.hero }} {{ control.hero.width }}w"
         sizes="100vw"
         width="{{ control.hero.width }}"
         height="{{ control.hero.height }}"{{ endif }}
         alt="{{ control.hero.alt }}">
</figure>
```

The `if` leaves the `srcset` and dimensions out for a linked web image, whose size is unknown.

### part.css

```css
:instance img {
    display: block;
    width: 100%;
    height: 400px;
    object-fit: cover;
    object-position: {{ control.hero.position }};
}
```
{% endraw %}
