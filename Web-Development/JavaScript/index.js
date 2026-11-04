// Variable is a named memory location(name: you assign it a name(variable name)
// Var is function scooped
// Not accesible outside the function 0 it is function scopped only
// Resassigment of a let variable is possible
let a = "Hello Mate"   // Initializing process
a = "kako"
console.log(a)

const b = "HELLO world"
// b = 20 ERROR 
console.log(b)
let $10 = 111
console.log($10)
// Camel Case creation of vsariable names: ageOfAnas -- rules: the first word must be lowercase, the second and the third variable must have their initial letter capitalized.
// let function = "hello" Error -- reservered variables cannot be kept as a vvariable name
console.log(typeof a, typeof $10)
let ageOfGuy = 90
console.log(ageOfGuy, typeof ageOfGuy)
let AGEOFPEOPLE = "unknown"
console.log(AGEOFPEOPLE, typeof AGEOFPEOPLE)
let what_is_my_age = 17
console.log(what_is_my_age)
// let house-number = "I dont remember"; Not valid in JS because it is interpreated as a minus sign used for subtraction in JS