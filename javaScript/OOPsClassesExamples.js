let today = new Date();
let todaysDate =
  today.getMonth() + 1 + "-" + today.getDate() + "-" + today.getFullYear();

class NHSstaff {
  constructor(name, age, trust = "NW") {
    this.name = name;
    this.age = age;
    this.startDate = todaysDate;
    this.trust = trust;
    this.payRollNumber = Math.floor(Math.random() * 10000000);
    this.leaveDate = "still employed";
  }

  changeAge(newAge) {
    this.age = newAge;
  }

  updateLeaveDate(date) {
    this.leaveDate = `expected to leave ${date}`;
  }
}

const rayPara = new NHSstaff("ray", 35, "NHS Scotland");
console.log(rayPara);

rayPara.changeAge(50);
console.log(rayPara); // age is changed to 50

console.log(Object.getPrototypeOf(rayPara)); //NHSstaff
console.log(NHSstaff.prototype); //NHSstaff {}

NHSstaff.prototype.changeName = function(newName) {
  this.name = newName;
};

console.log(NHSstaff.prototype); //NHSstaff { changeName: [Function] }

class InHospital extends NHSstaff {
  constructor(name, age, trust = "NW", ward, department) {
    super(name, age, trust);
    this.ward = ward;
    this.department = department;
  }

  changeWard(newWard) {
    this.ward = newWard;
  }
}

const jimPorter = new InHospital("jim", 50, "NHS Scotland", 20, "Obstetrics");
console.log(jimPorter);
/*
{
  name: 'jim',
  age: 50,
  startDate: '1-12-2020',
  trust: 'NHS Scotland',
  payRollNumber: 9659279,
  leaveDate: 'still employed',
  ward: 20,
  department: 'Obstetrics'
}
*/

jimPorter.changeAge(100);
console.log(jimPorter); //changes to 100 - so parent Class method is available to the child class

jimPorter.changeName("CHANGED IT");
console.log(jimPorter); //changes it so prototype addition to parent class also available

jimPorter.changeWard(30);
console.log(jimPorter); //changes ward

console.log(Object.getPrototypeOf(InHospital)); //[Function: NHSstaff]
console.log(Object.getPrototypeOf(NHSstaff)); //[Function]

InHospital.prototype.changeDepartment = function(newDep) {
  this.department = newDep;
};

jimPorter.changeDepartment("Oncology");
console.log(jimPorter);

console.log(NHSstaff.prototype.changeName); //[Function]
console.log(NHSstaff.prototype.changeAge); //[Function: changeAge]
//so both functions ARE on the prototype even though
console.log(NHSstaff.prototype); //only logs NHSstaff { changeName: [Function] }
console.log(NHSstaff.prototype.changeDepartment); //undefined

console.log(InHospital.prototype.hasOwnProperty("changeWard")); // true even if its not listed
console.log(InHospital.prototype.changeAge); //[Function: changeAge]
console.log(InHospital.prototype.changeDepartment); //[Function]

console.log(InHospital.prototype); //InHospital { changeDepartment: [Function] } its own prototype
console.log(Object.getPrototypeOf(InHospital)); //[Function: NHSstaff]
console.log(InHospital.__proto__); //[Function: NHSstaff] ie the parent prototype

console.log(jimPorter instanceof NHSstaff); //true
console.log(jimPorter instanceof InHospital); //true
console.log(rayPara instanceof InHospital); //false

class InAandE extends InHospital {}

const sarahAandENurse = new InAandE("sarah", 23);
console.log(sarahAandENurse);

InAandE.prototype.makeAande = function() {
  this.ward = "Accident and Emergency";
  this.department = "Acute Receiving";
  this.leaveDate = "less than 5 years from now";
};

sarahAandENurse.makeAande();
console.log(sarahAandENurse);

console.log(InAandE.prototype); //InAandE { makeAande: [Function] }
console.log(InAandE.prototype.changeName); //Function
console.log(Object.getPrototypeOf(InAandE)); //[Function: InHospital]
console.log(Object.getPrototypeOf(InHospital)); //[Function: NHSstaff]
