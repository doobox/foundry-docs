---
layout: default
title: Borders control group · Foundry Developer
permalink: /developer/borders-control-group.html
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector · control groups</p>
<h1>Borders</h1>
<p class="lede">Add border width, style, colour and rounded corners.</p>

## Quick example

Add this entry to your manifest’s `inspector` array:

```json
{
    "section": "Borders",
    "controls": [
        {
            "type": "borders",
            "id": "borders"
        }
    ]
}
```

Add this to your instance-scoped CSS file:

```css
:instance { {{ control.borders.css }} }
```

The group starts disabled. The author enables Borders in the Inspector; the composed CSS handles the off state for you.

The `id` is required. This page uses `borders`, so every template path starts with `control.borders.`. Choose a different ID when you need another instance of the same group.

## Properties

Each JSON example below is an alternative entry for your manifest’s `inspector` array, or for a section’s `controls` array. Start with the quick example and add the keys you need to that same group object; do not paste every example as another group with the same ID.

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Always `borders`. The group does not accept `label`, `group`, `responsive`, `backgroundTypes`, or `supportsHover`.


Choose this built-in group:

```json
{
    "type": "borders",
    "id": "borders"
}
```

<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

A unique name for this group in the part. Start with a letter; use letters, numbers, underscores or hyphens. Do not reuse another group or control’s ID. There is no default.

For `"id": "borders"`, read values as `control.borders.<controlID>`, and use `control.borders.css` for the complete CSS block. Keep this ID stable: it identifies the group’s saved values.


For example, name this group `panelStyle`:

```json
{
    "type": "borders",
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

Replaces complete base defaults using `borderEnabled`, `frameworkBorder`, `frameworkBorderColour`, or `frameworkRadius`.


For example, change the starting settings:

```json
{
    "type": "borders",
    "id": "borders",
    "defaults": {
        "borderEnabled": true,
        "frameworkBorder": {
            "style": "solid",
            "width": {
                "value": 1,
                "unit": "px"
            }
        }
    }
}
```

These are initial values, not locked settings. The author can still change the controls in the Inspector.

<h3 class="property-heading"><code>excludeControls</code></h3>
<div class="property-meta"><span class="property-type">Array of strings</span><span class="optional">Optional</span><span class="default">Default: exclude nothing</span></div>

Removes controls this part does not need. Use unique local IDs, without the group prefix. Dependent controls are removed too: omitting a mode also removes fields that only configure that mode. Omitted controls have no template value. You cannot explicitly omit every control; remove the group instead.


Keep the border controls, but leave corner radius to the part stylesheet.

```json
{
    "type": "borders",
    "id": "borders",
    "excludeControls": [
        "frameworkRadius"
    ]
}
```

The remaining controls still work with the same group output. Use the local IDs shown above—not full paths such as `control.borders.frameworkRadius`.

<h3 class="property-heading"><code>allowedOptions</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: all options</span></div>

Limits a select control to a non-empty list of its option values, in display order. Keys are local control IDs. Unknown or duplicate options, omitted controls, and controls without options are errors. The original default is kept if allowed; otherwise the first option becomes the default. A value in `defaults` must also be allowed. See the [configuration example](control-groups.html#configure-a-group).


**Not applicable to this group’s current controls.** None has a select option list that this key can narrow. Leave `allowedOptions` out. To remove a capability, use the `excludeControls` example above; to change an initial value, use `defaults`.

<h3 class="property-heading"><code>visibleWhen</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: always visible</span></div>

Shows these Inspector controls only when the [visibility condition](visible-when.html) matches. It does not disable their output. Reference an exact part-level ID: for example, `arrangement` for a standalone control or `contentSize.widthMode` for a grouped control. The condition is combined with each generated control’s own visibility rules.


This example includes the toggle that the condition reads. Add the whole section to `inspector`:

```json
{
    "section": "Optional borders settings",
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
            "type": "borders",
            "id": "borders",
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

These paths use the example ID `borders`. Change that prefix if you choose another ID.

<h3 class="property-heading"><code>control.borders.borderEnabled</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="default">Default: false</span><span>Responsive</span></div>

Shows or hides the other controls. Templates must check it explicitly.

<h3 class="property-heading"><code>control.borders.frameworkBorder</code></h3>
<div class="property-meta"><span class="property-type">Framework border</span><span class="default">Default: none, solid</span><span>Responsive</span></div>

Four border widths plus a visible style picker. Read `width`, individual edges, numeric and unit fields, and `style` as documented by [Framework border](framework-border-control.html).

<h3 class="property-heading"><code>control.borders.frameworkBorderColour</code></h3>
<div class="property-meta"><span class="property-type">Framework colour</span><span class="default">Default: muted palette</span><span>Responsive</span></div>

A framework or custom colour with opacity. Its structured fields match the [Framework colour control](framework-colour-control.html).

<h3 class="property-heading"><code>control.borders.frameworkRadius</code></h3>
<div class="property-meta"><span class="property-type">Framework radius</span><span class="default">Default: none</span><span>Responsive</span></div>

Four framework-aware corner radii with the same output as the [Framework radius control](framework-radius-control.html).

## Return value

<h3 class="property-heading"><code>control.borders.css</code></h3>
<div class="property-meta"><span class="property-type">CSS declarations</span></div>

`border-width`, `border-style`, `border-color` and `border-radius`, in one value. While `borderEnabled` is false the width and radius are `0` while style and colour stay as chosen — a zero width is what stops the border drawing. A group narrowed with `excludeControls` composes only the declarations it still generates.

<h3 class="property-heading">Individual values</h3>

- `control.borders.borderEnabled`: Boolean.
- `control.borders.frameworkBorder.width`: the four CSS widths in shorthand order — top, right, bottom, left.
- `control.borders.frameworkBorder.style`: a CSS `border-style` keyword.
- `control.borders.frameworkBorderColour`: a CSS colour.
- `control.borders.frameworkRadius`: the four CSS radii in shorthand order — top-left, top-right, bottom-right, bottom-left.

The border has **no** unqualified shorthand — `control.borders.frameworkBorder` on its own is not a CSS value, because width and style are separate properties. Reach for `width` and `style`, which carry the fields documented by [Framework border](framework-border-control.html):

- `width.top`, `width.right`, `width.bottom`, `width.left`: individual CSS widths.
- `width.css`: the same width shorthand.
- `width.values.<edge>`, `width.units.<edge>`: numeric amount and unit.

The radius is a four-corner object with the fields documented by [Framework radius](framework-radius-control.html), keyed `topLeft`, `topRight`, `bottomLeft`, `bottomRight` rather than by edge:

```text
{{ control.borders.frameworkRadius }}                    → var(--foundry-border-radius-md) …
{{ control.borders.frameworkRadius.topLeft }}            → var(--foundry-border-radius-md)
{{ control.borders.frameworkRadius.values.topLeft }}     → 6
{{ control.borders.frameworkRadius.units.topLeft }}      → px
{{ control.borders.frameworkBorder.width.top }}          → var(--foundry-border-width-sm)
{{ control.borders.frameworkBorder.style }}              → solid
```

Note the shorthand orders differ, because CSS differs: widths run top, right, bottom, left; radii run top-left, top-right, bottom-right, bottom-left. Framework widths resolve in `px` and framework radii in `px`, both as CSS variable references; custom values keep their entered unit.

The colour follows the [Framework colour control](framework-colour-control.html) exactly: a ready-to-use CSS colour rather than a palette ID, including `light-dark(…)` on sites that support both appearances, plus `.contrastColor` and the appearance-qualified and format-fragment fields documented there.

{% endraw %}
