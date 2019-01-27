const Discord = require('discord.js');
const fs = require('fs');

module.exports = {
  name: 'suggestion',
  description: 'Get info for a suggestion!',
  usage: '<number>, [status/notes], [status/notes]',
  category: 'sugg',
  guildOnly: false,
  args: true,
  mod: true,
  execute(message, args, client, time, final, prefix, start) {
    const config = require('../config.json');
    const author = message.author.username;
    const suggestion = args[0].substring(1);

    var number = args[0].substring(1);
    if (number < 10) {
      number = `0${number}`;
    }

    fileContent = fs.readFileSync(`./commands/suggestions/${number}.json`, (err) => {
      if (err) throw err;
    });
    var suggestionn = JSON.parse(fileContent);

    if (!args[1] || args[1] == '') {
      final.setTitle(`__Suggestion ${number}__`)
      .setDescription(`*Info for suggestion ${number}*`);

      final.addField('Author', suggestionn.who)
      .addField('Suggestion', suggestionn.what);
      try {
        final.addField('Status', suggestionn.status);
      } catch(err) {
        final.addField('Status', 'none');
      }
      try {
        final.addField('Notes', suggestionn.notes);
      } catch(err) {
        final.addField('Notes', 'none');
      }
    }
    else {
      if (args[1] == 'status' && message.author.username == 'Toaster') {
        suggestionn.status = args[2];
        final.setTitle(`__Status for ${number} has been Changed!__`)
        .setDescription(`'${args[2]}'`);

        const finalJSON = JSON.stringify(suggestionn);
        fs.writeFileSync(`./commands/suggestions/${number}.json`, finalJSON, (err) => {
          if (err) throw err;
        });
      }
      else if (args[1] == 'notes' && message.author.username == 'Toaster') {
        suggestionn.notes = args[2];
        final.setTitle(`__Notes for ${number} have been Changed!__`)
        .setDescription(`'${args[2]}'`);

        const finalJSON = JSON.stringify(suggestionn);
        fs.writeFileSync(`./commands/suggestions/${number}.json`, finalJSON, (err) => {
          if (err) throw err;
        });
      }
    }

    message.channel.send(final);
    console.log(`[${time}] ${message.author.username} got or changed info for a suggestion.`);
  },
};
