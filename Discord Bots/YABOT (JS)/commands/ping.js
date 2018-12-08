const Discord = require('discord.js');

module.exports = {
  name: 'ping',
  description: 'Ping the bot!',
  usage: '',
  guildOnly: true,
  args: false,
  execute(message, args) {
    message.channel.send('Pong!');
    console.log(`${message.author.username} pinged the bot from ${message.guild.name}.`);
  },
};
