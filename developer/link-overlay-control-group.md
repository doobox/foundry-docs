---
layout: default
title: Link control group · Foundry Developer
permalink: /developer/link-overlay-control-group.html
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector · control groups</p>
<h1>Link</h1>
<p class="lede">Give a whole part one destination and an accessible name.</p>

## Quick example

Add the group inside a named Inspector section:

```json
{
    "section": "Link",
    "systemImage": "link",
    "controls": [
        {
            "type": "linkOverlay",
            "id": "link"
        }
    ]
}
```

Use your normal part template. When a destination is selected, Foundry changes the root's opening and closing tags to `a`, adds the link attributes and supplies a keyboard focus outline. Clearing the destination restores the original root. No extra template expressions, CSS or JavaScript are required.

Supported block roots are `div`, `section`, `article`, `header`, `footer`, `nav`, `aside`, `main`, `figure`, `figcaption`, `p`, `h1`–`h6`, `address`, `blockquote` and `pre`. Supported inline roots are `span`, `em`, `strong`, `small`, `b`, `i`, `u`, `s`, `mark`, `code`, `kbd`, `samp`, `var`, `sub`, `sup`, `abbr`, `cite`, `q` and `time`. Other roots, including `img`, media elements, form controls and tables, produce a package-validation error. Declare only one Link group per root.

Position is untouched: static, relative, absolute, fixed and sticky all work. Foundry preserves block display with a low-specificity fallback; your explicit display rules, including flex and grid, take precedence. Classes, IDs, inline styles and children remain in place. Link-owned attributes such as `href`, `target` and `aria-label` take their values from the Link group.

Converting the root replaces its original semantics with link semantics. Style the part through `:instance` or classes, rather than selectors that depend on its original tag. Explicitly declare typography, spacing and other styling you need; browser defaults belonging to the original element do not carry over. For an image, use a supported container root around the actual `img`, which remains unchanged.

The `id` is required. This page uses `link`, so its template paths begin with `control.link.`. The Inspector section may be called anything; **Link** is the clearest user-facing name.

<div class="guidance" markdown="1">
<h3>Interactive content</h3>

A whole-part link is appropriate for passive content. Nested links, buttons, form controls and focusable or editable descendants prevent conversion. Foundry leaves that root unchanged and adds a `data-foundry-link-error` diagnostic and, when the root has no existing title, an explanatory tooltip. This check also applies to content supplied by child parts. Remove the conflicting interactive content to activate the root link.

Root hover rules such as `:instance:hover { transform: scale(1.02); }` continue to work. Use `:focus-visible` when the same visual treatment should appear for keyboard focus. Canvas clicks continue to select the part rather than navigate.
</div>

## Properties

Each JSON example below is an alternative entry for a section’s `controls` array. Start with the quick example and add the keys you need to that same group object.

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Always `linkOverlay`. The identifier is retained for compatibility; the implementation now converts the root and adds no overlay. This distinguishes the reusable group from the standalone [`link`](link-control.html) control. The group does not accept `label`, `group`, `responsive`, `backgroundTypes`, `supportsHover`, or `targetSelector`.

```json
{
    "type": "linkOverlay",
    "id": "link"
}
```

<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

A unique name for this group in the part. Start with a letter; use letters, numbers, underscores or hyphens. Do not reuse another group or control’s ID. There is no default.

For `"id": "link"`, read the generated values as `control.link.destination` and `control.link.accessibleName`. Keep this ID stable because it identifies the group’s saved values.

<h3 class="property-heading"><code>defaults</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: empty values</span></div>

Changes initial values using the local IDs `destination` and `accessibleName`, without the group prefix. Both accept strings. An empty destination means no link; a non-empty destination initializes a URL.

```json
{
    "type": "linkOverlay",
    "id": "link",
    "defaults": {
        "destination": "https://example.com",
        "accessibleName": "Visit the example site"
    }
}
```

These are initial values. Authors can replace or clear them in the Inspector.

<h3 class="property-heading"><code>excludeControls</code></h3>
<div class="property-meta"><span class="property-type">Array of strings</span><span class="optional">Optional</span><span class="default">Default: exclude nothing</span></div>

Removes generated controls by local ID. You may omit `accessibleName` when the generated link can use the image’s `source.alt` value as a dependable alternative. Do not omit `destination`; its dependent accessible-name control would also be removed, leaving the group empty.

```json
{
    "type": "linkOverlay",
    "id": "link",
    "excludeControls": ["accessibleName"]
}
```

<h3 class="property-heading"><code>visibleWhen</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: always visible</span></div>

Shows the group’s Inspector controls only when the [visibility condition](visible-when.html) matches. It does not remove a saved link or suppress template output.

```json
{
    "section": "Link",
    "controls": [
        {
            "type": "toggle",
            "id": "linkable",
            "label": "Show link settings",
            "defaults": { "base": true }
        },
        {
            "type": "linkOverlay",
            "id": "link",
            "visibleWhen": { "id": "linkable", "value": true }
        }
    ]
}
```

`allowedOptions` has no useful configuration for this group because neither generated control is a select.

## Generated controls

The entries below are generated values, not additional declarations to paste into `inspector`. These paths use the example ID `link`; change that prefix if you choose another ID.

Link values are not responsive.

<h3 class="property-heading"><code>control.link.destination</code></h3>
<div class="property-meta"><span class="property-type">Structured link</span><span class="default">Default: empty</span></div>

The whole-part destination. The base expression returns the resolved and escaped `href`. Its companion values are:

- `control.link.destination.target`: `_blank` when the author chooses a new window, otherwise empty.
- `control.link.destination.attributes`: validated custom attributes, with `rel="noopener noreferrer"` added for a new window unless the author supplies `rel`.

The Inspector labels this control **Destination**.

<h3 class="property-heading"><code>control.link.accessibleName</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="default">Default: empty</span></div>

Text that identifies the destination to assistive technology. The Inspector shows it only after a destination is selected. Foundry uses this value as the generated anchor’s `aria-label`. Supply a descriptive name. If empty, Foundry uses `source.alt` when available, then the resolved destination as a last fallback.

## Return value

The converted root consumes the values automatically. Templates can also read `control.link.destination`, its `.target` and `.attributes` companions, and `control.link.accessibleName`. There is no `.css` value to interpolate.

The destination follows the standalone [Link control](link-control.html) contract. Avoid creating another anchor from these values: the group makes the root itself the link.
{% endraw %}
