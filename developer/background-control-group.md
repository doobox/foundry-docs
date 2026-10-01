---
layout: default
title: Background control group · Foundry Developer
permalink: /developer/background-control-group.html
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector · control groups</p>
<h1>Background</h1>
<p class="lede">Add a colour, image or gradient background. Opt into video when your part supplies a positioned host.</p>

## Quick example

Add this entry to your manifest’s `inspector` array:

```json
{
    "section": "Background",
    "controls": [
        {
            "type": "background",
            "id": "background"
        }
    ]
}
```

Use your normal markup in `part.html`:

```html
<section class="{{ part.class }}" {{ part.attributes }}>
    <p>Your content goes here.</p>
</section>
```

Add this to your instance-scoped CSS file:

```css
:instance {
    {{ control.background.css }}
}
:instance:hover { {{ control.background.hover.css }} }
```

The default group offers colour, image and gradient. These need no special markup, positioning or isolation.

## Opt into video and combine it with Layout

Add `video` explicitly to `backgroundTypes`. This is the same public API used by Foundry's built-in parts; it is available to every developer.

```json
{
    "type": "background",
    "id": "background",
    "backgroundTypes": ["colour", "image", "gradient", "video"]
}
```

Insert the video output as a direct child of the element that owns the background. Keep your content alongside it:

```html
<section class="{{ part.class }}" {{ part.attributes }}>
    {{ control.background.video }}
    <p>Your content goes here.</p>
</section>
```

Keep the host positioned and isolated. A sticky, absolute or fixed host works too; do not add a later `position: relative` rule that overrides the chosen position. If Layout controls this host, exclude both None (`none`) and Static (`static`) so users cannot remove the video's positioning boundary:

```json
{
    "type": "layout",
    "id": "layout",
    "allowedOptions": {
        "position": ["relative", "absolute", "fixed", "sticky"]
    }
}
```

```css
:instance {
    isolation: isolate;
    {{ control.background.css }}
    {{ control.layout.css }}
}
:instance:hover { {{ control.background.hover.css }} }
```

This replaces the quick example's CSS. The Layout declaration supplies positioning, starting at `relative`. Alternatively, omit Layout's `position` control and set positioning in your stylesheet.

Opting into video does not automatically change or restrict Layout. The developer supplies this structure and these restrictions. The video output has its own decorative wrapper, which inherits the host's corner radius and does not capture clicks or take up layout space.

Overflow is still the part's choice. Leaving it visible permits dropdowns and other content to extend outside the section; choosing Hidden will intentionally clip that content. The video wrapper clips only the video in either case. Host isolation also creates a stacking boundary, so content cannot independently stack above a neighbouring part whose entire stacking context is higher.

The `id` is required. This page uses `background`, so every template path starts with `control.background.`. Choose a different ID when you need another instance of the same group.

## Properties

Each JSON example below is an alternative entry for your manifest’s `inspector` array, or for a section’s `controls` array. Start with the quick example and add the keys you need to that same group object; do not paste every example as another group with the same ID.

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Always `background`. The group does not accept `label`, `group`, or `responsive`.


Choose this built-in group:

```json
{
    "type": "background",
    "id": "background"
}
```

<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

A unique name for this group in the part. Start with a letter; use letters, numbers, underscores or hyphens. Do not reuse another group or control’s ID. There is no default.

For `"id": "background"`, read values as `control.background.<controlID>`, and use `control.background.css` for the complete CSS block. Keep this ID stable: it identifies the group’s saved values.


For example, name this group `panelStyle`:

```json
{
    "type": "background",
    "id": "panelStyle"
}
```

Use that same ID in your CSS:

```css
:instance { {{ control.panelStyle.css }} }
```

This only demonstrates the renamed output; keep any structural CSS from the quick example.

<h3 class="property-heading"><code>defaults</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: generated defaults</span></div>

Replaces complete generated base values using local IDs such as `backgroundMode`. Values must belong to the vocabulary left by `backgroundTypes`, `supportsHover` and option filtering. Use local control IDs directly: `"defaults": { "backgroundMode": "static" }`. Do not wrap group defaults in `base`; Foundry applies these as starting values and the author uses the blue dots for responsive changes.


For example, change the starting settings:

```json
{
    "type": "background",
    "id": "background",
    "defaults": {
        "backgroundMode": "static",
        "backgroundStyle": "gradient"
    }
}
```

These are initial values, not locked settings. The author can still change the controls in the Inspector.

