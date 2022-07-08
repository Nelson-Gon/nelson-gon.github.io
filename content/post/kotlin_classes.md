+++
date = '2022-07-07'
slug = "simple-look-at-kotlin-classes"
title = "Kotlin Classes for the Python Developer"
author = "Nelson Gonzabato"
description= "kotlin-classes-for-python-developers"
tags=["python","kotlin","fundamentals","open-source", "tutorial",
"reflection"]
categories = ["python", "open-source", "development", "kotlin"]
+++

# Introduction 

For anyone who has followed the tech scene and/or Android Development for some time, Kotlin, a language developed at [JetBrains](https://kotlinlang.org/docs/faq.html) is likely familiar. The language has also received a lot of media attention as the future of Android development, receiving [backing](https://insights.dice.com/2019/05/09/google-koltin-java-android/) from tech giant, Google. 

To understand why this is the case, I have recently started learning Kotlin mainly for fun and to see how well the language lives up to its hype (praise). So far, I have been impressed by a couple of features that I will summarise below. To do this, I will walk through a simple implementation of a `Search` class, from which `Binary` and `Linear` search subclasses inherit. As such, we will explore the concept of classes, inheritance, and a few unique Kotlin features that I found interesting.

# Defining a Kotlin Class 

As might be expected, we can create a class using the `class` keyword. For our walkthrough, we will create a class named `Search` as a `super` class. 


```kotlin 
abstract class Search{
    abstract fun search(): Int 
}

```

Let us break down this code. If you are coming from a language like `python` and are not familiar with Java like language, the most obvious difference in defining a class is the need to use keywords like `open`, `abstract`, `public`, etc. 

What exactly does `abstract` do? In Kotlin or Kotlin-like languages, an `abstract` class is used when we want for example to create a super class that we are not going to initialize directly. 

In this case, we create a super class `Search` and declare it `abstract`. We also define an `abstract` function for the actual search algorithm. By declaring `search` abstract, we can customize this for the specific search algorithm using the `override` keyword as we see below. It is interesting to note that we define a return type (`Int` here) in the `search` method. While this is optional, the default return type in Kotlin is `Unit` which can cause problems later on so I think it is better to be explicit about the return type.  


# Inheritance 

Alright, we now have a base class and are ready to define subclasses. To declare inheritance, we use the `:` operator as below. 

```kotlin
class LinearSearch(var lst: List<Int>, var target: Int):Search(){
    init{
        println("LinearSearch object created with list ${lst} of size ${lst.size}")

    }
    override fun search(): Int {
        return lst.indexOfFirst {it == target}
    }
}
```


In the above code, we create a `LinearSearch` class and use a [primary constructor](https://kotlinlang.org/docs/classes.html) which is defined as being part of the class header. A secondary constructor on the other hand is defined within the class body and bears the keyword `constructor`. 

For our `LinearSearch` above, we have defined an `lst` var in the constructor to hold our integer list and target to specify the target element of the list. 

`init` is similar to python `__init__` and here we define what happens on instance creation. Here, we use syntax similar to python f-strings to print the list and its size (length). 

**Null Safety**

[Null safety](https://kotlinlang.org/docs/null-safety.html) is a broad and important topic that ensures that values are not null when they shouldn't be. In our init, we could have used `lst.!!size` to ensure that size is always available but in this case this is redundant. 

**Overriding methods**

As mentioned briefly above, we can override a function with the `override` keyword. For the linear search algorithm, we are only interested in linearly finding the target so we use a built-in function `indexOfFirst` to do this. However, we could have written this from scratch. This line also introduces the `{...}` map-like syntax. 

Here, we are mapping every `it`eration within the list to check if it is equal to our target and return the index of the first true element.

The above briefly explains inheritance and we can proceed to implement a binary search. 

```kotlin

class BinarySearch(var lst: List<Int>, var start:Int = 0, 
var end:Int = lst.size - 1, 
var target:Int):Search(){
    var new_list = lst.sorted()
    init{
       println("BinarySearch object created with list $new_list of size ${new_list.size}")  
    }

    override fun search():Int{   
    var mid_index = (start + end) / 2 
    while(start <= end){
        
        if(new_list[mid_index] == target) return mid_index
        start = if(new_list[mid_index] < target) mid_index + 1 else start
        end = if(new_list[mid_index] > target)mid_index - 1 else end  
    }
    // If not found 
    return -111
    }
}

```

The details of the algorithm are available [online](https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search). Briefly, a binary search sorts an input list, and depending on the start and end indices defined compares the target value to the middle value of the sorted list and if these are equal returns the index of the middle value. Otherwise, the start and end points are redefined depending on the whether the target is greater than or less than the middle value. 

For our inheritance story, we note that within `BinarySearch`'s primary constructor we can create new variables (parameters) and also directly perform manipulations on these variables. For example here we set the initial end value to one less than the length of the input list. 

# Running the code 

Finally, we can encapsulate our code in a `main()` call and see what happens. 

```kotlin 
fun main(){

var my_list = listOf(25, 89, 56, 83)

var bin_search = BinarySearch(lst = my_list, target = 56)

var lin_search = LinearSearch(lst = my_list, target = 56)

println("Target ${bin_search.target} found via a binary search at index: ${bin_search.search()}")

println("Target ${lin_search.target} found at index: ${lin_search.search()}")
}
```

This yields the following at the console. Do you see any immediate difference in the algorithms based on the output from our `init`?  

```shell
BinarySearch object created with list [25, 56, 83, 89] of size 4
LinearSearch object created with list [25, 89, 56, 83] of size 4
Target 56 found via a binary search at index: 1
Target 56 found at index: 2

```

# Conclusion

Kotlin is an interesting language that simplifies the process of android app development by eliminating a lot of the boilerplate code that makes Java appear less readable. Admittedly, this blog post does not cover everything there is to know about Kotlin classes. For example `interface`s, `companion object`s, and other related concepts are not illustrated here. I hope however that this post gives more confidence to those coming from python and looking to work with Kotlin in how much similar to python the language is. 

As always, I am happy to talk about this and other coding issues either on Twitter or on my email.

Thank you and keep bulding.

Nelson 

**Further Reading**

- https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search

- https://kotlinlang.org/docs/classes.html

- https://kotlinlang.org/docs/interfaces.html
