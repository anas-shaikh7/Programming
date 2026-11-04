// LOOPS

let a = [1, 2, 3, 90, 101]
for (let index = 0; index < a.length; index++) {
    const element = a[index];
    console.log(element)   
}
a.forEach((value, index)=>{
    // console.log(value, index, arr)
    console.log(value, index)
})

let obj= {
1: "A",
2: "B",
3: "C"
}
console.log(obj[8])

for (const value in obj){
    if (!Object.hasOwn(obj, value)) continue;
    const element = obj[value];
    console.log(element, value);
    // This is used to iterate the properties relevent to the the object and not the properties relevent to its prototype. 
    //If you try to access a property on an object and it’s not found in that object’s own properties, JavaScript will look “up the chain” in its prototype.If it’s not there, it keeps climbing through the prototype chain until it either finds the property or reaches null. --> undefined
    // child object is the object created by the user.    
}
// for (const element of object) {
for (const element of a) {
    console.log(element)
}
// A is a string. 
// Arrays are iterable by default, but plain objects are not. We can iterate over objects by converting their keys/values/entries into arrays.

let b = [1, 2, 4, 5, 6]
for (let index = 0; index < b.length; index++) {
    const element = b[index];
    console.log(element**2," : ", index)   
}
// Instead Use Map
