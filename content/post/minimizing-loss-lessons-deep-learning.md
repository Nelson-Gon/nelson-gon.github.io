+++
date = '2020-09-14'
slug = "Minimizing Loss: Lessons From a Summer of Deep Learning"
title = "Minimizing Loss: Lessons From a Summer of Deep Learning"
author = "Nelson Gonzabato"
description = "Tips for your next deep learning project"
tags = ["python","deep learning","image-analysis","image-processing","computer-vision"]
+++

**Introduction**

While there is debate on how much similar deep learning(DL) operations are to the corresponding brain computations, these operations have been applied to several problems often generating excitement and sometimes unwarranted hype. Of all the DL applications, image processing has considerably matured and provided better results compared to traditional processes that relied on simple(r) kernel convolutions.

For the biomedical community, the UNet [algorithm](https://arxiv.org/abs/1505.04597) proposed by Ronneberger et al.(2015) has successfully been applied to several problems ranging from basic segmentation tasks to more complex tasks like cell tracking and cell cycle progress monitoring. I have had the opportunity to enhance a UNet [implementation](https://github.com/zhixuhao/unet) which I have now distributed as [cytounet](https://github.com/Nelson-Gon/cytounet). 

**AIMS**

In this blog entry, I summarise what I have learnt from this experience in the hope that this may help guide (fellow) students, researchers, or anyone with an interest in the application of DL to image processing problems. Below, I list what I think are the most important issues to think of when working on any DL or machine learning(ML) project.

**Lessons from my Experience with Deep Learning**

**Focus on Data Quality not Quantity**

One of the most common arguments against applying DL to biological problems is that it requires a lot of data. While this is generally true, I would like to argue that data quality is perhaps something better to optimise than quantity.

First, the age old acronym GIGO (Garbage In Garbage Out) is true for most DL/ML models. Even if you collected a very large dataset that was flawed, your model would only learn erroneous patterns which would waste time, resources(e.g. cells, reagents, etc).

Focusing on a small but high quality data set will lead to better results. I tested this while working on an embryo [dataset](https://bbbc.broadinstitute.org/BBBC030). This dataset had low contrast outlines which led to a constant loss and dice coefficient as seen [here](https://nbviewer.jupyter.org/github/Nelson-Gon/cytounet/blob/f1af3b16d4f49babe45f84b5bb29a6ee139e4814/examples/example_usage.ipynb). Even if I had collected more of this data, my model would still not learn anything except the same low contrast patterns. Using better outlines improved the training process and led to better [results](https://nbviewer.jupyter.org/github/Nelson-Gon/cytounet/blob/ff5ce0c2cc97e35baf1edacbc994661583200884/examples/example_usage.ipynb).

Second, it is now fairly common to do on-the-fly data augmentation. Again, increasing your dataset this way will only be useful if you use a good quality input to these augmenters.

Therefore, whenever in doubt, go for quality over quantity. It will always pay off!

**Focus on the bigger picture**

This should be straightforward but one would be surprised by how many DL applications exist whose problem is not really clear. Say you segmented some cars, why should anyone care about this? To paraphrase, why is it important that cars should be segmented and how can this fit into a business's goals and/or how does this advance the automobile industry?

It is therefore important that one understands the problem they are trying to solve. This is especially important in biology where the stakes are high(human life is at stake!). Models should not only be biologically plausible but also have clinical and/or research relevance.

**Know your metrics**

Related to understanding the problem you are trying to solve is understanding how your model works and why and how your metrics work. If you are minimising binary cross entropy for example, why is this the ideal metric for the task at hand? If you are using regularization, why have you chosen L2 or L1 and not something else?

A clear understanding of the above questions will boost your confidence and allow you to better explain your results in a way that the audience can understand.

**Document, Document, Document**

In the year 2020, it would be quite absurd for your model to not be reproducible simply because you failed to document your process. This is especially important for the data pre-processing steps where it is very easy to do this outside the main analysis and forget to report it for others. Documenting your work will also help you to reproduce your own results as a way to test that they are indeed reproducible.

To aid this process, I suggest that one utilize versioning control and always at least document all your functions and classes. The latter is something that has become a habit mostly due to my experience with CRAN submission and the `R` package development process. As of today, I unfortunately have not found an easy way to view past Notebook(`.ipynb`) versions on GitHub and will be happy to hear from you about some easy to use methods.

**Focus on the user**

This is mostly aimed at package/software developers. Do your users prefer a GUI or having flexibility via editing the source code? A common theme for DL projects is to publish them as main.py files. In my opinion, this grants the user very minimal flexibility unlike distributing a set of methods as a package.

I think a better approach would be to provide both runable scripts and a package. The former is something that I hope to do for [cytounet](https://github.com/Nelson-Gon/cytounet).

**Do not be afraid to fail**

Unfortunately(or not!), even if you have the best data and fully understand the problem, your model may never make it to production because it surprisingly does poorly on “real world” data. I think it is important to think of such models as a learning point about what works and learn from them to better understand how to build better industry/research relevant models.

You should aim to experiment and test out different ideas and share them either within your team or better with the “outside world”. This will provide critical feedback and hopefully open up new research ideas and collaborations.

**Conclusion**

I have learnt a lot working on [cytounet](https://github.com/Nelson-Gon/cytounet) this summer that a single post may not fully capture. If you are interested in what I have specifically learnt regarding [cytounet](https://github.com/Nelson-Gon/cytounet), please take a look at this [wiki](https://github.com/Nelson-Gon/cytounet/wiki) that tracks problems I met and how I solved them.

Thank you for reading and do not hesitate to [contact](https://nelson-gon.github.io/social/) me in case you have any issues with this post and/or general feedback on my work,

**Keep Building!**

**References**

https://arxiv.org/abs/1505.04597

https://github.com/Nelson-Gon/cytounet/wiki

https://nbviewer.jupyter.org/github/Nelson-Gon/cytounet/blob/ff5ce0c2cc97e35baf1edacbc994661583200884/examples/example_usage.ipynb

https://github.com/Nelson-Gon/cytounet

https://github.com/zhixuhao/unet

https://nbviewer.jupyter.org/github/Nelson-Gon/cytounet/blob/f1af3b16d4f49babe45f84b5bb29a6ee139e4814/examples/example_usage.ipynb

https://bbbc.broadinstitute.org/BBBC030