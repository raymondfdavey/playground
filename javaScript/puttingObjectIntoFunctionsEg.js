class Northcoder {
  constructor(name, cohort) {
    this.name = name;
    this.cohort = cohort;
    this.block = "fundamentals";
    this.stressLevel = 0;
  }

  //   increaseStress(num) {
  //     this.stressLevel += num;
  //   }
}

Northcoder.prototype.increaseStress = function (num) {
  this.stressLevel += num;
};
Northcoder.prototype.decreaseStress = function (num) {
  this.stressLevel -= num;
};

let ray = new Northcoder();
let billy = new Northcoder();

ray.increaseStress(5);
billy.increaseStress(6);

console.log("RAY PRE =", ray.stressLevel);
console.log("BILL PRE =", billy.stressLevel);

let testingObjectManipulationWithingAFunction = function (
  northcoderObject1,
  northcoderObject2
) {
  northcoderObject1.increaseStress(5);
  northcoderObject2.increaseStress(20);
};

testingObjectManipulationWithingAFunction(ray, billy);

console.log("RAY after test=", ray.stressLevel);
console.log("billy after test=", billy.stressLevel);

let attendTherapySession = function (...args) {
  args.forEach((northcoderObject) => {
    northcoderObject.decreaseStress(10);
  });
};

attendTherapySession(ray, billy);

console.log("RAY after therapy=", ray.stressLevel);
console.log("billy after therapy=", billy.stressLevel);
