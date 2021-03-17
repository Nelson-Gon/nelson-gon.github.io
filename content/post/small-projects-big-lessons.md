+++
date = '2021-03-17'
slug = "small-projects-not-so-small-lessons"
title = "Growing big by building small."
author = "Nelson Gonzabato"
description= "Small Open Source Projects, Not so Small Lessons"
tags=["python","dev-tools","developer","open-source", "teaching", "projects",
"reflection"]
categories = ["python", "open-source", "development"]
+++

**Why build when you can simply read?** 

The importance of learning as one builds has been echoed so many times in the 
open-source development world that another article on the same might seem not 
worth the time. However, our experiences are often unique and offer a unique perspective even on topics that have been read and written about countless times.


**When a problem sparks an idea**

A month or so ago, I was ready to submit updates to the `R` packages `manymodelr`
and `mde` and thought the process would go just as smooth as it always does, if you ignore the usual issues with fixing tests and unidentified bugs that is. Surprisingly, I was met with `CRAN` `NOTES` about outdated website links which thankfully developers at `r-lib` had figured a way to solve, and that too very efficiently. 

Being the learn-by-doing person that I am, I decided that it was probably a good idea to start a small project that would aim to do what `urlchecker` (from `r-lib`) does, but in `python`. This lead to the birth of an idea - `urlfix`, conveniently named to reflect the idea that we aim to fix broken web links (URLs). An idea is not really an idea unless it has been put out there, so a tweet "advertising" this new project was made.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">After struggling with <a href="https://twitter.com/hashtag/url?src=hash&amp;ref_src=twsrc%5Etfw">#url</a> redirects for <a href="https://twitter.com/hashtag/rstats?src=hash&amp;ref_src=twsrc%5Etfw">#rstats</a> CRAN submissions, I decided to work on urlfix, a <a href="https://twitter.com/hashtag/python?src=hash&amp;ref_src=twsrc%5Etfw">#python</a> package to fix outdated urls, inspired by r-lib&#39;s urlchecker. Currently beta, please provide ideas and criticism. Thanks! <a href="https://t.co/VW7WIAWOJw">https://t.co/VW7WIAWOJw</a></p>&mdash; NelsonGon (@bionelsongon) <a href="https://twitter.com/bionelsongon/status/1358420756682702853?ref_src=twsrc%5Etfw">February 7, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


**Learning big by building small**

When I initially had this idea, I thought it would take me a week or so and did not imagine how relatively complex it would become, one month later. For starters, I
intended to simply "grep" for links in Markdown files (since I use Markdown mostly), visit these links, and finally update them.

Like most of the projects I have worked on, the more I build, the more ideas I can come up with. I have enjoyed working on `urlfix` for the following reasons.

**Collaborating with open-source developers**

I was blown away by how much attention this got compared to other projects I have worked on. The project has now had six contributors each contributing something useful be it in the form of fixing issues I had planned to work on or ensuring that tests run as expected. 

This teamwork was useful because it gave me a chance to see other developers' thought processes via code review and discussions. This is something that I think someone who may not be working as part of a team in a professional setting gains from building open source software. 

**Speaking of code review...**

When reviewing some of the code, I realized that I took more time to think of things like efficiency which I probably have ignored had I written most of the code solo. For example in one case, I realized that we had double loops which was not really efficient if one wanted to replace 700,000 broken links for example. 

Another important lesson from code review was that sometimes bugs may be introduced unintentionally and if not enough tests are done could lead to a lot of wasted time trying to figure out exactly what went wrong. I think that only by building projects can one appreciate the importance of developer best practices like not pushing to main, using continuous integration, or setting a given threshold for code coverage reports. 

**Efficiency or lack thereof**

I recently talked to a more senior developer and was asked about concepts like scaling, multi-threading, and containerization which admittedly I have not had much exposure to beyond reading about them. As I thought more about how to make this small project even better, learning about parallelism, asynchronous calls, and multi-threading is something that I have now put on my todo list. This is important even beyond this small project because if you have a pipeline that is reading millions of lines of data, you do not want a user to spend an entire day waiting for results. I intend to look at the `python` `async` and `threading` packages to see how these could further improve this relatively small project.


**Tests, tests, and more tests**


Often when one is working on a project, it is easy to imagine that things work as expected. As I have come to learn, a program will almost always fail in some way or another. For `urlfix`, one of the earliest failures was that although we could replace outdated links, we did not have the text between the links reappearing in the replacement files. This also means that one should be specific about the nature of tests one writes. Tests should ideally capture all processes and expected results, even for small projects. 


**Conclusion**

It will be interesting to see how far the `urlfix` project goes but for now I can only predict that the lessons I have learned from this small project will be beneficial to me as a developer. This has been a very short reflective post and hopefully it provided some inspiration for someone else who may be looking to build something but thinks it's too trivial or too small to spend time on.

If you would like to contribute to [urlfix](https://github.com/Nelson-Gon/urlfix) or any of the other [projects](https://nelson-gon.github.io/projects), please feel free to contact me or open issues at the specific project, whichever may be easier.



**Thank you and Keep Building!** 















 