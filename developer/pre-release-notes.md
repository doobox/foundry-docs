---
layout: default
title: Pre Release Notes · Foundry Developer
permalink: /developer/pre-release-notes.html
description: Highlights from Foundry preview builds distributed before public release.
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<header class="release-hero">
    <p class="eyebrow">Foundry for macOS</p>
    <h1>Pre-release notes</h1>
    <p class="lede">A concise history of the preview builds shared with Foundry’s early developers. Each build includes everything listed in the builds before it.</p>
    <nav class="release-jump" aria-label="Jump to a preview build">
        <a href="#build-17">Build 17</a>
        <a href="#build-16">Build 16</a>
        <a href="#build-15">Build 15</a>
        <a href="#build-14">Build 14</a>
        <a href="#build-12">Build 12</a>
        <a href="#build-11">Build 11</a>
        <a href="#build-10">Build 10</a>
        <a href="#build-9">Build 9</a>
        <a href="#build-8">Build 8</a>
        <a href="#build-7">Build 7</a>
        <a href="#build-6">Build 6</a>
        <a href="#build-5">Build 5</a>
        <a href="#build-4">Build 4</a>
        <a href="#build-3">Build 3</a>
    </nav>
</header>

<div class="note release-note">
    <strong>Preview software:</strong> projects and part APIs may continue to evolve before Foundry’s public release. Keep a backup of important projects and development packs when moving between builds.
</div>

