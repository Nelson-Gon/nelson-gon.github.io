+++
date = '2023-01-08'
slug = "noise-a-review"
title = "Noise: A flaw in Human Judgement reviewed"
author = "Nelson Gonzabato"
description = "A review of Noise"
tags = ["decisions", "neuroscience", "data-science", "game theory", 
"decision-theory", "bias", "noise"]
+++

**Introduction**

I am seated at Prague Castle on a slightly cold Saturday afternoon when a young
man approaches me and starts a conversation.

Person: Hi, what book are you reading?!
Me: Noise, erm Noise, a flaw in human judgement.
**We both laugh**
Person: You're reading noise? **more laughter**.
Me: Yes, it is a strange title I must agree.
Person: What is it about?

What follows is an attempt at describing what noise, the book is and a description
of a few lessons/concepts I have learnt from reading the book, but first...

**What is noise?**

I think it is important to stress that we discuss noise, in the statistical sense
as opposed to noise as we would describe for example a noisy stadium or noisy
train station. 

Statistically, noise can be defined as any unexplained variability that is often random. In plain terms, this statistical noise can include for example the
unexplained difference in repeated measurements of the length of a field. 

**Types of noise from the book**

In the book, different types of noise are described. System noise and occasion noise.

**System noise** is perhaps the kind of noise that we can more easily "notice" as it
often relates to internal or external sources of variability. The authors break
down system noise into level noise and pattern noise. 

**Level noise** can be thought of as the "unexplained" difference between a judge's
average "harshness" compared to the average "harshness" of all judges. In the
forecasting business, this can be thought of as the difference in the average 
predictions of a forecaster compared to the averages of other forecasters.

**Pattern noise**, on the other hand, can be thought of as the tendency of a specific 
judge to display specific patterns, resulting in differences in the judgement of
cases. In the stock market, a broker who has previously gained by backing non-conventional companies may display increased likelihood of investing in stocks
from companies that some may be more pessimistic about. Pattern noise can also
be temporary for example due to recent events. 

**Occasion noise**, like the name suggests, is variability due to random factors
that may have no direct relation with the issue at hand. For example, the book
presents studies linking judge leniency with the weather, with judges being more
lenient on nicer days (less hot days). This could also be linked to mood as [The temperature of emotions](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8174739) explores. Briefly, research suggests a link between the weather and emotion(s), and it is established that people tend to associate hotter days with negative emotions.

We have defined noise and broken it down into types, but what effect does noise have on our daily lives.

**Cascades and social influence**

Whether we realize it or not, we are all part of information cascades that are under heavy social influence. In organizations, these cascades can have profound effects on hiring processes, product approvals, and so on. 

In presenting information cascades, the authors highlight how influential persons within an organization can sway the decisions of other members and steer the decision process in completely different ways. Specifically, in a meeting for example, if a likable person happens to support hiring a given candidate, this may influence other members to agree with them leading to a loss of diversity in the decision process.

**The power of first vote, group think, and group polarization**

Related to the social influence described above is the power of the first vote. In studies on the popularity of music, it has been established that a song that gets early approval (first download for example or first listen) was more likely to go on to be the most popular as people tend to stick to what appears to be popular. Similarly at meetings, the person to speak first could influence the entire decision process by driving the decision process in their direction. This can be problematic as alternative ideas could be lost or early popularity could lead to other members to staying quiet so as to blend in or as a form of respect. 

**Wisdom of the crowd**

When a group of people is asked to provide an estimate, the individual values may be less accurate but when these are averaged, the overall estimate of the group will be much closer to the real value. This is because averaging these estimates "cancels" out the noise, following the concept of the mean squared error.

**One's a crowd**

When tasked with providing an estimate, an individual's first guess has been found to be far off than their subsequent guesses. It is thought that on subsequent guesses, individuals taken into account more information that they may have missed the first time around, leading to less noisy "predictions". This is the premise of the dialectical bootstrap. 

**Algorithms and decision making**

An even more interesting concept presented in the book, is the surprising result that modeling a "predictor" (you) with a very simple model does just as well as and often beats the performance of predictor.

If instead of having a judge make judgement, it is shown that a model of the same judge will often make better "judgement" as measured by correlation coefficients and percent concordance. With even more sophistication and data as machine learning models provide for example, the performance outweighs human judgement and is less noisy.

While the authors present the possibility of reducing noise via ML and statistical models, they provide caution about making such a conclusion. For example, as might be expected, a ML model using a biased data set will only exaggerate the bias. 


**Closing remarks**

At the time of this post, I have not yet completed the book but found it quite interesting and worth a read and hopefully this account can give someone else the motivation to check the book out. As always, let me know if you notice any flaws and or have any comments.

Thank you,
NelsonGon
Prague 08.01.2023




