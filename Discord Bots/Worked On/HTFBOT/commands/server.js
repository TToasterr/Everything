const Discord = require('discord.js');

module.exports = {
  name: 'server',
  description: 'Get statistics for the server you\'re on!',
  usage: '',
  category: 'general',
  guildOnly: true,
  args: false,
  mod: false,
  execute(message, args, client, time, final, prefix) {
    const date = `${message.guild.createdAt}`.substring(0,16);
    final.addField('STATS', `**Name** - ${message.guild.name}\n**Members** - ${message.guild.memberCount}\n**Created** - ${date}\n**Region** - ${message.guild.region}`)
    .addBlankField()
    .addField('AVATAR', 'v')
    .setImage(message.guild.iconURL);

    message.channel.send(final);
    console.log(`[${time}] ${message.author.username} got server stats for the server ${message.guild.name}.`);
  },
};
