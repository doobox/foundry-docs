---
layout: default
title: Advanced control group · Foundry Developer
permalink: /developer/advanced-control-group.html
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector · control groups</p>
<h1>Advanced</h1>
<p class="lede">Opts the part into the Advanced Inspector section: an HTML ID, CSS classes, custom CSS, and custom attributes for the part, set per placed instance by the site author.</p>

## Quick example

```json
{
    "type" : "advanced"
}
```

Advanced has no `id` because it generates no control values. Put it directly in `inspector`, not inside another section.

Use these macros on your root element:

```html
<section class="{{ part.class }}" {{ part.attributes }}>
    <p>Your content goes here.</p>
</section>
```

Advanced owns its section: it always renders as Foundry’s Advanced section with its fixed gear icon, and must be declared at the top level of the `inspector`, never inside a section entry.

Parts do not show these fields by default. Declare the group when your part is a sensible anchor target or benefits from author-supplied classes and attributes — structural and landmark parts usually do; small decorative parts usually do not.

## What the section provides

Unlike other control groups, Advanced generates no `control.…` template values. Its fields bind to the placed instance and render through the root-element macros every template already uses:

- **ID** — an anchor for in-page links. Validated for uniqueness across the page and emitted as the root element's `id` through `{{ part.attributes }}`.
- **Classes** — space-separated class names appended to the root element's classes through `{{ part.class }}`.
- **CSS** — the author's own CSS for this instance. Foundry nests it inside the instance's selector, so it cannot reach anything outside the part: bare declarations style the part itself, selectors starting with a pseudo-class or pseudo-element attach to the part — `:hover { … }` styles the part when hovered — nested rules such as `h2 { … }` style its descendants, and `:instance` also stands for the part in selectors. The author's CSS takes precedence over the part's own rules, including its breakpoint rules. It needs no template macro: Foundry adds it to the instance's styles automatically.
- **Attributes** — author-defined name/value pairs (for example `data-…` or ARIA attributes), emitted through `{{ part.attributes }}`. The section carries its own **Add Attribute…** button beneath the attribute list.

Keep `{{ part.class }}` and `{{ part.attributes }}` on your template's root element — without them the author's values have nowhere to render. See [Template root attributes](template-root-attributes.html).

## Properties

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Always `advanced`. The group has no options: it does not accept `id`, `label`, `backgroundTypes`, `supportsHover`, `defaults`, `excludeControls`, or `allowedOptions`, and it declares no generated controls.

## Return value

None. Advanced is the only group with no `control.…` values at all — its ID, classes and attributes reach the page through `{{ part.class }}` and `{{ part.attributes }}`, which every part template already carries, and Foundry adds the custom CSS to the instance's styles itself. No additional control output is needed.
{% endraw %}
