function objectMaker(firstName, surName, team, gender) {
  const newObj = {};
  newObj.firstName = firstName;
  newObj.surName = surName;
  newObj.age = Math.floor(Math.random() * 90 + 10);
  newObj.team = team;
  newObj.gender = gender;
  return newObj;
}

const firstNames = [
  "Bill",
  "Ben",
  "Annie",
  "Will",
  "Mike",
  "Peter",
  "Wally",
  "Steph",
  "Caroline",
  "Angie"
];

const newArr = firstNames.map(element => {
  const surNames = ["Smith", "Smythe", "James", "Daffid"];
  const team = ["blue", "red", "green"];
  return objectMaker(
    element,
    surNames[Math.floor(Math.random() * 4)],
    team[Math.floor(Math.random() * 3)]
  );
});

console.log(newArr);
