const Discord = require('discord.js');

module.exports = {
  name: 'allservers',
  description: 'Lists all servers the bot is in!',
  usage: '',
  category: 'general',
  guildOnly: false,
  args: false,
  mod: false,
  execute(message, args, client) {
    const allGuilds = client.guilds.map(g => g.name);
    const guildMCount = client.guilds.map(g => g.memberCount);

    const final = new Discord.RichEmbed()
    .setColor('#00ff00')
    .setAuthor('BankerBot', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=530582447394521129&permissions=8&scope=bot')
    .setTitle('__**All Servers this bot is in, and their member counts.**__');

    var thing = '';

    for (var i = 0; i < allGuilds.length; i++) {
      thing += `\n**${allGuilds[i]}** - ${guildMCount[i]}`;
    }

    thing += `\n\n**Total Member Count** - ${client.users.size}`;
    final.setDescription(thing);

    message.channel.send(final);
    console.log(`${message.author.username} got the list of all servers the bot is in.`);
  },
};
