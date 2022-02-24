function changeActorToPlayedBy(arr) {
  if (!arr.length) {
    return [];
  } else {
    const newArr = [...arr];

    const answArr = newArr.map(element => {
      return {
        number: element.number,
        playedBy: element.actor,
        begin: element.begin,
        end: element.end
      };
    });
    return answArr;
  }
}

function progressStudents(arr) {
  if (!arr.length) {
    return [];
  } else {
    const newArr = arr.map(element => {
      if (element.courseStage < 6) {
        return {
          firstName: element.firstName,
          lastName: element.lastName,
          age: element.age,
          courseStage: element.courseStage + 1
        };
      } else {
        return {
          firstName: element.firstName,
          lastName: element.lastName,
          age: element.age,
          courseStage: element.courseStage,
          graduate: true
        };
      }
    });
    return newArr;
  }
}

function findNewLand(arr) {
  const newArr = [];
  const newObj = {};
  if (!arr.length) {
    return newArr;
  } else if (arr.length === 1 && Object.keys(arr[0]).length === 0) {
    newArr.push(newObj);
    return newArr;
  } else {
    arr.forEach(element => {
      let obj = {};
      obj.place = `New ${element.place}`;
      obj.population = (element.population / 100) * 90;
      newArr.push(obj);
    });
  }
  return newArr;
}

const objArr = [{ name: "ray", age: 35, country: "Scotland" }];

function copyObject(arr) {
  const newArr = arr.map(element => {
    return {
      name: element.name,
      age: element.age,
      country: element.country
    };
  });
  console.log(newArr);
  return newArr;
}

function copyObjectAlt(arr) {
  const newArr = arr.map(element => {
    const newObj = {};
    for (let key in element) {
      newObj[key] = element[key];
    }
    return newObj;
  });
  console.log(newArr);
  return newArr;
}

const answ = copyObjectAlt(objArr);
console.log(answ === objArr);
