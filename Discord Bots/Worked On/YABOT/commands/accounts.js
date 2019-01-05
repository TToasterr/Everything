const Discord = require('discord.js');
const fs = require('fs');

module.exports = {
  name: 'accounts',
  description: 'List all bank accounts,',
  usage: '',
  category: 'bank',
  guildOnly: false,
  args: false,
  mod: false,
  execute(message, args, client, time) {
    const config = require('../config.json');
    const author = message.author.username;

    const finalEmbed = new Discord.RichEmbed()
    .setColor('#00ff00')
    .setAuthor('YABOT (Yet Another Bot Of Toaster\'s)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')
    .setTitle('__**All Accounts**__')
    // .setDescription(`__*Number, status, and author are shown.*__`);

    var users = [];
    var accounts = [];
    var owners = {};

    fs.readdirSync('./commands/bank').forEach(file => {
      users.push(file);
    });

    for (var folder of users) {
      owners[folder] = [];
      var done = false;

      fs.readdirSync(`./commands/bank/${folder}`).forEach(file => {
        accounts.push(file);
        fileContent = fs.readFileSync(`./commands/bank/${folder}/${file}`, (err) => {
          if (err) throw err;
        });

        var account = JSON.parse(fileContent);
        owners[folder].push([account.name, account.balance]);
      });
    }

    for (var owner in owners) {
      var accountss = [];

      for (var i = 0; i < owners[owner].length; i++) {
        accountss.push(owners[owner][i]);
      }

      var temp01 = accountss.join(';;;');
      temp01 = temp01.replace(/\,/g, '** - $');
      accountss = temp01.split(';;;');

      if (accountss.join('\n') == '') {
        done = true;
      }

      if (!done) {
        finalEmbed.addField(`**${owner}**`, '**' + accountss.join('\n**'));
      }
    }

    message.channel.send(finalEmbed);
    console.log(`[${time}] ${message.author.username} listed accounts.`);
  },
};
