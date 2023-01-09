---
title: "The Article"
subtitle: "the fundamental unit of content"
author: /about
content:
    items: '@self.children'
child_type: article
show_gallery: false
---

Articles are nodes within our data system

Fundamental attributes for almost any block of content

===

[mermaid]
graph LR

	article --- hierarchy
    hierarchy --- sibling
    hierarchy --- children
    hierarchy --- breadcrumbs
  article --- type
    type --- items
    type --- collections
    type --- schema
  article --- taxonomy
    taxonomy --- categories
    taxonomy --- tags

  click article callback "Tooltip for a callback"
  click type "http://www.github.com" "This is a tooltip for a link"

  classDef key fill:#F90,stroke:#333,stroke-width:4px
  class article key
[/mermaid]

<script>
    var callback = function(){
        alert('A callback was triggered');
    }
</script>
