const Discord = require('discord.js');

module.exports = {
  name: 'ping',
  description: 'Ping the bot!',
  usage: '',
  category: 'general',
  guildOnly: true,
  args: false,
  mod: false,
  execute(message, args, client) {
    message.channel.send('Pong!');
    console.log(`${message.author.username} pinged the bot from ${message.guild.name}.`);
  },
};
