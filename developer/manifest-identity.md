---
layout: default
title: Identity and metadata · Foundry Developer
permalink: "/developer/manifest-identity.html"
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · part manifest</p>
<h1>Identity and metadata</h1>
<p class="lede">These keys declare the API contract and stable identity of a part, then describe how it appears to site authors in Foundry.</p>


## Required identity

Every part manifest must declare these four keys.

<h3 class="property-heading"><code>minimumAPIVersion</code></h3>
<div class="property-meta"><span class="property-type">Integer</span><span class="required">Required</span></div>

The oldest Foundry part API the part requires. Use `1` for the current API. A part continues working when Foundry adds newer APIs; it is rejected only when it requires a version newer than the installed Foundry supports, or when its minimum version is no longer supported.

```json
"minimumAPIVersion" : 1
```

<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

A globally unique, stable reverse-domain identifier. Foundry uses it for saved part instances, template deduplication, and package identity. Changing it creates a different part. Templates can read it as `{{ package.id }}`.

```json
"id" : "uk.co.example.callout"
```

<h3 class="property-heading"><code>title</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

The short part name shown on its tile in the Parts panel and in the part Inspector header.

```json
"title" : "Callout"
```

<h3 class="property-heading"><code>version</code></h3>
<div class="property-meta"><span class="property-type">Semantic-version String</span><span class="required">Required</span></div>

The part release in `MAJOR.MINOR.PATCH` form. Pre-release and build suffixes are supported. This is separate from `minimumAPIVersion`.

```json
"version" : "1.2.0"
```

## Presentation metadata

These optional keys help site authors identify, find, and evaluate the part in the Parts panel.

<h3 class="property-heading"><code>description</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: empty</span></div>

A concise explanation of what the part does. Foundry displays it beside the part icon when an author selects the part.

```json
"description" : "Highlights a short piece of important content."
```

<h3 class="property-heading"><code>author</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: Unknown Developer</span></div>

The developer, company, or publisher responsible for the part. Foundry displays it in the library Inspector and when inspecting an instance.

```json
"author" : "Example Parts"
```

<h3 class="property-heading"><code>group</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: Other</span></div>

The Parts-panel heading beneath which the part appears. Use `Layout`, `Content`, `Media`, `Navigation`, `Forms`, `Interactive`, or `Other`. Matching is case-insensitive; an omitted or unrecognised value uses Other.

```json
"group" : "Content"
```

<h3 class="property-heading"><code>tags</code></h3>
<div class="property-meta"><span class="property-type">String array</span><span class="optional">Optional</span><span class="default">Default: []</span></div>

Up to five brief terms that help authors recognise and find the part. Foundry displays them in a dedicated Tags section.

```json
"tags" : [
    "notice",
    "message"
]
```

<h3 class="property-heading"><code>showsInPartLibrary</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: true</span></div>

Whether the part appears in the Parts or Dev Parts panel. Set this to `false` for a supporting part that users should add only through a parent part's Child picker. The part remains installed and available to matching `pickerItems` declarations.

```json
"showsInPartLibrary" : false
```

<h3 class="property-heading"><code>allowedParents</code></h3>
<div class="property-meta"><span class="property-type">String array</span><span class="optional">Optional</span><span class="default">Default: any location</span></div>

Restricts this part to children of the listed part package identifiers. Foundry applies the restriction to Inspector additions, drops, pastes, moves and initial children. Omit it when the part may also appear at page level or beneath other parts.

```json
"allowedParents" : [
    "com.example.card-grid"
]
```

<h3 class="property-heading"><code>helpURL</code></h3>
<div class="property-meta"><span class="property-type">URL String</span><span class="optional">Optional</span><span class="default">Default: omitted</span></div>

An absolute URL for the part's documentation or support page. Use a stable HTTPS address that explains the part version users currently have installed. Foundry shows it as the Help link in the Inspector's Part Info, and snapshots it into documents so the canvas's missing-part placeholder can point authors there even on a machine that has never seen the pack. Published output includes no markup from a missing part itself — its children render in their place.

```json
"helpURL" : "https://example.com/parts/callout/help"
```

<h3 class="property-heading"><code>icon</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: generic mark, gray</span></div>

