const Discord = require('discord.js');

module.exports = {
  name: 'botstats',
  description: 'Get the stats for the bot!',
  usage: '',
  category: 'general',
  guildOnly: false,
  args: false,
  mod: false,
  execute(message, args, client, time, final, prefix, start) {
    final.setTitle('BOT STATS')
    .setDescription(`**Server Count** - ${client.guilds.size}\n**Channel Count** - ${client.channels.size}\n**User Count** - ${client.users.size}`);

    message.channel.send(final);
    console.log(`[${time}] ${message.author.username} got the stats for the bot.`);
  },
};
