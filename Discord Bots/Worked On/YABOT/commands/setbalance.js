const Discord = require('discord.js');
const fs = require('fs');

module.exports = {
  name: 'setbalance',
  description: 'Set the balance for a bank account you own.',
  usage: '<name>, <balance>',
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

      if (isNaN(balanceInput)) {
        const finalEmbed = new Discord.RichEmbed()
        .setColor('#00ff00')
        .setAuthor('YABOT (Yet Another Bot Of Toaster\'s)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')
        .setTitle('The balance wasn\'t a number!')
        .setDescription(`Please enter an integer value as the balance!`);
        message.channel.send(finalEmbed);
        return console.log(`[${time}] ${message.author.username} tried to set a bank accounts balance, but entered a non-int value.`);
      }
    }
    else {
      const finalEmbed = new Discord.RichEmbed()
      .setColor('#00ff00')
      .setAuthor('YABOT (Yet Another Bot Of Toaster\'s)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')
      .setTitle('You didn\'t enter a balance!')
      .setDescription(`Please enter an integer value as the balance!`);
      message.channel.send(finalEmbed);
      return console.log(`[${time}] ${message.author.username} tried to set a bank accounts balance, but didnt enter a balance.`);
    }

    try {
      fileContent = fs.readFileSync(`./commands/bank/${author}/${accountName}.json`, (err) => {
        if (err) {
          const finalEmbed = new Discord.RichEmbed()
          .setColor('#00ff00')
          .setAuthor('YABOT (Yet Another Bot Of Toaster\'s)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')
          .setTitle('That bank account didnt work!')
          .setDescription(`Please check if:\n-The account exists\n-You own the account`);
          message.channel.send(finalEmbed);
          return console.log(`[${time}] ${message.author.username} tried to set a bank accounts balance, but didnt enter a valid account.`);
        };
      });
    }
    catch (err) {
      const finalEmbed = new Discord.RichEmbed()
      .setColor('#00ff00')
      .setAuthor('YABOT (Yet Another Bot Of Toaster\'s)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')
      .setTitle('That bank account didnt work!')
      .setDescription(`Please check if:\n-The account exists\n-You own the account`);
      message.channel.send(finalEmbed);
      return console.log(`[${time}] ${message.author.username} tried to set a bank accounts balance, but didnt enter a valid account.`);
    }

    var account = JSON.parse(fileContent);
    account.balance = balanceInput;
    const final = JSON.stringify(account);

    fs.writeFileSync(`./commands/bank/${author}/${accountName}.json`, final, (err) => {
      // fs.mkdirSync(`./commands/bank/${author}`);
      // fs.writeFileSync(`./commands/bank/${author}/${accountName}.json`, final, (err) => {
      if (err) throw err;
      // });
    });

    const finalEmbed = new Discord.RichEmbed()
    .setColor('#00ff00')
    .setAuthor('YABOT (Yet Another Bot Of Toaster\'s)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')
    .setTitle('Sucessfully changed balance!')
    .setDescription(`**Owner:** ${account.owner}\n**Name:** ${account.name}\n**Balance:** ${account.balance}`);
    message.channel.send(finalEmbed);
    console.log(`[${time}] ${message.author.username} set the balance of a bank account.`);
  },
};
