+++
date = '2020-06-12'
slug = "hex-sticker-creation-r"
title = "Creating a Hexagon sticker with R in Minutes"
author = "Nelson Gonzabato"
description= "Hex sticker creation with r"
tags=["r","package-development","developer","package"]
+++

I have recently released new versions of [manymodelr](https://cran.r-project.org/package=manymodelr) and [mde](https://cran.r-project.org/package=mde), R packages you may or may not have heard of.

One common feature of many R packages is a hexagon shaped sticker that often summarises the goals of the package and/or gives an idea of the developer’s philosophy. I am, as those who know me well might tell you, not the best of artists. I however, have always marveled at these beautiful stickers in others’ packages and wished to create one myself.

To achieve this, I draw up a quick idea of the kind of information I would like to include in mde’s sticker and narrowed down to a simple lens and the word **d?ta**. To make things more exciting, I will not state what these mean and leave that to the reader as a for fun exercise.

**Making the sticker**

To make this sticker, I used the packages `magick`, `dplyr`(just the pipe, you can use `magrittr` instead), and `hexSticker`. Here is the code to produce this sticker:

```

Loading required libraries

library(magick)
## Linking to ImageMagick 6.9.9.14
## Enabled features: cairo, freetype, fftw, ghostscript, lcms, pango, rsvg, webp
## Disabled features: fontconfig, x11
library(dplyr)
## 
## Attaching package: 'dplyr'
## The following objects are masked from 'package:stats':
## 
##     filter, lag
## The following objects are masked from 'package:base':
## 
##     intersect, setdiff, setequal, union
library(hexSticker)

```

I used this [image](https://st.depositphotos.com/1041273/3800/v/450/depositphotos_38005243-stock-illustration-vector-magnifying-glass.jpg) for the lens.

**Basic Image Processing**


```

img <- image_read("images/glass.jpg")
img %>% 
  image_convert("png") %>% 
  image_resize("1080 x 200")%>% 
  image_fill(color="#062047", point="+45") %>% 
  image_annotate("d?ta", size=38, location = "+47+58", color="black") -> res

res

```

**Actual Sticker Creation**

```

# wrap in plot to preview ie plot(sticker(...))
final_res<-sticker(res, package="mde", p_size=30,
             p_y = 1.5,
             s_x=1, s_y=0.8, s_width=1.1,
             s_height = 14,
        filename="mde_icon_2.png",h_fill="#062047",h_color = "#062047")

plot(final_res)

```

![logo](https://github.com/Nelson-Gon/mde/raw/master/man/figures/mde_icon_2.png?raw=true)

That’s it. A very basic and minimal logo. For more info please see:

**References**

https://github.com/Nelson-Gon/mde

https://github.com/GuangchuangYu/hexSticker

https://github.com/tidyverse/dplyr

In case you have anything to add or criticise, please comment and/or contact me via the [contact](https://nelson-go.github.io/contact) information above.

Thank you!