const axios = require("axios");

function Pokemon(givenPokemon) {
  this.name = givenPokemon.name;
  this.health = 100;
  this.id = givenPokemon.id;
  //   this.order = givenPokemon.order;
  this.weight = givenPokemon.weight;
  this.species = givenPokemon.species.name;
  this.moves = givenPokemon.moves.reduce((res, singleMove) => {
    usefulBit = singleMove.move.name;
    res.push(usefulBit);
    return res;
  }, []);
  this.stats = givenPokemon.stats.reduce((res, currentStat) => {
    newObj = {
      [currentStat.stat.name]: currentStat.base_stat,
    };
    res = { ...newObj, ...res };
    return res;
  }, {});
}

function randomInteger(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

let pokeOneNumber = randomInteger(1, 500).toString();
let pokeTwoNumber = randomInteger(1, 500).toString();

console.log(pokeOneNumber);
console.log(pokeTwoNumber);

const baseUrl = "https://pokeapi.co/api/v2/pokemon/";

async function fetchPoke(pokeNum) {
  try {
    let response = await axios.get(baseUrl + pokeNum);
    return response.data;
  } catch (err) {
    console.log("ERROR");
  }
  return response;
}

(async () => {
  const pokeOneData = await fetchPoke(pokeOneNumber);
  const pokeTwoData = await fetchPoke(pokeTwoNumber);

  let pokeObjectOne = new Pokemon(pokeOneData);
  let pokeObjectTwo = new Pokemon(pokeTwoData);
  console.log(pokeObjectOne);
  console.log(pokeObjectTwo);
})();