<h3 class="property-heading"><code>backgroundTypes</code></h3>
<div class="property-meta"><span class="property-type">Array of strings</span><span class="optional">Optional</span><span class="default">Default: colour, image, gradient</span></div>

Selects the background styles offered by the Inspector. Accepted values are `colour`, `image`, `gradient`, and `video`. The array must contain at least one unique value. Its first value is the initial Static style. Omitting the key includes `colour`, `image`, and `gradient` only. Include `video` explicitly to generate the video controls. Video requires a positioned, isolated host; if Layout controls that host, restrict its positions to `relative`, `absolute`, `fixed`, and `sticky`, as shown above. Hover offers only the declared `colour`, `image`, and `gradient` styles; video is Static-only.

```json
{
    "type" : "background", "id": "background",
    "backgroundTypes" : [
        "colour",
        "image"
    ]
}
```

<h3 class="property-heading"><code>supportsHover</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: true</span></div>

Set to `false` when the part should not offer hover backgrounds. This removes the Hover choice and all hover-only controls. Normal backgrounds remain available. Leave it out, or set it to `true`, to offer hover styling for colour, image and gradient backgrounds. Video never has a hover background. Available only on Background groups.


Offer a static background without hover settings:

```json
{
    "type": "background",
    "id": "background",
    "supportsHover": false
}
```

Keep `control.background.css` in your normal CSS rule. A separate hover rule is unnecessary for this declaration.

<h3 class="property-heading"><code>excludeControls</code></h3>
<div class="property-meta"><span class="property-type">Array of strings</span><span class="optional">Optional</span><span class="default">Default: exclude nothing</span></div>

Removes controls this part does not need. Use unique local IDs, without the group prefix. Dependent controls are removed too: omitting a mode also removes fields that only configure that mode. Omitted controls have no template value. You cannot explicitly omit every control; remove the group instead.


Remove the image-repeat control. Image backgrounds still use the standard no-repeat behaviour.

```json
{
    "type": "background",
    "id": "background",
    "excludeControls": [
        "backgroundRepeat"
    ]
}
```

The remaining controls still work with the same group output. Use the local IDs shown above—not full paths such as `control.background.backgroundRepeat`.

<h3 class="property-heading"><code>allowedOptions</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: all options</span></div>

Limits a select control to a non-empty list of its option values, in display order. Keys are local control IDs. Unknown or duplicate options, omitted controls, and controls without options are errors. The original default is kept if allowed; otherwise the first option becomes the default. A value in `defaults` must also be allowed. Use `supportsHover: false` to disable hover for the entire group; use `allowedOptions` to limit choices within one remaining control.


Offer only Cover and Contain for image backgrounds.

```json
{
    "type": "background",
    "id": "background",
    "allowedOptions": {
        "backgroundSize": [
            "cover",
            "contain"
        ]
    }
}
```

<h3 class="property-heading"><code>visibleWhen</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: always visible</span></div>

Shows these Inspector controls only when the [visibility condition](visible-when.html) matches. It does not disable their output. Reference an exact part-level ID: for example, `arrangement` for a standalone control or `contentSize.widthMode` for a grouped control. The condition is combined with each generated control’s own visibility rules.


This example includes the toggle that the condition reads. Add the whole section to `inspector`:

```json
{
    "section": "Optional background settings",
    "controls": [
        {
            "type": "toggle",
            "id": "showOptions",
            "label": "Show options",
            "defaults": {
                "base": true
            }
        },
        {
            "type": "background",
            "id": "background",
            "visibleWhen": {
                "id": "showOptions",
                "value": true
            }
        }
    ]
}
```

Turning off Show options hides these settings in the Inspector; it does not turn off their styles. The condition uses `showOptions` because that toggle is a separate control, outside the group.

## Generated controls

The entries below are values generated by the group—not additional declarations to paste into `inspector`. To change a starting value, put its local ID in `defaults`, as shown above. Keep the group prefix when reading it in a template.

These paths use the example ID `background`. Change that prefix if you choose another ID.

Only values for the selected background types and supported hover settings are generated. With top-level Type set to Hover, the Inspector shows one set of controls at a time and `backgroundState` switches between Normal and Hover. Both states offer colour, image and gradient; neither offers video. Generated values are responsive except `backgroundMode`, video selections, and their posters. A Static video uses the same selected asset at every breakpoint.

### Mode

<h3 class="property-heading"><code>control.background.backgroundMode</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: none</span><span>Not responsive</span></div>

One of `none`, `static`, or `hover`. `static` gives the part a single background; `hover` gives it two, one for each state. `hover` is available only when `supportsHover` is `true` and at least one hover-compatible background type is available.

