---
title: How to add a custom Kaggle Favicon to Hugo's Blackburn Theme
author: Nelson Gonzabato
date: '2020-05-07'
slug: how-to-add-a-custom-kaggle-favicon-to-hugo-s-blackburn-theme
categories: ["r","hugo","blog","misc"]
tags: ["r","kaggle"]
description: 'Adding a Custom Kaggle Favicon with R'
---

In this short article, I show how I added a [Kaggle](https://www.kaggle.com) favicon to the site.

Prerequisites:

**R packages**

* `magrittr`

* `magick`

**Why did I need to create a custom favicon?**

I admittedly do not use Kaggle as much as I used to a year or so ago, mainly because I've found the site to be less enjoyable but that's a post for another day. 

The real reason for the need to create a custom icon was the desire to include Kaggle under the  side bar. However, Hugo only provides "out of the box" configurations for popular "social" sites.

**Creating the Favicon**

I have to first give credit to [goonR](https://tbradley1013.github.io/). Coincidentally, I found out that the blog author is an Arsenal fan like myself. Back to the point, most of what I present here is based on the blog [entry](https://tbradley1013.github.io/2018/08/24/add-rstudio-community-to-your-blogs-social-links/) which deals with RStudio Community.

To create the icon, I used code from that blog(I know, I was too lazy to create it and why do it if someone else already has?! DRY, remember?):

```r

kaggle_icon <- image_read("https://cdn3.iconfinder.com/data/icons/logos-and-brands-adobe/512/189_Kaggle-512.png")

kaggle_icon %>% 
  image_scale("14") %>% 
  image_write("static/images/kaggle_icon.png")

```

I did not edit the icon further because all I needed was to have it displayed, nothing more.

**Adding the icon to the blog**

To add the icon to the blog, we edit the file `themes/blackburn/layouts/partials/social.html` to include our need icon. For Kaggle, this becomes:

```html

<!-- Kaggle -->
{{ with .Site.Social.kaggle}}
<li class="pure-menu-item">
  <a class="pure-menu-link" href="https://Kaggle.com/{{ . }}" target="_blank"><img src = "/images/kaggle_icon.png" id = "kaggle-icon">Kaggle</a>
</li>
{{ end }}

```

As someone not very much into Web development, I found the above syntax interesting, especially with respect to its similarity to `rlang`'s recent `{{}}` syntax. If you're not familar with the latter, please see [this site](https://www.tidyverse.org/blog/2019/06/rlang-0-4-0/).

**Finishing up**

Having added the above, we can add our new section to the `[social]` section of our **TOML** file(`config.toml`) in the project home. This would then look like:

```html

[Social]

twitter = "name here"
github = "name here"
stackoverflow = "id/name"
kaggle = "name"

```

**Finally**

To see our changes, we can serve our site.

To serve our site, we call `serve_site` from `blogdown`:

`blogdown::serve_site()`

Finally, our site now has a link to `Kaggle`. The beauty about this is that you can use it to add any site, which is awesome. Let me know what you think. 

>For now, please file issues on my repo for a discussion of any of my content.

The relevant repo is [Nelson-Gon](https://www.github.com/nelson-gon.github.io)

Thank you!