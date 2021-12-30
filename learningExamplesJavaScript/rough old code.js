/*### mergeArrays()

Should take an array of arrays and return a flattened, single, **new array**, with the entries from each array returned in alternating order. If the arrays are not the same length, the shorter arrays should add `undefined` to the merged array until all values have been merged.*/

const input = [1, 2, 3];

function mergeArrays(array) {
  const newArr = [];
  if (array.length <= 1) {
    array.forEach(element => newArr.push(element));
    console.log(newArr);
  }
}
mergeArrays(input);

//array.forEach(element => {
//newArr.push(element));
//return newArr;

// [1, 'a', 2, 'b', 3, 'c', undefined, 'd']

const shortDocs = [
  { number: 1, actor: "William Hartnell", begin: 1963, end: 1966 },
  { number: 2, actor: "Patrick Troughton", begin: 1966, end: 1969 },
  { number: 3, actor: "Jon Pertwee", begin: 1970, end: 1974 },
  { number: 4, actor: "Tom Baker", begin: 1974, end: 1981 }
];

function changeActorToPlayedBy(arr) {
  const newArr = [...arr];

  const answArr = newArr.map(element => {
    return {
      number: element.number,
      playedBy: element.actor,
      begin: element.begin,
      end: element.end
    };
  });
  return answArr;
}

let ans = changeActorToPlayedBy(shortDocs);

console.log(ans);

//console.log(ans===shortDocs)
//console.log(ans == shortDocs)

/*function translateKey(student, keyToChange, translation) {
  const newStudent = {};

  for (const key in student) {
    if (key === keyToChange) {
      newStudent[translation] = student[keyToChange];
    } else {
      newStudent[key] = student[key];
    }
  }
  return newStudent;
}*/

/*function loopChange(arr) {
  const newArr = [...arr];
  const newArr2 = [];

  newArr.forEach(element => {
    const newDoc = {};
    for (const xKey in element) {
      if (xKey === "actor") {
        newDoc.playedBy = element.actor;
      } else {
        newDoc[xKey] = element[xKey];
      }
    }
    newArr2.push(newDoc);
  });
  return newArr2;
}*/

//let ans = loopChange(shortDocs);

//console.log(ans);
//console.log(shortDocs);
//ans[0].number = 10000;

//console.log(ans);
//console.log(shortDocs);

/*### changeActorToPlayedBy()

Write a function that takes the array of doctor objects and returns a **new array** of **new doctor objects** with the `actor` key replaced by `playedBy`.

const doctors = [
  { number: 1, actor: "William Hartnell", begin: 1963, end: 1966 },
  { number: 2, actor: "Patrick Troughton", begin: 1966, end: 1969 },
  { number: 3, actor: "Jon Pertwee", begin: 1970, end: 1974 },
  { number: 4, actor: "Tom Baker", begin: 1974, end: 1981 },
  { number: 5, actor: "Peter Davison", begin: 1982, end: 1984 },
  { number: 6, actor: "Colin Baker", begin: 1984, end: 1986 },
  { number: 7, actor: "Sylvester McCoy", begin: 1987, end: 1989 },
  { number: 8, actor: "Paul McGann", begin: 1996, end: 1996 },
  { number: 9, actor: "Christopher Eccleston", begin: 2005, end: 2005 },
  { number: 10, actor: "David Tennant", begin: 2005, end: 2010 },
  { number: 11, actor: "Matt Smith", begin: 2010, end: 2013 },
  { number: 12, actor: "Peter Capaldi", begin: 2013, end: 2017 },
  { number: 13, actor: "Jodie Whittaker", begin: 2017, end: 2017 }
];
//doctorByDuration(doctors, 4)
const answ = [
  { number: 3, actor: "Jon Pertwee", begin: 1970, end: 1974 },
  { number: 4, actor: "Tom Baker", begin: 1974, end: 1981 },
  { number: 10, actor: "David Tennant", begin: 2005, end: 2010 },
  { number: 12, actor: "Peter Capaldi", begin: 2013, end: 2017 }
];

*/

/*
arr.forEach(element => {
      let obj = {};
      obj.place = `New ${element.place}`;
      obj.population = (element.population / 100) * 90;
      newArr.push(obj);
    });*/
const grads = [
  { firstName: "Bill", lastName: "Jones", age: 35, courseStage: 2 },
  { firstName: "Ralph", lastName: "Aide", age: 24, courseStage: 6 },
  { firstName: "Elle", lastName: "Sproule", age: 40, courseStage: 5 },
  { firstName: "Amry", lastName: "Milfer", age: 18, courseStage: 6 },
  { firstName: "Susan", lastName: "Brock", age: 19, courseStage: 3 }
];

function sortStudent(arr, property, boolean)
const newArr = [...grads]

newArr.sort((a, b) => for (let i = 0; i < arr.length; i++)
arr.sort()



/*### sortStudents()

Write a function that takes three arguments: the student information, the property by which to sort, and a boolean that determines whether to sort ascending or descending. It should return a **new array** with the original student objects sorted according to the criteria passed in.
*/
function testFunc() {
  return "Function Has Worked";
}

const once = func => {
  let counter = 0;
  function innerFunction() {
    if (counter < 1) {
      counter++;
      return func();
    }
  }
  return innerFunction;
};

let initialise = once(testFunc);

console.log(initialise());
console.log(initialise());