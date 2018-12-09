const Discord = require('discord.js');

module.exports = {
  name: 'server',
  description: 'Get statistics for the server you\'re on!',
  usage: '',
  category: 'general',
  guildOnly: true,
  args: false,
  execute(message, args) {
    const date = `${message.guild.createdAt}`.substring(0,16);
    const final = new Discord.RichEmbed()
    .setColor('#00ff00')
    .setAuthor('YABOT (Yet Another Bot Of Toaster\'s)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')
    .addField('STATS', `**Name** - ${message.guild.name}\n**Members** - ${message.guild.memberCount}\n**Created** - ${date}\n**Region** - ${message.guild.region}`)
    .addBlankField()
    .addField('AVATAR', 'v')
    .setImage(message.guild.iconURL);
    // .addField('Server Name', message.guild.name, true)
    // .addField('Member Count', message.guild.memberCount, true)
    // .addField('Created', `${message.guild.createdAt}`.substring(0,16), true)
    // .addField('Region', message.guild.region, true);

    message.channel.send(final);
    console.log(`${message.author.username} got server stats for the server ${message.guild.name}.`);
  },
};
