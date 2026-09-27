---
layout: default
title: Layout control group · Foundry Developer
permalink: /developer/layout-control-group.html
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector · control groups</p>
<h1>Layout</h1>
<p class="lede">Control positioning, visibility, overflow and stacking.</p>

## Quick example

Add this entry to your manifest’s `inspector` array:

```json
{
    "section": "Layout",
    "controls": [
        {
            "type": "layout",
            "id": "layout"
        }
    ]
}
```

Add this to your instance-scoped CSS file:

```css
:instance { {{ control.layout.css }} }
```

Most controls start at None, so an untouched group adds no declarations. Put Layout after other groups when its Hidden control should override their display setting.

The `id` is required. This page uses `layout`, so every template path starts with `control.layout.`. Choose a different ID when you need another instance of the same group.

## Properties

Each JSON example below is an alternative entry for your manifest’s `inspector` array, or for a section’s `controls` array. Start with the quick example and add the keys you need to that same group object; do not paste every example as another group with the same ID.

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Always `layout`. The group does not accept `label`, `group`, `responsive`, `backgroundTypes`, or `supportsHover`.


Choose this built-in group:

```json
{
    "type": "layout",
    "id": "layout"
}
```

<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

A unique name for this group in the part. Start with a letter; use letters, numbers, underscores or hyphens. Do not reuse another group or control’s ID. There is no default.

For `"id": "layout"`, read values as `control.layout.<controlID>`, and use `control.layout.css` for the complete CSS block. Keep this ID stable: it identifies the group’s saved values.


For example, name this group `panelStyle`:

