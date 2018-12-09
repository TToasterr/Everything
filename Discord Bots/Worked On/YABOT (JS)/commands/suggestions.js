const Discord = require('discord.js');
const fs = require('fs');

module.exports = {
  name: 'suggestions',
  description: 'List all suggestions!',
  usage: '',
  category: 'sugg',
  guildOnly: false,
  args: false,
  execute(message, args) {
    const config = require('../config.json');
    const author = message.author.username;
    const suggestion = args[0].substring(1);

    var number = config.number;
    if (number < 10) {
      number = `0${number}`;
    }

    const finalEmbed = new Discord.RichEmbed()
    .setColor('#00ff00')
    .setAuthor('YABOT (Yet Another Bot Of Toaster\'s)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')
    .setTitle('__All Suggestions__')
    .setDescription(`__*Number, status, and author are shown.*__`);

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
        finalEmbed.addField(i + ' - ' + suggestionn.status, suggestionn.who);
      }
    }
    // .addField('', '');
    // message.channel.send('');
    message.channel.send(finalEmbed);
    console.log(`${message.author.username} listed suggestions.`);
  },
};
