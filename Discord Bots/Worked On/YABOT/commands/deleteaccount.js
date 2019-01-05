const Discord = require('discord.js');
const fs = require('fs');

module.exports = {
  name: 'deleteaccount',
  description: 'Delete a bank account.',
  usage: '<name>, [balance]',
  category: 'bank',
  guildOnly: false,
  args: true,
  mod: false,
  execute(message, args, client, time) {
    var config = require('../config.json');
    var failed = false;
    const author = message.author.username;
    const accountName = args[0].substring(1);

    fs.unlink(`./commands/bank/${author}/${accountName}.json`, (err) => {
      if (err) {
        const finalEmbed = new Discord.RichEmbed()
        .setColor('#00ff00')
        .setAuthor('YABOT (Yet Another Bot Of Toaster\'s)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')
        .setTitle('That account could not be found!')
        .setDescription(`Please check if:\n-The account exists\n-You own the account`);
        message.channel.send(finalEmbed);
        return console.log(`${message.author.username} tried to delete a bank account, but something went wrong.`);
      }j
    });

    const finalEmbed = new Discord.RichEmbed()
    .setColor('#00ff00')
    .setAuthor('YABOT (Yet Another Bot Of Toaster\'s)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')
    .setTitle('Sucessfully removed account!')
    .setDescription(`Hooray(?)`);
    message.channel.send(finalEmbed);
    return console.log(`${message.author.username} deleted a bank account.`);
  },
};
