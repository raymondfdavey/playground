const fs = require('fs')
let primeFractions = []

selectedDenom = '3'

for (let i = 0; i < 10000000; i++) {
    let stringyI = i.toString()
    let fraction = `${stringyI}/${selectedDenom}`
    primeFractions.push(fraction)
}
primeFractions = primeFractions.map(fraction => {
    let split = fraction.split("/")
    let numerator = split[0]
    let denomenator = split[1]
    if ((numerator % denomenator) == 0) {
        let value = numerator / denomenator
        let valueAsString = value.toString()
        return valueAsString
    } else {
        return fraction
    }

})
// console.log(primeFractions)

primeIndexes = []
primeFractions.forEach((fraction, i) => {
    if (fraction.includes("/") == false) {
        // console.log(fraction, i)
        let number = fraction.toString()
        // console.log(number)
        if (isPrime(number) == true) {
            primeIndexes.push(i)
        }
    }
})

console.log(primeIndexes)


function isPrime(num) {
    for (var i = 2; i < num; i++)
        if (num % i === 0) return false;
    return num > 1;
}

let gapsBetweenIndexes = []

for (let i = 1; i < primeIndexes.length; i++) {
    let gap = primeIndexes[i] - primeIndexes[i - 1]
    gapsBetweenIndexes.push(gap)
}
console.log(gapsBetweenIndexes)

gapsOverDenom = gapsBetweenIndexes.map(num => num / selectedDenom)
console.log(gapsOverDenom)
highestValue = Math.max(...gapsOverDenom)
console.log(highestValue)
json = {}
json[selectedDenom] = gapsOverDenom
json["Highest Value"] = highestValue
const jsonAsString = JSON.stringify(json)
console.log(jsonAsString)

fs.writeFile(`./primeGapsOf${selectedDenom}.json`, jsonAsString, err => {
    if (err) {
        console.log('Error writing file', err)
    } else {
        console.log('Successfully wrote file')
    }
})