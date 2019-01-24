const Discord = require('discord.js');

module.exports = {
  name: 'ping',
  description: 'Ping the bot!',
  usage: '',
  category: 'general',
  guildOnly: true,
  args: false,
  mod: false,
  execute(message, args, client, time, final, prefix) {
    final.setTitle(`Pong!`)
    .setDescription(`Im sorta too lazy to add a timer :p`);

    message.channel.send(final);
    console.log(`[${time}] ${message.author.username} pinged the bot from ${message.guild.name}.`);
  },
};
