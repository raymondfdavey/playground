let num = 10;

const func = function() {
  let num = 3;
  const printNum = function() {
    console.log(num);
  };
  printNum();
};

func(); //logs 3

const printNum2 = function() {
  console.log(num);
};

const func2 = function() {
  let num = 3;
  printNum2();
};

func2(); // logs 10
