var fs = require('fs');

var number = fs.readFileSync('number.txt');

if (process.argv[2] == 'read') {
  var suggestion = fs.readFileSync(process.argv[3], (err) => {
    if (err) throw err;
  });
  var suggestion = JSON.parse(suggestion);
  console.log(`\n${suggestion.who} suggests '${suggestion.what}'\nStatus: ${suggestion.status}\nNotes: ${suggestion.notes}`);
}


else if (process.argv[2] == 'suggest') {
  var object = {
    who: process.argv[3],
    what: (process.argv[4].split('-')).join(' '),
    status: process.argv[5],
    notes: (process.argv[6].split('-')).join(' ')
  }

  number++;
  fs.writeFile('number.txt', number, (err) => {
    if (err) throw err;
  });
  if (number < 10) {
    number = `0${number}`;
  }

  var final = JSON.stringify(object);

  fs.writeFileSync(`${number}.json`, final, (err) => {
    if (err) throw err;
  });
}


else if (process.argv[2] == 'remove') {
  numberr = parseInt(process.argv[3], 10);
  finalnumber = numberr;

  if (numberr < 10) {
    finalnumber = `0${numberr}`;
  }

  for (var i = 0; i <= number; i++) {
    if (i > numberr && i < 10) {
      fs.rename(`0${i}.json`, `0${i - 1}.json`, (err) => {
        if (err) throw err;
      });
    }
    else if (i > numberr) {
      fs.rename(`${i}.json`, `${i - 1}.json`, (err) => {
        if (err) throw err;
      });
    }
  }
  number--;
  fs.writeFile('number.txt', number, (err) => {
    if (err) throw err;
  });
  fs.unlinkSync(`${finalnumber}.json`, (err) => {
    if (err) throw err;
  });
}
