+++
date = '2021-07-19'
slug = "shiny-lessons"
title = "Building User Interfaces with R's Shiny"
author = "Nelson Gonzabato"
description = "Shiny Lessons from a shiny R project."
tags = ["user-interface","github", "r", "git", "programming", "open-source", "missing-data", "dashboards"]
+++

**Update 22nd September 2021**

The dashboard/app referred to in this blog post can now be tested and used in a browser by visiting https://nelson-gon.shinyapps.io/shinymde. 

**Introduction**


Admittedly, it has been a long time since my last blog entry. Between that time, I have been working on a number of [projects](https://nelson-gon.github.io/projects) that I maintain over at my [GitHub](https://github.com/Nelson-Gon) and more importantly, I was working on my final year thesis and finalizing my undergraduate studies. 

I have also been reading a few programming books, more recently deciding to delve into shiny app development after a brief tour of [Mastering Shiny](https://mastering-shiny.org).

**Introducing shinymde**

For those who may have come across my work, you may be aware of an R package that I developed to ease the process of missing data exploration. This package, [mde](https://nelson-gon.github.io/mde) may be useful to those who are more into writing code and find it faster than using graphical user interfaces (GUIs). 

That said, GUIs can have a number of advantages including but not limited to increasing access to the R programming language to those who may feel intimidated with command-line like interfaces or who may not have decided to go full programmer (yet). GUIs may also be more visually appealing especially if enough time and effort is taken into their beautification. Also, for some users, it may be easier and faster to simply click on an interface than simply writing a bunch of commands. 

The cons and pros for GUIs may require their own independent post and are most likely biased by personal choice. However, I do believe in providing users with choice and for this reason have decided to develop [shinymde](https://github.com/Nelson-Gon/shinymde) that under the hood calls `mde` functions with the added advantage of being simpler to use for anyone who may want to explore missingness in their dataset. 

**What's so good about shiny?**

If one were given shiny code to review, their first thought would probably be about how overwhelmingly complex such code might appear. Even for the more experienced R programmer, looking at `shiny` code may feel extremely overwhelming unless one has prior `shiny` experience. 

Like most aspects of programming, as one goes from a simple "Hello World" program to more complex programs, one is more likely to enjoy the hurdles and challenges as they show up. This in my opinion is even truer for `shiny` given that one can immediately get visual feedback which in turn can lead to excitement and courage to try even more complex features. 

**What is there to learn?**

There is still much more for me to learn about `shiny` but so far here are a few things I have loved about developing `shinymde`:

**Meet conditionalPanel**

* It is surprisingly easier to do complex JavaScript/Web development tasks thanks to the plethora of shiny extensions. One feature that I particularly struggled with was hiding a given part of the UI, conditionally. If you run the `shinymde` [app](https://github.com/Nelson-Gon/shinymde), you might notice that the "Input Data" tab can conditionally ask for a file path or an inbuilt dataset (at the time of writing). This relatively simple task can be achieved by either using `conditionalPanel` from `shiny` or `hide`, `toggle` or `hidden` from `shinyjs`. 

Initially (even after reading the documentation), the `conditionalPanel` syntax was not one that I could readily wrap my head around. If you are familiar with `python`, you may be familiar with the "dot syntax" of accessing elements/items i.e. `[list].item` or accessing module methods for instance. This is the kind of syntax that `conditionalPanel` uses to conditionally show a panel such that 

```shell
# some conditional ui part
conditionalPanel(condition="input.input_element=='target_condition'", selectInput(...))
```


Another source of confusion, at least for me, was that in accessing input elements, one uses `$` as in `R` syntax. Finally, I did expect to have the `selectInput` (or whatever function) show up before the condition argument. 

After getting my head around this syntax, it was exciting to see that the panel did conditionally show up as intended. 

**shinyjs, a powerful shiny extension**


* In my search for an easy way to conditionally hide elements I came across `shinyjs`'s `hide`, `hidden`, and `toggle` which respectively hide, initially hide, and turn off/on selected parts of the user interface based on shiny tags. These are fairly straightforward and for the most part work as one may expect without much hassle.


**...Dynamically rendered user interfaces and reactivity**

* Another component of `shiny` programming is that one can dynamically render a user interface for example using `renderUI`, `renderPlot`, and so on. Another reactive function, `reactive` is also handy especially if you would like to use a given input in multiple places as the case may be for input datasets.

At the time of writing, I found issues with `shinyjs::hide` and `shinyjs::show` or `toggle` not working when wrapped under certain `reactive` pieces of code. Regardless, reactivity is an interesting `shiny` feature that I have so far found great to work with. 


**selectInput and selectsize: what if you need a null init?**

* The more one builds, the more features of a programming language or framework one meets. To allow users to select input, one can use `selectInput` or `selectsize` and a list of choices. For the most part, this may be sufficient until one needs to set the initial value in `selected` to `NULL`. 

For `mde`, I did write some code that would only work if only one but not two arguments were set to `NULL`. It was therefore necessary that in `shinymde`, I had a way of setting one of these to `NULL` initially. At the time of this post, it is unfortunately not sufficient to set `selected` to `NULL`. Instead, one should set `selected` to `FALSE`, `selectsize` to `FALSE` and providing a numeric to `list` in my case just 4 since I had only four options. This is a neat workaround although visually `selectsize` looks more appealing.   

**Themes, themes, and more themes**

* To make a standout dashboard, it may at some point be necessary to go beyond the standard `shiny` layout and get more creative either by writing custom bootstrap, javascript, or editing css tags. An even easier and quicker way to create themes is to use `bslib` which provides a way to theme a shiny app by providing a bootswatch theme to the theme argument in the `ui` part of the code. 

**observeEvent, observe,req, and observers**


I have not looked a lot into the `observe` family but these, like their name suggests, provide a simple way to achieve a certain task only after some other tasks happens. In essence, they are like a switch that is only on after some other switch is on. They also seem related to `req` which in my brief usage seems to halt execution until something happens i.e. tasks are suspended until a users performs some action. 


**Conclusion**

Shiny apps provide an easy way to increase access to programming and general data analysis. They also are a good way to share data in real time (for example through vaccination rate trackers) if published. I have briefly outlined some lessons and observations from my experience developing [shinymde](https://github.com/Nelson-Gon/shinymde) that should hopefully give you something to think about or inspire you to build your own shiny app if you haven't already.

As always, I am excited to receive feedback on these posts or projects.

Thank you and keep building,

Nelson 






