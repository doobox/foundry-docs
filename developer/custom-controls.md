---
layout: default
title: Custom controls · Foundry Developer
permalink: "/developer/custom-controls.html"
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector</p>
<h1>Custom controls</h1>
<p class="lede">Each dictionary in <code>inspector</code> creates part of the part Inspector. Declare what the author can change, then read the resulting value from HTML, CSS, JavaScript, or PHP.</p>

<div class="note">
<strong>See every control live.</strong> With <em>Enable Developer Tools</em> on in Settings, the Developer panel has two sections, <strong>Debugger</strong> and <strong>Controls</strong>. Controls lists every control and control group; click one and Foundry shows it on a scratch <em>Controls</em> page — the real Inspector controls on the right, a sheet on the canvas that reacts as you change them, and <strong>Snippets</strong> at the top of the Inspector with a Copy button for the declaration, its template usage and any CSS. The scratch page lives only in memory: it is never listed with your pages, saved, exported or undone. Switching to Debugger, hiding the panel or choosing a real page discards it, unloads the showcase parts and returns you to the page you were on.
</div>
<h2>Declare one control</h2>
<p>Every dictionary in <code>inspector</code> with a <code>type</code> is one complete control declaration. Value-producing controls have a stable <code>id</code>, an author-facing <code>label</code> value, a <code>type</code>, a matching <code>defaults.base</code>, and explicit responsive behaviour. Controls declared at the top level of the <code>inspector</code> appear in the <code>Settings</code> Inspector section; wrap controls in a section entry to place them elsewhere.</p>

<div markdown="1">

```json
"inspector" : [
    {
        "id" : "heading",
        "label" : "Heading",
        "type" : "text",
        "defaults" : {
            "base" : "Welcome"
        },
        "responsive" : false
    }
]
```

</div>

<p>Read the saved value with <code>{{ control.heading }}</code>. Each control-type page below lists the exact required keys, accepted options, stored value, and a working declaration.</p>
<h2>Initial values and breakpoints</h2>

Declare initial values in one <code>defaults</code> dictionary, even when only a base value is needed. <code>base</code> is required inside it. Each breakpoint entry is a complete value of the same type as <code>base</code>, including complete arrays and structured values.

```json
"type" : "frameworkSpacing",
"id" : "gap",
"responsive" : true,
"defaults" : {
    "base" : "sm",
    "medium" : "md",
    "large" : "xl"
}
```

Accepted breakpoint names are `small`, `medium`, `large`, `extraLarge`, and `doubleExtraLarge`. Non-base entries require a responsive value control and `responsive: true`. Missing entries inherit from the preceding enabled breakpoint, starting at `base`. Thresholds come from the project's framework, not fixed pixel values in the part.

Disabled project breakpoints are skipped; their defaults and saved overrides remain available if re-enabled. At each enabled breakpoint, a user override wins over the developer default. A later explicit developer default starts a new value in the cascade, so a user override at Medium does not replace a developer's Large default. Resetting a breakpoint removes its user override and reveals the cascade again.

Use responsive values in CSS templates to generate breakpoint rules. HTML and JavaScript do not automatically change their contents when the browser resizes.

Slider requires an explicit numeric `defaults.base` within its range, just like Number. Image may omit `defaults` to start empty; its asset default is base-only. Note, Divider, Math and ChildPicker do not accept `defaults`; ChildPicker uses `initial` for its children.

[SVG](svg-control.html) also starts empty when `defaults` is omitted. Unlike Image's URL value, SVG supplies sanitised inline markup for placement directly inside the template's HTML.

<h2>Sections</h2>

An entry in `inspector` without a `type` declares an Inspector section. It names the section once with `section`, optionally names its disclosure-header icon with `systemImage`, and lists the section's controls in its own `controls` array. Controls left at the top level of the part's `inspector` array belong to `Settings`:

```json
"inspector" : [
    {
        "type" : "text",
        "id" : "heading",
        "label" : "Heading",
        "defaults" : {
            "base" : "Welcome"
        }
    },
    {
        "section" : "Gallery",
        "systemImage" : "photo.stack",
        "controls" : [
            {
                "type" : "number",
                "id" : "columns",
                "label" : "Columns",
                "defaults" : {
                    "base" : 3
                }
            },
            {
                "type" : "toggle",
                "id" : "captions",
                "label" : "Captions",
                "defaults" : {
                    "base" : true
                }
            }
        ]
    }
]
```

