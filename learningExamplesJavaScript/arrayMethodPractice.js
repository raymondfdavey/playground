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
  { firstName: "Angie", surName: "Smythe", age: 94, team: "green" }
];

// const newArr = array.map(element => {
//   const genderOps = ["male", "female"];
//   element.gender = genderOps[Math.floor(Math.random() * 2)];
//   return element;
// });
// console.log(newArr);
// //adds random gender to each object

// const filtered = array.filter(element => element.team === "green");
// //console.log(filtered); //all green team

// const reduced = array.reduce((res, element) => {
//   if (element.team === "green") {
//     res.push(element);
//   }
//   return res;
// }, []);
// //console.log(reduced); //also all green team

// const reduced2 = array.reduce((res, element) => {
//   if (element.team === "green") {
//     res.push(`${element.firstName} ${element.surName}`);
//   }
//   return res;
// }, []);
// //console.log(reduced2); //pushed first and second names of green teamers

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
