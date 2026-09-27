---
layout: default
title: Reveal control group · Foundry Developer
permalink: /developer/reveal-control-group.html
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector · control groups</p>
<h1>Reveal</h1>
<p class="lede">Animate a part as it enters the viewport.</p>

## Quick example

Add this entry to your manifest’s `inspector` array:

```json
{
    "section": "Reveal",
    "controls": [
        {
            "type": "reveal",
            "id": "reveal"
        }
    ]
}
```

Use your normal part template. Foundry animates its root element automatically.

Foundry supplies the animation and required libraries. No CSS interpolation or custom JavaScript is needed. The author turns Reveal on in the Inspector.

The `id` is required. This page uses `reveal`, so every template path starts with `control.reveal.`. Choose a different ID when you need another instance of the same group.

## Animate an inner element

Replace the declaration above with this entry to animate only the content wrapper:

```json
{
    "type": "reveal",
    "id": "contentReveal",
    "targetSelector": ".content"
}
```

```html
<section class="{{ part.class }}" {{ part.attributes }}>
    <div class="content">
        <p>Your content goes here.</p>
    </div>
</section>
```

The wrapper becomes both the animated element and the scroll trigger. With Stagger enabled, its direct children animate instead. No template interpolation is needed.

## Properties

Each JSON example below is an alternative entry for your manifest’s `inspector` array, or for a section’s `controls` array. Start with the quick example and add the keys you need to that same group object; do not paste every example as another group with the same ID.

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Always `reveal`. The group does not accept `label`, `group`, `responsive`, `backgroundTypes`, or `supportsHover`.


Choose this built-in group:

```json
{
    "type": "reveal",
    "id": "reveal"
}
```

<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

A unique name for this group in the part. Start with a letter; use letters, numbers, underscores or hyphens. Do not reuse another group or control’s ID. There is no default.

For `"id": "reveal"`, read values as `control.reveal.<controlID>`. Keep this ID stable: it identifies the group’s saved values.


For example, name this group `panelStyle`:

```json
{
    "type": "reveal",
    "id": "panelStyle"
}
```

Its values now start with `control.panelStyle.`, for example `control.panelStyle.revealEnabled`. The animation remains automatic.

<h3 class="property-heading"><code>targetSelector</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: part root</span></div>

A literal CSS selector for exactly one descendant element owned by this part, such as `.content` or `:scope > .content`. Omit the key to animate the root. Empty strings and template expressions are not accepted. This key is available only on Reveal groups.

The selector is searched inside the current part. Nested parts and their internal elements are excluded. If the selector is invalid, matches nothing, or matches more than one owned element, Foundry skips this group's animation and logs a browser-console warning. It never falls back to the root.

Two Reveal groups can use different IDs and different targets. Avoid targeting the same element from both: separate settings do not prevent conflicting animations.


For a direct child wrapper with class `content`:

```json
{
    "type": "reveal",
    "id": "reveal",
    "targetSelector": ":scope > .content"
}
```

Use the HTML in “Animate an inner element” above. `targetSelector` is part-developer configuration, not an Inspector control.

<h3 class="property-heading"><code>defaults</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: generated defaults</span></div>

Changes initial values using local control IDs, without the group prefix. Each value replaces the complete base default and must use the type and allowed values documented below. Unknown or omitted IDs are errors. For example, use `revealEnabled`, not `reveal.revealEnabled`, as the configuration key.


For example, change the starting settings:

```json
{
    "type": "reveal",
    "id": "reveal",
    "defaults": {
        "revealEnabled": true,
        "revealEffect": "fade",
        "revealDuration": 800
    }
}
```

These are initial values, not locked settings. The author can still change the controls in the Inspector.

<h3 class="property-heading"><code>excludeControls</code></h3>
<div class="property-meta"><span class="property-type">Array of strings</span><span class="optional">Optional</span><span class="default">Default: exclude nothing</span></div>

Removes controls this part does not need. Use unique local IDs, without the group prefix. Dependent controls are removed too: omitting a mode also removes fields that only configure that mode. Omitted controls have no template value. You cannot explicitly omit every control; remove the group instead.


Remove the stagger control so the selected target animates as one element.

```json
{
    "type": "reveal",
    "id": "reveal",
    "excludeControls": [
        "revealStagger"
    ]
}
```

The remaining controls still work with the same group output. Use the local IDs shown above—not full paths such as `control.reveal.revealStagger`.

<h3 class="property-heading"><code>allowedOptions</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: all options</span></div>

