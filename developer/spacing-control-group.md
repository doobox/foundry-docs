---
layout: default
title: Spacing control group · Foundry Developer
permalink: /developer/spacing-control-group.html
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector · control groups</p>
<h1>Spacing</h1>
<p class="lede">Add padding inside an element and margin outside it.</p>

## Quick example

Add this entry to your manifest’s `inspector` array:

```json
{
    "section": "Spacing",
    "controls": [
        {
            "type": "spacing",
            "id": "spacing"
        }
    ]
}
```

Add this to your instance-scoped CSS file:

```css
:instance { {{ control.spacing.css }} }
```

The framework size scale is available for both controls, with custom values when needed. Switching spacing off outputs zero padding and margin.

The `id` is required. This page uses `spacing`, so every template path starts with `control.spacing.`. Choose a different ID when you need another instance of the same group.

## Properties

Each JSON example below is an alternative entry for your manifest’s `inspector` array, or for a section’s `controls` array. Start with the quick example and add the keys you need to that same group object; do not paste every example as another group with the same ID.

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Always `spacing`. The group does not accept `label`, `group`, `responsive`, `backgroundTypes`, or `supportsHover`.


Choose this built-in group:

```json
{
    "type": "spacing",
    "id": "spacing"
}
```

<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

A unique name for this group in the part. Start with a letter; use letters, numbers, underscores or hyphens. Do not reuse another group or control’s ID. There is no default.

For `"id": "spacing"`, read values as `control.spacing.<controlID>`, and use `control.spacing.css` for the complete CSS block. Keep this ID stable: it identifies the group’s saved values.


For example, name this group `panelStyle`:

```json
{
    "type": "spacing",
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

Replaces the complete base default of a generated control. Accepted keys are `spacingEnabled`, `frameworkPadding`, and `frameworkMargin`; values must use the corresponding return-value format below.


For example, change the starting settings:

```json
{
    "type": "spacing",
    "id": "spacing",
    "defaults": {
        "spacingEnabled": true,
        "frameworkPadding": "md"
    }
}
```

These are initial values, not locked settings. The author can still change the controls in the Inspector.

<h3 class="property-heading"><code>excludeControls</code></h3>
<div class="property-meta"><span class="property-type">Array of strings</span><span class="optional">Optional</span><span class="default">Default: exclude nothing</span></div>

Removes controls this part does not need. Use unique local IDs, without the group prefix. Dependent controls are removed too: omitting a mode also removes fields that only configure that mode. Omitted controls have no template value. You cannot explicitly omit every control; remove the group instead.


Keep padding controls and remove margin controls.

```json
{
    "type": "spacing",
    "id": "spacing",
    "excludeControls": [
        "frameworkMargin"
    ]
}
```

The remaining controls still work with the same group output. Use the local IDs shown above—not full paths such as `control.spacing.frameworkMargin`.

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
    "section": "Optional spacing settings",
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
            "type": "spacing",
            "id": "spacing",
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

These paths use the example ID `spacing`. Change that prefix if you choose another ID.

<h3 class="property-heading"><code>control.spacing.spacingEnabled</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="default">Default: true</span><span>Responsive</span></div>

Shows or hides the remaining controls in the Inspector. Templates must check it explicitly; disabling spacing does not change the padding or margin values.

<h3 class="property-heading"><code>control.spacing.frameworkPadding</code></h3>
<div class="property-meta"><span class="property-type">Framework padding</span><span class="default">Default: none</span><span>Responsive</span></div>

Four-edge framework-aware padding. It has the same structured output as the [Framework padding control](framework-padding-control.html), including edge, numeric and unit fields.

<h3 class="property-heading"><code>control.spacing.frameworkMargin</code></h3>
<div class="property-meta"><span class="property-type">Framework margin</span><span class="default">Default: none</span><span>Responsive</span></div>

Four-edge framework-aware margin. It has the same structured output as the [Framework margin control](framework-margin-control.html), including edge, numeric and unit fields.

## Return value

<h3 class="property-heading"><code>control.spacing.css</code></h3>
<div class="property-meta"><span class="property-type">CSS declarations</span></div>

`padding` and `margin`, in one value. While `spacingEnabled` is false both are `0` rather than absent, so the block always resets a narrower breakpoint. A group narrowed with `excludeControls` composes only the declarations it still generates.

<h3 class="property-heading">Individual values</h3>

- `control.spacing.spacingEnabled`: Boolean.
- `control.spacing.frameworkPadding`, `control.spacing.frameworkMargin`: the four CSS lengths in shorthand order — top, right, bottom, left.

Both are four-edge objects carrying the same qualified fields as their standalone controls:

- `top`, `right`, `bottom`, `left`: resolved CSS lengths.
- `css`: the same shorthand as the unqualified value.
- `values`: an object holding the numeric amount for each edge.
- `units`: an object holding the corresponding unit String for each edge.

```text
{{ control.spacing.frameworkPadding }}            → var(--foundry-space-md) var(--foundry-space-md) …
{{ control.spacing.frameworkPadding.top }}        → var(--foundry-space-md)
{{ control.spacing.frameworkPadding.values.top }} → 1
{{ control.spacing.frameworkPadding.units.top }}  → rem
```

Framework choices resolve to CSS variable references so later framework edits keep reaching the part; custom lengths resolve to a literal with its unit. The two are therefore not interchangeable — use `values` with `units` for calculations and JavaScript, never to rebuild a length.

Margin accepts `auto`, which is not a measurement: that edge's CSS field is `auto`, its unit is an empty String, and it has **no** entry in `values`, so interpolating the number renders nothing. Padding cannot reach this state.

{% endraw %}
