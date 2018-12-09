const Discord = require('discord.js');
const fs = require('fs');

module.exports = {
  name: 'suggestion',
  description: 'Get info for a suggestion!',
  usage: '<number>, [status/notes], [status/notes]',
  category: 'sugg',
  guildOnly: false,
  args: true,
  execute(message, args) {
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

    const finalEmbed = new Discord.RichEmbed()
    .setColor('#00ff00')
    .setAuthor('YABOT (Yet Another Bot Of Toaster\'s)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')

    if (!args[1] || args[1] == '') {
      finalEmbed.setTitle(`__Suggestion ${number}__`)
      .setDescription(`*Info for suggestion ${number}*`);

      finalEmbed.addField('Author', suggestionn.who)
      .addField('Suggestion', suggestionn.what);
      try {
        finalEmbed.addField('Status', suggestionn.status);
      } catch(err) {
        finalEmbed.addField('Status', 'none');
      }
      try {
        finalEmbed.addField('Notes', suggestionn.notes);
      } catch(err) {
        finalEmbed.addField('Notes', 'none');
      }
    }
    else {
      if (args[1] == 'status' && message.author.username == 'Toaster') {
        suggestionn.status = args[2];
        finalEmbed.setTitle(`__Status for ${number} has been Changed!__`)
        .setDescription(`'${args[2]}'`);

        const final = JSON.stringify(suggestionn);
        fs.writeFileSync(`./commands/suggestions/${number}.json`, final, (err) => {
          if (err) throw err;
        });
      }
      else if (args[1] == 'notes' && message.author.username == 'Toaster') {
        suggestionn.notes = args[2];
        finalEmbed.setTitle(`__Notes for ${number} have been Changed!__`)
        .setDescription(`'${args[2]}'`);

        const final = JSON.stringify(suggestionn);
        fs.writeFileSync(`./commands/suggestions/${number}.json`, final, (err) => {
          if (err) throw err;
        });
      }
    }

    message.channel.send(finalEmbed);
    console.log(`${message.author.username} got info for a suggestion.`);
  },
};
