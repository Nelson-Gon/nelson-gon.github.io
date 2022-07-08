abstract class Search{
    abstract fun search(): Int 
}

class LinearSearch(var lst: List<Int>, var target: Int):Search(){
    init{
        println("LinearSearch object created with list ${lst} of size ${lst.size}")

    }
    override fun search(): Int {
        return lst.indexOfFirst {it == target}
    }
}

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



fun main(){

var my_list = listOf(25, 89, 56, 83)

var bin_search = BinarySearch(lst = my_list, target = 56)

var lin_search = LinearSearch(lst = my_list, target = 56)

println("Target ${bin_search.target} found via a binary search at index: ${bin_search.search()}")

println("Target ${lin_search.target} found at index: ${lin_search.search()}")
}




