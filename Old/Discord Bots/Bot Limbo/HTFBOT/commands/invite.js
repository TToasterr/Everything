const Discord = require('discord.js');

module.exports = {
  name: 'invite',
  description: 'Get an invite link for the bot!',
  usage: '',
  category: 'general',
  guildOnly: false,
  args: false,
  mod: false,
  execute(message, args, client, time, final, prefix, start) {
    final.setTitle('Invite Link')
    .setDescription('Add me to your server by clicking my name above!');

    message.channel.send(final);
    console.log(`[${time}] ${message.author.username} got an invite link for the bot.`);
  },
};