```json
{
    "type": "layout",
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

Changes initial values using local control IDs, without the group prefix. Each value replaces the complete base default and must use the type and allowed values documented below. Unknown or omitted IDs are errors. For example, use `position`, not `layout.position`, as the configuration key.



For example, change the starting settings:

```json
{
    "type": "layout",
    "id": "layout",
    "defaults": {
        "position": "relative",
        "overflow": "visible"
    }
}
```

These are initial values, not locked settings. The author can still change the controls in the Inspector.

<h3 class="property-heading"><code>excludeControls</code></h3>
<div class="property-meta"><span class="property-type">Array of strings</span><span class="optional">Optional</span><span class="default">Default: exclude nothing</span></div>

Removes controls this part does not need. Use unique local IDs, without the group prefix. Dependent controls are removed too: omitting a mode also removes fields that only configure that mode. Omitted controls have no template value. You cannot explicitly omit every control; remove the group instead.


Remove the z-index mode and its dependent custom zIndex control.

```json
{
    "type": "layout",
    "id": "layout",
    "excludeControls": [
        "zIndexMode"
    ]
}
```

The remaining controls still work with the same group output. Use the local IDs shown above—not full paths such as `control.layout.zIndexMode`.

<h3 class="property-heading"><code>allowedOptions</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: all options</span></div>

Limits a select control to a non-empty list of its option values, in display order. Keys are local control IDs. Unknown or duplicate options, omitted controls, and controls without options are errors. The original default is kept if allowed; otherwise the first option becomes the default. A value in `defaults` must also be allowed. See the [configuration example](control-groups.html#configure-a-group).


Keep the element positioned. This is useful when the part contains an absolutely positioned child.

```json
{
    "type": "layout",
    "id": "layout",
    "allowedOptions": {
        "position": [
            "relative",
            "absolute",
            "fixed",
            "sticky"
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
    "section": "Optional layout settings",
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
            "type": "layout",
            "id": "layout",
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

These paths use the example ID `layout`. Change that prefix if you choose another ID.

<h3 class="property-heading"><code>control.layout.position</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: none</span><span>Responsive</span></div>

One of `none`, `static`, `relative`, `absolute`, `fixed`, or `sticky`. `none` means the template should emit no <code>position</code>; `static` is the explicit CSS value — normal flow, offsets and z-index inert — useful for overriding positioning set elsewhere.

`static` is the one value that stops the part being the containing block for its absolutely positioned descendants. If your markup contains one — a stretched link overlay, an authored background video, a corner badge — an author who picks `static` sends it off to the nearest positioned ancestor instead, and the part breaks with no way to diagnose it from the Inspector.

Narrow the control to the values your markup survives, and write `position` unconditionally:

```json
{
    "type" : "layout", "id": "layout",
    "allowedOptions" : {
        "position" : ["relative", "absolute", "fixed", "sticky"]
    }
}
```

```css
:instance { position: {{ control.layout.position }}; }
```

Dropping `none` as well makes the menu honest: a part that needs a containing block has no unpositioned state, so the first listed value — `relative` here — [becomes the default](control-groups.html) and the part's stylesheet no longer needs a `position: relative` of its own. Leave both in place for a part with nothing positioned inside it.

<h3 class="property-heading"><code>control.layout.zIndexMode</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: none</span><span>Responsive</span></div>

One of `none`, `auto`, or `custom`, shown as a segmented control. `none` means the template should emit no <code>z-index</code>; `custom` reveals the numeric value below.

<h3 class="property-heading"><code>control.layout.zIndex</code></h3>
<div class="property-meta"><span class="property-type">Number</span><span class="default">Default: 0</span><span>Responsive</span></div>

The custom stacking value, −9999 through 9999. Shown only while <code>zIndexMode</code> is <code>custom</code>, and unavailable to templates otherwise (<code>valueAvailability: whenVisible</code>).

<h3 class="property-heading"><code>control.layout.offsets</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: none</span><span>Responsive</span></div>

One of `none`, `uniform`, or `individual`, shown as a segmented control — how the top/right/bottom/left offsets are edited. `uniform` reveals one shared length; `individual` reveals the four-edge control.

<h3 class="property-heading"><code>control.layout.offset</code></h3>
<div class="property-meta"><span class="property-type">Framework spacing</span><span class="default">Default: none</span><span>Responsive</span></div>

The shared offset applied to every edge, as a framework spacing token or custom length — the CSS <code>inset</code> shorthand with one value. Shown only while <code>offsets</code> is <code>uniform</code>, and unavailable to templates otherwise (<code>valueAvailability: whenVisible</code>).

<h3 class="property-heading"><code>control.layout.offsetEdges</code></h3>
<div class="property-meta"><span class="property-type">Edges</span><span class="default">Default: 0px each edge</span><span>Responsive</span></div>

Independent top/right/bottom/left offsets as raw lengths in `px`, `%`, `rem`, or `em`. Shown only while <code>offsets</code> is <code>individual</code>, and unavailable to templates otherwise (<code>valueAvailability: whenVisible</code>). The direct value renders the four-value <code>inset</code> shorthand; qualified values such as <code>control.layout.offsetEdges.top</code> remain available.

<h3 class="property-heading"><code>control.layout.hidden</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="default">Default: false</span><span>Responsive</span></div>

A switch for removing the part from the flow at a breakpoint — templates typically emit <code>display: none</code> while it is on.

<h3 class="property-heading"><code>control.layout.visibility</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: default</span><span>Responsive</span></div>

One of `default`, `visible`, or `hidden`. `default` means the template should emit no <code>visibility</code> — CSS visibility has no `auto` keyword, so the sentinel is named honestly. Unlike <code>hidden</code> above, CSS visibility keeps the part's space in the flow.

<h3 class="property-heading"><code>control.layout.overflow</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: none</span><span>Responsive</span></div>

One of `none`, `visible`, `hidden`, `scroll`, or `auto`. `none` means the template should emit no <code>overflow</code>.

Isolation is a part-developer decision, not an Inspector setting. If the part needs a local stacking boundary, set `isolation: isolate;` in its stylesheet. Layout does not change it.

## Return value

<h3 class="property-heading"><code>control.layout.css</code></h3>
<div class="property-meta"><span class="property-type">CSS declarations</span></div>

`position`, `z-index`, `inset`, `display`, `visibility` and `overflow`, in one value — each omitted when its control sits on the sentinel. An untouched group composes an empty String. `display: none` comes last, so the value overrides a `display` set earlier in the same rule. A group narrowed with `excludeControls` composes only the declarations it still generates.

<h3 class="property-heading">Individual values</h3>

- `control.layout.position`, `control.layout.zIndexMode`, `control.layout.offsets`, `control.layout.visibility`, `control.layout.overflow`: Strings, each with a sentinel (`none` or `default`) meaning "emit nothing".
- `control.layout.zIndex`: Number.
- `control.layout.hidden`: Boolean.
- `control.layout.offset`: a resolved CSS length — the single-value `inset` shorthand.
- `control.layout.offsetEdges`: the four raw lengths in shorthand order — top, right, bottom, left.

`offset` is a single framework spacing value with the fields of the [Framework spacing control](framework-spacing-control.html) — `css`, `value`, `unit`. `offsetEdges` is a four-edge object with the fields of the [Edges control](edges-control.html):

```text
{{ control.layout.offset }}                   → var(--foundry-space-md)
{{ control.layout.offset.value }}             → 1
{{ control.layout.offsetEdges }}              → 0.0px 12.0px 0.0px 12.0px
{{ control.layout.offsetEdges.top }}          → 0.0px
{{ control.layout.offsetEdges.values.right }} → 12
{{ control.layout.offsetEdges.units.right }}  → px
```

`offsetEdges` never returns CSS variable references — it has no framework picker, so every length is the entered amount with its unit.

Both offset values declare `valueAvailability: whenVisible`, so **exactly one of them exists at a time** and the other, along with all its qualified fields, is absent rather than empty. That is what lets the quick example interpolate both on one line without a conditional: whichever mode is inactive contributes nothing.

{% endraw %}
