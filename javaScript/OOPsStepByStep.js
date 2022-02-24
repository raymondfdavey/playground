//normal function that creates single accounts

function makeAccounts(name) {
  const newAccount = {};
  newAccount.name = name;
  newAccount.number = Math.floor(Math.random() * 10000000);
  newAccount.basket = [];
  newAccount.addToBasket = addToBasket;
  return newAccount;
}

function addToBasket(item) {
  this.basket.push(item);
}
//method stored outside the function so all created accounts can use it without replicating the function code inside every account

const raysAccountByFunction = makeAccounts("ray");
console.log(raysAccountByFunction); //{name: 'ray', number: 3418437, basket: [], addToBasket: [Function: addToBasket]}}

raysAccountByFunction.addToBasket("BOOZE");
console.log(raysAccountByFunction); //{ name: 'ray', number: 2484638, basket: [ 'BOOZE' ], addToBasket: [Function: addToBasket]}

//NOW WITH CONSTRUCTOR FUNCTION

function Account(name) {
  this.name = name;
  this.number = Math.floor(Math.random() * 10000000);
  this.basket = [];
}

Account.prototype.addToBasket2 = function(item) {
  this.basket.push(item);
};

// NB. for constructors the capital at the start of Account, and the new used to declare a new instance

const raysAccountWithConstructor = new Account("ray");
console.log(raysAccountWithConstructor); //Account { name: 'ray', number: 5426408, basket: [] }

raysAccountWithConstructor.addToBasket2("MORE BOOZE");
console.log(raysAccountWithConstructor); //Account { name: 'ray', number: 7434276, basket: [ 'MORE BOOZE' ] }

//NOW FOR CLASSES

class ClassAccount {
  constructor(name) {
    this.name = name;
    this.accountNumber = Math.floor(Math.random() * 10000000);
    this.basket = [];
  }

  addToBasket3(item) {
    this.basket.push(item);
  }
  removeFromBasket(item) {
    this.basket.unshift(item);
  }
}

const rayAccountWithClass = new ClassAccount("ray");
console.log(rayAccountWithClass);

rayAccountWithClass.addToBasket3("BREAD");
console.log(rayAccountWithClass);

function Account2() {
  this.name = "bill";
  this.age = 24;
}

const bill = new Account2();
console.log(bill); //Account { name: 'bill', age: 24 }

Account2.prototype.changeName = function(newName) {
  this.name = newName;
};

bill.changeName("andy");
console.log(bill); //Account { name: 'andy', age: 24 }

console.log(bill.changeName); //[Function]
console.log(bill.__proto__); //Account { changeName: [Function] }

class AmbulanceStaff {
  constructor(name, trust, jobRole) {
    this.name = name;
    this.trust = trust;
    this.job = jobRole;
    this.crb = true;
    this.qualfied = "yes";
  }
  changeName(name) {
    this.name = name;
  }
}

class Technician extends AmbulanceStaff {
  constructor(name, trust, jobRole, certHEPassed = "pass", drivingGrade) {
    super(name, trust, jobRole);
    this.certHEpassed = certHEPassed;
    this.driving = drivingGrade;
  }
  changeDriving(grade) {
    this.driving = grade;
  }
}

const paraRay = new AmbulanceStaff("ray", "NHS lothian", "paramedic");
console.log(paraRay);
// AmbulanceStaff {
//   name: 'ray',
//   trust: 'NHS lothian',
//   job: 'paramedic',
//   crb: true,
//   qualfied: 'yes'
// }

const techRay = new Technician("Ray", "South West", "technician");
console.log(techRay);
// Technician {
//   name: 'Ray',
//   trust: 'South West',
//   job: 'technician',
//   crb: true,
//   qualfied: 'yes',
//   certHEpassed: 'pass',
//   driving: undefined
// }

console.log(paraRay.__proto__); //AmbulanceStaff {}
console.log(techRay.__proto__); //Technician {}

techRay.changeName("Bill");
console.log(techRay);
// Technician {
//   name: 'Bill',
//   trust: 'South West',
//   job: 'technician',
//   crb: true,
//   qualfied: 'yes',
//   certHEpassed: 'pass',
//   driving: undefined
// }

techRay.changeDriving("bad");
console.log(techRay);
// Technician {
//   name: 'Bill',
//   trust: 'South West',
//   job: 'technician',
//   crb: true,
//   qualfied: 'yes',
//   certHEpassed: 'pass',
//   driving: 'bad'
// }

// paraRay.changeDriving("good"); <- TypeError: paraRay.changeDriving is not a function

function User(name) {
  this.name = name;
  this.basket = [];
  this.searchHistory = [];
}

const userRay = new User("ray");
console.log(userRay); //User { name: 'ray', basket: [], searchHistory: [] }
