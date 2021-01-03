+++
date = '2020-12-25'
slug = "hugo-blogdown-pitfalls-to-avoid"
title = "Hugo, Blogdown, and Github: What could go wrong?"
author = "Nelson Gonzabato"
description = "Rare hugo pitfalls and how to avoid them."
tags = ["versioning","github", "r", "git", "blogdown","hugo", "open-source"]
+++

One of the most beautiful things about open source development is the idea that one picks up crucial skills like versioning be it via git* or any version control system of their choosing. For non developers, such versioning can be accomplished via syncing files to the cloud or manually uploading files each time. Alternatively, and in the most extreme scenario, one could simply version their files by simple file number incrementation: `file_1_edit`, `file_1_edit_final`, `file_1_edit_final_final_finally`.

Yet even in the most extreme and manual versioning system, one can be sure that at least they would always have copies of their files backed up somewhere. 


**When things go wrong**

As a fairly "seasoned" git user, I have almost always backed up all my files. Recently, however, my laptop was irreversibly damaged which meant that a replacement was necessary. No problem, I thought, after all all my files are backed up somewhere. All I needed to do was get the new laptop, restore files and continue with my development/school work.

**Git and Caching: A Case of forgotten files**

As any `hugo` and `R` user may be aware, one can quickly set up a website using `blogdown` and a theme from github (such as `ghostwriter` that I use here). To keep my webiste and repositories as simple as possible, I decided at some point to store some files only locally by running:

```
git rm --cached -r mysite/directory_to_keep_local

```

Hopefully, it should be clear by now how this might be problematic. On cloning the site's repository to my new laptop, I was suprised to find that some blog posts were only available in `html` and not `.md`/`.rmd` format. What this essentially meant was that:

* I could not edit these blog posts if I ever needed to someday

* These posts would be lost on rebuilding the site.

**Pitfalls and Possible Solutions**

With this in mind, I list what I think are rare but potentially problematic pitfalls in the `hugo`-`blogdown` workflow:

**HTML to Markdown Conversion**

The `rmarkdown` package has a great function `pandoc_convert` that can run `pandoc` and convert to any file format. While this is useful, it is mostly great for single `html` to `md` file conversion and the files sometimes require further editing.

I attempted to write a function that would solve this issue by taking a `.txt` file of filenames and converting these to `.md`. Unfortunately, I did not like the results and abandoned this script. Who knows, maybe someday I may need to revisit this problem. 

**Theme editing**

For aesthetic reasons, I prefer to have the site in a dark mode. Since I am currently doing this manually, I found the theme editing workflow a bit less obvious. To edit the `body` for instance, it is crucial that one edits the theme's `static/dist/site.css` (it may also be in some other location). Importantly, these edits may not be implemented if you also do not delete `public`. 



**Conclusion**

In my case, all this would have been unnecessary had I remembered to back up all files in different places and also pushed all changes to the remote repository. I do hope however that there was at least a thing or two that could be useful to your own blogging and/or hugo development. 

I am always happy to discuss further about these posts and programming in general. You can [contact me](https://nelson-gon.github.io) if you would like to have such discussions. 



**Thank you and Keep Building!**

