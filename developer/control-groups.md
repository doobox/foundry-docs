---
layout: default
title: Control groups · Foundry Developer
permalink: "/developer/control-groups.html"
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector</p>
<h1>Control groups</h1>
<p class="lede">Add ready-made Inspector controls, then choose where their styles apply in your part.</p>

## Start with one group

Add this entry to your manifest's `inspector` array:

```json
{
    "section": "Sizing",
    "controls": [
        { "type": "sizing", "id": "size" }
    ]
}
```

In your instance-scoped CSS file, apply the group's output:

```css
:instance {
    {{ control.size.css }}
}
```

`type` chooses the controls. `id` names this instance. The example uses `size`, so its output is `control.size.css` and its individual values include `control.size.widthMode`.

Every group requires an ID except **Advanced**, which exposes native HTML identity fields instead of control values. Missing IDs are errors; there is no unnamed form.

The section only organises the Inspector. It does not choose which HTML element receives the styles. Your CSS does that.

## Use the same group twice

A section can have separate sizing controls for its outer element and its inner content container:

```json
{
    "section": "Section and content",
    "controls": [
        {
            "type": "sizing",
            "id": "sectionSize",
            "excludeControls": ["widthMode", "minWidth", "maxWidth"]
        },
        {
            "type": "sizing",
            "id": "contentSize",
            "allowedOptions": {
                "widthMode": ["full", "breakpoint", "custom"]
            }
        }
    ]
}
```

```css
:instance {
    width: 100%;
    {{ control.sectionSize.css }}
}

:instance > .content {
    {{ control.contentSize.css }}
}
```

The CSS above expects an inner element with the class `content`:

```html
<section class="{{ part.class }}" {{ part.attributes }}>
    <div class="content">
        {{ dropZone("content") }}
    </div>
</section>
```

The outer width stays fixed by the part. The first group supplies height controls; the second supplies the content container's sizing controls. Their saved values are independent.

## Configure a group

Use local control IDs inside configuration dictionaries. Use the group prefix only when reading a value in a template or referencing it from another control.

```json
{
    "type": "sizing",
    "id": "contentSize",
    "defaults": {
        "widthMode": "custom",
        "customWidth": 800
    },
    "allowedOptions": {
        "widthMode": ["full", "custom"]
    }
}
```

Here the configuration key is `customWidth`, while the template value is `control.contentSize.customWidth`.

Group `defaults` maps control IDs directly to their starting values. Unlike a standalone control’s `defaults`, it has no `base` wrapper. Authors still use the blue dots to change values at different screen sizes.

Choose configuration by the job you need:

- **Starting values:** `defaults`.
- **Remove a setting:** `excludeControls`.
- **Limit a setting’s choices:** `allowedOptions`.
- **Show settings conditionally:** `visibleWhen`.
- **Background choices:** `backgroundTypes` and `supportsHover`.
- **Animate an inner element:** Reveal’s `targetSelector`.

You can leave all of these out. Most groups need only `type` and `id`.

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

One of `background`, `spacing`, `sizing`, `borders`, `effects`, `flexbox`, `layout`, `reveal`, or `advanced`. Each group's page lists its controls and output.

<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required except Advanced</span></div>

A unique name within this part. Start with a letter; use only letters, numbers, underscores or hyphens. Do not reuse another group or control's ID. There is no default. Advanced does not accept an ID.

All values use `control.<id>.<controlID>`. CSS-producing groups also provide `control.<id>.css`. Keep IDs stable: changing one changes the saved control identifiers.

<h3 class="property-heading"><code>defaults</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: group defaults</span></div>

Changes initial values. Each key is a local generated control ID; each value replaces that control's complete base default. Use the value format documented on the group's page. Unknown keys are errors. Available on every group except Advanced.

<h3 class="property-heading"><code>excludeControls</code></h3>
<div class="property-meta"><span class="property-type">Array of strings</span><span class="optional">Optional</span><span class="default">Default: exclude nothing</span></div>

Removes controls the part does not support. Use unique local IDs. Dependent controls go too: omitting `widthMode` also removes `customWidth`. An omitted control has no template value. You cannot explicitly omit every control; remove the group instead. Available on every group except Advanced.

<h3 class="property-heading"><code>allowedOptions</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: all options</span></div>

Limits a select control to supported choices. Each key is a local control ID; each value is a non-empty array of that control's option values, in display order. Duplicate or unknown options are errors. You cannot narrow an omitted control or a control without options.

If the original default remains, it is kept. Otherwise the first option becomes the default. Any `defaults` value must also be in the allowed list. Controls made permanently invisible by option filtering remain present; use `excludeControls` to remove them. Available on every group except Advanced.

<h3 class="property-heading"><code>visibleWhen</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: always visible</span></div>

Shows the group's Inspector controls only when the condition matches. Uses the [visibility condition](visible-when.html) syntax. It affects Inspector visibility, not whether the group's CSS is applied. Available on every group except Advanced.

For example, if your part has a select control called `arrangement`:

```json
{
    "type": "flexbox",
    "id": "contentFlow",
    "visibleWhen": { "id": "arrangement", "value": "flex" }
}
```

Conditions built into a group automatically reference that group's own controls. Your group-level condition uses the exact part-level ID, such as `arrangement` or `contentSize.widthMode`.

## Responsive changes

Generated controls marked Responsive use the same blue-dot breakpoint overrides as custom controls. There is no separate group-level override mechanism.

- Without an override at a wider breakpoint, the earlier value continues to apply.
- Set a value at that breakpoint to override it.
- Remove the override using the blue dot to inherit the earlier value again.

To cancel a constraint at a wider breakpoint, choose the appropriate value in that control. For example, set Height to Custom at 200px on mobile, then choose Fit content on desktop. To remove an earlier maximum height, choose None for Max height. These changes affect that setting, not the whole group.

Each group's reference documents which controls are responsive and what its None or automatic values mean. Keep using the group's composed CSS output; the ordinary responsive system supplies its values.

## Choose a group

- [Sizing](sizing-control-group.html): width, height and limits.
- [Spacing](spacing-control-group.html): padding and margin.
- [Flexbox](flexbox-control-group.html): arrange immediate children.
- [Background](background-control-group.html): colour, image, gradient and video.
- [Borders](borders-control-group.html): border appearance and corner radius.
- [Effects](effects-control-group.html): shadow and opacity.
- [Layout](layout-control-group.html): positioning, visibility, overflow and stacking.
- [Reveal](reveal-control-group.html): automatic entrance animation.
- [Advanced](advanced-control-group.html): native HTML ID, classes and attributes.

CSS groups supply declarations; place their `.css` value inside a CSS rule. If several groups share an element, put Layout last so its Hidden setting can override another group's `display` declaration.

Reveal is different from the CSS groups: it runs an animation. Its optional `targetSelector` chooses one inner element; omitting it selects the part root. See the [Reveal target example](reveal-control-group.html#animate-an-inner-element).

Hand-written controls do not become groups because their IDs resemble generated controls. Declare the group explicitly to use its composed output.
{% endraw %}
