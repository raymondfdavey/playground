function sortStudents(arr, property, order) {
  let newArr = [...arr];

  if (!arr.length || property === undefined) {
    return newArr;
  } else if (order === undefined || order === "asc") {
    newArr.sort((student1, student2) => {
      if (student1[property] < student2[property]) {
        return -1;
      } else if (student1[property] > student2[property]) {
        return 1;
      } else {
        return 0;
      }
    });
    return newArr;
  } else if (order === "desc") {
    newArr.sort((student1, student2) => {
      if (student1[property] > student2[property]) {
        return -1;
      } else if (student1[property] < student2[property]) {
        return 1;
      } else {
        return 0;
      }
    });
    return newArr;
  }
}

/*The orderVeg function should take a array of vegetables and return a 
  new array in which the vegetables are sorted in ascending order according to quantity.
  */

function orderVeg(array) {
  console.log(
    array.sort((vegOne, vegTwo) => vegOne.quantity - vegTwo.quantity)
  );
}
