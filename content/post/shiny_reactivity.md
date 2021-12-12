+++
date = '2021-12-12'
slug = "shiny-reactivity"
title = "Shiny Modals, Performance, Reactivity, and Observers."
author = "Nelson Gonzabato"
description = "How to speed up your shiny app"
tags = ["user-interface","github", "r", "git", "programming", "open-source", "missing-data", "dashboards", "shiny"]
+++

Since my last [post](https://nelson-gon.github.io/19/07/2021/shiny-lessons/) almost five months ago, a lot has changed both in my personal and professional life. On a personal note, I finally moved to the beautiful and magical city of Prague, walked the famous Charles Bridge, enjoyed the clock show at the lovely Old Town Square, tried Czech dumplings, and enjoyed Kofola. Professionally, I have worked more with R's shiny system as part of my job, learning a lot in the process. 

This post aims to summarize a few tips and tricks that have upped my shiny game. In a slight change of style, I will include a sample application to demonstrate the points raised. This app can be browsed at https://nelson-gon.shinyapps.io/sampleapp/ 

**Require, require, require**

Perhaps one of the most underrated features/functions of `shiny` is `req`. Let us say you wanted to build an app that takes a user's CSV file, prints it on read and filters only numeric columns displaying these on the next panel. The app's UI could look something like:

```
ui <- navbarPage(
  tabsetPanel(
    tabPanel("Input Data",
  sidebarLayout(
    sidebarPanel(
      fileInput("user_csv", label="CSV File")
      
    ),
    mainPanel(
      dataTableOutput("disp_input")
    )
  )),
  tabPanel(
    sidebarLayout(
      selectInput("col_name",
                  "Column Name",
                  choices = c("col_1","col_2")
        
      ),
      mainPanel(
       dataTableOutput("filtered_only") 
      )
    )
  )
))

```

While writing this blog post, I noticed errors in the above code. Do you spot them? As a test, you could try to see any errors before proceeding with the following section.

If you took, the test, you should have noticed that our UI code, fails to specify a title in the second `tabPanel`. This will lead to an unexpected display. We correct this below. For stylistic reasons, I have also used a `navbarPage` instead:

```
ui <- fluidPage(navbarPage("Simple App",
                    id="super_simple_app", 
    tabPanel("Input Data",
  sidebarLayout(
    sidebarPanel=sidebarPanel(
      fileInput("user_csv", label="CSV File")
      
    ),
    mainPanel=mainPanel(
      dataTableOutput("disp_input")
    )
  )),
  tabPanel("Filtered Data",
    sidebarLayout(
      sidebarPanel=sidebarPanel(
      selectInput("col_name",
                  "Column Name",
                  choices = c("col_1","col_2")
        
      )),
      mainPanel=mainPanel(
       dataTableOutput("filtered_only") 
      )
    )
  )
))

```

Now that we have a UI, we can write code for the server. 

```
server <- function(session, input, output){
  
 input_data <- reactive(
   read.csv(input$user_csv$datapath, header=TRUE)
 )
 
 output$disp_input <- renderDataTable(input_data(),
                                      options = list(
                                        pageLength = 25
                                      ))
  
}

```

When we run this app with `shinyApp(ui, server)`, we see first that there is an error immediately when we run the app. The specific error being:

>'file' must be a character string or connection

Why would this be the case? Meet `req`. I talked about `req` in the previous post but not that extensively. To re-emphasize, one should always `req`uire a key input to ensure that other functions/outputs that depend on this part of the app being present do not run until it exists. We therefore need to change our server code to:

```
 input_data <- reactive(
   read.csv(req(input$user_csv$datapath), header=TRUE)
 )
```

Excellent, we have now made our code more elegant with respect to requiring that required data exists. An alternative way to `validate` input is to do it directly on the reactive object. I must admit that it was surprising to learn that this was valid. We therefore could instead have changed the output part to:

```
output$disp_input <- renderDataTable(req(input_data()),
                                      options = list(
                                        pageLength = 25
                                      ))
```

You may have noticed that the `server` did not include any code for the second panel. This introduces us to the next part of this blog post.

**updateSelectInput vs renderUI**

As a new shiny user/developer, I was happy to learn that one could generate a UI within the server. For our app, our UI code could have looked like:

```
uiOutput("col_names")
```

In the server, we could then update our target names (only numeric columns) as follows:

```
only_numeric <- reactive(
   Filter(is.numeric, input_data())
 )
 output$col_names <- renderUI(selectInput(
   "col_name", "Column Name",
   choices = names(only_numeric())
 ))
```

The above works as we expect, except it is extremely slow when time is of the essence (think analyzing very large datasets). This is because the UI would have to be rendered each time which is inefficient. This is well explained in the performance [chapter](https://mastering-shiny.org/performance.html) of Mastering Shiny. 

Instead, we should change our code to use `selectizeInput` (this is useful where you have thousands  of column names) in the UI and `updateSelectizeInput` at the server side. We then have:

```
# ui part
selectizeInput("col_name",
                   "Column Name",
                   choices = c("col_1","col_2"))
```

For the server side, you may have noticed that our `server` function includes a `session` argument. This is useful in cases like this, we need to update our inputs based on session changes. 

```
 observe(
   updateSelectizeInput(session, "col_name",
                        "Colum Name",
                        choices = names(only_numeric()))
 )
 
```

We also use `observe` to observe any changes and update accordingly. An alternative could be to use a button that confirms we need to update our inputs. In this case, we would use an `observeEvent` or `eventReactive`. The former will change for every click. The latter has the added advantage that it will allow us to programmatically access changes and use them elsewhere if we desire. 

Let us add a button that confirms user input after uploading a file. I also use this button to illustrate `modals` (think of them as pop ups) and `eventReactive`

Our UI button

```
actionButton("confirm_in","Confirm",
                   icon = icon("check"))

```

We now update our `server` based on this button. Specifically we show a `popup` (modal) once a user confirms input and also only read the data after this confirmation has occured. Granted this may waste a user's time but it is also sometimes helpful to ensure users do not make mistakes.

Our updated server. 


```
 observeEvent(input$confirm_in,
              showModal(
                modalDialog(
                title = "Thank you for confirming!" 
                )
              )
              
 )
  
  input_data <- eventReactive(input$confirm_in,
    read.csv(req(input$user_csv$datapath), header=TRUE)
  )
  
```

With these concepts now hopefully clearer, we can update our server code to also show our filtered data, completing our simple yet elegant app. 

```
 output$filtered_only <- renderDataTable(
   only_numeric(), options= list(pageLength = 25)
 )

```

Our full app is then:

```

library(shiny)

ui <- fluidPage(navbarPage("Simple App",
                    id="super_simple_app", 
    tabPanel("Input Data",
  sidebarLayout(
    sidebarPanel=sidebarPanel(
      fileInput("user_csv", label="CSV File"), 
      actionButton("confirm_in","Confirm",
                   icon = icon("check"))
      
    ),
    mainPanel=mainPanel(
      dataTableOutput("disp_input")
    )
  )),
  tabPanel("Filtered Data",
    sidebarLayout(
      sidebarPanel=sidebarPanel(
      selectizeInput("col_name",
                   "Column Name",
                   choices = c("col_1","col_2"))
        
      ),
      mainPanel=mainPanel(
       dataTableOutput("filtered_only") 
      )
    )
  )
))

server <- function(session, input, output){
  

 observeEvent(input$confirm_in,
              showModal(
                modalDialog(
                title = "Thank you for confirming!" 
                )
              )
              
 )
  
  input_data <- eventReactive(input$confirm_in,
    read.csv(req(input$user_csv$datapath), header=TRUE)
  )
 output$disp_input <- renderDataTable(input_data(),
                                      options = list(
                                        pageLength = 25
                                      ))
 only_numeric <- reactive(
   Filter(is.numeric, input_data())
 )
 observe(
   updateSelectizeInput(session, "col_name",
                        "Colum Name",
                        choices = names(only_numeric()))
 )

 output$filtered_only <- renderDataTable(
   only_numeric(), options= list(pageLength = 25)
 )
  
}

shinyApp(ui, server)


```

You can also view the code at https://github.com/Nelson-Gon/nelson-gon.github.io/blob/78ce2a8a09e2046d85c4e5859d9111d6b2de80eb/code/elegant_shiny.R and try out the app at https://nelson-gon.shinyapps.io/sampleapp/.  

As a further step or challenge/way to review for yourself, you could try to do the following:

* Show the second tab only after the first tab contains data.

* Show helpful error messages when a user inputs non CSV files.

* Add a fun plot that takes advantage of the `selectInput` on tab 2. This currently does nothing. 


If you made it to the end, thank you so much for reading. I enjoy writing about R and helping others get better at R programming/data analysis. If this helped, please share with someone else and or provide any other feedback.

Thank you,

NelsonGon

In Prague, 12.12.2021

**References**

- https://mastering-shiny.org/performance.html
