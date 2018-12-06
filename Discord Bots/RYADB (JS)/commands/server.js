const Discord = require('discord.js');

module.exports = {
  name: 'server',
  description: 'Get statistics for the server you\'re on!',
  usage: '',
  guildOnly: true,
  args: false,
  execute(message, args) {
    const final = new Discord.RichEmbed()
    .setColor('#00ff00')
    .setAuthor('YABOT (Yet Another Bot Of Toasters)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')
    .addBlankField()
    .addField('Server Name', message.guild.name, true)
    .addField('Member Count', message.guild.memberCount, true)
    .addBlankField()
    .addField('Created', `${message.guild.createdAt}`.substring(0,16), true)
    .addField('Region', message.guild.region, true);

    message.channel.send(final);
    console.log(`${message.author.username} got server stats for the server ${message.guild.name}.`);
  },
};
