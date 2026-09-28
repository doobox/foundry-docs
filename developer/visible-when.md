---
layout: default
title: Conditional visibility · Foundry Developer
permalink: "/developer/visible-when.html"
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">Shared control capability</p>
<h1>Conditional visibility <code class="title-code">visibleWhen</code>
</h1>
<p class="lede">Show a control only when another control in the same part satisfies a condition. A false condition removes the complete control and its layout space from the Inspector.</p>

<h2>Equality</h2>
<p>Add a <code>visibleWhen</code> dictionary directly to any control. Its <code>id</code> identifies the controlling control and <code>value</code> supplies the expected JSON value. When <code>operation</code> is omitted, Foundry uses exact, type-aware equality.</p>


<div markdown="1">

```json
"visibleWhen" : {
    "id" : "layout",
    "value" : "grid"
}
```

</div>


<p>The item is shown only while <code>layout</code> equals <code>grid</code>. String <code>"1"</code>, Number <code>1</code>, Boolean <code>true</code>, and String <code>"true"</code> are different values. Equality does not coerce types or round numbers.</p>

<h2>Template value availability</h2>
<p>Inspector visibility does not change template values by default. Add <code>valueAvailability</code> beside <code>visibleWhen</code> when a hidden control should instead be unavailable through <code>control.&lt;id&gt;</code>.</p>

```json
"visibleWhen" : {
    "id" : "sizeMode",
    "value" : "preset"
},
"valueAvailability" : "whenVisible"
```

<p><code>valueAvailability</code> is an optional String with a default of <code>always</code>. It accepts <code>always</code> or <code>whenVisible</code>; <code>whenVisible</code> requires <code>visibleWhen</code>. A false condition preserves the stored value but makes the primary value and its qualified derived values unavailable while templates render.</p>

<p>Mutually exclusive controls can therefore contribute to one declaration without repeating their selection condition:</p>

```css
:instance {
    font-size: {{ control.presetSize }}{{ control.customSize }};
}
```

<p>Declare both size controls with <code>valueAvailability</code> set to <code>whenVisible</code> and complementary conditions. Ensure exactly one condition succeeds; if neither succeeds, both substitutions are empty.</p>

<h2>Compound conditions</h2>
<p>Combine conditions with <code>all</code> and <code>any</code>. Each key contains a non-empty array of complete condition dictionaries, and compound expressions may be nested. Use exactly one of <code>id</code>, <code>all</code>, or <code>any</code> in each dictionary.</p>

```json
"visibleWhen" : {
    "all" : [
        {
            "id" : "state",
            "value" : "hover"
        },
        {
            "any" : [
                {
                    "id" : "style",
                    "value" : "image"
                },
                {
                    "id" : "style",
                    "value" : "video"
                }
            ]
        }
    ]
}
```

<p>The example is visible when <code>state</code> is <code>hover</code> and <code>style</code> is either <code>image</code> or <code>video</code>.</p>

<h2>visibleWhen dictionary keys</h2>
<section class="key-reference"><h3><code>id</code></h3>
<div class="key-meta">
<span>String</span><strong>Conditionally required</strong>
</div>
<p>ID of another value-producing control in the same part. Required for a leaf condition and mutually exclusive with <code>all</code> and <code>any</code>. Append a zero-based index such as <code>titles[2]</code> to read one member of a multi-control.</p></section>
<section class="key-reference"><h3><code>all</code></h3>
<div class="key-meta"><span>Array of condition dictionaries</span><strong>Conditionally required</strong></div>
<p>Succeeds only when every nested condition succeeds. Mutually exclusive with <code>id</code> and <code>any</code>.</p></section>
<section class="key-reference"><h3><code>any</code></h3>
<div class="key-meta"><span>Array of condition dictionaries</span><strong>Conditionally required</strong></div>
<p>Succeeds when at least one nested condition succeeds. Mutually exclusive with <code>id</code> and <code>all</code>.</p></section>
<section class="key-reference"><h3><code>operation</code></h3>
<div class="key-meta">
<span>String</span><strong>Optional</strong><span>Default: ==</span>
</div>
<p>The comparison to perform. Use one of the canonical operations below.</p></section>
<section class="key-reference"><h3><code>value</code></h3>
<div class="key-meta">
<span>String, Number, Boolean or array</span><strong>Conditionally required</strong>
</div>
<p>Expected value. Required by every operation except <code>isEmpty</code> and <code>isNotEmpty</code>, which reject it.</p></section>

