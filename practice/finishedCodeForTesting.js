function createStudentReport(arr) {
  const newObj = {
    numberOnRole: arr.length
  };

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
  return newObj;
}

module.exports = { createStudentReport };
