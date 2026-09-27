---
layout: default
title: Effects control group · Foundry Developer
permalink: /developer/effects-control-group.html
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector · control groups</p>
<h1>Effects</h1>
<p class="lede">Add a shadow and control opacity.</p>

## Quick example

Add this entry to your manifest’s `inspector` array:

```json
{
    "section": "Effects",
    "controls": [
        {
            "type": "effects",
            "id": "effects"
        }
    ]
}
```

Add this to your instance-scoped CSS file:

```css
:instance { {{ control.effects.css }} }
```

The group starts disabled. Its CSS converts the opacity percentage into the fraction CSS expects, and restores normal opacity when disabled.

The `id` is required. This page uses `effects`, so every template path starts with `control.effects.`. Choose a different ID when you need another instance of the same group.

## Properties

Each JSON example below is an alternative entry for your manifest’s `inspector` array, or for a section’s `controls` array. Start with the quick example and add the keys you need to that same group object; do not paste every example as another group with the same ID.

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Always `effects`. The group does not accept `label`, `group`, `responsive`, `backgroundTypes`, or `supportsHover`.


Choose this built-in group:

```json
{
    "type": "effects",
    "id": "effects"
}
```

<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

A unique name for this group in the part. Start with a letter; use letters, numbers, underscores or hyphens. Do not reuse another group or control’s ID. There is no default.

For `"id": "effects"`, read values as `control.effects.<controlID>`, and use `control.effects.css` for the complete CSS block. Keep this ID stable: it identifies the group’s saved values.


For example, name this group `panelStyle`:

```json
{
    "type": "effects",
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

Replaces complete base defaults using `effectsEnabled`, `frameworkShadow`, or `opacity`.


For example, change the starting settings:

```json
{
    "type": "effects",
    "id": "effects",
    "defaults": {
        "effectsEnabled": true,
        "opacity": 85
    }
}
```

These are initial values, not locked settings. The author can still change the controls in the Inspector.

<h3 class="property-heading"><code>excludeControls</code></h3>
<div class="property-meta"><span class="property-type">Array of strings</span><span class="optional">Optional</span><span class="default">Default: exclude nothing</span></div>

Removes controls this part does not need. Use unique local IDs, without the group prefix. Dependent controls are removed too: omitting a mode also removes fields that only configure that mode. Omitted controls have no template value. You cannot explicitly omit every control; remove the group instead.


Offer opacity without a shadow control.

```json
{
    "type": "effects",
    "id": "effects",
    "excludeControls": [
        "frameworkShadow"
    ]
}
```

The remaining controls still work with the same group output. Use the local IDs shown above—not full paths such as `control.effects.frameworkShadow`.

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
    "section": "Optional effects settings",
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
            "type": "effects",
            "id": "effects",
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

These paths use the example ID `effects`. Change that prefix if you choose another ID.

<h3 class="property-heading"><code>control.effects.effectsEnabled</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="default">Default: false</span><span>Responsive</span></div>

Shows or hides Shadow and Opacity. Templates must check the value explicitly.

<h3 class="property-heading"><code>control.effects.frameworkShadow</code></h3>
<div class="property-meta"><span class="property-type">Framework shadow</span><span class="default">Default: none</span><span>Responsive</span></div>

A framework shadow with the structured output documented by the [Framework shadow control](framework-shadow-control.html).

<h3 class="property-heading"><code>control.effects.opacity</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 100</span><span>Responsive</span></div>

An integer percentage from 0 through 100. The template value is the number, not a CSS fraction or percentage string.

## Return value

<h3 class="property-heading"><code>control.effects.css</code></h3>
<div class="property-meta"><span class="property-type">CSS declarations</span></div>

`box-shadow` and `opacity`, in one value, with the percentage already divided into a CSS fraction — `85` composes as `opacity: 0.85`. While `effectsEnabled` is false it resets to `none` and `1`. A group narrowed with `excludeControls` composes only the declarations it still generates.

<h3 class="property-heading">Individual values</h3>

- `control.effects.effectsEnabled`: Boolean.
- `control.effects.frameworkShadow`: a CSS-ready `box-shadow` String, or `none`.
- `control.effects.opacity`: a Number from 0 through 100 — **not** a CSS value.

The shadow is a flat String with no qualified fields, as documented by the [Framework shadow control](framework-shadow-control.html). A framework choice resolves to a variable reference; a custom shadow resolves to its comma-separated layers; an untouched or missing choice resolves to `none`, so it can be interpolated unguarded.

If you write opacity yourself, divide by 100 and handle the disabled state:

```css
:instance {
    opacity: {{ if control.effects.effectsEnabled }}calc({{ control.effects.opacity }} / 100){{ else }}1{{ endif }};
}
```

{% endraw %}