Heading appears in Settings; Columns and Captions appear together in a Gallery section. `systemImage` is an SF Symbol name and is optional; a section without one uses a generic fallback icon. [Grouped controls](control-groups.html) belong in sections too: declared inside a section entry their generated controls join it, alongside any of the part’s own controls. Only the [`advanced`](advanced-control-group.html) group must stay at the top level.

A section entry may omit `controls` to set only an icon. The implicit `Content` section — where editable template content lives — accepts an icon this way:

```json
{
    "section" : "Content",
    "systemImage" : "doc.text"
}
```

Each section name may be declared only once, and sections cannot nest: a section entry inside another section entry is a validation error, as is a duplicate name.

<h2>Control types</h2>
<div class="card-grid">
<a class="card" href="text-control.html"><strong>text</strong><p>Single-line text.</p></a><a class="card" href="text-area-control.html"><strong>textArea</strong><p>Multi-line text.</p></a><a class="card" href="link-control.html"><strong>link</strong><p>A structured internal or external link.</p></a><a class="card" href="image-control.html"><strong>image</strong><p>A project image picker with canvas drag-and-drop, alt text, focal point and renditions.</p></a><a class="card" href="video-control.html"><strong>video</strong><p>A project video picker with Finder and Resources drag-and-drop.</p></a><a class="card" href="number-control.html"><strong>number</strong><p>Numeric input with bounds and units.</p></a><a class="card" href="framework-border-control.html"><strong>frameworkBorder</strong><p>Border widths with an optional style picker.</p></a><a class="card" href="framework-spacing-control.html"><strong>frameworkSpacing</strong><p>A single framework-aware spacing value.</p></a><a class="card" href="framework-radius-control.html"><strong>frameworkRadius</strong><p>Framework-aware radii for four corners.</p></a><a class="card" href="framework-padding-control.html"><strong>frameworkPadding</strong><p>Framework-aware space inside four edges.</p></a><a class="card" href="framework-margin-control.html"><strong>frameworkMargin</strong><p>Framework-aware space outside four edges.</p></a><a class="card" href="slider-control.html"><strong>slider</strong><p>Numeric slider with optional ticks.</p></a><a class="card" href="date-control.html"><strong>date</strong><p>An ISO-8601 date.</p></a><a class="card" href="colour.html"><strong>color</strong><p>A literal hexadecimal colour picker.</p></a><a class="card" href="framework-colour-control.html"><strong>frameworkColor</strong><p>A framework colour with an optional custom choice.</p></a><a class="card" href="icon-control.html"><strong>icon</strong><p>A searchable picker for Foundry’s built-in icon library.</p></a><a class="card" href="select-control.html"><strong>select</strong><p>A single choice from declared or framework values, with optional custom overrides.</p></a><a class="card" href="framework-shadow-control.html"><strong>frameworkShadow</strong><p>A framework shadow picker with optional editable custom layers.</p></a><a class="card" href="toggle-control.html"><strong>toggle</strong><p>A Boolean switch.</p></a><a class="card" href="button-control.html"><strong>button</strong><p>A persistent action button.</p></a><a class="card" href="math-control.html"><strong>math</strong><p>A derived numeric value.</p></a><a class="card" href="text-alignment.html"><strong>textAlignment</strong><p>Logical CSS alignment.</p></a><a class="card" href="note-control.html"><strong>note</strong><p>Presentation-only help text.</p></a><a class="card" href="divider-control.html"><strong>divider</strong><p>Presentation-only separator.</p></a><a class="card" href="spacer-control.html"><strong>spacer</strong><p>Presentation-only vertical space.</p></a><a class="card" href="child-picker-control.html"><strong>childPicker</strong><p>Add and manage accepted child parts.</p></a>
</div>
<div class="page-links">
<a class="card" href="framework-font-control.html"><strong>frameworkFont</strong><p>A configurable font family, weight and style control.</p></a>
</div>
<h2>Shared capabilities</h2>
<div class="page-links">
<a class="card" href="control-arrays.html"><strong>Control arrays</strong><p>Place two to four controls in one inspector row, with optional subtitles.</p></a><a class="card" href="visible-when.html"><strong>Conditional visibility</strong><p>Use <code>visibleWhen</code> to show a control only when another control’s value satisfies a condition.</p></a><a class="card" href="template-controls.html"><strong>Template values</strong><p>Use property values and instance helpers in rendered files.</p></a><a class="card" href="framework-controls.html"><strong>Framework values</strong><p>Allow supported controls to follow the active project framework.</p></a>
</div>
{% endraw %}
