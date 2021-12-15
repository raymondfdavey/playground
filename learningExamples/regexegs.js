let inputCode = [
  '<div id="online-menu">A La Carte</div>',
  '<div id="red-box">Welcome to the site</div>',
  '<div id="northcoders-in-leeds">Hello</div>'
];

const getIDs = divs => {
  const str = divs.toString();
  const matches = str.match(/"(.*?)"/g);

  const realAnsw = [];
  matches.forEach(element => {
    const newVar = element.match(/"(.*?)"/);
    realAnsw.push(newVar[1]);
  });
  return realAnsw;
  //const newArr = str.match(/"(.*?)"/);
  //const answ = [newArr[1]];

  //console.log(answ);
  // this function should iterate over an array of html
  // strings in order to extract the id property
  // in each string
};
getIDs(inputCode);
