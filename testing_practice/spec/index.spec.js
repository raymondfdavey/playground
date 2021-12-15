const { expect } = require("chai");

const { createStudentReport } = require("../finishedCodeForTesting");

describe("createStudentReport", () => {
  it("takes an array of student objects and returns an abject with the property `numberOnRole` (the total number of students in the array)", () => {
    const input = [
      { firstName: "Bill", lastName: "Jones", age: 35, courseStage: 2 },
      { firstName: "Amry", lastName: "Milfer", age: 18, courseStage: 6 },
      { firstName: "Bert", lastName: "Sproule", age: 40, courseStage: 4 },
      { firstName: "Marg", lastName: "Brock", age: 19, courseStage: 3 },
      { firstName: "Ralph", lastName: "Aide", age: 24, courseStage: 6 }
    ];
    const result = createStudentReport(input);
    expect(result.numberOnRole).to.eql(5);
  });
  it("takes an array of student objects and returns an abject with the property atStage1 which is an array of the names of the students at stage 1", () => {
    const input = [
      { firstName: "Bill", lastName: "Jones", age: 35, courseStage: 2 },
      { firstName: "Amry", lastName: "Milfer", age: 18, courseStage: 6 },
      { firstName: "Bert", lastName: "Sproule", age: 40, courseStage: 4 },
      { firstName: "Marg", lastName: "Brock", age: 19, courseStage: 3 },
      { firstName: "Ralph", lastName: "Aide", age: 24, courseStage: 6 }
    ];
    const result = createStudentReport(input);
    expect(result.atStage1).to.eql([]);
  });
  it("takes an array of student objects and returns an abject with the property atStage2 which is an array of the names of the students at stage 2", () => {
    const input = [
      { firstName: "Bill", lastName: "Jones", age: 35, courseStage: 2 },
      { firstName: "Amry", lastName: "Milfer", age: 18, courseStage: 6 },
      { firstName: "Bert", lastName: "Sproule", age: 40, courseStage: 4 },
      { firstName: "Marg", lastName: "Brock", age: 19, courseStage: 3 },
      { firstName: "Ralph", lastName: "Aide", age: 24, courseStage: 6 }
    ];
    const result = createStudentReport(input);
    expect(result.atStage2).to.eql(["Bill Jones"]);
  });
  it("takes an array of student objects and returns an abject with the property atStage3 which is an array of the names of the students at stage 3", () => {
    const input = [
      { firstName: "Bill", lastName: "Jones", age: 35, courseStage: 2 },
      { firstName: "Amry", lastName: "Milfer", age: 18, courseStage: 6 },
      { firstName: "Bert", lastName: "Sproule", age: 40, courseStage: 4 },
      { firstName: "Marg", lastName: "Brock", age: 19, courseStage: 3 },
      { firstName: "Ralph", lastName: "Aide", age: 24, courseStage: 6 }
    ];
    const result = createStudentReport(input);
    expect(result.atStage3).to.eql(["Marg Brock"]);
  });
  it("takes an array of student objects and returns an abject with the property atStage4 which is an array of the names of the students at stage 4", () => {
    const input = [
      { firstName: "Bill", lastName: "Jones", age: 35, courseStage: 2 },
      { firstName: "Amry", lastName: "Milfer", age: 18, courseStage: 6 },
      { firstName: "Bert", lastName: "Sproule", age: 40, courseStage: 4 },
      { firstName: "Marg", lastName: "Brock", age: 19, courseStage: 3 },
      { firstName: "Ralph", lastName: "Aide", age: 24, courseStage: 6 }
    ];
    const result = createStudentReport(input);
    expect(result.atStage4).to.eql(["Bert Sproule"]);
  });
  it("takes an array of student objects and returns an abject with the property atStage5 which is an array of the names of the students at stage 5", () => {
    const input = [
      { firstName: "Bill", lastName: "Jones", age: 35, courseStage: 2 },
      { firstName: "Amry", lastName: "Milfer", age: 18, courseStage: 6 },
      { firstName: "Bert", lastName: "Sproule", age: 40, courseStage: 4 },
      { firstName: "Marg", lastName: "Brock", age: 19, courseStage: 3 },
      { firstName: "Ralph", lastName: "Aide", age: 24, courseStage: 6 }
    ];
    const result = createStudentReport(input);
    expect(result.atStage5).to.eql([]);
  });
  it("takes an array of student objects and returns an object with the property averageAge which is the mean average age of all students", () => {
    const input = [
      { firstName: "Bill", lastName: "Jones", age: 35, courseStage: 2 },
      { firstName: "Amry", lastName: "Milfer", age: 18, courseStage: 6 },
      { firstName: "Bert", lastName: "Sproule", age: 40, courseStage: 4 },
      { firstName: "Marg", lastName: "Brock", age: 19, courseStage: 3 },
      { firstName: "Ralph", lastName: "Aide", age: 24, courseStage: 6 }
    ];
    const result = createStudentReport(input);
    expect(result.averageAge).to.eql(27.2);
  });
  it("takes an array of student objects andreturns an object with the following properties: `numberOnRole` (the total number of students in the array), `atStage1`, `atStage2` ... up to `atStage6` (an array of student names at each stage) and `averageAge` (the mean average age of all students).", () => {
    const input = students;
    const result = createStudentReport(input);
    expect(result).to.eql({
      numberOnRole: 10,
      atStage1: ["Colin Milfer"],
      atStage2: ["Bill Jones", "Andrew Jones"],
      atStage3: ["Susan Brock", "Marg Brock"],
      atStage4: ["Bert Sproule"],
      atStage5: ["Elle Sproule"],
      atStage6: ["Amry Milfer", "Ralph Aide", "Steph Aide"],
      averageAge: 30
    });
  });
});

/*
### createStudentReport()

Write a function that takes the same information and returns an object with the following properties: `numberOnRole` (the total number of students in the array), `atStage1`, `atStage2` ... up to `atStage6` (an array of student names at each stage) and `averageAge` (the mean average age of all students).
*/
