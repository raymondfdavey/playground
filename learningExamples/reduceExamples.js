//createStudentReport(students);

/*### createStudentReport()

Write a function that takes the same information and returns an object with the following properties: `numberOnRole` (the total number of students in the array), `atStage1`, `atStage2` ... up to `atStage6` (an array of student names at each stage) and `averageAge` (the mean average age of all students).
Too easy? Use only `reduce` to compile your object and return it directly.
*/

//without reduce
const students = [
  { firstName: "Bill", lastName: "Jones", age: 35, courseStage: 2 },
  { firstName: "Amry", lastName: "Milfer", age: 18, courseStage: 6 },
  { firstName: "Ralph", lastName: "Aide", age: 24, courseStage: 6 },
  { firstName: "Elle", lastName: "Sproule", age: 40, courseStage: 5 },
  { firstName: "Susan", lastName: "Brock", age: 19, courseStage: 3 },
  { firstName: "Andrew", lastName: "Jones", age: 35, courseStage: 2 },
  { firstName: "Colin", lastName: "Milfer", age: 25, courseStage: 1 },
  { firstName: "Steph", lastName: "Aide", age: 45, courseStage: 6 },
  { firstName: "Bert", lastName: "Sproule", age: 40, courseStage: 4 },
  { firstName: "Marg", lastName: "Brock", age: 19, courseStage: 3 }
];

function createStudentReport(arr) {
  const newObj = {
    numberOnRole: arr.length
  };

  let stage1Counter = 0;
  arr.forEach(element => {
    if (element.courseStage === 1) {
      stage1Counter++;
    }
  });
  newObj.atStage1 = stage1Counter;

  let stage1 = [];
  arr.forEach(element => {
    if (element.courseStage === 1) {
      stage1.push(`${element.firstName} ${element.lastName}`);
    }
  });
  newObj.atStage1 = stage1;

  let stage2 = [];
  arr.forEach(element => {
    if (element.courseStage === 2) {
      stage2.push(`${element.firstName} ${element.lastName}`);
    }
  });
  newObj.atStage2 = stage2;

  let stage3 = [];
  arr.forEach(element => {
    if (element.courseStage === 3) {
      stage3.push(`${element.firstName} ${element.lastName}`);
    }
  });
  newObj.atStage3 = stage3;

  let stage4 = [];
  arr.forEach(element => {
    if (element.courseStage === 4) {
      stage4.push(`${element.firstName} ${element.lastName}`);
    }
  });
  newObj.atStage4 = stage4;

  let stage5 = [];
  arr.forEach(element => {
    if (element.courseStage === 5) {
      stage5.push(`${element.firstName} ${element.lastName}`);
    }
  });
  newObj.atStage5 = stage5;

  let stage6 = [];
  arr.forEach(element => {
    if (element.courseStage === 6) {
      stage6.push(`${element.firstName} ${element.lastName}`);
    }
  });
  newObj.atStage6 = stage6;

  let counter = 0;
  arr.forEach(element => {
    counter += element.age;
  });

  newObj.averageAge = counter / arr.length;

  console.log(newObj)
  return newObj;
}

createStudentReport(students);

//with reduce

function reducer(arr) {
  const newObj = {
    numberOnRole: arr.length,

    atStage1: arr.reduce((result, student) => {
      if (student.courseStage === 1) {
        result.push(`${student.firstName} ${student.lastName}`);
      }
      return result;
    }, []),

    atStage2: arr.reduce((result, student) => {
      if (student.courseStage === 2) {
        result.push(`${student.firstName} ${student.lastName}`);
      }
      return result;
    }, []),

    atStage3: arr.reduce((result, student) => {
      if (student.courseStage === 3) {
        result.push(`${student.firstName} ${student.lastName}`);
      }
      return result;
    }, []),

    atStage4: arr.reduce((result, student) => {
      if (student.courseStage === 4) {
        result.push(`${student.firstName} ${student.lastName}`);
      }
      return result;
    }, []),

    atStage5: arr.reduce((result, student) => {
      if (student.courseStage === 5) {
        result.push(`${student.firstName} ${student.lastName}`);
      }
      return result;
    }, []),

    atStage6: arr.reduce((result, student) => {
      if (student.courseStage === 6) {
        result.push(`${student.firstName} ${student.lastName}`);
      }
      return result;
    }, []),

    averageAge:
      arr.reduce((result, student) => result + student.age, 0) / arr.length
  };
  console.log(newObj);
  return newObj
}

