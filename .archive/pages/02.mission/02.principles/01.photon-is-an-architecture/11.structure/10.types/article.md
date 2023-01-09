---
title: Types
subtitle: 'Entities in photon'
author: /home
content:
    items: '@self.children'
child_type: article
show_gallery: true
---

graphs

===



[mermaid]
graph TD
  article
  subgraph data items
    article --> person
    article --> organization
    article --> event
    article --> creation
  end
  subgraph special collections
    article --> calendar
    article --> portfolio
  end
  calendar -.- event
  portfolio -.- creation

[/mermaid]
