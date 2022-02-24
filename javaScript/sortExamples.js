function sortStudents(arr, property, order) {
  let newArr = [...arr];

  if (!arr.length || property === undefined) {
    return newArr;
  } else if (order === undefined || order === "asc") {
    newArr.sort((student1, student2) => {
      if (student1[property] < student2[property]) {
        return -1;
      } else if (student1[property] > student2[property]) {
        return 1;
      } else {
        return 0;
      }
    });
    return newArr;
  } else if (order === "desc") {
    newArr.sort((student1, student2) => {
      if (student1[property] > student2[property]) {
        return -1;
      } else if (student1[property] < student2[property]) {
        return 1;
      } else {
        return 0;
      }
    });
    return newArr;
  }
}

/*The orderVeg function should take a array of vegetables and return a 
  new array in which the vegetables are sorted in ascending order according to quantity.
  */

function orderVeg(array) {
  console.log(
    array.sort((vegOne, vegTwo) => vegOne.quantity - vegTwo.quantity)
  );
}

let array = [
  { firstName: "Bill", surName: "James", age: 14, team: "blue" },
  { firstName: "Ben", surName: "Smythe", age: 39, team: "blue" },
  { firstName: "Annie", surName: "Daffid", age: 43, team: "green" },
  { firstName: "Will", surName: "Smith", age: 38, team: "green" },
  { firstName: "Mike", surName: "Smythe", age: 47, team: "blue" },
  { firstName: "Peter", surName: "Smith", age: 19, team: "green" },
  { firstName: "Wally", surName: "Daffid", age: 85, team: "blue" },
  { firstName: "Steph", surName: "Smith", age: 56, team: "green" },
  { firstName: "Caroline", surName: "James", age: 72, team: "red" },
  { firstName: "Angie", surName: "Smythe", age: 94, team: "green" },
];

const sortedByTeam = array.sort((a, b) => {
  if (a.team < b.team) {
    return -1;
  }
  if (a.team > b.team) {
    return 1;
  }
  return 0;
});

console.log(sortedByTeam);

const sortedByAge = array.sort((a, b) => a.age - b.age);
console.log(sortedByAge);
