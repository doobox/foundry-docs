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
<video src="{{ control.film }}"
       poster="{{ control.film.poster }}"
       {{ control.film.attributes }}></video>
```

<p>Like the image control, this one hands over values and your template writes the markup — so you are free to add <code>&lt;source&gt;</code> alternatives, a <code>&lt;track&gt;</code> for captions, classes, or a wrapper. <code>control.film</code> is the video's URL, and <code>control.film.attributes</code> expands the Inspector's playback choices to the matching HTML attributes; write your own instead whenever the part wants fixed behaviour. The Inspector can choose an existing video from project Resources, import one from the Mac, or accept a video dropped from Finder or Resources. Imported files are added to Resources. The media well shows Foundry’s generated poster together with the filename, dimensions, duration and file size. Other media types are rejected, and formats that may not play consistently across browsers are identified in the Inspector.</p>

## Playback options

The **Pick** button opens the Mac file picker. The adjacent link button opens **Video on the Web**, with **Import Copy** on the left and **Link** as the primary action on the right.

**Link** accepts a direct HTTP(S) video-file URL or a YouTube video link without importing the movie. Direct files depend on the host and browser format support. They have no generated poster or local file metadata; the canvas shows a **Linked video** placeholder unless a custom poster is supplied. Vimeo page links are not supported.

For YouTube, paste a watch, share, Shorts, live-video or embed URL. **Import Copy** is unavailable: Foundry embeds the video rather than downloading it. **Show poster first** defaults to on. The published page initially shows a poster with a Play button; activating it replaces the entire button and poster with YouTube's player and requests playback. Browser playback restrictions can still apply. Turning the option off loads the standard player directly.

The poster defaults to the highest available YouTube thumbnail, with lower-resolution fallbacks. Use **Choose…** in the Poster row to supply your own image; **Clear** restores the automatic thumbnail. Custom posters are included in the site's assets. Automatic thumbnails require an internet connection and contact YouTube even before playback. `control.film.poster` returns the custom poster URL when selected, otherwise the preferred YouTube thumbnail URL. `control.film.posterFirst` is a Boolean, and `control.film.customPoster` indicates whether a poster was supplied to the renderer. YouTube controls its own player after activation; Foundry never leaves the poster above it. Controls, Loop and Start At apply to YouTube; Autoplay and Muted remain hidden. Background video remains limited to direct files.

Use the standard `<video src="{{ control.film }}" ...></video>` pattern above for source-aware rendering. When the selection is YouTube, Foundry replaces that element with a styled wrapper containing a thumbnail on the canvas, and either the poster-first button or a privacy-enhanced YouTube iframe in preview and published output. The poster-first behaviour includes its required JavaScript automatically. Classes remain on the wrapper; style classes rather than relying on a `video` tag selector. Native-video children such as `<source>` and `<track>` do not apply to YouTube. The original URL remains available through the direct control value and `href`; placing that URL in arbitrary markup does not turn it into a playable video-file URL. The `video("name")` template primitive also recognises YouTube links, using a direct player. Embedding must be allowed by the video's owner, and privacy-enhanced mode still connects to YouTube.

**Import Copy** downloads and validates a video file up to 100 MB, adds it to Resources, and uses the normal generated-poster workflow. Import failures appear in the popover. Closing the popover cancels an in-progress import.

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

<p><code>control.film</code> is the video's URL, empty when none is selected. The structured values below cover everything else:</p>

```text
control.film.source
control.film.attributes
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

<p><code>control.film.source</code> is the exported path with the Start At media fragment applied, which is what Foundry substitutes into your <code>src</code>. <code>control.film.attributes</code> is the ready-made attribute list — <code>autoplay</code>, <code>muted</code>, <code>loop</code>, <code>controls</code> as chosen, always with <code>playsinline</code>. <code>control.film.href</code> returns the exported video path without the Start At fragment. <code>control.film.poster</code> returns a custom poster when one was chosen, otherwise the still frame Foundry generates for the selected video. Playback fields return the Inspector selections: <code>autoplay</code> is <code>never</code> or <code>onLoad</code>, the three attribute switches are Booleans, and <code>startAt</code> is a number of seconds. Use these values to build custom markup when the standard element is not suitable. The editing canvas receives the poster but does not receive or load the selected video URL. Preview and published output receive the exported video path and a separate managed poster-image path.</p>

<p>Foundry rewrites your <code>&lt;video&gt;</code> for the editing canvas exactly as it does an image's <code>&lt;img&gt;</code>: while no video is selected the element becomes Foundry&rsquo;s standard drop well, and once filled it keeps your poster and attributes but carries no <code>src</code>, so the editor never streams the movie. Dropping a movie onto it replaces the video; dropping an image sets the poster.</p>

<p>Video and poster selections are not responsive: one selection is used at every breakpoint. A custom poster is retained when a video is subsequently selected or replaced. <code>duration</code> is the video length in seconds. Dimensions, aspect ratio and duration are empty when that metadata is unavailable.</p>
{% endraw %}
