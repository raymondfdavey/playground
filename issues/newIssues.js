//QUESTION = WHERE DO THE METHODS DEFINED IN A CLASSES OBJECT GO = THEY ARE ON THE PROTOTYPE AS THEY ARE ACCESSIBLE TO CHILD CLASSES BUT THEY ARE NOT VIEWABLE ON THE PROTOTYPE

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

console.log(NHSstaff.prototype); //NHSstaff {} i.e. blank?
//and yet...

console.log(NHSstaff.prototype.changeAge); //[Function: changeAge]
console.log(NHSstaff.prototype.updateLeaveDate); //[Function: updateLeaveDate]

NHSstaff.prototype.changeName = function(newName) {
  this.name = newName;
};

console.log(NHSstaff.prototype); //NHSstaff { changeName: [Function] } i.e. one function only
console.log(NHSstaff.prototype.changeName); //[Function]
