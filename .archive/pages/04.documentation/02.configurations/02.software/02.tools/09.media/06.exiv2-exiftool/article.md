---
title: exiv2 / exiftool
subtitle: Image Metadata Library and Tools
date: 12/08/2020
author: /phi
content:
    title: Articles
    items: '@self.children'
taxonomy:
    category: 
    tag: 
        - json
        - php
---

> Exiv2 is a C++ library and a command line utility to read, write, delete and modify Exif, IPTC, XMP and ICC image metadata.
> - [Exiv2/exiv2: Image metadata library and tools](https://github.com/exiv2/exiv2)
> - Tue Dec 08 2020

===


# exiv2 features

> Print Exif, IPTC and XMP image metadata in different formats: Exif summary info, interpreted values, or the plain data for each tag
Print the structure of images. This is useful for image file analysis.
Set, add and delete Exif, IPTC, XMP metadata and ICC profile from command line modify commands or command scripts
Adjust the Exif timestamp (that's how it all started...)
Rename Exif image files according to the Exif timestamp
Extract, insert and delete Exif, IPTC and XMP metadata and JPEG comments
Convert from Exif and IPTC to XMP properties and vice versa
Extract previews from RAW images and thumbnails from the Exif metadata
Insert and delete the thumbnail image embedded in the Exif metadata
Print, set and delete the JPEG comment of JPEG images
Fix the Exif ISO setting of picture taken with Canon and Nikon cameras
Metadata and ICC Profiles can be very conveniently piped on the command-line from one image to others.
> - [Exiv2 - Image metadata library and tools](https://exiv2.org/getting-started.html)
> - Tue Dec 08 2020



# How does Exiv2 compare to Exiftool?

> Phil Harvey's excellent Exiftool is a bit older than Exiv2 and was initially a pure Exif reader, while Exiv2 was designed to read and write Exif metadata from the beginning. Today Exiftool is amazingly complete, it reads and writes metadata, supports more image formats, more types of metadata and more Makernotes than Exiv2 and Andreas considers it the reference implementation for image metadata.

> The key difference is that Exiv2 is written in C++ and Exiftool is written in Perl. Because of that, Exiv2 naturally has faster performance and is easier to integrate with C/C++ and Obj/C applications. Exiftool on the other hand has a more comprehensive feature set.

> That said, Phil Harvey has written a C++ interface for ExifTool| [[http://owl.phy.queensu.ca/~phil/cpp_exiftool/]].
> - [How does Exiv2 compare to Exiftool - Exiv2](https://dev.exiv2.org/projects/exiv2/wiki/How_does_Exiv2_compare_to_Exiftool)
> - Tue Dec 08 2020


# remove thumbnail

```
exiftool -ifd1:all= -ext jpg FILE
```

> Here I have added "-ext jpg" to be sure only JPEG images are processed if FILE is a directory. This is important because you don't want to delete IFD1 from other image formats.
> - [How to remove thumbnail from a jpeg using Image::ExifTool](https://perlmaven.com/how-to-remove-thumbnail-from-a-jpeg-using-image-exiftool)
> - Wed Dec 09 2020

# export json or php array
