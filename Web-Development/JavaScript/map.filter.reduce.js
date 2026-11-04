
let b = [1, 2, 4, 5, 6]
// for (let index = 0; index < b.length; index++) {
//     const element = b[index];
//     console.log(element**2," : ", index)   
// }
// Instead Use Map
b.map((value)=>{
console.log(value**2)
})

// OR

let newb = b.map((element, index)=>{
    return element**2
})
console.log(newb)
// let newb = b.map((element)=>{
//     return element**2
// })

// Filters first account for a condition in the first array and then produce a new array based on true conditons.
let array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
let newa = array.filter((value)=>{
    if(value>5){
        return true
    }
    return false
})
console.log(newa)

// OR create a function and then call it in the filter method.
 const valuegreaterthan5 = (value)=>{
    if(value>5){
        return true
    }
    return false
 }
 console.log(array.filter(valuegreaterthan5))

// OR
console.log(array.filter(value =>{
if(value>5){
    return true 
}
return false
}))

let array2 = [1, 2, 3, 5]
let newarray2 = (a, b)=>{
    return a+b
}
console.log(array2.reduce(newarray2))


let c = [1, 2, 3, 4, 5]
let newc = (k, n)=>{
    return k+n
}
console.log(c.reduce (newc))

let d = "Shaikh-Sahab"
console.log(Array.from(d))
// Converts a string into an array