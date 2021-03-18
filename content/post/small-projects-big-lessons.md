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
worth the time. However, our experiences are unique and offer a unique perspective even on topics that may have been read and written about countless times.


**When a problem sparks an idea**

A month or so ago, I was ready to submit updates to the `R` packages [manymodelr](htpps://nelson-gon.github.io/manymodelr)
and [mde]((htpps://nelson-gon.github.io/manymodelr)) and thought the process would go just as smooth as it always does, if you ignore the usual issues with fixing tests and unidentified bugs that is. Surprisingly, I was met with `CRAN` notes about outdated website links which thankfully developers at [r-lib](https://github.com/r-lib) had figured a way to solve, and that too very efficiently. 

Being the learn-by-doing person that I am, I decided that it was probably a good idea to start a small project that would aim to do what `urlchecker` (from `r-lib`) does, but in `python`. This led to the birth of an idea - `urlfix`, conveniently named to reflect the idea that we aim to fix broken web links (URLs). An idea is not really an idea unless it has been put out there, so a tweet "advertising" this new project was made.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">After struggling with <a href="https://twitter.com/hashtag/url?src=hash&amp;ref_src=twsrc%5Etfw">#url</a> redirects for <a href="https://twitter.com/hashtag/rstats?src=hash&amp;ref_src=twsrc%5Etfw">#rstats</a> CRAN submissions, I decided to work on urlfix, a <a href="https://twitter.com/hashtag/python?src=hash&amp;ref_src=twsrc%5Etfw">#python</a> package to fix outdated urls, inspired by r-lib&#39;s urlchecker. Currently beta, please provide ideas and criticism. Thanks! <a href="https://t.co/VW7WIAWOJw">https://t.co/VW7WIAWOJw</a></p>&mdash; NelsonGon (@bionelsongon) <a href="https://twitter.com/bionelsongon/status/1358420756682702853?ref_src=twsrc%5Etfw">February 7, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


**Learning big by building small**

When I initially had this idea, I thought it would take me a week or so and did not imagine how relatively complex it would become, one month later. For starters, I
intended to simply "grep" for links in Markdown files (since I use Markdown mostly), visit these links, and finally update them.

It has been a fun learning experience so far and below I list some of the lessons  from working on `urlfix`.

**Collaborating with open-source developers**

I was blown away by how much attention this got compared to other projects I have worked on. The project has now had six contributors each contributing something useful be it in the form of fixing issues, reporting bugs, or ensuring tests work as expected.  

This teamwork has given me a chance to see other developers' thought processes via code review and discussions. This is something that I think someone who may not be working as part of a team in a professional setting gains from building open source software, however small they may be. 

**Speaking of code review...**

When reviewing some of the code, I realized that I took more time to think of development best practices like efficiency which I would probably have ignored had I written most of the code alone. For example in one case, I realized that we had double loops which was not really efficient if one wanted to replace 700,000 broken links for example. 

Another important lesson from code review has been that sometimes bugs may be introduced unintentionally and if not enough tests are done could lead to a lot of wasted time in trying to figure out what exactly went wrong. Other developer best practices I have got to learn include branching out from main for features instead of having just main and dev, and setting a suitable threshold for code coverage workflows.  

**Efficiency or lack thereof**

I recently talked to a senior developer and was asked about concepts like scaling, multi-threading, and containerization which admittedly I have not had much exposure to beyond reading about them. As I thought more about how to make this small project even better, learning about parallelism, asynchronous calls, and multi-threading is something that I have now put on my todo list. This is important even beyond this small project because if you have a pipeline that is reading millions of lines of data, you do not want a user to spend an entire day waiting for results. I intend to look at the `python` `async` and `threading` packages to see how these could further improve this relatively small project.


**Tests, tests, and more tests**


Often when one is working on a project, it is easy to imagine that features will work as expected. As I have come to learn, a program will almost always fail in one way or another. For `urlfix`, one of the earliest failures was that although we could replace outdated links, we lost anything that was not a link in the process.
This was only brought to my attention by an issue which allowed me to fix this bug and write more comprehensive tests. 

The takeaway from this is that even tests should not simply test for some expected return value but should instead at least test each part of the process leading to the final return value. 


**Conclusion**

It will be interesting to see how far the `urlfix` project goes but for now I can only predict that the lessons I have learned from this small project will be beneficial to me as a developer going forward. This has been a very short reflective post and hopefully it provided some inspiration for someone else who may be looking to build something but thinks it is too trivial or too small to spend time on.

As always, if you would like to contribute to [urlfix](https://github.com/Nelson-Gon/urlfix) or any of the other [projects](https://nelson-gon.github.io/projects), please feel free to contact me or open issues at the specific project, whichever may be easier.


**Thank you and Keep Building!** 















 