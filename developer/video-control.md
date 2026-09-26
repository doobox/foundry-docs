---
layout: default
title: Video control · Foundry Developer
permalink: "/developer/video-control.html"
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector</p>
<h1>Video</h1>
<p class="lede">Let someone choose, import, replace or clear a project video using the standard media well.</p>

## Quick example

```json
{
    "type" : "video",
    "id" : "film",
    "label" : "Video",
    "defaults" : {
        "base" : ""
    }
}
```

```html
{{ control.film }}
```

<p>The direct value renders the complete video element, including its selected or generated poster and playback settings. The Inspector can choose an existing video from project Resources, import one from the Mac, or accept a video dropped from Finder or Resources. Imported files are added to Resources. The media well shows Foundry’s generated poster together with the filename, dimensions, duration and file size. Other media types are rejected, and formats that may not play consistently across browsers are identified in the Inspector.</p>

## Playback options

<p>The video control includes its complete playback experience; a part developer does not need to declare separate controls for these settings.</p>

<section class="key-reference"><h3>Autoplay</h3><div class="key-meta"><span>Never or On page load</span><span>Default: Never</span></div><p>Controls whether Foundry emits the <code>autoplay</code> attribute. Browsers commonly require an autoplaying video to be muted.</p></section>
<section class="key-reference"><h3>Muted</h3><div class="key-meta"><span>Boolean</span><span>Default: false</span></div><p>Emits the <code>muted</code> attribute.</p></section>
<section class="key-reference"><h3>Controls</h3><div class="key-meta"><span>Boolean</span><span>Default: true</span></div><p>Shows the browser’s native video controls.</p></section>
<section class="key-reference"><h3>Loop</h3><div class="key-meta"><span>Boolean</span><span>Default: false</span></div><p>Emits the <code>loop</code> attribute.</p></section>
<section class="key-reference"><h3>Start At</h3><div class="key-meta"><span>Number of seconds</span><span>Default: 0</span></div><p>Starts playback at the chosen time. Positive values are applied to the generated video source as a media-fragment start time.</p></section>

## Properties

<section class="key-reference"><h3><code>type</code></h3><div class="key-meta"><span>String</span><strong>Required</strong><span><code>video</code></span></div></section>
<section class="key-reference"><h3><code>id</code></h3><div class="key-meta"><span>String</span><strong>Required</strong></div><p>The unique control and template value name.</p></section>
<section class="key-reference"><h3><code>label</code></h3><div class="key-meta"><span>String</span><span>Optional</span></div></section>
<section class="key-reference"><h3><code>defaults</code></h3><div class="key-meta"><span>Dictionary</span><strong>Required</strong></div><p>Use an empty String for no selected video.</p></section>
<section class="key-reference"><h3><code>tooltip</code></h3><div class="key-meta"><span>String</span><span>Optional</span></div></section>
<section class="key-reference"><h3><code>visibleWhen</code></h3><div class="key-meta"><span>Dictionary</span><span>Optional</span></div><p>Conditionally shows the complete video row. A hidden row retains its selected value.</p></section>
<section class="key-reference"><h3><code>valueAvailability</code></h3><div class="key-meta"><span>String</span><span>Optional</span><span>Default: always</span></div><p>Use <code>always</code> to keep this control's template value available while hidden, or <code>whenVisible</code> to make the value and its qualified derived values unavailable while <code>visibleWhen</code> is false. The stored value is preserved. <code>whenVisible</code> requires <code>visibleWhen</code>.</p></section>

## Template values

<p><code>control.film</code> renders the complete video element. It is empty when neither a video nor a custom poster is present. Use the structured values when the part needs different markup or playback behaviour:</p>

```text
control.film.href
control.film.filename
control.film.poster
control.film.autoplay
control.film.muted
control.film.controls
control.film.loop
control.film.startAt
control.film.extension
control.film.mimeType
control.film.byteCount
control.film.width
control.film.height
control.film.aspectRatio
control.film.duration
```

<p><code>control.film.href</code> returns the exported video path without the Start At fragment. <code>control.film.poster</code> returns a custom poster when one was chosen, otherwise the still frame Foundry generates for the selected video. Playback fields return the Inspector selections: <code>autoplay</code> is <code>never</code> or <code>onLoad</code>, the three attribute switches are Booleans, and <code>startAt</code> is a number of seconds. Use these values to build custom markup when the standard element is not suitable. The editing canvas receives the poster but does not receive or load the selected video URL. Preview and published output receive the exported video path and a separate managed poster-image path.</p>

<p>On the editing canvas the rendered element is itself a drop target. While no video is selected it appears as Foundry&rsquo;s standard drop well; once filled, dropping a movie file replaces the video and dropping an image sets the poster. The published element carries the <code>fd-video</code> class.</p>

<p>Video and poster selections are not responsive: one selection is used at every breakpoint. A custom poster is retained when a video is subsequently selected or replaced. <code>duration</code> is the video length in seconds. Dimensions, aspect ratio and duration are empty when that metadata is unavailable.</p>
{% endraw %}
