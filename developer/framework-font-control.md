---
layout: default
title: Framework font control · Foundry Developer
permalink: "/developer/framework-font-control.html"
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">manifest.json · inspector</p>
<h1>Framework font</h1>
<p class="lede">One configurable font control with coordinated family, weight, style and size rows. Font browsing and previews remain in the Framework Editor.</p>


<figure class="control-screenshot">
    <img src="assets/screenshots/framework-font-control.png" width="348" height="101" alt="Framework font set to Heading, with Weight 400 and Style Normal." />
    <figcaption>The optional weight and style pickers appear beneath the font choice.</figcaption>
</figure>

## Quick example

Add this dictionary to your part's `inspector` array:

```json
{
    "type" : "frameworkFont",
    "id" : "font",
    "defaults" : {
        "base" : "body"
    }
}
```

Use it in the part's CSS template:

```css
:instance {
    font-family: {{ control.font.family }};
}
```

## Properties

<h3 class="property-heading"><code>type</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Always `frameworkFont`. This is not a `select` extension. It does not accept `count`, `options`, `frameworkValues` or `allowsCustom`. Authors manage custom fonts in the Framework Editor, not inside this control.

<h3 class="property-heading"><code>id</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="required">Required</span></div>

Unique control identifier, starting with a letter and containing letters, numbers, underscores or hyphens. Templates read it as `{{ control.yourID }}`.

<h3 class="property-heading"><code>label</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: empty</span></div>

Text in the family row’s left-hand label column. Enabled companion rows are labelled Weight, Style and Size.

<h3 class="property-heading"><code>defaults</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="required">Required</span></div>

A dictionary containing the required `base` value and optional breakpoint values: `small`, `medium`, `large`, `extraLarge`, and `doubleExtraLarge`. Breakpoint entries require `responsive: true`. Every entry uses the complete value format described below; omitted breakpoints inherit the preceding enabled value. Disabled project breakpoints are skipped without discarding their declarations. A new part starts with each breakpoint entry already pinned, exactly as if the user had pinned it: its blue dot is set in the Inspector, and the user can edit or unpin it like any other pinned value. When `showsFamily` is false, the family is fixed: every entry must use the same family as `base`; enabled Weight and Style may still vary.

<h3 class="property-heading"><code>defaults.base</code></h3>
<div class="property-meta"><span class="property-type">Dictionary or String</span><span class="required">Required</span></div>

A dictionary containing required `family` (`body`, `heading` or `monospaced`), optional `weight` (an integer from 1 to 1000, default 400 when enabled), optional `style` (`normal` or `italic`, default normal when enabled), and optional `size` (a predefined framework size ID such as `base` or `xl`, default `base` when enabled). Explicit weight/style/size defaults require their corresponding capability to be enabled. Unknown dictionary keys are rejected.

A role string such as `heading` is shorthand for a dictionary containing only `family`. Arbitrary family names and custom font IDs are not valid manifest defaults. Authors choose project custom fonts in the Inspector; selections retain the role or custom identity.

<h3 class="property-heading"><code>showsFamily</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: true</span></div>

Shows the native family picker, grouped into Framework Fonts and Custom Fonts. Set false to fix the family to the declared default while exposing weight and/or style. A hidden family does not receive responsive overrides, but is still returned in the structured value. At least one of the control's capabilities must be enabled.

<h3 class="property-heading"><code>showsWeight</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: false</span></div>

Adds a Weight row for the selected family. Static faces use a menu; variable faces use a numeric weight field. When false, the return value has no weight field and Foundry does not impose a weight.

<h3 class="property-heading"><code>showsStyle</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: false</span></div>

Adds a Style row offering normal/italic as supported by the selected family and weight. When false, the return value has no style field and Foundry does not impose a style.

<h3 class="property-heading"><code>showsSize</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: false</span></div>

Adds a Size row using the framework's font-size scale — the same picker as a standalone [frameworkFontSize](framework-font-size-control.html) control, including project custom sizes. When false, the return value has no size field and Foundry does not impose a size.

<h3 class="property-heading"><code>responsive</code></h3>
<div class="property-meta"><span class="property-type">Boolean</span><span class="optional">Optional</span><span class="default">Default: false</span></div>

Allows each exposed field to override independently at responsive breakpoints. Changing only weight does not pin the inherited family or style. Each row has its own responsive indicator. Use the fields in the part CSS template for responsive styling. All fields are shared between light and dark appearance.

<h3 class="property-heading"><code>tooltip</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: omitted</span></div>

Help text explaining the control.

<h3 class="property-heading"><code>subtitle</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: empty</span></div>

Supporting text below the picker.

<h3 class="property-heading"><code>visibleWhen</code></h3>
<div class="property-meta"><span class="property-type">Dictionary</span><span class="optional">Optional</span><span class="default">Default: shown</span></div>

Shows the control when another control meets the declared condition. See [Conditional visibility](visible-when.html).
<h3 class="property-heading"><code>valueAvailability</code></h3>
<div class="property-meta"><span class="property-type">String</span><span class="optional">Optional</span><span class="default">Default: always</span></div>

Controls when this control's value is available to templates. `always` preserves the value when the control is hidden. `whenVisible` makes `control.<id>` and its qualified derived values unavailable while `visibleWhen` is false, without discarding the stored value. `whenVisible` requires `visibleWhen`. See [Conditional visibility](visible-when.html).


## Return value

The template receives one structured value. Read `{{ control.font.family }}` for the CSS font-family variable, `{{ control.font.weight }}` for the numeric weight when enabled, `{{ control.font.style }}` for the style keyword when enabled, and `{{ control.font.size }}` for the font-size variable when enabled, with its paired leading at `{{ control.font.size.lineHeight }}`. Do not insert the entire object directly into CSS. Only write weight/style/size declarations when those capabilities are enabled.

A missing family shows a warning and its family field resolves to `inherit`. Unavailable saved weight/style selections are retained with warnings; the browser may substitute or synthesize a face. Letter spacing remains a separate concern; size and its paired line height are available through `showsSize`.

## Available faces

Uploaded font files supply their face metadata. Google fonts configured in the Framework Editor supply their saved included faces and weight ranges, which also drive the Google stylesheet request. Both sources coordinate the Weight and Style rows automatically—no control-ID linking is needed.

Existing Google entries without saved metadata offer **Configure included styles…** in the Framework Editor. Until configured, those entries and system fonts offer standard CSS choices with availability marked unverified in help.

Disabling an included face in the Framework Editor does not rewrite parts. If a selected style or weight disappears entirely, the control offers the remaining family choices so authors can recover.

## Example

```json
{
    "type" : "frameworkFont",
    "id" : "font",
    "label" : "Font",
    "showsWeight" : true,
    "showsStyle" : true,
    "showsSize" : true,
    "defaults" : {
        "base" : {
            "family" : "heading",
            "weight" : 700,
            "style" : "normal",
            "size" : "xl"
        }
    },
    "responsive" : true
}
```

In the part CSS template:

```css
.title {
    font-family: {{ control.font.family }};
    font-weight: {{ control.font.weight }};
    font-style: {{ control.font.style }};
    font-size: {{ control.font.size }};
    line-height: {{ control.font.size.lineHeight }};
}
```

{% endraw %}
