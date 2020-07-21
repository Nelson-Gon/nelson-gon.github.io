+++
title = "2020 07 21 R Loops for the Python Programmer"
description = ""
author = "Nelson Gonzabato"
date = 2020-07-21T23:35:25+08:00
tags = ["r", "python", "loops", "tutorials", "beginner", "novice"]
draft = true
+++

**TLDR**: Whenever possible use vectorised alternatives instead of loops, `seq_along` and `1:length` will be handy when looping through data.

The R vs Python debate is one that has stood the test of time. Thousands of articles and tweets have been made that aim to argue for the use of one language over another. Fortunately for the reader, this post is not aimed at justifying the use of one language. 

On the contrary, as someone who is fairly proficient in both languages, I thought it would be nice to write about key differences between loops in R and python. This post assumes basic R and python proficiency and/or general interest in the same.

**Loops in python**

It has been argued that `python` is close to pseudocode in the sense that one often can write what they think of and it just works, well sort of. For our example, will use an array of `range(5)`.


```

import numpy as np
my_arr = np.arange(5)

```

What we now want to do is fairly simple: replace each value with the value multiplied by 5. This can be written as follows:


```

for i in my_arr:
    my_arr[i] *= 5

```

Our result should show that our values have been updated:


```

my_arr

Out[17]: array([ 0,  5, 10, 15, 20])

```

**R is picky, or is it?**

So far all good(I think). Now, if you're coming from `python` to `R`, you would typically try to reproduce the above as follows:


```

my_arr = 0:4
for(i in my_arr){
  my_arr[i] = my_arr[i] * 5
}


```

To your surprise, `my_arr` only gets updated at the second value(indexing starts at 1 in `R` not 0):


```

my_arr

[1]  0  5 10 15  4

```

**Meet seq_along**

The reason the above fails is to do with the fact that `for` loops in R are not vectorised. This simply means that you're looping over the first value alone and not the entire "array". 

To get the desired effect, you would need to use either `seq_along` or `1:length` to loop over the entire vector("array"). What you need would then be:


```

my_arr = 0:4
for(i in seq_along(my_arr)){
   my_arr[i] = my_arr[i] * 5
 }

 my_arr
[1]  0  5 10 15 20

```

Using `1:length`:

```
my_arr = 0:4
for (i in 1:length(my_arr)){
   my_arr[i] = my_arr[i] * 5
 }
 my_arr
[1]  0  5 10 15 20

```

**No loops, please**


While loops are great, there is often a vectorised solution to do what you would like to do, just like most operations are vectorised in `numpy`. 

Here are a few ways to achieve the same without using explicit loops:

For this simple example, you don't need loops at all:


```

0 : 4 * 5

0  5 10 15 20

```

This is similar to what you would do in `python`:

```

my_arr *= 5

array([ 0,  5, 10, 15, 20])

```

For more complex examples(I should think of a better example next time), things are not always as straightforward. 

This is an overkill for this task but `do.call` is an equally useful function for the task.

```

do.call("*", list(0:4,5))

[1]  0  5 10 15 20

```

Using `Reduce`:

```

Reduce("*", list(0:4,5))

[1]  0  5 10 15 20

```

Using the `apply` family:


```

sapply(0:4,function(x) x* 5)

[1]  0  5 10 15 20


```

It would be overambitious to try and list all possibilities. The key takeway is that one should often try to use vectorised implemenations and if loops are needed, one should always remember that these are not vectorised in R.

Thank you for reading. Hopefully, I will come up with better examples in the future.

