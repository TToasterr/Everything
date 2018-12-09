const Discord = require('discord.js');
const fs = require('fs');

module.exports = {
  name: 'suggest',
  description: 'Suggest something to Toaster!',
  usage: '<suggestion>',
  category: 'general',
  guildOnly: false,
  args: true,
  execute(message, args) {
    var config = require('../config.json');
    const author = message.author.username;
    const suggestion = args[0].substring(1);

    var object = {
      who: author,
      what: suggestion,
      status: '',
      notes: ''
    }

    config.number++;

    fs.writeFile('./config.json', JSON.stringify(config), (err) => {
      if (err) throw err;
    });

    var number = config.number;
    if (number < 10) {
      number = `0${number}`;
    }

    const final = JSON.stringify(object);

    fs.writeFileSync(`./commands/suggestions/${number}.json`, final, (err) => {
      if (err) throw err;
    });

    const finalEmbed = new Discord.RichEmbed()
    .setColor('#00ff00')
    .setAuthor('YABOT (Yet Another Bot Of Toaster\'s)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')
    .setTitle('Sucessfully added suggestion!')
    .setDescription(`**By:** ${object.who}\n**Suggestion:** ${object.what}`);
    // .addField('', '');
    // message.channel.send('');
    message.channel.send(finalEmbed);
    // console.log(`${message.author.username} did something.`);
  },
};
