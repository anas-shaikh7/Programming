let word = {
    plasuible: "Reasonable/believable",
    optimistic: "hopeful/positive",
    yearning: "Long desire",
    Susceptible: "prone to something",
    homogenus : "similar"
}
console.log(word)


let k = "200"
let l = 200
// if(k=100 && l="200"){ ----- wrong because = is not a compariosn operator and when using conditionls we compare using == or ===
if(k==100 && l=== "200"){
    console.log("OK")

}

else{
    console.log("not ok")
}

// if(!(k==300)){ This will check the whole condtion

// if(!k==300){ this will first check !k which means !100 which is actually true but ! will make it false, now if(false == 300) --- the false becomes 0 -> if(0 == 300) -- this condition is not true hence else runs  
if(!(k==300)){ 
    console.log("yes")
}
else{
    console.log("no")
}



let o = 22
let r = 43
if(o>r){
console.log("hello mate")
}

if(o-r<r){
    console.log("Salam")
}
else{
    console.log("bye mate")
}

let q = o>r || r>1 ? console.log("hello") : console.log("bye")
age = 17
if(age>18){
    console.log("allowed")
}
else if(age > 1 && age>=17){
console.log("maybe")
}

else if(age > 5 && age>16){
    console.log("growing")
}

else{
    console.log("not allowed")
}

let _r = sum(100, 90);
console.log("the result of sum is:", _r)
function sum(k,r, h=10){
    return k + r + h+10
}