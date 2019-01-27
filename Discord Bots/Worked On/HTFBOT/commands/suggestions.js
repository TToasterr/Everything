const Discord = require('discord.js');
const fs = require('fs');

module.exports = {
  name: 'suggestions',
  description: 'List all suggestions!',
  usage: '',
  category: 'sugg',
  guildOnly: false,
  args: false,
  mod: false,
  execute(message, args, client, time, final, prefix, start) {
    const config = require('../config.json');
    const author = message.author.username;
    const suggestion = args[0].substring(1);

    var number = config.number;
    if (number < 10) {
      number = `0${number}`;
    }

    final.setTitle('__All Suggestions__')
    .setDescription(`__*Number, author, and status are shown.*__`);

    for (var i = 0; i <= config.number; i++) {
      if (i != 0) {
        var fileContent;
        if (i < 10) {
          fileContent = fs.readFileSync(`./commands/suggestions/0${i}.json`, (err) => {
            if (err) throw err;
          });
        }
        else {
          fileContent = fs.readFileSync(`./commands/suggestions/${i}.json`, (err) => {
            if (err) throw err;
          });
        }
        var suggestionn = JSON.parse(fileContent);
        final.addField(i + `\ - \'` + suggestionn.what + `\'`, `**Status:** ${suggestionn.status}\n--------------`);
      }
    }
    message.channel.send(final);
    console.log(`[${time}] ${message.author.username} listed suggestions.`);
  },
};
