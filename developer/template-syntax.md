---
layout: default
title: Syntax at a glance · Foundry Developer
permalink: /developer/template-syntax.html
---
{% raw %}
{% endraw %}{% include breadcrumbs.html %}{% raw %}
<p class="eyebrow">Template API</p>
<h1>Syntax at a glance</h1>
<p class="lede">Recognise what each expression returns before placing it in HTML, CSS, JavaScript or PHP.</p>

<div class="api-table">
<div class="api-row api-header"><strong>Pattern</strong><span>Example</span><span>Output</span><span>Use</span></div>
<div class="api-row"><strong>Dotted value</strong><span><code>{{ control.frameworkPadding }}</code></span><span>Escaped value</span><span>Read controls, package identity, page values and paths.</span></div>
<div class="api-row"><strong>Asset function</strong><span><code>{{ asset("images/icon.svg") }}</code></span><span>Escaped URL</span><span>Resolve one path declared by the manifest’s <code>assets</code> array.</span></div>
<div class="api-row"><strong>Editable function</strong><span><code>{{ text("heading") }}</code></span><span>Editable content</span><span>Place persistent text, HTML, image or video content.</span></div>
<div class="api-row"><strong>Drop zone</strong><span><code>{{ dropZone("content") }}</code></span><span>Child markup</span><span>Place an ordinary area accepting any part.</span></div>
<div class="api-row"><strong>Managed child area</strong><span><code>{{ childArea("cards") }}</code></span><span>Child markup</span><span>Place children governed by a declared <code>childPicker</code>.</span></div>
<div class="api-row"><strong>Condition</strong><span><code>{{ if control.featured }}</code></span><span>Selected branch</span><span>Include markup according to a validated expression.</span></div>
<div class="api-row"><strong>Loop</strong><span><code>{{ loop control.count }}</code></span><span>Repeated part</span><span>Repeat bounded markup until <code>{{ endloop }}</code>.</span></div>
<div class="api-row"><strong>Filter</strong><span><code>{{ control.color | lighten(20) }}</code></span><span>Transformed value</span><span>Transform output without changing stored data.</span></div>
</div>

<h2>Required part root</h2>

<div markdown="1">

```html
<section class="my-part {{ part.class }}" {{ part.attributes }}>
    …
</section>
```

</div>

<h2>CSS targeting</h2>

<div markdown="1">

```css
.my-part { } /* Developer-owned class */
:host { }         /* Every instance from this package */
:instance { }     /* This exact placed instance */
```

</div>

<p>Use <code>:instance</code> for rules containing control values. Use <code>:host</code> only when the rule and its values are identical for every instance of the package.</p>
{% endraw %}
