---
title: sxiv
subtitle: simple x image viewer
date: 12/07/2020
author: /phi
content:
    title: Details
    items: '@self.children'
taxonomy:
    category: 
        - image
        - viewer
    tag: 
        - hooks
        - xdg
---

- fast display of a set of images
- allows selection to pass to next process
- keybindings and custom handlers

===

> The sole purpose of sxiv is to be the perfect image viewer for me. It is free software so that you can use it and modify it for your needs. Please file a bug report if something does not work as documented or expected. Contributions are welcome but there is no guarantee that they will be incorporated.
> - [muennich/sxiv: Simple X Image Viewer](https://github.com/muennich/sxiv)
> - Wed Dec 09 2020

# features
> Basic image operations, e.g. zooming, panning, rotating
    Customizable key and mouse button mappings (in config.h)
    Thumbnail mode: grid of selectable previews of all images
    Ability to cache thumbnails for fast re-loading
    Basic support for multi-frame images
    Load all frames from GIF files and play GIF animations
    Display image information in status bar
> - [muennich/sxiv: Simple X Image Viewer]( https://github.com/muennich/sxiv )
> - Mon Dec 07 2020

# CLI Options


# Key Bindings

# image-info


# key-handler
Additional external keyboard commands can be defined using a handler program located in $XDG_CONFIG_HOME/sxiv/exec/key-handler. The handler is invoked by pressing Ctrl-x. The next key combo is passed as its first argument. Passed via stdin are the images to act upon, one path per line: all marked images, if in thumbnail mode and at least one image has been marked, otherwise the current image. sxiv(1) will block until the handler terminates. It then checks which images have been modified and reloads them.

The key combo argument has the following form: "[C-][M-][S-]KEY", where C/M/S indicate Ctrl/Meta(Alt)/Shift modifier states and KEY is the X keysym as listed in /usr/include/X11/keysymdef.h without the "XK_" prefix.

There is also an example script installed together with sxiv as /usr/share/sxiv/exec/key-handler.
> - [sxiv - Simple X Image Viewer - man page | ManKier](https://www.mankier.com/1/sxiv#External_Key_Handler)
> - Wed Dec 09 2020
