// abstract classes cannot be instantiated 
abstract class Person{
    abstract fun raise():Any  
}

class Employee(age:Int, name:String, var current_salary:Int = 0,
var raise_by: Int= 1
):Person(){

init{
    var new_name = name.replaceFirstChar{it.uppercase()}.also{println("$it")}
    println("Name: $new_name Age: $age Current_Salary: $current_salary")
}


override fun raise(): Any{
    var new_salary = current_salary + (current_salary * raise_by / 100)
    println("Current salary raised by ${new_salary - current_salary} to $new_salary")
    return new_salary

}

}

fun main(){
var john = Employee(name = "tester", age = 25, current_salary = 20000, raise_by = 67)
john.raise()
}