<h3 class="property-heading"><code>control.background.backgroundState</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: normal</span><span>Not responsive</span></div>

Either `normal` or `hover`, shown only while `backgroundMode` is `hover`. It chooses which of the two states the controls beneath it are editing — both states keep their own complete set of values, so switching back and forth never discards anything. This is an editing affordance rather than output: templates read the Static and Hover values below, never this.

### Static values

<h3 class="property-heading"><code>control.background.backgroundStyle</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: first declared style</span></div>

One of `color`, `image`, `gradient`, or `video` while top-level Type is Static. When Type is Hover, the Normal state offers only `color`, `image`, and `gradient`. The manifest spelling `colour` becomes the template value `color`.

<h3 class="property-heading"><code>control.background.backgroundColor</code></h3>
<div class="property-meta"><span class="property-type">CSS colour</span><span class="default">Default: surface palette</span><span>Responsive</span></div>

The resolved framework or custom colour, including opacity.

<h3 class="property-heading"><code>control.background.backgroundImage</code></h3>
<div class="property-meta"><span class="property-type">Image</span><span class="default">Default: empty</span><span>Responsive</span></div>

The selected managed image path. Its structured fields follow the [Image control](image-control.html).

The image offers the Inspector's Focal Point button. The chosen point becomes the background's `background-position` as `x% y%`, so it stays in view when `cover` crops the image. The default is `50% 50%`. `control.background.backgroundImage.position` returns the same value.

<h3 class="property-heading"><code>control.background.backgroundSize</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: cover</span><span>Responsive</span></div>

One of `cover`, `contain`, or `auto`.

<h3 class="property-heading"><code>control.background.backgroundRepeat</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: no-repeat</span><span>Responsive</span></div>

One of `no-repeat`, `repeat`, `repeat-x`, `repeat-y`, `space`, or `round`.

<h3 class="property-heading"><code>control.background.backgroundGradientType</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: linear</span><span>Responsive</span></div>

One of `linear`, `radial`, or `conic`.

<h3 class="property-heading"><code>control.background.backgroundGradientDirection</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: to bottom</span><span>Responsive</span></div>

The CSS direction for a linear gradient.

<h3 class="property-heading"><code>control.background.backgroundGradientFrom</code></h3>
<div class="property-meta"><span class="property-type">CSS colour</span><span class="default">Default: surface palette</span><span>Responsive</span></div>

The first resolved framework or custom colour.

<h3 class="property-heading"><code>control.background.backgroundGradientFromPosition</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 0</span><span>Responsive</span></div>

The first stop position from 0 through 100.

<h3 class="property-heading"><code>control.background.backgroundGradientTo</code></h3>
<div class="property-meta"><span class="property-type">CSS colour</span><span class="default">Default: accent palette</span><span>Responsive</span></div>

The second resolved framework or custom colour.

<h3 class="property-heading"><code>control.background.backgroundGradientToPosition</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 100</span><span>Responsive</span></div>

The second stop position from 0 through 100.

<h3 class="property-heading"><code>control.background.backgroundVideo</code></h3>
<div class="property-meta"><span class="property-type">Video</span><span class="default">Default: empty</span><span>Not responsive</span></div>

Generated only when `backgroundTypes` includes `video`. The selected Static background video. `control.background.video` already writes the element from it, so most parts never read this: it is here for a part that wants the underlying values. The unqualified value and `.href` return the exported video path. `.poster` is always the automatically generated still: the canvas uses its image data, and published output uses an exported JPEG. Background videos have no custom-poster picker and ignore previously saved custom posters. Standalone [Video controls](video-control.html) retain custom posters. Filename, extension, MIME type, byte count, duration and dimensions use the other structured video values. These values are available only when top-level Type is Static.

<h3 class="property-heading"><code>control.background.backgroundOverlayEnabled</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="default">Default: false</span><span>Responsive</span></div>

Enables a solid-colour overlay on an image or video background, without tinting the part's content. Generated when `backgroundTypes` includes `image` or `video`. Normal and Hover share this setting and the overlay colour, rather than having independent overlays. The controls appear when the Static background is an image or video, or either Hover-mode state uses an image, regardless of which state is being edited. There is no gradient overlay option.

<h3 class="property-heading"><code>control.background.backgroundOverlayColor</code></h3>
<div class="property-meta"><span class="property-type">Framework colour</span><span class="default">Default: standard.black at 0.2 opacity (20%)</span><span>Responsive</span></div>

