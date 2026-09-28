---
layout: default
title: Sizing control group · Foundry Developer
permalink: /developer/sizing-control-group.html
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector · control groups</p>
<h1>Sizing</h1>
<p class="lede">Set a part’s width and height, with optional minimum and maximum sizes.</p>

## Quick example

Add this entry to your manifest’s `inspector` array:

```json
{
    "section": "Sizing",
    "controls": [
        {
            "type": "sizing",
            "id": "sizing"
        }
    ]
}
```

Add this to your instance-scoped CSS file:

```css
:instance { {{ control.sizing.css }} }
```

Sizing changes the element where you place its CSS. Put it on the outer section to size the section, or on an inner element to size its content box.

The `id` is required. This page uses `sizing`, so every template path starts with `control.sizing.`. Choose a different ID when you need another instance of the same group.

## Properties

Each JSON example below is an alternative entry for your manifest’s `inspector` array, or for a section’s `controls` array. Start with the quick example and add the keys you need to that same group object; do not paste every example as another group with the same ID.

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Always `sizing`. The group does not accept `label`, `group`, `responsive`, `backgroundTypes`, or `supportsHover`.


Choose this built-in group:

```json
{
    "type": "sizing",
    "id": "sizing"
}
```

<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

A unique name for this group in the part. Start with a letter; use letters, numbers, underscores or hyphens. Do not reuse another group or control’s ID. There is no default.

For `"id": "sizing"`, read values as `control.sizing.<controlID>`, and use `control.sizing.css` for the complete CSS block. Keep this ID stable: it identifies the group’s saved values.


For example, name this group `panelStyle`:

