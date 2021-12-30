function findVal(arr, val) {
  let value = false;

  if (!arr.length) return value;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === val) {
      return (value = true);
    } else if (Array.isArray(arr[i])) {
      return findVal(arr[i], val);
    }
  }
  return value;
}
const arr = [1, 2, 3, [5, 6, [7]]];
const arr2 = [1, 2, 3, 4, 5, 6, 7];
console.log(findVal(arr, 7)); //logs true
console.log(findVal(arr, 9)); //logs false

//but then why does the following also work if the value hasn't been changed? like how does the return true value carry all the way out to the global scope and not get garbage collected, and why doesn't the value being false get returned?

function findVal2(arr, val) {
  let value = false;

  if (!arr.length) return value;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === val) {
      return true;
    } else if (Array.isArray(arr[i])) {
      return findVal(arr[i], val);
    }
  }
  return value;
}
console.log(findVal2(arr, 7)); //logs true
console.log(findVal2(arr2, 7)); //logs true
console.log(findVal2(arr, 9)); //logs false

function factorial(n) {
  if (n <= 1) return 1;
  return n * factorial(n - 1);
}

function sumsInt(n) {
  if (n <= 1) return 1;
  return n + sumsInt(n - 1);
}

function reverseString(str) {
  if (!str.length) return str;
  const shorterString = str.substring(0, str.length - 1);
  return str.slice(-1) + reverseString(shorterString);
}

function countsWhiteSpace(str) {
  if (str === "") return 0;
  if (str.charAt(0) === " ") {
    return 1 + countsWhiteSpace(str.substring(1));
  } else {
    return countsWhiteSpace(str.substring(1));
  }
}

function sumDigits(n) {
  if (n < 10) return n;
  let numFirst = +n.toString().slice(0, 1);
  let numRest = +n.toString().substring(1);
  let returnValue = numFirst + sumDigits(numRest);
  return sumDigits(returnValue);
}

function fib(n) {
  const start = [0, 1, 1];
  if (n <= 2) {
    return start[n - 1];
  }
  return fib(n - 1) + fib(n - 2);
}

function sumNests(arr) {
  let count = 0;

  for (let i = 0; i < arr.length; i++) {
    if (typeof arr[i] === "number") {
      count += arr[i];
    }
    if (Array.isArray(arr[i])) {
      count += sumNests(arr[i]);
    }
  }
  return count;
}

function findVal(arr, val) {
  let value = false;

  if (!arr.length) return value;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === val) {
      return (value = true);
    } else if (Array.isArray(arr[i])) {
      return findVal(arr[i], val);
    }
  }
  return value;
}

function countObjects(obj) {
  let count = 0;

  if (typeof obj !== "object") {
    return 0;
  }
  if (typeof obj === "object") {
    count++;
  }
  for (let key in obj) {
    count += countObjects(obj[key]);
  }
  return count;
}

function deepFreeze(obj) {
  if (typeof obj !== "object") return "not an object";
  //Object.freeze(obj);
}

/*

10. Implement your own version of the [deep-freeze function](https://www.npmjs.com/package/deep-freeze), which takes an object (or an array) and freezes it and all of its child array/objects, meaning none of them can be mutated.

You may wish to read up more on [Object.freeze](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze) to understand how it works shallowly on objects and arrays.

*/
