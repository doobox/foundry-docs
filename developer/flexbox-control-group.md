---
layout: default
title: Flexbox control group · Foundry Developer
permalink: /developer/flexbox-control-group.html
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector · control groups</p>
<h1>Flexbox</h1>
<p class="lede">Arrange an element’s immediate children in a row or column.</p>

## Quick example

Add this entry to your manifest’s `inspector` array:

```json
{
    "section": "Flexbox",
    "controls": [
        {
            "type": "flexbox",
            "id": "flexbox"
        }
    ]
}
```

Add this to your instance-scoped CSS file:

```css
:instance { {{ control.flexbox.css }} }
:instance > * { {{ control.flexbox.childCSS }} }
```

The default is a vertical column. Direction, wrapping, gaps and alignment are responsive. The first rule makes the element a flex container. The second lets its children shrink instead of forcing it wider when they contain long text or wide content. Foundry does not insert either rule automatically.

The `id` is required. This page uses `flexbox`, so every template path starts with `control.flexbox.`. Choose a different ID when you need another instance of the same group.

## Apply Flexbox to an inner container

Using the same declaration above, place both outputs on the corresponding inner elements:

```html
<section class="{{ part.class }}" {{ part.attributes }}>
    <div class="content">
        <p>First item</p>
        <p>Second item</p>
    </div>
</section>
```

```css
:instance > .content { {{ control.flexbox.css }} }
:instance > .content > * { {{ control.flexbox.childCSS }} }
```

## Properties

Each JSON example below is an alternative entry for your manifest’s `inspector` array, or for a section’s `controls` array. Start with the quick example and add the keys you need to that same group object; do not paste every example as another group with the same ID.

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Always `flexbox`. The group does not accept `label`, `group`, `responsive`, `backgroundTypes`, or `supportsHover`.


Choose this built-in group:

```json
{
    "type": "flexbox",
    "id": "flexbox"
}
```

<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

A unique name for this group in the part. Start with a letter; use letters, numbers, underscores or hyphens. Do not reuse another group or control’s ID. There is no default.

For `"id": "flexbox"`, read values as `control.flexbox.<controlID>`, and use `control.flexbox.css` for the complete CSS block. Keep this ID stable: it identifies the group’s saved values.


For example, name this group `panelStyle`:

