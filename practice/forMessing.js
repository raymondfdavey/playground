function multiplier(passed) {
  function innerFunction(inner) {
    return passed * inner;
  }
  return innerFunction;
}

const timeByTen = multiplier(10);

console.log(timeByTen(5));
let counter = 0;
function sumFunc() {
  counter += 1;
  return counter;
}

function limitingFunction(func, num) {
  let value;
  function innerFunction() {
    if (--num >= 0) value = func();
    return value;
  }
  return innerFunction;
}

const limitedSum = limitingFunction(sumFunc, 5);

console.log(limitedSum(12, 19));
console.log(limitedSum(12, 19));
console.log(limitedSum(12, 19));
console.log(limitedSum(12, 19));
console.log(limitedSum(12, 19));
console.log(limitedSum(12, 19));
console.log(limitedSum(12, 19));
console.log(limitedSum(12, 19));
console.log(limitedSum(12, 19));