The overlay uses the [Framework colour control](framework-colour-control.html), with custom colours allowed and the opacity slider enabled. Shown when Overlay is enabled. Users can choose a palette or literal colour and adjust its opacity; the default is black at 20% opacity. The same tint covers the video's generated poster and its playing frames. Use `control.background.css` to apply the finished appearance; no additional overlay markup is needed.

<h3 class="property-heading"><code>control.background.backgroundVideoLoop</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="default">Default: true</span><span>Not responsive</span></div>

Generated when `backgroundTypes` includes `video`. Repeats the background video. When disabled, the video plays once and stays on its last frame.

### Hover values

When hover is supported, the Hover configuration exposes the corresponding selected style values with a `backgroundHover` prefix:

- `control.background.backgroundHoverStyle`
- `control.background.backgroundHoverColor`
- `control.background.backgroundHoverImage`
- `control.background.backgroundHoverSize`
- `control.background.backgroundHoverRepeat`
- `control.background.backgroundHoverGradientType`
- `control.background.backgroundHoverGradientDirection`
- `control.background.backgroundHoverGradientFrom`
- `control.background.backgroundHoverGradientFromPosition`
- `control.background.backgroundHoverGradientTo`
- `control.background.backgroundHoverGradientToPosition`

Each Hover value has the same type, accepted values and default as its Static counterpart. Both states use the shared `backgroundOverlayEnabled` and `backgroundOverlayColor` values. When either state uses an image, an enabled overlay stays unchanged across both states, including when the other state uses a colour or gradient. `backgroundHoverStyle` defaults to the first declared hover-compatible style.

## Return value

The group resolves every selection into the `control.background` namespace, and the part decides where those values land. Each value is always present, so templates need no conditionals.

<h3 class="property-heading"><code>control.background.css</code></h3>
<div class="property-meta"><span class="property-type">CSS declarations</span></div>

The background paint declarations: `background-color`, `background-image`, `background-position`, `background-size` and `background-repeat`. Image overlays are included in these values. For video, it also supplies `--foundry-background-overlay`, which the decorative video layer inherits from its host. It never sets host positioning, isolation or overflow. Drop it into a rule body on the host.

<h3 class="property-heading"><code>control.background.video</code></h3>
<div class="property-meta"><span class="property-type">HTML</span></div>

The complete decorative video layer, or an empty string unless the group opts into video and a Static video has a selected video or poster. Published output wraps a muted, looping, `playsinline` `<video>` in a `foundry-background-layer` div; the canvas uses the poster `<img>` inside that same wrapper. Without a poster, the canvas emits no layer rather than a broken image.

The generated still supplies the published video's `poster` attribute while playback loads. Foundry exports one JPEG per referenced video, shared across instances and pages. If poster generation is unavailable, it omits the attribute rather than writing a broken image URL; video playback remains available.

With JavaScript and Intersection Observer available, background videos automatically pause offscreen or while the browser tab is hidden, then resume from the same point when visible again. A completed non-looping video does not restart on re-entry. This behaviour is supplied when the group opts into video; developers need no playback script. Browser autoplay restrictions still apply. Without Intersection Observer, the normal autoplay and loop attributes remain the fallback.

The built-in stylesheet positions the wrapper behind content, clips its contents, inherits the host's corner radius and disables pointer events. Media fills the wrapper using `object-fit: cover`. The wrapper and media are `aria-hidden`. Insert this output directly inside a positioned, isolated host, as in the video opt-in example. Keep content alongside the layer, not inside it.

<h3 class="property-heading">Individual values</h3>

`color` is a colour or `transparent`. `image` is `none`, a `url(…)`, or a composed `linear-gradient(…)`/`radial-gradient(…)`/`conic-gradient(…)`. An enabled image overlay adds a uniform solid-colour CSS paint layer above the image; `position`, `size` and `repeat` then contain matching comma-separated values, preserving the image's focal point, sizing and repeat settings. Without an overlay, `position` is the image's focal point as `x% y%`; `size` and `repeat` are the image keywords. Use `.css` for the complete appearance, including video overlay styling. There is no `videoCSS` output: host structure belongs in the part's stylesheet.

`css` and the image-related values have `control.background.hover.*` counterparts; video is Static-only. The individual `backgroundColor`, `backgroundGradientFrom` and similar control values also remain available when a part wants to compose something different — each with its own control's shape, so the framework colours carry the [Framework colour control](framework-colour-control.html) fields and `backgroundImage` carries the [Image control](image-control.html) fields.

{% endraw %}