The part's artwork: one square single-colour glyph plus a system tint. Foundry renders the glyph as a stencil — only its shape and opacity matter — painted white on a tint-filled tile in the Parts panel, and painted in the tint directly in the Structure tree. The system tints adapt to light and dark appearance automatically, so no dark variants exist.

```json
"icon" : {
    "file" : "icon.svg",
    "tint" : "blue"
}
```

<h3 class="property-heading"><code>icon.file</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span></div>

A square SVG in `Resources/`, at most 64 KiB. Draw the glyph to the edges of the viewBox — the viewBox is the glyph's bounding box, and Foundry supplies all whitespace, fitting the glyph into the same padded area it uses for SF Symbols so both kinds render at one size.

Foundry uses only the glyph's shape and repaints it, so the colour you draw in makes no difference: any solid fill works, including none at all. What does change the result is anything that makes parts of the shape partly transparent — opacity, colours with an alpha channel — which come out faint, and gradients, embedded images, patterns or filters, which flatten into a plain silhouette. Validation warns when it finds any of these.

<h3 class="property-heading"><code>icon.symbol</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span></div>

An SF Symbol name, for parts without drawn artwork. When both `file` and `symbol` are declared the file is used and the symbol is its fallback. A symbol name the running system does not recognise falls back to the generic part mark.

```json
"icon" : {
    "symbol" : "photo",
    "tint" : "green"
}
```

<h3 class="property-heading"><code>icon.tint</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: gray</span></div>

One of `red`, `orange`, `yellow`, `green`, `mint`, `teal`, `cyan`, `blue`, `indigo`, `purple`, `pink`, `brown`, or `gray`, mapping to the macOS system colours. An unrecognised token renders as gray and reports a validation error.

<div class="guidance" markdown="1">
<h3>How Foundry presents the part</h3>

The Parts panel shows each part as an icon and title beneath its `group` heading. Selecting it reveals the icon, title, description, developer, version, category, identifier, documentation link, and tags in the Inspector.

Parts loaded from a development pack receive a small red dot beside their title. Foundry supplies this marker; part authors do not declare it in `manifest.json`.
</div>

## Complete example

```json
"minimumAPIVersion" : 1,
"id" : "uk.co.example.callout",
"title" : "Callout",
"version" : "1.2.0",
"description" : "Highlights a short piece of important content.",
"author" : "Example Parts",
"group" : "Content",
"icon" : {
    "file" : "icon.svg",
    "tint" : "blue"
},
"showsInPartLibrary" : false,
"tags" : [
    "notice",
    "message"
]
```

## Updates

<h3 class="property-heading"><code>updates</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span>Default: absent</span></div>

Update configuration belongs to the outer pack's root `manifest.json`, not an individual part manifest. The updater replaces the complete pack as one unit. Without this dictionary, the pack does not declare an update feed. Foundry's [release publishing workflow](pack-updates.html) writes it when preparing a development pack.

```json
"updates" : {
    "appcastURL" : "https://example.com/updates/com.example.layout/appcast.php",
    "publicKey" : "BASE64_PUBLIC_KEY_FROM_FOUNDRY"
}
```

<h3 class="property-heading"><code>updates.appcastURL</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required when updates is present</span><span>No default</span></div>

An HTTPS URL returning the pack's JSON appcast. The built-in publisher uses an `appcast.php` endpoint. Keep the URL reachable for installed copies.

<h3 class="property-heading"><code>updates.publicKey</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required when updates is present</span><span>No default</span></div>

The publisher's Base64-encoded raw Ed25519 public key. Use the value generated by Foundry, not the placeholder above. Installed copies use it to verify downloaded releases. Never place the private signing key in this field, and retain the same public key across updates.

<h2 id="validation-failures">Validation failures</h2>
<p>Foundry refuses to load a part whose manifest or declared files violate the API contract. The Developer panel reports every diagnostic Foundry produced for that pack, including the relevant key or file when available.</p>
<p>Manifest keys are strict. Unknown or misspelled keys are validation errors rather than ignored extensions, so correct the declaration named by the diagnostic before reloading the pack.</p>
<div class="note">
<strong>Do not rely on undocumented fallbacks.</strong> Foundry validates the current manifest shape and does not translate legacy aliases. Correct the reported declaration in the pack and reload it.</div>

{% endraw %}
