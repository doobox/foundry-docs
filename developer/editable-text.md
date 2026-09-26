---
layout: default
title: Editable content · Foundry Developer
permalink: "/developer/editable-text.html"
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">Canvas editing</p>
<h1>Editable content primitives</h1>
<p class="lede">Put editable text, trusted HTML or an image directly into developer-owned markup without declaring a visible <code>inspector</code> control.</p>
<h2>Editable rich text</h2>

<div markdown="1">

```html
<h2>{{ text("heading", default: "A useful heading") }}</h2>
<p>{{ text("body") }}</p>
```

</div>

<p>The first quoted argument permanently names the editable value. The optional <code>default:</code> argument supplies its starting text; when omitted, Foundry uses its placeholder paragraph. Double-clicking any text primitive on the canvas opens the same rich-text editor, whether the text is a short label, a heading or a longer passage. Authors can format selected text with bold, italic, underline, strikethrough, size, colour and structured links.</p>
<p>Text colours come from the framework's colour picker — framework roles, standard palettes and the project's custom palettes, with a shade selection. Foundry stores the palette reference, not a literal colour: the resolved value is emitted where the text renders, so palette edits recolour existing text, and sites supporting both appearances emit an adaptive <code>light-dark()</code> colour. If a referenced custom palette is later deleted, that text inherits its part's colour until recoloured.</p>
<p>The link popover supports the same destinations as a Link control: URLs, pages, resources, anchors, new-window behaviour and custom attributes. Page and resource links remain connected to their Foundry items if the site is reorganised.</p>
<p>Unformatted values remain plain text and are HTML-escaped. When formatting is used, Foundry stores the value in a versioned internal form and emits only the supported inline markup. Part developers do not need to change their template.</p>
<h2>Trusted HTML</h2>

<div markdown="1">

```html
<div class="rich-content">
    {{ html("content", default: "<ul><li>First item</li></ul>") }}
</div>
```

</div>

<p><code>{{ html("content") }}</code> creates a source editor for HTML, CSS and JavaScript. HTML is inserted unescaped at the primitive’s position. Its CSS is emitted with that part instance’s page CSS and its JavaScript with that instance’s page script. Foundry supplies a small list when <code>default:</code> is omitted.</p>
<div class="callout warning">
<strong>HTML is trusted source.</strong> This primitive is intended for authors who are allowed to add executable website code. Do not use it for arbitrary visitor input.</div>
<h2>Image</h2>

<div markdown="1">

```html
<figure class="media {{ part.class }}" {{ part.attributes }}>
    {{ image("hero") }}
</figure>
```

</div>

<p><code>{{ image("hero") }}</code> creates an implicit image value and a drop target in the canvas. Once an image is selected, Foundry emits an <code>img.fd-image</code> element. Add captions, aspect-ratio wrappers and production styling in your own template and CSS.</p>
<h2>Video</h2>

<div markdown="1">

```html
<figure class="media {{ part.class }}" {{ part.attributes }}>
    {{ video("film") }}
</figure>
```

</div>

<p><code>{{ video("film") }}</code> creates an implicit video value and a video drop target in the canvas — the video counterpart to <code>{{ image() }}</code>. Authors fill it by dropping a movie file from the Finder or a video asset from the Assets panel. On the canvas Foundry shows the movie&rsquo;s generated poster frame without loading the movie itself; the published page emits a <code>video.fd-video</code> element with <code>controls</code> and <code>playsinline</code>. For configurable playback — autoplay, muting, looping, custom posters — declare a <a href="video-control.html">video control</a> in the manifest instead.</p>
<h2>Permanent names</h2>
<p>Every editable macro requires a quoted developer-defined name. It must begin with a letter and may then contain letters, numbers, underscores and hyphens. Names must be unique across all editable macros and drop zones in the part and cannot duplicate an <code>inspector</code> control <code>id</code>.</p>

<div markdown="1">

```html
<article class="article {{ part.class }}" {{ part.attributes }}>
    <h2>{{ text("title", default: "Title") }}</h2>
    <div>{{ html("body") }}</div>
    <small>{{ text("footnote", default: "Footnote") }}</small>
</article>
```

</div>


<p>The name is part of the part’s persistent API. Reordering named macros leaves their values attached correctly. Removing a macro preserves its stored value, and restoring the same name reconnects it. Changing a name removes the old editable area and creates a new one.</p>
<p>Defaults use quoted strings with JSON-style escaping. Write <code>\&quot;</code> for a double quote, <code>\\</code> for a backslash, and <code>\n</code> for a line break.</p>
<div class="callout warning">
<strong>Use controls for Inspector values.</strong> If content needs responsive variants, reuse in another template file, conditional visibility, or specialised Inspector UI, declare it under <code>inspector</code>.</div>
{% endraw %}
