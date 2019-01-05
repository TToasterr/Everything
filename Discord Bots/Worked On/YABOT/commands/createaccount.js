const Discord = require('discord.js');
const fs = require('fs');

module.exports = {
  name: 'createaccount',
  description: 'Create a bank account, under your Discord username.',
  usage: '<name>, [balance]',
  category: 'bank',
  guildOnly: false,
  args: true,
  mod: false,
  execute(message, args, client, time) {
    var config = require('../config.json');
    const author = message.author.username;
    const accountName = args[0].substring(1);
    var balanceInput = args[1]

    if (balanceInput) {
      balanceInput++;
      balanceInput--;

      var object = {
        owner: author,
        name: accountName,
        balance: balanceInput
      }

      if (isNaN(balanceInput)) {
        const finalEmbed = new Discord.RichEmbed()
        .setColor('#00ff00')
        .setAuthor('YABOT (Yet Another Bot Of Toaster\'s)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')
        .setTitle('The balance wasn\'t a number!')
        .setDescription(`Please enter an integer value as the balance!`);
        message.channel.send(finalEmbed);
        return console.log(`[${time}] ${message.author.username} tried to make a bank account, but entered a non-int value for the balance.`);
      }
    }
    else {
      var object = {
        owner: author,
        name: accountName,
        balance: 0
      }
    }

    const final = JSON.stringify(object);

    try {
      fs.writeFileSync(`./commands/bank/${author}/${accountName}.json`, final);
    }
    catch (err) {
      fs.mkdirSync(`./commands/bank/${author}`);
      fs.writeFileSync(`./commands/bank/${author}/${accountName}.json`, final, (err) => {
        if (err) throw err;
      });
    }

    const finalEmbed = new Discord.RichEmbed()
    .setColor('#00ff00')
    .setAuthor('YABOT (Yet Another Bot Of Toaster\'s)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')
    .setTitle('Sucessfully added account!')
    .setDescription(`**Owner:** ${object.owner}\n**Name:** ${object.name}\n**Balance:** ${object.balance}`);
    message.channel.send(finalEmbed);
    console.log(`[${time}] ${message.author.username} made a bank account.`);
  },
};
