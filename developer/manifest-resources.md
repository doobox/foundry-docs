---
layout: default
title: Libraries and assets · Foundry Developer
permalink: "/developer/manifest-resources.html"
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json</p>
<h1>Libraries and assets</h1>
<p class="lede">Use libraries for Foundry-managed web dependencies and assets for part-owned files that templates reference but do not process as source templates.</p>

<h2>libraries</h2>
<section class="reference-entry">
<h3>libraries</h3>
<div class="api-meta">
<span class="pill">Dictionary array</span><span class="pill">Optional</span><span class="pill">Default: []</span>
</div>
<p>Requests a web library supplied by Foundry. Foundry includes a requested library only when the site uses a part that declares it, and deduplicates the same request across parts.</p>
<p>Library IDs use a stable Foundry identifier based on the familiar upstream name. Foundry owns the tested patch release within the requested major version, publishes the files locally, loads dependencies in order and includes each library only once per page. Parts never bundle or download their own copy.</p>


<div markdown="1">

```json
"libraries" : [
    {
        "id" : "bootstrapIcons",
        "majorVersion" : 1
    }
]
```

</div>

<p>After declaring the library, use Bootstrap Icons classes in markup, for example <code>&lt;i class="bi bi-alarm"&gt;&lt;/i&gt;</code>. To let authors choose the icon, add Foundry’s searchable <a href="icon-control.html"><code>icon</code> custom control</a>.</p>

<h3>Available libraries</h3>

<dl class="syntax-list">
<dt><code>bootstrapIcons</code> · major <code>1</code></dt>
<dd><a href="https://icons.getbootstrap.com/">Bootstrap Icons</a>. Use classes such as <code>bi bi-alarm</code>. An <a href="icon-control.html"><code>icon</code> control</a> requests it automatically.</dd>
<dt><code>alpine</code> · major <code>3</code></dt>
<dd><a href="https://alpinejs.dev/">Alpine.js</a>, exposed through its normal global <code>Alpine</code> API. Foundry loads Alpine after page-level part scripts so those scripts can register extensions with the standard <code>alpine:init</code> event before Alpine starts.</dd>
<dt><code>gsap</code> · major <code>3</code></dt>
<dd><a href="https://gsap.com/docs/v3/">GSAP</a>, exposed through the normal global <code>gsap</code> API. Core easing such as <code>power2.out</code>, <code>back.out(1.7)</code>, <code>elastic.out(1,0.3)</code> and <code>bounce.out</code> is available.</dd>
<dt><code>gsapScrollTrigger</code> · major <code>3</code></dt>
<dd><a href="https://gsap.com/docs/v3/Plugins/ScrollTrigger/">GSAP ScrollTrigger</a>, exposed through the normal global <code>ScrollTrigger</code> API. Requesting it automatically includes and loads <code>gsap</code> first. The <a href="reveal-control-group.html"><code>reveal</code> control group</a> requests both automatically.</dd>
<dt><code>glightbox</code> · major <code>3</code></dt>
<dd><a href="https://biati-digital.github.io/glightbox/">GLightbox 3</a>, exposed through its normal global <code>GLightbox</code> API with its standard stylesheet. It automatically includes locally bundled Plyr 3 for video playback. The <a href="lightbox-control-group.html"><code>lightbox</code> control group</a> requests it automatically.</dd>
<dt><code>plyr</code> · major <code>3</code></dt>
<dd><a href="https://plyr.io/">Plyr 3</a>, exposed through its normal global <code>Plyr</code> API and stylesheet. Requesting GLightbox includes it first, so lightbox video playback never needs to download the player runtime from a CDN.</dd>
</dl>

<p>Request one or more libraries with separate dictionaries:</p>

<div markdown="1">

```json
"libraries" : [
    {
        "id" : "alpine",
        "majorVersion" : 3
    },
    {
        "id" : "gsapScrollTrigger",
        "majorVersion" : 3
    }
]
```

</div>

<p>Part JavaScript may use the upstream APIs directly. When registering Alpine data or extensions, attach the handler before Alpine loads:</p>

