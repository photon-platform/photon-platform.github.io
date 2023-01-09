---
title: v4l2loopback
subtitle: device utilities
date: 03/26/2021
author: /phi
content:
    title: Articles
    items: '@self.children'
taxonomy:
    photon:
    category: 
    tag: 
---



===


sudo apt install v4l2loopback-dkms
sudo modprobe v4l2loopback video_nr=6 card_label=photon
sudo apt install v4l-utils
