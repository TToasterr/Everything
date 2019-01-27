const Discord = require('discord.js');
const fs = require('fs');

module.exports = {
  name: 'suggest',
  description: 'Suggest something to Toaster!',
  usage: '<suggestion>',
  category: 'sugg',
  guildOnly: false,
  args: true,
  mod: false,
  execute(message, args, client, time, final, prefix) {
    let config = require('../config.json');
    const author = message.author.username;
    const suggestion = args[0].substring(1);

    let object = {
      who: author,
      what: suggestion,
      status: '',
      notes: ''
    }

    config.number++;

    fs.writeFile('./config.json', JSON.stringify(config), (err) => {
      if (err) throw err;
    });

    let number = config.number;
    if (number < 10) {
      number = `0${number}`;
    }

    const finalJSON = JSON.stringify(object);

    fs.writeFileSync(`./commands/suggestions/${number}.json`, finalJSON, (err) => {
      if (err) throw err;
    });

    final.setTitle('Sucessfully added suggestion!')
    .setDescription(`**By:** ${object.who}\n**Suggestion:** ${object.what}`);

    message.channel.send(final);
    let user = client.fetchUser('184474965859368960')
    .then(user => {
      user.send(`${message.author.username} just made a suggestion!\n\`${object.what}\``);
    })
    console.log(`[${time}] ${message.author.username} made a suggestion.`);
  },
};
