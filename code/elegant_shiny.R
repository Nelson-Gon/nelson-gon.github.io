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
