package main

import (
	"fmt"
	"net/http"
	)
// Comments

func main(){

	//standard printing, uses "fmt"
	fmt.Println("Hello World")
	//var, varibale name, type, and then the value
	var favNum int = 9
	//OR you can just do this! (Type inference like in Python and Ruby)
	secondFavNum := 10
	//lets print them out
	fmt.Println(favNum,secondFavNum)
	// you can perform arithmatic with varibales
	fmt.Println(favNum,"+",secondFavNum,"=", favNum+secondFavNum)
	//this is how constants are made
	const foreverNum int = 5

	var myName string = "Valentin Cantu"
	//prints the length of a String variable
	fmt.Println("my name is",len(myName),"characters long")

	var Boolean bool = true;
	fmt.Println(Boolean)
	//3 basic boolean operators
	fmt.Println("true && false is", true&&false)
	fmt.Println("true || false is", true&&false)
	fmt.Println("!true is", !true)

	//for loops are fun and easy!
	sum := 0
	for i := 50; i <= 100; i++{
		if i % 2 != 0 {
			sum += i
		}
	}
	fmt.Println(sum)

	// if/else statements are fun too!
	age := 21
	if (age >= 21){
		fmt.Println("You can drink!")
	}else{
		fmt.Println("Put that drink down!")
	}
	//Short circuit evaluation!
	newAge := 21
	if (newAge >= 21 || newAge >= 18){
		fmt.Println("You can drink!")
	}else if (newAge >= 18){
		fmt.Println("You can Vote")
	}else{
		fmt.Println("Put that drink down!")
	}

	//Arrays are simple!
	nums := [5]int {1,2,3,4,5}
	fmt.Println(nums)
	fmt.Println(nums[2])
	//slice of an array (exlusive) up to but not including
	numSlice := nums[3:5]
	fmt.Println(numSlice)
	//you can add up your array elements
	sumOfArray := 0
	for _, val := range nums {
		sumOfArray += val
	}
	fmt.Println(sumOfArray)
	//MAPS!!! theyre basically tuples
	Prolangs := make(map[string] string)
	Prolangs["Best Language"] = "Go and Python share first place "
	fmt.Println(Prolangs["Best Language"])

	//function calls
	fmt.Println("This simply returns the parameter *2 which is:",simpleReturn(2))
	//return two things; special to Go
	twoByTwo,TwoByFour := doubleReturn(2)
	fmt.Println("This returns 2*2 and 2*4 which is:",twoByTwo,"and",TwoByFour)

	//you can even declare fucntions inside the main!
	num5 := 5
	doubleNum := func() int {
		num5 *= 2
		return num5
	}
	fmt.Println(doubleNum())
	fmt.Println(doubleNum())

	//Creating a web server!
	http.HandleFunc("/something", handler)
   http.ListenAndServe(":8060", nil)
}
//declaring fucntions
func simpleFunc(){
	//do nothing
}
func simpleReturn(number int)(int){
	return number*2
}
//you can also return two things!
func doubleReturn(number int)(int,int){
	return number*2,number*4
}
//handler function for web server
func handler(w http.ResponseWriter, r *http.Request){
	fmt.Fprintf(w, "Hello Earth)
}
