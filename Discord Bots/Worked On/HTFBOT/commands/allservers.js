const Discord = require('discord.js');

module.exports = {
  name: 'allservers',
  description: 'Lists all servers the bot is in!',
  usage: '',
  category: 'general',
  guildOnly: false,
  args: false,
  mod: false,
  execute(message, args, client, time, final, prefix, start) {
    const allGuilds = client.guilds.map(g => g.name);
    const guildMCount = client.guilds.map(g => g.memberCount);

    final.setTitle('__**All Servers this bot is in, and their member counts.**__');

    var thing = '';

    for (var i = 0; i < allGuilds.length; i++) {
      thing += `\n**${allGuilds[i]}** - ${guildMCount[i]}`;
    }

    thing += `\n\n**Total Member Count** - ${client.users.size}`;
    final.setDescription(thing);

    message.channel.send(final);
    console.log(`[${time}] ${message.author.username} got the list of all servers the bot is in.`);
  },
};
