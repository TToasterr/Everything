const Discord = require('discord.js');
const hrtime = require('process');

module.exports = {
  name: 'ping',
  description: 'Ping the bot!',
  usage: '',
  category: 'general',
  guildOnly: true,
  args: false,
  mod: false,
  execute(message, args, client, time, final, prefix, start) {
    final.setTitle(`Pong!`)
    .setDescription(`Took ${process.hrtime(start, `us`)}us`);

    message.channel.send(final);
    console.log(`[${time}] ${message.author.username} pinged the bot from ${message.guild.name}.`);
  },
};
