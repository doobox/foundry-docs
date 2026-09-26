---
layout: default
title: Pack structure · Foundry Developer
permalink: "/developer/bundle-structure.html"
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">Packages</p>
<h1>Pack structure</h1>
<p class="lede">A Foundry pack is one outer package containing typed directories for parts, templates and frameworks. Items inside those directories are ordinary folders, not nested packages.</p>

<div markdown="1">

```text
Example.foundrypack/
├── manifest.json
├── Parts/
│   └── uk.co.example.callout/
│       ├── manifest.json
│       └── Resources/
│           ├── part.html
│           ├── part.css
│           └── icon.svg          (optional mono glyph — manifest icon.file)
├── Templates/
│   ├── Heroes/               (organization folder)
│   │   └── 7B6E…/
│   │       ├── manifest.json
│   │       └── Resources/
│   └── 3F91…/
│       ├── manifest.json
│       └── Resources/
├── Frameworks/
│   └── Brand/
│       ├── manifest.json
│       └── Resources/
├── Assets/
│   └── stock-photos/
│       ├── manifest.json        (optional — licence and title)
│       ├── hero.jpg
│       └── badges/
│           └── badge.svg
└── Sites/
    └── Restaurant Starter/
        ├── site.foundry
        ├── preview.jpg       (optional — chooser card artwork)
        └── manifest.json        (optional — title and description)
```

</div>

<h2>Outer manifest.json</h2>
<p>The root manifest identifies and versions the complete pack. Its only required key is <code>id</code>; the rest is pack metadata used for installation and updates. A part's inspector and templates do not belong in this manifest.</p>

<div markdown="1">

```json
"id" : "uk.co.example.components",
"title" : "Example Components",
"version" : "1.0.0",
"minimumAPIVersion" : 1
```

</div>

<h2>Typed directories</h2>
<dl>
<dt>Parts</dt>
<dd>Each direct child is one part. Its <code>manifest.json</code> declares the part API, and paths declared by that manifest are relative to its sibling <code>Resources</code> directory.</dd>
<dt>Templates</dt>
<dd>Reusable page-content templates saved by Foundry. Each template owns its manifest, serialized part tree, preview and embedded assets. Templates organize into plain subdirectories: a child folder without a <code>manifest.json</code> is an organization folder, shown as a folder in the Templates panel — arrange a pack's templates in Finder and Foundry presents that structure as-is, folders first, alphabetically.</dd>
<dt>Frameworks</dt>
<dd>Reusable design frameworks, including framework metadata, <code>framework.json</code>, preview artwork and bundled font assets.</dd>
<dt>Assets</dt>
<dd>Curated collections of importable files — photos, SVG icons, textures, fonts, video. Each direct child folder is one collection: put files straight inside it, organized into nested folders however you like, and Foundry presents that structure as-is. No manifest is required — the folder's name is its title. Add an optional <code>manifest.json</code> at the collection's root to declare a display <code>title</code>, a stable <code>id</code>, and <code>license</code>, <code>licenseURL</code> and <code>attribution</code>, which Foundry shows before anything imports. Importing always copies files into the project's own asset library — published sites never reference a pack.</dd>
<dt>Sites</dt>
<dd>Starter project kits. Each child folder holds one <code>.foundry</code> document plus optional card artwork — <code>preview.png</code>, <code>preview.jpg</code>, or <code>preview.webp</code> — and an optional <code>manifest.json</code> declaring a display <code>title</code> and one-line <code>description</code>. Kits appear in Foundry's Create a New Project chooser; choosing one stamps a fresh project with its own identity and factory publishing settings — the kit is never opened in place.</dd>
<dt>Resources</dt>
<dd>Optional resources shared by the pack as a whole. Item-specific files remain in the item's own <code>Resources</code> directory.</dd>
</dl>
<p>The parent directory determines an item's type. Item folder names are storage names and do not replace the stable identifier in the item's manifest. For the full story on shipping asset collections and template packs, see <a href="assets-and-templates.html">Assets &amp; templates</a>.</p>
<div class="callout warning"><strong>Only the outer directory uses a Foundry pack extension.</strong> Do not add <code>.foundrypack</code>, <code>.foundrydevpack</code>, <code>.foundryframework</code>, or a macOS <code>Contents</code> directory to an item.</div>

<h2>Development packs</h2>
<p>Use <code>.foundrydevpack</code> while developing and <code>.foundrypack</code> for distribution. Their internal structure is identical. Foundry loads an opened development pack in place and watches its complete typed-directory tree for the current session.</p>
<p>You can also place packs in <code>~/Library/Application Support/Foundry/Packs</code>. Installed release packs are treated as read-only; saved personal templates and frameworks are written to <code>My Library.foundrydevpack</code>.</p>
<div class="note"><strong>Pack boundary.</strong> Foundry does not recursively search inside an outer pack for more packs. Unknown visible top-level directories fail validation; hidden files such as <code>.git</code> are ignored, so a development pack can live inside a source checkout. While a development pack is open, an incomplete item folder — for example a part still missing its <code>manifest.json</code> or <code>Resources</code> — is skipped so the rest of the pack keeps loading, but installing or releasing a <code>.foundrypack</code> that contains one is rejected. Asset collections are exempt: any plain folder under <code>Assets</code> is complete.</div>

<h2>Declared part resources</h2>
<p>HTML, CSS, JavaScript and PHP template files are named under <a href="templates.html"><code>templates</code></a>. Other part files referenced with <code>{{ asset("…") }}</code> must be listed under <a href="manifest-resources.html"><code>assets</code></a>. Every path is relative to that part's <code>Resources</code> directory.</p>

<div class="page-links">
<a class="card" href="nested-packs.html"><strong>Pack contents</strong><p>Combine multiple content types in one distributable pack.</p></a>
<a class="card" href="manifest-identity.html"><strong>Part identity and metadata</strong><p>Declare an individual part beneath <code>Parts</code>.</p></a>
</div>
{% endraw %}