Limits a select control to a non-empty list of its option values, in display order. Keys are local control IDs. Unknown or duplicate options, omitted controls, and controls without options are errors. The original default is kept if allowed; otherwise the first option becomes the default. A value in `defaults` must also be allowed. See the [configuration example](control-groups.html#configure-a-group).


Offer only Fade and Fade up.

```json
{
    "type": "reveal",
    "id": "reveal",
    "allowedOptions": {
        "revealEffect": [
            "fade",
            "fade-up"
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
    "section": "Optional reveal settings",
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
            "type": "reveal",
            "id": "reveal",
            "visibleWhen": {
                "id": "showOptions",
                "value": true
            }
        }
    ]
}
```

Turning off Show options hides these settings in the Inspector; it does not turn off their styles or animation. The condition uses `showOptions` because that toggle is a separate control, outside the group.

## Generated controls

The entries below are values generated by the group—not additional declarations to paste into `inspector`. To change a starting value, put its local ID in `defaults`, as shown above. Keep the group prefix when reading it in a template.

These paths use the example ID `reveal`. Change that prefix if you choose another ID.

Reveal values are intentionally not responsive. ScrollTrigger recalculates positions when the viewport changes, while one animation configuration remains consistent across breakpoints.

<h3 class="property-heading"><code>control.reveal.revealEnabled</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="default">Default: false</span></div>

Enables the generated animation and shows the remaining Reveal controls.

<h3 class="property-heading"><code>control.reveal.revealEffect</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: fade-up</span></div>

Accepts `fade`, `fade-up`, `fade-down`, `fade-left`, `fade-right`, `scale`, or `blur`.

<h3 class="property-heading"><code>control.reveal.revealDistance</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 32</span></div>

Movement in pixels for directional effects and blur radius in pixels for `blur`. Accepts integers from 0 through 200.

<h3 class="property-heading"><code>control.reveal.revealDuration</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 600</span></div>

Animation duration in milliseconds. Accepts 100 through 3000 in steps of 50.

<h3 class="property-heading"><code>control.reveal.revealDelay</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 0</span></div>

Delay before animation in milliseconds. Accepts 0 through 3000 in steps of 50.

<h3 class="property-heading"><code>control.reveal.revealEase</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: power2.out</span></div>

Accepts `power1.out`, `power2.out`, `power3.out`, `back.out(1.7)`, `elastic.out(1,0.3)`, `bounce.out`, or `none`.

<h3 class="property-heading"><code>control.reveal.revealStagger</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 0</span></div>

At zero, Foundry animates the selected target (the root when `targetSelector` is omitted). A value above zero animates that element's direct children in order, using the value as the interval in milliseconds. The selected element remains the scroll trigger. Accepts 0 through 1000 in steps of 25.

<h3 class="property-heading"><code>control.reveal.revealTrigger</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 85</span></div>

Viewport percentage at which the selected target's top edge triggers the animation. Accepts 0 through 100.

<h3 class="property-heading"><code>control.reveal.revealOnce</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="default">Default: true</span></div>

When `true`, the reveal plays once. When `false`, it reverses after scrolling back above its trigger and can play again.

## Return value

- `control.reveal.revealEnabled`, `control.reveal.revealOnce`: Booleans.
- `control.reveal.revealEffect`, `control.reveal.revealEase`: Strings — the effect name and a GSAP easing identifier.
- `control.reveal.revealDistance`, `control.reveal.revealDuration`, `control.reveal.revealDelay`, `control.reveal.revealStagger`, `control.reveal.revealTrigger`: Numbers, with no unit attached.

Every value is flat — no qualified fields — and none is a CSS value. The numbers carry the units named above (pixels for `revealDistance`, milliseconds for the three timings, a viewport percentage for `revealTrigger`) as bare numbers, so append or convert if you use them in CSS or your own JavaScript.

Unlike every other group, Reveal consumes its own values: it generates the GSAP animation and requests GSAP with ScrollTrigger. A part needs to read none of them, and reading them cannot change the generated animation. They are exposed so a part can reflect the configuration elsewhere — matching a manual transition to `revealDuration`, say.

These values are deliberately not responsive, so there are no breakpoint variants to account for.

## Runtime behavior

The animation returns to the part's existing appearance. When the visitor requests reduced motion, Foundry skips the animation and leaves the part unmodified. If JavaScript or either library is unavailable, the original markup remains visible because Foundry does not pre-hide it with CSS.

Part JavaScript can use `gsap` and `ScrollTrigger` directly alongside the generated animation. Use a separate manifest library request only when the part needs those APIs without declaring this group.
{% endraw %}
