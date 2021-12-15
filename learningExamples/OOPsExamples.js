//Functions, Classes and Extends

// BC (Before Classes...)

function Northcoder(name, cohort) {
  this.name = name;
  this.cohort = cohort;
  this.block = "fundamentals";
  this.stressLevel = 0;
}

Northcoder.prototype.changeBlock = function(newBlock) {
  this.block = newBlock;
};

// AC (After Classes...)

class Northcoder {
  constructor(name, cohort) {
    this.name = name;
    this.cohort = cohort;
    this.block = "fundamentals";
    this.stressLevel = 0;
  }

  changeBlock(newBlock) {
    this.block = newBlock;
  }
}

Northcoder.prototype.changeBlock = function(newBlock) {
  this.block = newBlock;
};