<div markdown="1">

```js
document.addEventListener("alpine:init", () => {
    Alpine.data("disclosure", () => ({ open: false }));
});

gsap.registerPlugin(ScrollTrigger);
gsap.from(".feature", {
    autoAlpha: 0,
    y: 32,
    scrollTrigger: ".feature"
});
```

</div>
</section>

<h2>assets</h2>
<section class="reference-entry">
<h3>assets</h3>
<div class="api-meta">
<span class="pill">Dictionary array</span><span class="pill">Optional</span><span class="pill">Default: []</span>
</div>
<p>Lists part-owned resources that templates use without processing them as templates—for example images, fonts, JSON, video, or a PHP endpoint. Each array entry must be a dictionary representing one file or folder to publish. Bare string entries are not accepted.</p>


<div markdown="1">

```json
"assets" : [
    {
        "path" : "images/badge.svg"
    },
    {
        "path" : "data/defaults.json"
    }
]
```

</div>


<p>Reference a declared asset with <code>{{ asset("&lt;path&gt;") }}</code>:</p>


<div markdown="1">

```html
<img src="{{ asset("images/badge.svg") }}" alt="">
```

</div>


<dl class="syntax-list">
<dt><code>path</code></dt>
<dd>Required. A safe path relative to the individual part's <code>Resources</code> directory. It must identify an existing file or folder.</dd>
<dt><code>scope</code></dt>
<dd>Optional. Accepts <code>page</code> or <code>site</code> and defaults to <code>page</code> when omitted.</dd>
</dl>
<p>Foundry publishes a page asset once in that page’s <code>files/</code> directory, regardless of how many part instances use it. A declared file publishes using only its filename; a declared directory publishes recursively and retains the directory name.</p>
<p>Use <code>site</code> scope to publish an asset once for the entire website:</p>


<div markdown="1">

```json
{
    "path" : "shared/icons",
    "scope" : "site"
}
```

</div>


<p>Foundry publishes site assets once below the website’s global <code>assets/</code> directory, preserving the declared path. They are not part-namespaced, so any template can use a known path with <code>{{ path.siteAssets }}/shared/icons/star.svg</code>.</p>
<div class="callout warning">
<strong>Site asset paths are shared.</strong> Identical files targeting the same path are deduplicated. Different contents targeting the same path stop preview and publishing with an error.</div>
</section>

<h2>requiresPHP</h2>
<section class="reference-entry">
<h3>requiresPHP</h3>
<div class="api-meta">
<span class="pill">Boolean</span><span class="pill">Optional</span><span class="pill">Default: false</span>
</div>
<p>Declares that the part needs PHP-capable hosting. When <code>true</code>, every page containing the part uses a <code>.php</code> extension. Set it when the part declares a PHP template or a PHP asset, including a separate endpoint called by JavaScript.</p>


<div markdown="1">

```json
"requiresPHP" : true
```

</div>


<div class="callout warning">
<strong>Keep the declaration explicit.</strong> A <code>.php</code> file alone does not replace this key. <code>requiresPHP</code> is the part’s statement that the page and its hosting environment require PHP.</div>
</section>

<h2>Template files are not assets</h2>
<p>Put a file under <code>templates</code> when Foundry should process its macros and emit its result. Put it under <code>assets</code> when Foundry should copy it as a resource. A path should not be declared in both places.</p>
<div class="rule-summary">
    <div>
<strong>Template</strong><span>Foundry reads and processes the source.</span>
</div>
    <div>
<strong>Asset</strong><span>Foundry publishes the packaged file.</span>
</div>
    <div>
<strong>Library</strong><span>Foundry supplies and deduplicates the dependency.</span>
</div>
</div>

<div class="page-links">
    <a class="card" href="templates.html"><strong>Template files</strong><p>See the supported source file types and scopes.</p></a>
    <a class="card" href="template-identity.html"><strong>Asset template values</strong><p>Use declared assets safely from part markup and styles.</p></a>
</div>
{% endraw %}
