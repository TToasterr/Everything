const Discord = require('discord.js');

module.exports = {
  name: 'botstats',
  description: 'Get the stats for the bot!',
  usage: '',
  category: 'general',
  guildOnly: false,
  args: false,
  mod: false,
  execute(message, args, client) {
    const final = new Discord.RichEmbed()
    .setColor('#00ff00')
    .setAuthor('YABOT (Yet Another Bot Of Toaster\'s)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')
    .setTitle('BOT STATS')
    .setDescription(`**Server Count** - ${client.guilds.size}\n**Channel Count** - ${client.channels.size}\n**User Count** - ${client.users.size}`);
    message.channel.send(final);
    console.log(`${message.author.username} got the stats for the bot.`);
  },
};