```json
{
    "type": "sizing",
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

Changes initial values using local control IDs, without the group prefix. Each value replaces the complete base default and must use the type and allowed values documented below. Unknown or omitted IDs are errors. For example, use `widthMode`, not `sizing.widthMode`, as the configuration key.


For example, change the starting settings:

```json
{
    "type": "sizing",
    "id": "sizing",
    "defaults": {
        "widthMode": "custom",
        "customWidth": 800
    }
}
```

These are initial values, not locked settings. The author can still change the controls in the Inspector.

<h3 class="property-heading"><code>excludeControls</code></h3>
<div class="property-meta"><span class="property-type">Array of strings</span><span class="optional">Optional</span><span class="default">Default: exclude nothing</span></div>

Removes controls this part does not need. Use unique local IDs, without the group prefix. Dependent controls are removed too: omitting a mode also removes fields that only configure that mode. Omitted controls have no template value. You cannot explicitly omit every control; remove the group instead.


Offer height controls only. Omitting widthMode also removes its dependent customWidth field.

```json
{
    "type": "sizing",
    "id": "sizing",
    "excludeControls": [
        "widthMode",
        "minWidth",
        "maxWidth"
    ]
}
```

The remaining controls still work with the same group output. Use the local IDs shown above—not full paths such as `control.sizing.widthMode`.

<h3 class="property-heading"><code>allowedOptions</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: all options</span></div>

Limits a select control to a non-empty list of its option values, in display order. Keys are local control IDs. Unknown or duplicate options, omitted controls, and controls without options are errors. The original default is kept if allowed; otherwise the first option becomes the default. A value in `defaults` must also be allowed. See the [configuration example](control-groups.html#configure-a-group).


Offer only Fill parent and Custom width. Because auto is no longer available, full becomes the initial choice.

```json
{
    "type": "sizing",
    "id": "sizing",
    "allowedOptions": {
        "widthMode": [
            "full",
            "custom"
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
    "section": "Optional sizing settings",
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
            "type": "sizing",
            "id": "sizing",
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

These paths use the example ID `sizing`. Change that prefix if you choose another ID.

<h3 class="property-heading"><code>control.sizing.widthMode</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: auto</span><span>Responsive</span></div>

One of `auto`, `full`, `fit`, `screen`, `breakpoint`, or `custom`.

<ul>
<li><code>auto</code> — CSS's automatic width. In ordinary block flow it fills the available width after margins, padding and borders; in flex and grid layouts its size also depends on the parent’s layout and alignment.</li>
<li><code>full</code> — Fill parent. Uses stretch sizing to fill the available width while accounting for margins.</li>
<li><code>fit</code> — shrink-wraps the content (<code>fit-content</code>).</li>
<li><code>screen</code> — Viewport. Requests <code>100svw</code>, regardless of the parent. It can exceed the parent and does not automatically align or centre the part against the viewport.</li>
<li><code>breakpoint</code> — Framework container. Fills available space up to the framework's container width for the current breakpoint, via <code>var(--foundry-container-width)</code>.</li>
<li><code>custom</code> — fills available space up to the pixel value from <code>customWidth</code> below. Max width can reduce this size but cannot enlarge it.</li>
</ul>

<h3 class="property-heading"><code>control.sizing.customWidth</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 320</span><span>Responsive</span></div>

A pixel width from 0 through 10,000. Shown when `widthMode` is `custom`.

<h3 class="property-heading"><code>control.sizing.heightMode</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: auto</span><span>Responsive</span></div>

Choose one of:

- `auto` — Fit content. Height follows the content.
- `fill` — Fill remaining space. Uses `flex-grow: 1`; requires a flex parent. Growth follows the parent’s direction, so it is horizontal in a row and vertical in a column.
- `viewport` — At least viewport height. Uses a minimum of `100svh` and can grow with content.
- `custom` — Uses `customHeight` in pixels.

Switching away from Fill resets `flex-grow` to `0`. The group does not change `flex-shrink` or `flex-basis`.

<h3 class="property-heading"><code>control.sizing.customHeight</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 400</span><span>Responsive</span></div>

A pixel height from 0 through 10,000. Shown when `heightMode` is `custom`.

<h3 class="property-heading"><code>control.sizing.aspectRatio</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: none</span><span>Responsive</span></div>

One of `none`, `1 / 1`, `4 / 3`, `3 / 2`, `16 / 9`, `21 / 9`, or `custom`. Shown when `heightMode` is `auto`, because a ratio can only shape a part whose height follows its width. The values other than `none` and `custom` are ready to use as a CSS `aspect-ratio`.

<h3 class="property-heading"><code>control.sizing.aspectRatioWidth</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 4</span><span>Responsive</span></div>

The first term of a custom ratio, from 1 through 1,000. Shown when `aspectRatio` is `custom`.

<h3 class="property-heading"><code>control.sizing.aspectRatioHeight</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 3</span><span>Responsive</span></div>

The second term of a custom ratio, from 1 through 1,000. Shown when `aspectRatio` is `custom`.

<h3 class="property-heading"><code>control.sizing.minWidth</code></h3>
<div class="property-meta"><span class="property-type">Framework spacing</span><span class="default">Default: none</span><span>Responsive</span></div>

The smallest width, as a framework spacing token or custom length. `none` emits `0` — CSS's own "no constraint" for this property.

<h3 class="property-heading"><code>control.sizing.maxWidth</code></h3>
<div class="property-meta"><span class="property-type">Framework spacing</span><span class="default">Default: none</span><span>Responsive</span></div>

The largest width, as a framework spacing token or custom length. `none` emits `none` — CSS's own "no constraint" for this property. The composed CSS combines this limit with the selected width mode; you do not need to build that expression yourself.

<h3 class="property-heading"><code>control.sizing.minHeight</code></h3>
<div class="property-meta"><span class="property-type">Framework spacing</span><span class="default">Default: none</span><span>Responsive</span></div>

The smallest height, as a framework spacing token or custom length. `none` emits `0`. In viewport mode the composed CSS uses the larger of this value and `100svh`.

<h3 class="property-heading"><code>control.sizing.maxHeight</code></h3>
<div class="property-meta"><span class="property-type">Framework spacing</span><span class="default">Default: none</span><span>Responsive</span></div>

The largest height, as a framework spacing token or custom length. `none` emits `none` — CSS's own "no constraint" for this property.

## Return value

<h3 class="property-heading"><code>control.sizing.css</code></h3>
<div class="property-meta"><span class="property-type">CSS declarations</span></div>

The width, height, aspect ratio and size limits as CSS declarations. A group narrowed with `excludeControls` composes only the declarations it still generates; a group containing only minimum/maximum controls also exposes this value.

The mapping it applies, and why:

| Width mode | Composes |
|---|---|
| Auto | `width: auto` |
| Fill parent | `width: -webkit-fill-available; width: -moz-available; width: stretch` |
| Fit content | `width: fit-content` |
| Viewport | `width: 100svw; max-width: none` |
| Framework container | the `stretch` family, then `max-width: min(100%, var(--foundry-container-width))` |
| Custom | the `stretch` family, then `max-width: min(100%, <customWidth>px)` |

Fill parent accounts for margins. Custom and Framework container also shrink when the parent has less room.

`max-width: 100%` leads the width block as a parent-width limit. For Custom and Framework container, an additional Max width is combined with the mode's cap using `min(100%, <mode cap>, <maximum>)`, so it can only tighten the requested size. Viewport width escapes the parent limit unless Max width is set. These rules constrain the part's box; oversized descendants and an explicit Min width can still cause overflow.

| Height mode | Composes |
|---|---|
| Fit content | `flex-grow: 0; height: auto` |
| Fill remaining space | `flex-grow: 1; height: auto` |
| At least viewport height | `flex-grow: 0; height: auto; min-height: max(100svh, <minHeight>)` |
| Custom | `flex-grow: 0; height: <customHeight>px` |

At least viewport height uses a minimum rather than a fixed height, allowing the section to grow with content. A larger Min height remains effective. As with ordinary CSS sizing, a minimum wins when it conflicts with a maximum.

| Aspect ratio | Composes |
|---|---|
| None, or any height mode other than Fit content | `aspect-ratio: auto` |
| A preset | `aspect-ratio: 16 / 9` and so on |
| Custom | `aspect-ratio: <aspectRatioWidth> / <aspectRatioHeight>` |

The ratio follows the height block. Writing `auto` when it does not apply means a ratio chosen at a wider breakpoint cannot leak into a narrower one that uses a fixed height.

Breakpoint and omission rules:

- Max height set to None writes `max-height: none`, clearing an earlier maximum.
- Max width set to None keeps the selected width mode’s cap. If `widthMode` is omitted, it writes `max-width: none` instead.
- Omitted controls contribute no values. Height mode still controls `min-height` so switching away from Viewport clears that earlier minimum.
- With `minHeight` omitted, Viewport uses `max(100svh, 0px)`; other height modes use `min-height: 0`.


<h3 class="property-heading">Individual values</h3>

Use these when the part needs a different mapping — a wrapper that fills while an inner element is capped, say.

- `control.sizing.widthMode`, `control.sizing.heightMode`: Strings — the semantic choice, not CSS.
- `control.sizing.customWidth`, `control.sizing.customHeight`: Numbers, in pixels with no unit attached.
- `control.sizing.aspectRatio`: a String — `none`, `custom` or a CSS ratio such as `16 / 9`. `control.sizing.aspectRatioWidth` and `control.sizing.aspectRatioHeight`: the two Numbers of a custom ratio.
- `control.sizing.minWidth`, `control.sizing.maxWidth`, `control.sizing.minHeight`, `control.sizing.maxHeight`: a resolved CSS length.

The four constraints are single framework spacing values, with the same qualified fields as the standalone [Framework spacing control](framework-spacing-control.html):

- `css`: the same CSS length as the unqualified value.
- `value`: the numeric amount.
- `unit`: the corresponding unit String.

```text
{{ control.sizing.minWidth }}        → var(--foundry-space-lg)
{{ control.sizing.minWidth.value }}  → 2
{{ control.sizing.minWidth.unit }}   → rem
{{ control.sizing.maxWidth }}        → none
```

Each constraint's `none` resolves to whatever CSS means "no constraint" for that property: `0` for the two minimums, `none` for the two maximums. That is why they can be interpolated unguarded, and why `minWidth` and `maxWidth` do not return the same thing when both are untouched. In both cases `value` is `0` and `unit` is an empty String, so `none` and a genuine zero are indistinguishable through the numeric fields — read the CSS field if you need to tell them apart.

Framework choices resolve to CSS variable references; custom lengths resolve to a literal with its unit. Use `value` with `unit` for calculations, not to rebuild a length.

{% endraw %}
