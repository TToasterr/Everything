const Discord = require('discord.js');

module.exports = {
  name: 'invite',
  description: 'Get an invite link for the bot!',
  usage: '',
  guildOnly: false,
  args: false,
  execute(message, args) {
    const final = new Discord.RichEmbed()
    .setColor('#00ff00')
    .setAuthor('YABOT (Yet Another Bot Of Toaster\'s)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')
    .setTitle('Invite Link')
    .setDescription('Add me to your server by clicking my name above!')
    message.channel.send(final);
    console.log(`${message.author.username} got an invite link for the bot.`);
  },
};