<div class="release-timeline">
    <article class="release-build" id="build-17">
        <header class="release-build-header">
            <div>
                <span class="release-build-number">Build 17</span>
                <h2>Collections, reusable typography and a Masonry Gallery</h2>
            </div>
            <time datetime="2026-10-07">7 October 2026</time>
        </header>
        <p class="release-summary">Build 17 adds an ordered-record Collection control, a responsive Typography control group and a built-in Masonry Gallery. Collection items use ordinary Foundry controls, remain editable at every breakpoint and can be selected directly from the canvas. Hover triggers can now follow any matching Part ID on the page, while renderer and filter fixes make conditional values and opacity output more precise.</p>

        <div class="callout breaking">
            <h3>Breaking changes for packs and existing projects</h3>
            <ul class="release-list">
                <li><strong>The standalone Bento Grid part is removed.</strong> Existing instances of <code>foundry.layout.bento-grid</code> and pack rules that name it are not migrated automatically during the preview period. Use Grid, Flexbox or the new Masonry Gallery as appropriate.</li>
                <li><strong>The standalone Lightbox part is removed.</strong> Lightboxes are a capability supplied by the <a href="lightbox-control-group.html">Lightbox control group</a>, not a content part. Existing <code>foundry.content.lightbox</code> instances must be replaced with a media or custom-content part that declares the group.</li>
                <li><strong>Effects no longer exposes opacity.</strong> The Effects group now emits only its framework shadow. Remove references to <code>control.effects.opacity</code> and use <code>control.filters.filtersOpacity</code> or <code>control.filters.filtersHoverOpacity</code> from the Filters group.</li>
            </ul>
        </div>

        <div class="release-groups">
            <section class="release-group">
                <h3>Collections and Masonry Gallery</h3>
                <ul class="release-list">
                    <li><strong><a href="collection-control.html">Collection control.</a></strong> A pack can declare <code>type: collection</code> with a repeated <code>controls</code> array and optional <code>itemLabel</code>. Authors can add, duplicate, delete, reorder and select records while each record keeps the values of its text, media, link and other ordinary controls.</li>
                    <li>Nested collection controls support their normal defaults, conditional visibility, value availability and responsive overrides. Collections cannot themselves be responsive or counted, and cannot contain another Collection, Child Picker or Math control.</li>
                    <li>Templates receive collections as ordered arrays of structured records. <code>{{ loop.attributes }}</code> on a repeated item's outer element lets a canvas click select the matching record in the Inspector without adding published markup.</li>
                    <li><strong>Masonry Gallery.</strong> The new built-in part uses a Collection to give every image its own focal point, crop shape, title, description and link. It supports responsive column counts and gaps, framework corner radii, below/overlay/hidden captions and separate typography for titles and descriptions.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Typography and styling</h3>
                <ul class="release-list">
                    <li><strong>Typography control group.</strong> Packs can declare <code>type: typography</code> to compose responsive font family, weight, style, size, line height, optional colour, alignment, decoration and capitalisation into <code>control.&lt;id&gt;.css</code>.</li>
                    <li>Background, Filters and Transforms now label their external hover target as <strong>Part ID</strong>. The target may be any part on the page, rather than only an ancestor, and the generated selector activates while that part is hovered.</li>
                    <li>Filters omit an unnecessary <code>opacity: 1</code> declaration when neither state changes opacity, avoiding an extra WebKit compositing path. Hover mode still emits both opacity states when either differs from 100%.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Rendering, validation and fixes</h3>
                <ul class="release-list">
                    <li>The manifest schema and validator understand Collection fields, reject unsupported nesting and conflicting options, validate record defaults, and preserve stable item identity as records are reordered or duplicated.</li>
                    <li>Collection media and link values resolve through the canvas and static-site renderers, imported assets inside records are counted correctly, and exact dotted keys remain addressable when templates traverse structured values.</li>
                    <li><code>valueAvailability: whenVisible</code> is carried through adapted property definitions, so hidden conditional controls—including fields inside Collections—do not leak values into rendered templates.</li>
                    <li>The Controls showcase includes working Collection and Typography examples, and canvas selection keeps the chosen collection item and its Inspector controls in sync.</li>
                </ul>
            </section>
        </div>
    </article>

    <article class="release-build" id="build-16">
        <header class="release-build-header">
            <div>
                <span class="release-build-number">Build 16</span>
                <h2>SVG, lightboxes, web video and more expressive hover states</h2>
            </div>
            <time datetime="2026-10-05">5 October 2026</time>
        </header>
        <p class="release-summary">Build 16 adds first-class inline SVG artwork, a Lightbox control group, direct and YouTube web video, configurable hover triggers, and clearer Inspector change indicators. It also replaces Container with Section, lets project fonts override framework fonts with the same name, and separates whole-part opacity from Shadow by moving it into the Filters state controls.</p>

        <div class="callout breaking">
            <h3>Breaking changes for packs and existing projects</h3>
            <ul class="release-list">
                <li><strong>Container is replaced by Section.</strong> The built-in identifier changes from <code>foundry.layout.container</code> to <code>foundry.layout.section</code>. Build 15 Container instances and pack rules that name the old identifier are not migrated automatically during the preview period; replace them with Section and update allowed-parent references.</li>
                <li><strong>Whole-part opacity moved from Effects to Filters.</strong> Effects is now named Shadow and no longer supplies <code>control.effects.opacity</code>. Use <code>control.filters.filtersOpacity</code> for the normal state and <code>control.filters.filtersHoverOpacity</code> for the hovered state; previously saved Effects opacity must be set again.</li>
                <li><strong>Built-in hover selectors are now configurable.</strong> Background, Filters and Transforms expose <code>control.&lt;group&gt;.hover.selector</code>. Packs that want Parent Part or Part ID triggering must use that value in their hover rule; a hard-coded <code>:instance:hover</code> continues to mean This Part only.</li>
            </ul>
        </div>

        <div class="release-groups">
            <section class="release-group">
                <h3>New parts and controls</h3>
                <ul class="release-list">
                    <li><strong>SVG.</strong> Import or drop an SVG as a dedicated part or declare an <a href="svg-control.html">SVG control</a>. Foundry sanitises the source and renders safe inline markup, allowing fill and stroke styling without treating the artwork as an image URL. Repeated templates can create SVG areas with <code>{{ svg("name") }}</code>.</li>
                    <li><strong>Image Gallery.</strong> The new built-in Image Gallery uses an <a href="image-control.html">image control</a> with <code>allowsMultiple: true</code>. Its compact image well accepts multiple files or a folder, opens a thumbnail collection editor for reordering and removal, and exposes the ordered images as a template collection for <code>loop</code>. The part adds responsive columns, gap, image ratio and fit controls, plus None, Zoom in, Zoom out, Lift, Dim and Brighten thumbnail-hover presets with matching keyboard-focus treatment.</li>
                    <li><strong>Video Gallery.</strong> The new built-in Video Gallery uses a <a href="video-control.html">video control</a> with <code>allowsMultiple: true</code>. It accepts multiple local movies, a folder, direct-video links and YouTube URLs; provides ordered collection editing with shared playback settings; and opens the collection through GLightbox.</li>
                    <li><strong>Gallery lightboxes.</strong> The Lightbox group supports single media and image collections. Image lightboxes use bundled GLightbox 3 with its clean interface, Zoom opening and closing, Slide, Fade, Zoom or None gallery transitions, touch-follow and keyboard navigation, adjacent-image preloading and configurable looping. Foundry applies the shared Transitions group's duration and easing, backdrop colour and blur, plus a live counter and optional clickable thumbnail strip.</li>
                    <li><strong>GLightbox library.</strong> Parts can request bundled GLightbox 3 with <code>{"id":"glightbox","majorVersion":3}</code>. Foundry publishes its JavaScript and standard stylesheet locally, exposes the normal <code>GLightbox</code> global, and requests it automatically for the Lightbox control group.</li>
                    <li><strong>Lightbox.</strong> The new <a href="lightbox-control-group.html">Lightbox control group</a> lets media parts and third-party custom-content parts provide an accessible overlay, close controls and the required published-page behaviour without hand-written JavaScript. Built-in Image, Image Gallery, SVG and Video offer it; there is no separate built-in Lightbox part.</li>
                    <li><strong>Section.</strong> The full-width Section replaces Container, with constrained inner content and the same role as the page's primary structural wrapper.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Video on the web</h3>
                <ul class="release-list">
                    <li>Video controls can import a copy of a direct HTTP(S) movie up to 100 MB or link to it without adding it to Resources.</li>
                    <li>YouTube watch, share, Shorts, live and embed URLs render through the privacy-enhanced player. <strong>Show poster first</strong> presents a thumbnail and Play button before loading the player, and a custom poster can replace the automatic YouTube thumbnail.</li>
                    <li>The renderer, canvas and template primitive recognise YouTube sources consistently; video imports can be cancelled and report validation or download failures in the web-video popover.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Inspector and styling</h3>
                <ul class="release-list">
                    <li>Background, Filters and Transforms hover modes can be triggered by <strong>This Part</strong>, the nearest <strong>Parent Part</strong>, or any part on the page with a matching <strong>Part ID</strong>. The generated hover selector is available to part templates.</li>
                    <li>Effects is renamed <strong>Shadow</strong>. Whole-part opacity is a numeric value inside Filters, with independent Normal and Hovered values alongside the other filter controls.</li>
                    <li>Section headers are marked only when their effective values differ from their defaults, and each changed control's label is highlighted so the source of a customised section is immediately visible.</li>
                    <li>Adding or importing a part selects it and brings the Structure panel forward, keeping the new item visible in the page hierarchy.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Frameworks, canvas and fixes</h3>
                <ul class="release-list">
                    <li>A custom project font now overrides a framework font with the same name, so templates and controls resolve the user's intentional replacement.</li>
                    <li>Parent hover resolves the nearest logical part ancestor even when canvas wrappers sit between the two parts.</li>
                    <li>Dormant Shadow and Filters modes no longer make their Inspector sections appear changed, and hover-state opacity is stored and rendered with the state it belongs to.</li>
                    <li>Canvas rendering and selection are more reliable for retained parts, media drops and newly inserted content.</li>
                </ul>
            </section>
        </div>
    </article>

    <article class="release-build" id="build-15">
        <header class="release-build-header">
            <div>
                <span class="release-build-number">Build 15</span>
                <h2>Filters, transforms, transitions and a whole-part Link group</h2>
            </div>
            <time datetime="2026-10-01">1 October 2026</time>
        </header>
        <p class="release-summary">Build 15 adds four control groups — Filters, Transforms, Transitions and Link — to every built-in part and to the developer API; gives the Background group a shared overlay and makes video an explicit opt-in; puts an opacity slider on framework colours; reworks Container, Flexbox and Grid so children keep their natural size and sections centre their content without extra controls; adds Reset to every Inspector control and section; reserves the <code>foundry.</code> identifier prefix; and fixes a colour bug that hit every German-region Mac.</p>

        <div class="callout breaking">
            <h3>Breaking changes for packs and existing projects</h3>
            <ul class="release-list">
                <li><strong>The <code>foundry.</code> identifier prefix is reserved.</strong> A pack whose <code>id</code> starts with <code>foundry.</code> is refused at load time with <em>“The 'foundry.' prefix is reserved for Foundry's own parts”</em>, whether or not validation is enabled. Rename the pack with your own reverse-DNS prefix.</li>
                <li><strong>Background video is opt-in.</strong> Omitting <code>backgroundTypes</code> now offers colour, image and gradient only. A part that relied on the default to offer video must list <code>"video"</code> explicitly, insert <code>{{ control.background.video }}</code> as a direct child of a positioned, isolated host, and keep Layout from offering None or Static. <code>control.background.backgroundVideo</code> and <code>backgroundVideoLoop</code> are generated only when video is declared.</li>
                <li><strong>Sizing's Fit content width mode is gone.</strong> <code>allowedOptions.widthMode</code> that lists <code>fit</code> fails validation; a stored <code>fit</code> renders as <code>width: auto</code>. The remaining modes are Auto, Full, Screen, Site width and Custom. Only the titles changed: <code>full</code>, <code>screen</code>, <code>breakpoint</code> and <code>custom</code> are the same values.</li>
                <li><strong>Built-in whole-part links moved to the Link group.</strong> Container, Flexbox, Grid, Flex Item, Grid Item and Image no longer declare their own <code>destination</code> and <code>linkLabel</code> controls; they use <code>control.link.destination</code> and <code>control.link.accessibleName</code>. Previously saved flat-key links must be set again in the Link section; there is no automatic migration during the preview period.</li>
                <li><strong>Layout parts behave differently.</strong> Inside a Container, children keep their natural width — a button stays button-sized — rather than stretching; Flexbox starts empty and stacks vertically; Grid starts empty with start alignment and its column preview on. Pages built on Build 14 will lay out differently until their parts are revisited. Container's Content Spacing section and its Breakpoint width option are replaced by a single <strong>Container</strong> section with a <strong>Site Width</strong> option.</li>
            </ul>
        </div>

        <div class="release-groups">
            <section class="release-group">
                <h3>New control groups</h3>
                <ul class="release-list">
                    <li><strong><a href="filters-control-group.html">Filters</a></strong>: blur, brightness, contrast, saturation, grayscale, sepia, invert and hue rotation, a drop shadow and a backdrop blur, with independent Normal and Hovered states. Output is <code>control.filters.css</code> and <code>control.filters.hover.css</code>.</li>
                    <li><strong><a href="transforms-control-group.html">Transforms</a></strong>: origin, scale, rotation, X and Y translation and X and Y skew, again with Normal and Hovered states, as <code>control.transforms.css</code> and <code>control.transforms.hover.css</code>.</li>
                    <li><strong><a href="transitions-control-group.html">Transitions</a></strong>: an on switch, the property scope, easing, duration and delay for state changes, as <code>control.transitions.css</code>.</li>
                    <li><strong><a href="link-overlay-control-group.html">Link</a></strong> (<code>linkOverlay</code>): a Destination and an Accessible name that turn the part's root element into an anchor when a destination is chosen. Position, classes, children and your display rules are untouched; a keyboard focus outline is supplied; nested links, buttons and form controls prevent conversion and are reported with a <code>data-foundry-link-error</code> diagnostic. No template work is needed.</li>
                    <li>Every built-in part gains Filters, Transforms, Transitions and Link sections in the Inspector.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Control groups</h3>
                <ul class="release-list">
                    <li><strong>Background</strong> gains an <strong>Overlay</strong> switch and <strong>Overlay colour</strong> for image and video backgrounds, black at 20% by default. One overlay serves both the Normal and Hovered states; it never changes on hover. The hover state is now titled Hovered. Background videos pause when they scroll out of view or the tab is hidden, and resume when they return.</li>
                    <li><strong>Framework colour</strong> controls with <code>opacity: true</code> show a 0–100% slider for palette colours as well as custom ones, and <code>defaults.base.opacity</code> sets the starting value. Light and dark opacity can differ.</li>
                    <li><strong>Sizing</strong>'s Width menu reads Auto, Full, Screen, Site width and Custom. Max width and Max height start unconstrained, and switching one to a custom length begins at a useful 1200px or 800px instead of zero.</li>
                    <li><strong>Flexbox</strong> labels are in plain English: Horizontal and Vertical directions, Wrapping, Distribution, Item Alignment and Wrapped Lines.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Built-in parts</h3>
                <ul class="release-list">
                    <li><strong>Container 3.3.0.</strong> A single Container section holds Width (Site Width, Full, Fit Content, Custom), Vertical position and Content Gap; Vertical position appears only once the section has spare height. The content rail is centred and children own their own margins and padding. Container's defaults for its children are low priority, so a child's own Custom width, Site width, Max width or Min height now wins; previously the Container overrode them.</li>
                    <li><strong>Flexbox 2.2.0</strong> starts empty and vertical instead of pre-filling Flex Items. <strong>Grid 1.2.0</strong> starts empty with start alignment and its preview columns on. <strong>Flex Item</strong> and <strong>Grid Item 1.1.0</strong> rename Equal Width to Equal Space, Align to Item Alignment and Gap to Content Gap.</li>
                    <li><strong>Image</strong> gains a <strong>Width</strong> of its own — Fill, Original or Custom — that drives both the CSS width and the <code>sizes</code> attribute. SVGs and animated GIFs no longer have renditions generated for them.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Inspector and canvas</h3>
                <ul class="release-list">
                    <li><strong>Reset.</strong> Right-click any control for Reset, which returns it to the part's default at every breakpoint, and use Reset Section at the foot of a section to reset everything in it in one undoable step, including a global part's shared definition.</li>
                    <li>The Advanced section's <strong>CSS</strong> field keeps the cursor where you are typing and highlights CSS syntax, sharing the editor used by the HTML part.</li>
                    <li>The image well's <strong>Pick</strong> button opens the file chooser and <strong>Image on the Web</strong> offers Import Copy or Link for an address.</li>
                    <li>The canvas no longer leaves a part in its hovered appearance after the pointer leaves the window, and a constrained empty Container highlights its visible drop target.</li>
                    <li>The canvas remembers the breakpoint you last chose and restores it on launch, falling back by width when a project uses different breakpoints.</li>
                    <li>The home page's filename can be edited, but accepts only <code>index</code>, <code>index.html</code> or <code>index.php</code>.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Packs and the developer API</h3>
                <ul class="release-list">
                    <li>The <code>type</code> of a control group may now be <code>filters</code>, <code>transforms</code>, <code>transitions</code> or <code>linkOverlay</code>. The validator reports a second Link group on one root, a root the Link group cannot convert, and interactive descendants that would stop conversion.</li>
                    <li>A <code>frameworkSpacing</code> control's <code>noneValue</code> — the CSS its None choice emits, <code>auto</code> or <code>none</code> instead of <code>0</code> — is documented for the first time on the <a href="framework-spacing-control.html">framework spacing</a> page.</li>
                    <li><code>defaults.base.opacity</code> on a framework colour is validated: it requires <code>opacity: true</code> and must be a number from 0 to 1.</li>
                    <li>Numbers written into CSS and HTML always use a dot for the decimal point and never a thousands separator, whatever the user's region.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Documentation</h3>
                <ul class="release-list">
                    <li>New pages for the <a href="filters-control-group.html">Filters</a>, <a href="transforms-control-group.html">Transforms</a>, <a href="transitions-control-group.html">Transitions</a> and <a href="link-overlay-control-group.html">Link</a> groups, listed under Control groups in the sidebar.</li>
                    <li>The <a href="background-control-group.html">Background</a> page is rewritten around opt-in video and the shared overlay; <a href="framework-colour-control.html">Framework colour</a> documents the opacity slider and default; <a href="sizing-control-group.html">Sizing</a> lists the five width modes; <a href="manifest-identity.html">Identity</a> states the reserved prefix.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Fixes</h3>
                <ul class="release-list">
                    <li>On a Mac set to a region that writes decimals with a comma, any colour opacity below 100% produced <code>rgb(91 91 214 / 0,819)</code>, which browsers reject, so the colour vanished. The alpha is now always written with a dot.</li>
                    <li>Adding an SVG to an Image part no longer raises a persistent missing-image warning: renditions are made only for images that can have them.</li>
                    <li>Typing in the Advanced CSS field no longer sends the cursor to the end after each character.</li>
                    <li>A child's Sizing width inside a Container was overridden by the Container's own child rules; measured in WebKit, a 300px child filled the full 1024px rail. Fixed.</li>
                    <li>The built-in Flexbox failed to load after its identifier changed to <code>foundry.layout.flexbox</code>; Flex Item's allowed parents and the app's own reference now match.</li>
                    <li>Entering <code>index.htm</code> as the home page filename silently reverted; the rule is now explicit.</li>
                </ul>
            </section>
        </div>
    </article>

    <article class="release-build" id="build-14">
        <header class="release-build-header">
            <div>
                <span class="release-build-number">Build 14</span>
                <h2>Controls showcase, responsive images and a focal point everywhere</h2>
            </div>
            <time datetime="2026-09-28">28 September 2026</time>
        </header>
        <p class="release-summary">Build 14 adds a Controls section to the Developer panel that demonstrates every control and control group live, with copyable snippets; rebuilds the Image part around renditions, a focal point and a Fit choice; gives the Sizing group an aspect ratio and the Background group a focal point; lets an image come from a web address; and stops a duplicated control id from crashing the app.</p>

        <div class="callout breaking">
            <h3>Breaking change for packs</h3>
            <ul class="release-list">
                <li><strong>The Background group's Position presets are gone.</strong> <code>control.background.backgroundPosition</code> and <code>control.background.backgroundHoverPosition</code> no longer exist; the group's image controls have a Focal Point button instead, and <code>control.background.position</code> (and <code>hover.position</code>) now carry that point as <code>x% y%</code>. Templates that read the removed values must switch to <code>position</code> or to the image's own <code>control.background.backgroundImage.position</code>. There is no automatic migration during the preview period.</li>
            </ul>
        </div>

        <div class="release-groups">
            <section class="release-group">
                <h3>Developer panel</h3>
                <ul class="release-list">
                    <li>The panel has two sections, <strong>Debugger</strong> and <strong>Controls</strong>. Controls lists every control and control group; click one and Foundry shows it on a scratch <em>Controls</em> page with the real Inspector controls, a canvas sheet that reacts as you change them, and <strong>Snippets</strong> at the top of the Inspector with a Copy button for the declaration, its template usage and any CSS. An <strong>API Docs</strong> button beside the part title opens the reference page.</li>
                    <li>Each showcase exercises the control's forms — presentation variants, count arrays, responsive values, ticks and labels, configured control groups — and prints every template value the control provides.</li>
                    <li>The scratch page lives only in memory: never listed with your pages, saved, exported or undone. Leaving Controls discards it, returns you to the page you were on and unloads the showcase parts; they are read in only while the section is open.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Image part</h3>
                <ul class="release-list">
                    <li><strong>Renditions and <code>srcset</code>.</strong> The built-in Image declares 480, 960 and 1600 pixel renditions and emits <code>srcset</code> and <code>sizes</code>, with <code>sizes</code> following the Sizing group's width. Renditions are made only at export, once per image and size, and cached.</li>
                    <li><strong>Focal Point</strong> is a button in the image control: turning it on shows the draggable marker, turning it off returns the image to centre. The image well's <strong>Pick</strong> button splits: <em>From URL…</em> imports a copy of a web image or links to it live, and an image dragged from a browser imports a copy.</li>
                    <li>A <strong>Loading</strong> choice (Lazy, or Immediate with <code>fetchpriority="high"</code>), a <strong>Fit</strong> choice (Cover or Contain) shown once the part has a shape of its own, Alignment under Sizing and hidden when the part fills its parent, and the whole-part link named by the alt text when no label is given.</li>
                    <li>A fixed, minimum or maximum height, or an aspect ratio, now reaches the image, so it is cropped around its focal point rather than clipped from the top.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Control groups</h3>
                <ul class="release-list">
                    <li><strong>Sizing</strong> gains <strong>Aspect ratio</strong> — 1:1, 4:3, 3:2, 16:9, 21:9 or a custom pair — shown when Height is Fit content.</li>
                    <li><strong>Background</strong> images offer the Focal Point button, and the chosen point becomes <code>background-position</code>.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Packs and the developer API</h3>
                <ul class="release-list">
                    <li>Every image rendition reports its own <code>width</code> and <code>height</code> — <code>control.hero.rendition.small.width</code> — so <code>srcset</code> descriptors are right for portrait images and for images already smaller than a rendition. The canvas reports the same sizes while showing the full image.</li>
                    <li>An image whose value is a web address renders as is: its dimensions, renditions and file metadata are empty, so guard <code>srcset</code> behind <code>{{ if control.hero.width }}</code>, as the <a href="image-control.html">image control</a>'s complete example does.</li>
                    <li><code>visibleWhen</code>'s <code>isEmpty</code> and <code>isNotEmpty</code> treat a framework length left at None as empty, so a control can appear only once a limit is set.</li>
                    <li>A manifest's <code>group</code> may now name any of fifteen Parts-panel headings, listed on the <a href="manifest-identity.html">identity</a> page in the order the panel shows them.</li>
                    <li>The <a href="image-control.html">image control</a> page gains an example for every key and a complete manifest, template and stylesheet.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Inspector and canvas</h3>
                <ul class="release-list">
                    <li>The image well shows a linked web image and lets you place a focal point on it; when the image cannot be fetched it shows the address instead. Import Copy and Link are both prominent choices in the From URL… popover.</li>
                    <li>Fit appears for an image as soon as any of Height, Aspect ratio, Min height or Max height gives the part a shape, not only for a fixed height.</li>
                    <li>Built-in part icons for Button, Copyright, HTML, Image and Navigation have new tints.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Documentation</h3>
                <ul class="release-list">
                    <li>The Build 12 entry below now opens with a red box listing the pack changes that broke Build 11 parts — the required control-group <code>id</code>, the renamed configuration keys, <code>layoutItem</code>, the slider and video changes — with the one-line fix.</li>
                    <li>The <a href="background-control-group.html">Background</a> page describes the image focal point in place of the Position presets; the <a href="sizing-control-group.html">Sizing</a> page documents the aspect ratio controls and their composed CSS; <a href="visible-when.html">visibleWhen</a> notes that a framework length at None is empty; and <a href="custom-controls.html">Custom controls</a> explains the Developer panel's Controls section.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Fixes</h3>
                <ul class="release-list">
                    <li>Two controls or text macros with the same id no longer crash Foundry while a pack loads; the validator reports <em>Duplicate control identifier</em> and the part is rejected.</li>
                    <li>An image under a Max height was clipped from the top instead of cropped around its focal point; the Image part now lays out as a flex column so every height rule reaches the image.</li>
                    <li>The built-in Divider is created under its current <code>foundry.layout.divider</code> identifier.</li>
                </ul>
            </section>
        </div>
    </article>

    <article class="release-build" id="build-12">
        <header class="release-build-header">
            <div>
                <span class="release-build-number">Build 12</span>
                <h2>Rebuilt layout parts, consistent part options and a faster canvas</h2>
            </div>
            <time datetime="2026-09-28">28 September 2026</time>
        </header>
        <p class="release-summary">Build 12 rebuilds Container, Flexbox and Grid and adds a simple Columns part, gives every built-in part the same set of Inspector sections — including per-instance custom CSS — makes developer breakpoint defaults behave like ordinary pinned values, replaces the Inspector slider with the native one and expands its API, adds a Video part and more expressive part icons, and makes pasting into large pages effectively instant.</p>

        <div class="callout breaking">
            <h3>Breaking changes for packs built with Build 11</h3>
            <p>Parts made for earlier builds will not load until their <code>manifest.json</code> is updated. The most common failure is <em>“Missing key 'id' (at inspector[…].controls[…])”</em>, which points at a control group without an <code>id</code>.</p>
            <ul class="release-list">
                <li><strong>Every control group needs an <code>id</code>.</strong> <code>sizing</code>, <code>spacing</code>, <code>background</code>, <code>borders</code>, <code>effects</code>, <code>layout</code>, <code>reveal</code> and <code>flexbox</code> references must declare one; only <code>advanced</code> is exempt. The id is the group's template namespace, so using the type name keeps existing templates working: <code>{ "type": "spacing", "id": "spacing" }</code> is read as <code>control.spacing.css</code>, exactly as before.</li>
                <li><strong>Group configuration keys were renamed</strong> and the old names are rejected:
                    <table>
                        <thead><tr><th>Build 11</th><th>Build 12</th></tr></thead>
                        <tbody>
                            <tr><td><code>defaultOverrides</code></td><td><code>defaults</code></td></tr>
                            <tr><td><code>optionOverrides</code></td><td><code>allowedOptions</code></td></tr>
                            <tr><td><code>omit</code></td><td><code>excludeControls</code></td></tr>
                            <tr><td><code>target</code></td><td><code>targetSelector</code></td></tr>
                            <tr><td><code>states</code> and <code>styles</code> on <code>background</code></td><td><code>supportsHover</code> and <code>backgroundTypes</code></td></tr>
                        </tbody>
                    </table>
                </li>
                <li><strong><code>layoutItem</code> is gone.</strong> Use the <a href="layout-control-group.html"><code>layout</code></a> control group instead.</li>
                <li><strong>Slider:</strong> <code>showsValueField</code> is replaced by <a href="slider-control.html"><code>editableValue</code></a>.</li>
                <li><strong>Video control:</strong> the template now writes the <code>&lt;video&gt;</code> element from the control's values, as the image control does; see the <a href="video-control.html">video control</a> page.</li>
                <li><strong>Part icons:</strong> the separate icon and tile artwork files are no longer read. A pack without an <a href="manifest-identity.html"><code>icon</code></a> dictionary still loads, but shows a generic icon until it declares one.</li>
            </ul>
            <p>Each control group page shows the current keys with an <code>id</code> in every example. There is no automatic migration during the preview period.</p>
        </div>

        <div class="release-groups">
            <section class="release-group">
                <h3>Layout parts</h3>
                <ul class="release-list">
                    <li><strong>Container, Flexbox and Grid are rebuilt</strong> with new defaults chosen for people who never check the mobile view. Flexbox and Grid accept any part directly, one per cell or slot, and start with three items; add a Grid Item or Flex Item when a cell needs its own spanning, background, padding or alignment.</li>
                    <li><strong>Grid</strong> starts with 1, 2 and 3 columns across phone, tablet and desktop; its alignment defaults to Auto, so boxes stretch to fill their cells while images and video keep their proportions. A single <strong>Rows</strong> slider runs from Auto to 12, a new <strong>Placement</strong> control can Fill Gaps left by spanning items, and <strong>Preview Grid</strong> draws the column and row tracks on the canvas only — never in preview or published pages.</li>
                    <li><strong>Flexbox</strong> now wraps by default and centres its items, so rows reflow on small screens and mixed parts line up. <strong>Flex Item</strong> gains a Size choice — Fit Content, Fill Space, Equal Width or Custom — with Grow, Shrink and Starting Size under Custom.</li>
                    <li><strong>Container</strong> content width is Breakpoint, Full, Fit Content or a Custom width that never exceeds the screen; the separate content height was removed in favour of the section's own Sizing height. New Containers start with comfortable padding, and its alignment controls read Vertical and Horizontal.</li>
                    <li>Added <strong>Columns</strong>, a simple layout for less experienced users: choose a preset — 50/50, 33/67, 67/33, 25/75, 75/25, three or four equal, or 25/50/25 — and each column is its own drop area. Columns stack on phones and sit side by side from tablets up, and <strong>Reverse Order</strong> mirrors both the order and the widths, per breakpoint.</li>
                    <li>The Divider moved to the Layout group with new artwork, and parts within each library group are now listed alphabetically.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Consistent part options</h3>
                <ul class="release-list">
                    <li>Every built-in part now offers the standard sections — Sizing, Spacing, Background, Borders, Effects, Layout, Reveal and Advanced — wherever they make sense, so Headings, Paragraphs, Images, Buttons and the rest can be styled the same way as layout parts. Sections that would duplicate a part's own settings, such as Background on Button, are deliberately left out.</li>
                    <li>A whole-part <strong>Link</strong> is available on Container, Flexbox, Image, Grid Item and Flex Item, for clickable sections, images and cards.</li>
                    <li>The Image part uses the standard Sizing group, starting at 1200 pixels wide as before; with a fixed height, the image covers the area around its focal point.</li>
                    <li>The Advanced section gains a <strong>CSS</strong> field for per-instance custom CSS. Declarations style the part itself, <code>:hover { … }</code> styles it when hovered, and nested rules such as <code>h2 { … }</code> style elements inside it. The CSS is scoped to the part, takes precedence over the part's own rules, and cannot leak onto the rest of the page — even when its braces don't balance.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Responsive editing</h3>
                <ul class="release-list">
                    <li>Breakpoint defaults declared by a part now behave exactly as if you had pinned them: a new part shows its blue dots from the start, editing at that breakpoint updates the pin, and clicking the dot or Reset returns the breakpoint to inheriting from the one below.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Inspector</h3>
                <ul class="release-list">
                    <li>Sliders are now native SwiftUI sliders: they draw exactly the tick marks a part asks for, snap to their step, and show their current value beside the track — as a read-only label, or an editable field where the part enables one. Tick labels, text at special values such as "Auto", end symbols and a centre-out fill are all available to parts.</li>
                    <li>Number steppers stop at their minimum and maximum instead of wrapping round.</li>
                    <li>Separate controls sit as closely as the rows of a multi-part control; parts add separation where they want it with the new spacer or a divider, which now has even space above and below.</li>
                    <li>The child picker's Add button fills its column like its neighbours, and segmented buttons without subtitles no longer reserve space for them.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Media and icons</h3>
                <ul class="release-list">
                    <li>Added the <strong>Video</strong> part and the <code>{{ video("name") }}</code> primitive with its own drop wells and canvas poster frames; dropping a movie onto the canvas creates a Video part, as dropping an image creates an Image part.</li>
                    <li>Part icons are declared as one glyph — an SVG file or an SF Symbol — plus a system tint, replacing the separate icon and tile artwork files. Any solid colour works in an SVG glyph.</li>
                    <li>Tints accept <strong>light and dark shades</strong>, such as <code>blue.light</code>, and SVG icons can set <code>"rendering": "original"</code> to appear as authored in full colour. The Structure tree always uses the base colour, and an unrecognised tint simply renders gray.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Canvas and workspace</h3>
                <ul class="release-list">
                    <li><strong>Pasting and duplicating no longer slow down on large pages.</strong> The canvas updates only the parts an edit touches, keeps each part's styles in their own element, and caches every instance's CSS. On a 400-part page a paste now costs the same as on a small one.</li>
                    <li>The canvas's light and dark appearance toggle now also switches <code>prefers-color-scheme</code>, drop zones use symbols, and insertion bars replace the drop slab wherever a target already has children.</li>
                    <li>Sidebars use the system's own translucent material.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Packs and the developer API</h3>
                <ul class="release-list">
                    <li>The slider control's <code>showsValueField</code> is replaced by <a href="slider-control.html"><code>editableValue</code></a>, and sliders gain <code>tickLabels</code>, <code>valueLabels</code>, <code>minimumLabel</code>, <code>maximumLabel</code> and <code>neutralValue</code>.</li>
                    <li>Added the <a href="spacer-control.html"><code>spacer</code></a> control, and <code>id</code> is now optional on dividers, notes and spacers.</li>
                    <li>The <a href="layout-control-group.html"><code>layout</code></a> control group replaces <code>layoutItem</code>, covering position, z-index, offsets, display, overflow and isolation; Sizing gains minimum and maximum limits and six width modes; Spacing starts disabled; edge controls link in pairs; and <code>frameworkSpacing</code> controls may declare the CSS their <code>none</code> value emits.</li>
                    <li>A part's breakpoint defaults are applied as pins on new instances, and the control pages describe the change.</li>
                    <li>The <a href="manifest-identity.html"><code>icon</code></a> dictionary documents <code>file</code>, <code>symbol</code>, tint shades and <code>rendering</code>; the <a href="advanced-control-group.html">Advanced</a> group documents the custom CSS field; and the video control now hands over its URL and values for the template to write the markup, like the image control.</li>
                </ul>
            </section>
        </div>
    </article>

    <article class="release-build" id="build-11">
        <header class="release-build-header">
            <div>
                <span class="release-build-number">Build 11</span>
                <h2>Structured layout, page metadata and a faster preview</h2>
            </div>
            <time datetime="2026-09-25">25 September 2026</time>
        </header>
        <p class="release-summary">Build 11 restructures the layout system around Container, Flex and Grid working as a team — including the new Flex Item and Grid Item parts — completes per-page metadata and SEO, splits the documentation into a user guide and developer reference, introduces site kits and the project chooser, moves pack manifests to JSON with named Inspector sections, and makes preview generation roughly three times faster.</p>

        <div class="release-groups">
            <section class="release-group">
                <h3>Layout parts</h3>
                <ul class="release-list">
                    <li>Container gained a <strong>Content Layout</strong> section — Align, Align Horizontally and Gap for its content — plus a Custom content width alongside Contained and Full Width. Vertical alignment now works in every height mode, including Fill Viewport.</li>
                    <li>Added the <strong>Fill Remaining Space</strong> height mode to Container, Flex and Grid: the part grows into whatever viewport space its siblings leave free. The page body is now a viewport-height flex column, so top-level filling and alignment behave dependably; Fill Viewport is a true minimum that grows with content, keeping backgrounds behind everything.</li>
                    <li>Renamed Stack to <strong>Flex</strong>, now defaulting to a wrapping row, and unified control names, defaults and section order across Container, Flex and Grid — Distribute, Align, Gap and friends mean the same thing everywhere.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Flex Item and Grid Item</h3>
                <ul class="release-list">
                    <li>Added two supporting parts: <strong>Flex Item</strong> carries Grow, Shrink and Align Self; <strong>Grid Item</strong> carries responsive Span Columns and Span Rows. Both arrange their own children with Flexbox, so a spanning grid card is also a column stack.</li>
                    <li>Selecting a Flex or Grid now shows an <strong>Items</strong> row with an Add button that inserts the matching item part — the first built-in use of the <a href="child-picker-control.html"><code>childPicker</code></a> slot. Both areas still accept any part dropped in directly.</li>
                    <li>The item parts stay out of the parts library and only offer themselves inside the parents they belong to; the developer setting for hidden parts reveals them when needed.</li>
                    <li>Removed the Layout Item section from every built-in part: in-parent behaviour now lives on the item parts, so Paragraphs, Headings and Buttons carry no inert flex or grid settings. The <a href="layout-item-control-group.html"><code>layoutItem</code></a> group remains available to pack developers.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Pages, metadata and search</h3>
                <ul class="release-list">
                    <li>Rebuilt Page Info as a native grouped form: browser title and descriptions with live character counts that warn near the limits, social title, description and a social image well, and a curated language picker shared with Site Settings.</li>
                    <li>Added per-page <strong>Folder</strong> and <strong>Filename</strong> overrides that control the exported path and links, with PHP pages keeping their required extension.</li>
                    <li>Added per-page <strong>Include in Sitemap</strong> and <strong>Include in Search</strong> toggles — excluded pages emit <code>noindex</code> and leave the sitemap, and the sitemap lists only indexable pages.</li>
                    <li>Sites now emit social tags automatically: <code>og:site_name</code>, <code>og:type</code>, <code>og:locale</code>, <code>og:url</code> and Twitter cards, with new Site Identity fields for the social image description and social account.</li>
                    <li>The home page wears a house icon in the Structure panel.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Built-in parts</h3>
                <ul class="release-list">
                    <li>Added the <strong>Copyright</strong> part, rendering an always-current copyright line. Removed the Image Slider.</li>
                    <li>Navigation 1.1 adds Content Width, Link Spacing, Link Style, Capitalise Links and open-on-hover dropdown menus.</li>
                    <li>Redrew artwork for every built-in part under the new two-file contract: a square <code>icon.svg</code> plus an optional 2:1 <code>tile.svg</code>, each with dark-appearance variants, presented on refreshed parts-panel tiles.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Packs and the developer API</h3>
                <ul class="release-list">
                    <li>Part manifests are now <strong>JSON</strong> (<code>manifest.json</code>), replacing property lists across parts, packs and the documentation.</li>
                    <li>The <code>inspector</code> array replaces <code>controls</code>, and named <strong>section wrappers</strong> give developers full ownership of Inspector sectioning — every section is declared with its name, icon and contents, with the Advanced group remaining top level.</li>
                    <li>Added <strong>site kits</strong> and the Create a New Project chooser, a sectioned template library with project templates, asset collections in tabbed pack libraries, and the hand-authorable typed-directory pack format with document-owned publish manifests.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Documentation</h3>
                <ul class="release-list">
                    <li>The documentation site now opens with a landing page forking into the new <strong>Foundry User Guide</strong> and the Developer API reference, and the app's Help menu links to each directly.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Performance</h3>
                <ul class="release-list">
                    <li>Preview generation is roughly <strong>three times faster</strong> on layout-heavy pages: stylesheet tidying is a single linear pass, per-page navigation values are computed once instead of per part, and property resolution in both renderers stopped rescanning part definitions per key.</li>
                    <li>Site kits scan lazily at launch, and project assets continue to load on demand.</li>
                </ul>
            </section>
        </div>
    </article>

    <article class="release-build" id="build-10">
        <header class="release-build-header">
            <div>
                <span class="release-build-number">Build 10</span>
                <h2>Navigation, extensible control groups and motion</h2>
            </div>
            <time datetime="2026-09-22">22 September 2026</time>
        </header>
        <p class="release-summary">Build 10 adds a complete built-in Navigation part, makes Foundry’s built-in control groups manifest-backed and directly inspectable, introduces Alpine, GSAP and ScrollTrigger resources, and adds an opt-in Reveal group for polished entrance motion.</p>

        <div class="release-groups">
            <section class="release-group">
                <h3>Navigation</h3>
                <ul class="release-list">
                    <li>Added a built-in Navigation part with responsive desktop and mobile menus, nested page dropdowns, current-page and ancestor states, and configurable menu sources.</li>
                    <li>Navigation follows the Pages panel’s mixed page-and-folder order. Navigation folders become labelled menu groups, while folders excluded from navigation transparently promote their included contents.</li>
                    <li>Added the <a href="page-folder-control.html"><code>pageFolder</code></a> control for selecting a page folder as a Part value, including an optional whole-site choice.</li>
                    <li>The Help menu now links directly to the browsable Foundry Developer documentation.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Control groups</h3>
                <ul class="release-list">
                    <li>Foundry’s Background, Borders, Effects, Layout Item, Sizing and Spacing groups are now defined by readable JSON manifests, using the same control model available to Part developers.</li>
                    <li>Each built-in group now has its own API reference page, with its generated controls, defaults, output values and rendering behaviour documented independently.</li>
                    <li>Added <code>valueAvailability: whenVisible</code> for controls whose values should disappear from templates while their <code>visibleWhen</code> condition is false. This is useful when a hidden dependent value must not affect output.</li>
                    <li>Presentation-only controls remain intentionally unavailable as <code>control.&lt;id&gt;</code> values; visibility conditions target real value-producing controls.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Libraries and Reveal</h3>
                <ul class="release-list">
                    <li>Part manifests can request bundled Alpine 3, GSAP 3 and GSAP ScrollTrigger resources. Foundry resolves dependencies, loads scripts in the required order and exports each requested library once.</li>
                    <li>Added the <a href="reveal-control-group.html">Reveal control group</a> with fade, directional, scale and blur effects plus distance, duration, delay, easing, stagger, trigger position and replay settings.</li>
                    <li>Reveal is available on the built-in content, media and layout parts, remains disabled by default, and respects the visitor’s reduced-motion preference.</li>
                    <li>Reveal uses the standard global GSAP and ScrollTrigger APIs, so Part developers remain free to build their own timelines and interactions alongside it.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Template API</h3>
                <ul class="release-list">
                    <li>HTML, CSS and JavaScript templates can inspect every project breakpoint through <code>breakpoints.&lt;name&gt;.enabled</code> and the numeric <code>breakpoints.&lt;name&gt;.minimumWidth</code> value.</li>
                    <li>Breakpoint metadata is available in instance-, page- and site-scoped templates, including canvas, preview and published rendering.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Pack format</h3>
                <ul class="release-list">
                    <li>Foundry packs now use one outer <code>.foundrypack</code> or <code>.foundrydevpack</code> with plain <code>Parts</code>, <code>Templates</code> and <code>Frameworks</code> directories.</li>
                    <li>Removed recursive nested packs, collection manifests, standalone framework bundles and macOS-style <code>Contents</code> directories. This alpha build intentionally does not load the earlier format.</li>
                    <li>Development packs are watched in place, while installed release-pack content remains read-only. Personal templates and frameworks are saved into a writable personal development pack.</li>
                </ul>
            </section>
        </div>
    </article>

    <article class="release-build" id="build-9">
        <header class="release-build-header">
            <div>
                <span class="release-build-number">Build 9</span>
                <h2>Custom framework values and text colours</h2>
            </div>
            <time datetime="2026-09-21">21 September 2026</time>
        </header>
        <p class="release-summary">Every framework scale now accepts your own custom values, the Framework editor sections share one refined row-per-value layout, editable text gains framework palette colours that follow later palette edits, and the Part API adds <code>frameworkFontSize</code> and <code>frameworkStackingOrder</code> controls.</p>

        <div class="release-groups">
            <section class="release-group">
                <h3>Editable text colours</h3>
                <ul class="release-list">
                    <li>The text editor's colour picker is now the framework palette popover: colours are stored as palette references and resolved at render time, so palette edits recolour existing text, and light/dark appearances resolve per palette shade. Deleting a palette lets text fall back to its inherited colour without losing the reference.</li>
                    <li>Rebuilt the text editor's toolbar along the top of the sheet with regular-size native controls and the expected shortcuts: ⌘B/I/U, ⇧⌘X for strikethrough, ⌘− and ⌘= for text size, and ⌘K for links.</li>
                    <li>The HTML source editor no longer substitutes curly quotes or autocorrects while you type code.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Framework editor</h3>
                <ul class="release-list">
                    <li>Renamed Type Scale to <strong>Font Size</strong> and rebuilt it in the Fonts layout: a sidebar of custom and framework sizes with a per-size detail pane, where the size slider carries an ideal line height with it and the line-height slider overrides manually.</li>
                    <li>Rebuilt Spacing, Border Width, Border Radius and Stacking Order as single pages with one row per value — name, slider, precise field and unit — with a Custom Values card above each framework scale for adding, renaming and deleting your own entries.</li>
                    <li>Spacing now edits in rem, the unit the published CSS actually uses, with the pixel equivalent alongside.</li>
                    <li>Reset Scale sits inside the card it resets, restores the source framework's saved values, never touches custom values, and disables when nothing has changed. Custom values stay editable on built-in frameworks.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Custom framework values</h3>
                <ul class="release-list">
                    <li>Border widths, corner radii and stacking order now accept project custom values alongside custom spacing, each emitting its own <code>--foundry-*</code> CSS variable; custom spacing and stacking values also generate <code>fd-*</code> utility classes.</li>
                    <li>Added a <strong>4XL</strong> spacing token (8 rem / 128 px) to the predefined scale for section-level whitespace.</li>
                    <li>Framework value pickers list your custom values in a Custom section above the framework scale.</li>
                    <li>Deleting a custom value no longer asks for a replacement: parts still using it keep its exact size baked in as a custom length, token-only selections snap to the closest predefined token, and the whole operation is one undoable step.</li>
                    <li>Custom values survive switching frameworks, and new entries are named <code>new</code>, <code>new1</code>, <code>new2</code>…</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Part API</h3>
                <ul class="release-list">
                    <li>Added the <a href="framework-font-size-control.html"><code>frameworkFontSize</code></a> control: a picker of the framework's font sizes resolving both the size variable and its paired <code>.lineHeight</code> variable.</li>
                    <li>Added the <a href="framework-stacking-order-control.html"><code>frameworkStackingOrder</code></a> control: a picker of the framework's stacking tokens with the framework-mode toggle switching to a custom integer, matching the spacing controls.</li>
                    <li>The built-in Paragraph and Heading parts gained an opt-in <strong>Custom Size</strong> toggle revealing a framework Size picker with its paired line height, responsive per breakpoint.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Globals</h3>
                <ul class="release-list">
                    <li>Added <strong>Explode Global</strong> to a global root's Structure and canvas context menus and its Inspector, permanently converting the whole instance back to ordinary parts.</li>
                    <li>Local Override is now child-level only; an overridden child keeps its global badge in blue as <em>Global — Child — Overridden</em>, and selected global children show their own part type in the Inspector.</li>
                    <li>Global canvas chrome is now consistently green, including a lighter green for hover and drop targets, mirroring the blue used by ordinary parts.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Fixes and workspace</h3>
                <ul class="release-list">
                    <li>The Templates and Globals panels support multiple selection for bulk deleting and rearranging, matching Assets.</li>
                    <li>The derived <code>contrastColor</code> now prefers white whenever it clears the WCAG 3:1 large-text bar, so colours like the macOS system blue read as white-on-blue rather than black.</li>
                </ul>
            </section>
        </div>
    </article>

    <article class="release-build" id="build-8">
        <header class="release-build-header">
            <div>
                <span class="release-build-number">Build 8</span>
                <h2>Foundry CSS</h2>
            </div>
            <time datetime="2026-09-20">20 September 2026</time>
        </header>
        <p class="release-summary">Every project now compiles its own build of <strong>Foundry CSS</strong> — the framework generated from the Framework editor's values — shared identically by the canvas, browser preview and published output. This build also removes the last framework-owned legacy classes and completes the framework naming sweep with <code>frameworkShadow</code>.</p>

        <div class="release-groups">
            <section class="release-group">
                <h3>Foundry CSS 1</h3>
                <ul class="release-list">
                    <li>Published sites ship one <code>files/site.css</code> built from the project: three cascade layers (<code>foundry.tokens</code>, <code>foundry.base</code>, <code>foundry.utilities</code>) with Part and page CSS unlayered — a Part's own styles beat the framework by architecture, never by specificity fights. See the new <a href="foundry-css.html">Foundry CSS</a> reference.</li>
                    <li>Every Framework editor value is a documented <code>--foundry-*</code> token, joined by reserved motion durations, a standard easing curve and a focus-ring outline value.</li>
                    <li>Token-mirroring utility classes with the <code>fd-{property}-{token}</code> grammar cover spacing, gap, text sizes, colour roles, fonts, radii, borders, shadows, z-index and the container — including classes for your custom tokens, and mobile-first responsive variants such as <code>fd-md:p-lg</code> for enabled screens.</li>
                    <li>The base layer is a token-driven reset and defaults: honours reduced-motion by zeroing the motion tokens, brand-matches native form controls through <code>accent-color</code>, consumes the focus-ring token on <code>:focus-visible</code>, balances heading wrapping, and styles plain <code>hr</code>, <code>blockquote</code> and <code>table</code> content from tokens.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Legacy classes removed</h3>
                <ul class="release-list">
                    <li>The framework no longer owns the <code>.foundry-container</code>, <code>.foundry-button</code>, <code>.foundry-grid</code> and <code>.foundry-heading</code> global rules; built-in parts style themselves. Parts that relied on those rules must declare their own styles.</li>
                    <li>Framework-generated image markup now uses <code>.fd-image</code>; Part CSS targeting <code>.foundry-image</code> must be updated.</li>
                    <li>Fixed the Container part's Max Width control being silently overpowered by the old global rule.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>frameworkShadow</h3>
                <ul class="release-list">
                    <li>Renamed the <code>shadow</code> control type to <code>frameworkShadow</code>, completing the framework prefix across every framework-aware control. The old name is a validation error; update existing manifests. See <a href="framework-shadow-control.html">Framework shadow</a>.</li>
                    <li>The control now presents like the other framework controls: the framework-mode toggle beside the picker switches between framework shadows and the custom layer editor, replacing the popup's Custom entry.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Fixes</h3>
                <ul class="release-list">
                    <li>Button, Heading and other single-primitive parts can be deleted from the canvas with the Delete key again.</li>
                    <li>The Foundry Framework document type is now declared as an exported type, silencing the launch-time UTI warning.</li>
                </ul>
            </section>
        </div>
    </article>

    <article class="release-build" id="build-7">
        <header class="release-build-header">
            <div>
                <span class="release-build-number">Build 7</span>
                <h2>Frameworks, box-model editing and manual responsive pins</h2>
            </div>
            <time datetime="2026-09-20">20 September 2026</time>
        </header>
        <p class="release-summary">A breaking platform release: frameworks replace themes across the app, the Part API and every file format, alongside redesigned four-edge editors, generic length controls, richer framework colours and a new manual model for responsive overrides.</p>

        <div class="release-groups">
            <section class="release-group">
                <h3>Themes are now frameworks</h3>
                <ul class="release-list">
                    <li>Renamed themes to <strong>frameworks</strong> throughout the app, the documentation and the Part API — they are complete design systems, and the shippingbox symbol now represents them everywhere.</li>
                    <li>Renamed the manifest control types: <code>frameworkColor</code>, <code>frameworkPadding</code>, <code>frameworkMargin</code>, <code>frameworkBorder</code>, <code>frameworkRadius</code>, <code>frameworkSpacing</code> and <code>frameworkFont</code>, plus the <code>frameworkValues</code> key. The old <code>theme*</code> names are validation errors; update existing manifests.</li>
                    <li>Renamed framework bundles to <code>.foundryframework</code>. Earlier projects and <code>.foundrytheme</code> bundles do not open in this build; recreate test content.</li>
                    <li>Added a z-index token scale to frameworks.</li>
                    <li>Moved this documentation to framework-named pages; earlier theme-named links no longer resolve.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Manifest controls</h3>
                <ul class="release-list">
                    <li>Grouped controls are now declared inline in the <code>controls</code> array at the position you want them, in exactly the author's order. The separate <code>controlGroups</code> key has been removed and no longer validates.</li>
                    <li>Added the generic <strong>Edges</strong> and <strong>Corners</strong> controls: the four-length box editors with raw values only — your declared <code>units</code>, an optional <code>linked</code> starting state, and no framework values or mode button.</li>
                    <li>Extended <code>frameworkColor</code> with derived values: appearance-aware <code>contrastColor</code>, the colour filters, an <code>outputFormat</code> accepting the complete-colour formats, and per-appearance channels, accessibility values and fragment formats behind <code>light</code>/<code>dark</code> qualification.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Inspector editing</h3>
                <ul class="release-list">
                    <li>Replaced the four-row spacing editors with box-model controls: padding, margin and border widths place each edge field around linked pair lines, and radius places each corner in a two-by-two grid joined by a single all-or-none link ring.</li>
                    <li>Replaced the per-edge Custom picker item with one shippingbox mode button that switches every edge between framework values and custom lengths, carrying amounts into custom mode and snapping to the nearest framework value on the way back. The single framework spacing control gained the same button.</li>
                    <li>Framework value pickers now label options as token and amount, such as <code>SM - 1rem</code>.</li>
                    <li>Restyled the Part Inspector edge-to-edge with tighter spacing and per-section symbols.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Responsive editing</h3>
                <ul class="release-list">
                    <li>Breakpoint overrides are now created only by clicking the blue dot, which pins the value currently showing at that breakpoint. Editing a value no longer creates overrides silently.</li>
                    <li>An edit fills whichever pin — or the base value — governs the breakpoint being viewed, so with no pins a change applies everywhere, and pinned breakpoints hold their range until unpinned.</li>
                    <li>Developer-declared breakpoint defaults behave as implicit pins: editing above one materialises the change at the default's breakpoint without leaking below it.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Projects and performance</h3>
                <ul class="release-list">
                    <li>Made project asset loading lazy, keeping large projects responsive on open.</li>
                    <li>Fixed publishing debounce so repeated publishes no longer rebuild the full bundle unnecessarily.</li>
                </ul>
            </section>
        </div>
    </article>

    <article class="release-build" id="build-6">
        <header class="release-build-header">
            <div>
                <span class="release-build-number">Build 6</span>
                <h2>Site identity and flexible publishing</h2>
            </div>
            <time datetime="2026-09-16">16 September 2026</time>
        </header>
        <p class="release-summary">A project-configuration release that brings site identity, generated web icons, search visibility and reusable publishing destinations into one clearer workflow.</p>

        <div class="release-groups">
            <section class="release-group">
                <h3>Project and site settings</h3>
                <ul class="release-list">
                    <li>Moved Site Settings into its own resizable project window and redesigned it with consistent grid rows and dedicated sections for General, Site Identity, Web Icons, SEO &amp; Search, Publishing and Code &amp; Analytics.</li>
                    <li>Improved General settings with web-address validation, a language picker, managed site-logo artwork and alt text, and the project’s dark-mode option.</li>
                    <li>Added site-wide title suffix, default description and social-image fallbacks for pages that do not provide their own metadata.</li>
                    <li>Added site-logo and social-image wells with native file picking and drag-and-drop workflows.</li>
                    <li>Separated search indexing, canonical URL, sitemap and robots.txt controls from publishing configuration, with guidance when a valid public web address is required.</li>
                    <li>Exported managed site artwork with the project while keeping source artwork private to the document package.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Web icons</h3>
                <ul class="release-list">
                    <li>Added a managed web-icon generator that accepts a square source image of at least 256 pixels.</li>
                    <li>Generated and stored favicon and Apple touch-icon variants once, then reused them across previews and published output.</li>
                    <li>Kept imported source artwork and generated icon files private to the project while emitting depth-correct icon links on every exported page.</li>
                    <li>Removed generated icon output cleanly when the source is cleared.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Structure and workspace</h3>
                <ul class="release-list">
                    <li>Added the current page as the root item in Structure, making the page itself selectable for metadata inspection.</li>
                    <li>Allowed Parts to be dragged directly onto the page root and made root-level ordering clearer alongside nested drop zones and child pickers.</li>
                    <li>Kept the page root and selected Part hierarchy expanded when revealing selections.</li>
                    <li>Refined Pages, Structure and Assets outline backgrounds so they blend correctly with sidebar materials.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Publishing destinations</h3>
                <ul class="release-list">
                    <li>Added multiple named Local Folder, SFTP, FTP, FTPS and Amazon S3 destinations with one clearly selected default.</li>
                    <li>Added reusable destination bookmarks for recalling connection settings in other projects, with credentials retained securely in Keychain.</li>
                    <li>Improved connection testing with clear success and failure states, including recognition of remote directories that will be created on first publish.</li>
                    <li>Extended the toolbar Publish control with destination selection, full republishing and direct access to Publishing Setup.</li>
                    <li>Automatically migrated projects using the earlier single-destination publishing settings.</li>
                    <li>Scoped local folders, credentials and publishing manifests to their individual destinations while keeping the sole remaining destination as the default.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Developer reliability</h3>
                <ul class="release-list">
                    <li>Added validation requiring a Part’s primary HTML output to have one stable top-level root when developer validation is enabled.</li>
                    <li>Added the Inspector’s canonical String, wildcard, array-membership and empty-value predicates to template expressions, with shared matching semantics across both APIs.</li>
                    <li>Improved live-refresh boundary coverage so malformed templates are reported before they can produce unreliable canvas updates.</li>
                    <li>Expanded regression coverage for project migration, managed site artwork, generated icons, publishing URLs and package validation.</li>
                </ul>
            </section>
        </div>
    </article>

    <article class="release-build" id="build-5">
        <header class="release-build-header">
            <div>
                <span class="release-build-number">Build 5</span>
                <h2>Selection clarity and batch editing</h2>
            </div>
            <time datetime="2026-09-15">15 September 2026</time>
        </header>
        <p class="release-summary">A focused interaction release that made complex and nested canvases easier to understand, select and edit.</p>

        <div class="release-groups">
            <section class="release-group">
                <h3>Canvas chrome</h3>
                <ul class="release-list">
                    <li>Unified chrome state priority so editing, drop targets, selection and hover no longer compete visually.</li>
                    <li>Kept selected labels visible after pointer exit while clearing genuine hover state when leaving the canvas.</li>
                    <li>Improved nested and multiple-selection label ordering, giving the primary selection visual priority.</li>
                    <li>Separated drop indicators from rendered Part styles so dragging no longer replaces a Part’s own box shadow.</li>
                    <li>Added empty-canvas click and Escape as clear ways to remove the current selection.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Multiple-Part editing</h3>
                <ul class="release-list">
                    <li>Allowed multiple instances of the same Part to share one Inspector and be edited together.</li>
                    <li>Used the last instance added to the selection as the Inspector’s visible source value.</li>
                    <li>Applied each subsequent change across every compatible selected instance, including conditional and visibility-related settings.</li>
                    <li>Refined canvas synchronisation after grouped edits so all affected instances update together.</li>
                </ul>
            </section>
        </div>
    </article>

    <article class="release-build" id="build-4">
        <header class="release-build-header">
            <div>
                <span class="release-build-number">Build 4</span>
                <h2>World-class layout foundations</h2>
            </div>
            <time datetime="2026-09-15">15 September 2026</time>
        </header>
        <p class="release-summary">The first major pass over Foundry’s built-in layout system, with a shared Inspector language and more dependable live canvas rendering.</p>

        <div class="release-groups">
            <section class="release-group">
                <h3>Built-in layout Parts</h3>
                <ul class="release-list">
                    <li>Added dedicated <strong>Stack</strong> and <strong>Grid</strong> Parts alongside Section, Container and Columns.</li>
                    <li>Greatly expanded Section, Container and Columns with responsive flex, grid, alignment, sizing and spacing options.</li>
                    <li>Standardised common Inspector groups so equivalent settings appear in predictable places across layout Parts.</li>
                    <li>Added opt-in presentation controls and hover states where they make sense, while hiding unused settings until enabled.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Canvas fidelity</h3>
                <ul class="release-list">
                    <li>Fixed cases where the canvas could fall behind the current Inspector settings while browser Preview remained correct.</li>
                    <li>Moved editing chrome inside Part bounds so developer borders remain visible.</li>
                    <li>Improved chrome visibility over images and highly styled Parts.</li>
                    <li>Added regression coverage for live Part updates and the built-in layout system.</li>
                </ul>
            </section>
        </div>
    </article>

    <article class="release-build" id="build-3">
        <header class="release-build-header">
            <div>
                <span class="release-build-number">Build 3</span>
                <h2>Developer platform and preview foundations</h2>
            </div>
            <time datetime="2026-09-14">14 September 2026</time>
        </header>
        <p class="release-summary">A broad foundation release that established the modern Part API, rebuilt the framework workflow and made large previews substantially more responsive.</p>

        <div class="release-groups">
            <section class="release-group">
                <h3>Parts and the developer API</h3>
                <ul class="release-list">
                    <li>Standardised the product language around <strong>Parts</strong>, including packs, the Inspector, Structure and developer documentation.</li>
                    <li>Expanded the custom-control API with colour, date, icon, link, shadow, typography, spacing, margin, padding, border and radius controls.</li>
                    <li>Added responsive defaults and framework-aware values so controls can inherit from project frameworks while retaining breakpoint overrides.</li>
                    <li>Added named drop zones, managed child pickers, collection loops and persistent editable text, HTML and image areas.</li>
                    <li>Added the signed Part update workflow, update discovery and in-app release availability.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Canvas and editing</h3>
                <ul class="release-list">
                    <li>Introduced targeted canvas patches and revisioned updates for faster control editing without full-page reloads.</li>
                    <li>Kept linked global Parts synchronised across placements, including structural changes and canvas chrome.</li>
                    <li>Improved image controls with drag and drop, focal-point editing, renditions and reusable on-disk rendition caching.</li>
                    <li>Refined canvas selection, context menus, inline editing, responsive indicators and undo grouping.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Frameworks and projects</h3>
                <ul class="release-list">
                    <li>Redesigned the Framework Editor around persistent colour palettes, fonts, type scales, spacing, shadows, borders and radii.</li>
                    <li>Moved responsive breakpoints to project settings so changing frameworks no longer changes a project’s responsive behaviour.</li>
                    <li>Allowed built-in frameworks to be adjusted within a project without modifying the installed framework.</li>
                    <li>Added a native welcome window, recent-project access and substantial workspace and Inspector refinements.</li>
                </ul>
            </section>

            <section class="release-group">
                <h3>Preview and distribution</h3>
                <ul class="release-list">
                    <li>Moved browser previews to disk-backed, incremental output to keep memory use predictable on large sites.</li>
                    <li>Made external preview auto-reload follow both project edits and internal page changes.</li>
                    <li>Cached generated image renditions on disk and reused them across preview and export.</li>
                    <li>Prepared the bundled PHP runtime for hardened-runtime signing and direct app distribution.</li>
                </ul>
            </section>
        </div>
    </article>

</div>
{% endraw %}
