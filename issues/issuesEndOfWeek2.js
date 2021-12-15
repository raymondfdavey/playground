// Questions

// 1. How to deal with for loops in global execution diagram? (got a bit confused when trying to understand the return issue with the failing recursion example below

// 2. Return. Don't quite feel I get how it works some times and when it is needed or not needed or how to use it effectively. Not sure how it works in: 'Reduce', or when when you are trying to amend something (e.g. poke fight example) but also was an issue in recursion

// 3. Object.prototype.method - why is it outside the creator function? Surely if you know it already why not have it in the creator function?

//4. What is the test gonna be like?

/*
reduce to array of students only on courseStage6
*/
// I don't quite what's happening - like in the first one why doesn't it just return 3 - i.e. the first implimentation of res+current value? like how does it know to wait till the end to return it? It seems in the second example you explicitly have to sepratate what happens for each current val (building up the array) and then, at the end of the process, return that array? or if not, if you are returning the array each time why doesn't it return [[Amry Milfer], [Ralph Aide]]

const nums = [1, 2, 3, 4];

const numAnswer = nums.reduce((res, currentVal) => {
  return res + currentVal;
});

console.log(numAnswer);

const students = [
  { firstName: "Bill", lastName: "Jones", age: 35, courseStage: 2 },
  { firstName: "Amry", lastName: "Milfer", age: 18, courseStage: 6 },
  { firstName: "Ralph", lastName: "Aide", age: 24, courseStage: 6 }
];

const sutdentsAnswer = students.reduce((res, currentVal) => {
  if (currentVal.courseStage === 6) {
    res.push(`${currentVal.firstName} ${currentVal.lastName}`);
  }
  return res;
}, []);

console.log(sutdentsAnswer); // returns [ 'Amry Milfer', 'Ralph Aide' ]

/*
get this turn to change after each fight sequence
*/

function Battle(trainer1, trainer2, poke1, poke2) {
  this.trainer1 = trainer1;
  this.trainer2 = trainer2;
  this.trainer1.pokeSack.push(poke1);
  this.trainer2.pokeSack.push(poke2);
  this.turn = 1;
}

Battle.prototype.fight = function() {
  if (this.turn === 1) {
    this.trainer2.pokeSack[0].health -= this.trainer1.pokeSack[0].attack;
    this.turn = 2;
  } else {
    this.trainer1.pokeSack[0].health -= this.trainer2.pokeSack[0].attack;
    this.turn = 1;
  }
};

//RECURSION EXAMPLE
/* 
Implement a function that determines if an array includes a particular value at any level of nesting. Return true if found, false if not
*/

function findVal(arr, val) {
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
const arr = [1, 2, 3, [5, 6, [7]]];
const arr2 = [1, 2, 3, 4, 5, 6, 7];

console.log(findVal(arr, 7)); //correctly logs true
console.log(findVal(arr, 9)); //correctly logs false

//BUT
const arr3 = [1, 2, [1, 2], 3, [1, [1, 7, [3]]], [1, [2], [1, 2, [4, [5]]]]];
const checkAns = findVal(arr3, 7);
console.log(findVal(arr3, 7)); //wrongly logs false

function findVal(arr, val) {
  let value = false;

  if (!arr.length) return value;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === val) {
      return true;
    } else if (Array.isArray(arr[i])) {
      value = findVal(arr[i], val);
    }
  }
  return value;
}
const arr = [1, 2, 3, [5, 6, [7]]];
const arr2 = [1, 2, 3, 4, 5, 6, 7];

console.log(findVal(arr, 7)); //correctly logs true
console.log(findVal(arr, 9)); //correctly logs false

//BUT
const arr3 = [1, 2, [1, 2], 3, [1, [1, 7, [3]]], [1, [2], [1, 2, [4, [5]]]]];
const checkAns = findVal(arr3, 7);
console.log(findVal(arr3, 7)); // logs TRUE! solved!