reducer(students);

//below mini example just playing around
const students2 = [
  { firstName: "Bill", lastName: "Jones", age: 35, courseStage: 2 },
  { firstName: "Amry", lastName: "Milfer", age: 18, courseStage: 6 },
  { firstName: "Ralph", lastName: "Aide", age: 24, courseStage: 6 }
];

console.log(
  students2.reduce(
    (acc, currVal) => {
      if (currVal.courseStage === 6) {
        acc.push({ bin: "yo" });
      }
      return acc;
    },
    [1, 2]
  )
);

const students3 = [
  { firstName: "Bill", lastName: "Jones", age: 35, courseStage: 2 },
  { firstName: "Amry", lastName: "Milfer", age: 18, courseStage: 6 },
  { firstName: "Ralph", lastName: "Aide", age: 24, courseStage: 6 }
];

console.log(
  students3.map(element => {
    if (element.courseStage === 6) {
      return element;
    }
  })
);

console.log(
  students3.reduce((res, currentVal) => {
    if (currentVal.courseStage === 2) {
      res.push(currentVal);
    }
    return res;
  }, [])
);

// THE ABOVE IS AN INTERESTING EXAMPLE OF USING REDUCE ALMOST LIKE MAP OR FILTER BUT EVEN BETTER BECAUSE FILTER CAN ONLY RETURN THE FILTERED ARRAY WHEREAS REDUCE CAN REALLY FILTER AND EXTRACT FOR EXAMPLE
someArr.reduce((result, iterativeArrValue) => {some operation on iterativeValue to create res, which when returned  }, [])
console.log(
  students.reduce((res, currentVal) => {
    if (currentVal.courseStage === 2) {
      res.push(currentVal.age);
    }
    return res;
  }, [])
);
// BELOW IS INTERESTING EXAMPLE OF REDUCING QUITE A COMPLEXED NESTED OBJECT PROPERTIES TO a new array of new objects
//"takes an array of pop star objects with information about the amount they have spent so far this year on confectionery at the cinema, and how much they have spent on today's visit. It return a **new array** of **new objects** with a property for the pop star's `name` and the `yearlyCumulativeSpend` property updated to include today's costs";
const input = [
  {
    name: "Beyonce Bowls",
    yearlyCumulativeSpend: "£44",
    purchaseToday: {
      item: "White mice",
      costPerItem: "£3",
      amountBought: 17
    }
  },
  {
    name: "Kray-Z",
    yearlyCumulativeSpend: "£28",
    purchaseToday: {
      item: "Flying saucers",
      costPerItem: "£2",
      amountBought: 28
    }
  }
];

const newObj = input.reduce((res, celeb) => {
  const spendSoFar = celeb.yearlyCumulativeSpend;
  const spendSoFarNum = +spendSoFar.match(/\£(\d+)/)[1];

  const cost = celeb.purchaseToday.costPerItem;
  const costNum = +cost.match(/\£(\d+)/)[1];
  const todaysPurchases = celeb.purchaseToday.amountBought * costNum;

  const objy = {
    name: celeb.name,
    yearlyCumulativeSpend: spendSoFarNum + todaysPurchases
  };
  res.push(objy);
  return res;
}, []);

console.log(newObj);

//HERE IT IS DONE AS MAP
function calculateConfectioneryCosts(arr) {
  const answer = arr.map(celeb => {
    const spendSoFar = celeb.yearlyCumulativeSpend;
    const spendSoFarNum = +spendSoFar.match(/\£(\d+)/)[1];

    const cost = celeb.purchaseToday.costPerItem;
    const costNum = +cost.match(/\£(\d+)/)[1];
    const todaysPurchases = celeb.purchaseToday.amountBought * costNum;
    return {
      name: celeb.name,
      yearlyCumulativeSpend: `£${spendSoFarNum + todaysPurchases}`
    };
  });
  return answer;
}

const ans = calculateConfectioneryCosts(input);

console.log(ans);