<h2>Equality and numbers</h2>
<ul class="rule-list">
<li>
<code>==</code> performs exact, type-aware equality. Aliases: <code>=</code>, <code>equals</code>, <code>equalTo</code>.</li>
<li>
<code>!=</code> performs exact inequality. Aliases: <code>notEqual</code>, <code>notEqualTo</code>.</li>
<li>
<code>&lt;</code>, <code>&lt;=</code>, <code>&gt;</code>, and <code>&gt;=</code> compare Numbers only.</li>
<li>Numeric aliases: <code>lessThan</code>, <code>lessThanOrEqualTo</code>, <code>lessThanOrEquals</code>, <code>greaterThan</code>, <code>greaterThanOrEqualTo</code>, and <code>greaterThanOrEquals</code>.</li>
</ul>
<p>Symbolic operators are plain JSON strings:</p>

<div markdown="1">

```json
"operation" : ">=",
"value" : 600
```

</div>



<h2>Strings and wildcards</h2>
<ul class="rule-list">
<li>
<code>contains</code> and <code>notContains</code> perform case-sensitive substring searches.</li>
<li>
<code>containsInsensitive</code> and <code>notContainsInsensitive</code> perform substring searches while ignoring case.</li>
<li>
<code>matches</code> and <code>notMatches</code> perform case-sensitive whole-string wildcard matches.</li>
<li>
<code>matchesInsensitive</code> and <code>notMatchesInsensitive</code> perform wildcard matches while ignoring case.</li>
</ul>
<p>Wildcard patterns use <code>*</code> for zero or more characters and <code>?</code> for exactly one character. <code>Red*</code> matches <code>Red</code> and <code>Reddish</code>; <code>R?d</code> matches <code>Red</code> and <code>Rad</code>.</p>
<h2>Empty and array values</h2>
<ul class="rule-list">
<li>
<code>isEmpty</code> succeeds for an empty String, empty array, unselected asset, link with no destination, or framework length set to None.</li>
<li>
<code>isNotEmpty</code> is the inverse. Neither empty operation accepts a <code>value</code> key.</li>
<li>Number <code>0</code> and Boolean <code>false</code> are valid values and are never empty.</li>
<li>
<code>containsValue</code> checks an array for one exact, type-aware value; <code>notContainsValue</code> is its inverse.</li>
</ul>


<div markdown="1">

```json
"visibleWhen" : {
    "id" : "destination",
    "operation" : "isNotEmpty"
}
```

</div>



<h2>Multi-control members</h2>
<p>Use the template language’s zero-based array notation to inspect one member. This example reads the third title:</p>


<div markdown="1">

```json
"visibleWhen" : {
    "id" : "titles[2]",
    "operation" : "containsInsensitive",
    "value" : "featured"
}
```

</div>


<p>To search the complete array for an exact member, reference its unindexed ID and use <code>containsValue</code>.</p>

<h2>Runtime behaviour</h2>
<ul class="rule-list">
<li>An item without <code>visibleWhen</code> is shown. A failed condition hides the complete inspector item rather than disabling it.</li>
<li>Hiding an item preserves its stored value. The value remains available to templates unless <code>valueAvailability</code> is <code>whenVisible</code>.</li>
<li>The Inspector updates when the controlling value changes.</li>
<li>Responsive conditions use the controlling property’s effective value at the selected breakpoint.</li>
<li>Framework-backed controls compare their stored semantic reference rather than resolved CSS output.</li>
<li>A missing or unavailable runtime value safely evaluates as hidden.</li>
</ul>

<h2>Validation</h2>
<p>Foundry rejects empty compound arrays, dictionaries that combine <code>id</code>, <code>all</code>, or <code>any</code>, malformed indexed references, unknown control IDs, self-references, dependency cycles, unsupported operations, missing required values, values supplied to empty checks, and indexes outside a multi-control’s declared count.</p>
<div class="page-links">
<a class="card" href="custom-controls.html"><strong>All custom controls</strong><p>Choose the inspector building part to conditionally present.</p></a><a class="card" href="control-arrays.html"><strong>Control arrays</strong><p>Declare and reference two to four related values.</p></a>
</div>
{% endraw %}