```json
{
    "type": "flexbox",
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

Changes initial values using local control IDs, without the group prefix. Each value replaces the complete base default and must use the type and allowed values documented below. Unknown or omitted IDs are errors. For example, use `direction`, not `flexbox.direction`, as the configuration key. The generated defaults are column-first and start-aligned: intrinsic-width children like buttons keep their natural size instead of stretching. Parts whose children should fill the container regardless declare their own `width: 100%`, as Foundry's text parts do.



For example, change the starting settings:

```json
{
    "type": "flexbox",
    "id": "flexbox",
    "defaults": {
        "direction": "row",
        "wrap": "wrap"
    }
}
```

These are initial values, not locked settings. The author can still change the controls in the Inspector.

<h3 class="property-heading"><code>excludeControls</code></h3>
<div class="property-meta"><span class="property-type">Array of strings</span><span class="optional">Optional</span><span class="default">Default: exclude nothing</span></div>

Removes controls this part does not need. Use unique local IDs, without the group prefix. Dependent controls are removed too: omitting a mode also removes fields that only configure that mode. Omitted controls have no template value. You cannot explicitly omit every control; remove the group instead.


Remove the wrapped-line alignment control while retaining direction, gaps and item alignment.

```json
{
    "type": "flexbox",
    "id": "flexbox",
    "excludeControls": [
        "alignContent"
    ]
}
```

The remaining controls still work with the same group output. Use the local IDs shown above—not full paths such as `control.flexbox.alignContent`.

<h3 class="property-heading"><code>allowedOptions</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: all options</span></div>

Limits a select control to a non-empty list of its option values, in display order. Keys are local control IDs. Unknown or duplicate options, omitted controls, and controls without options are errors. The original default is kept if allowed; otherwise the first option becomes the default. A value in `defaults` must also be allowed. See the [configuration example](control-groups.html#configure-a-group).


Offer Row and Column without the reverse directions.

```json
{
    "type": "flexbox",
    "id": "flexbox",
    "allowedOptions": {
        "direction": [
            "row",
            "column"
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
    "section": "Optional flexbox settings",
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
            "type": "flexbox",
            "id": "flexbox",
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

These paths use the example ID `flexbox`. Change that prefix if you choose another ID.

<h3 class="property-heading"><code>control.flexbox.direction</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: column</span><span>Responsive</span></div>

One of `column`, `row`, `column-reverse`, or `row-reverse` — the direction of flow. Justify Content distributes along it; Align Items and Align Content work across it. The default is `column`, matching how page sections most often stack; use `defaults` for row-first parts.

<h3 class="property-heading"><code>control.flexbox.wrap</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: nowrap</span><span>Responsive</span></div>

One of `nowrap`, `wrap`, or `wrap-reverse`. Wrapping creates the multiple lines that `alignContent` spaces.

<h3 class="property-heading"><code>control.flexbox.columnGap</code></h3>
<div class="property-meta"><span class="property-type">Framework spacing</span><span class="default">Default: md</span><span>Responsive</span></div>

The horizontal gap between items, as a framework spacing token or custom length. Shown only while it can apply: in a row direction, or whenever wrapping is on.

<h3 class="property-heading"><code>control.flexbox.rowGap</code></h3>
<div class="property-meta"><span class="property-type">Framework spacing</span><span class="default">Default: md</span><span>Responsive</span></div>

The vertical gap between items and wrapped lines, as a framework spacing token or custom length. Shown only while it can apply: in a column direction, or whenever wrapping is on.

<h3 class="property-heading"><code>control.flexbox.alignItems</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: flex-start</span><span>Responsive</span></div>

One of `flex-start`, `center`, `flex-end`, `stretch`, or `baseline` — how each item sits across the direction of flow. `stretch` gives items matching cross-axis sizes, such as equal-height cards in a row.

<h3 class="property-heading"><code>control.flexbox.alignContent</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: flex-start</span><span>Responsive</span></div>

One of `flex-start`, `center`, `flex-end`, `stretch`, `space-between`, `space-around`, or `space-evenly` — how wrapped lines share the cross-axis space. Shown only while Wrap Items is on, because single-line layouts are unaffected.

<h3 class="property-heading"><code>control.flexbox.justifyContent</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: flex-start</span><span>Responsive</span></div>

One of `flex-start`, `center`, `flex-end`, `space-between`, `space-around`, or `space-evenly` — how the items are distributed along the direction of flow.

## Return value

<h3 class="property-heading"><code>control.flexbox.css</code></h3>
<div class="property-meta"><span class="property-type">CSS declarations</span></div>

Every declaration a flex container needs, in one value: `display: flex` followed by `flex-direction`, `flex-wrap`, `column-gap`, `row-gap`, `align-items`, `align-content` and `justify-content`. Drop it into a rule body.

<h3 class="property-heading"><code>control.flexbox.childCSS</code></h3>
<div class="property-meta"><span class="property-type">CSS declarations</span></div>

Returns `min-width: 0;`. Apply it to the immediate children of the element receiving `control.flexbox.css`. It does not choose a selector or insert a rule for you.

This structural output is always available. If your part needs different child sizing, write its own CSS instead.

<h3 class="property-heading">Individual values</h3>

- `control.flexbox.direction`, `control.flexbox.wrap`, `control.flexbox.alignItems`, `control.flexbox.alignContent`, `control.flexbox.justifyContent`: Strings, each already a CSS keyword.
- `control.flexbox.columnGap`, `control.flexbox.rowGap`: a resolved CSS length.

The two gaps are single framework spacing values with the fields of the [Framework spacing control](framework-spacing-control.html):

```text
{{ control.flexbox.columnGap }}       → var(--foundry-space-md)
{{ control.flexbox.columnGap.css }}   → var(--foundry-space-md)
{{ control.flexbox.columnGap.value }} → 1
{{ control.flexbox.columnGap.unit }}  → rem
```

Framework choices resolve to CSS variable references so framework edits keep reaching the part; custom lengths resolve to a literal with its unit. Use `value` with `unit` for calculations, not to rebuild a length. A gap of None resolves to CSS `0`.

Every value here is safe to interpolate unguarded — none of them has an "emit nothing" sentinel, unlike the Layout group.

{% endraw %}
