const Discord = require('discord.js');

module.exports = {
  name: 'user',
  description: 'Get data for a user!',
  usage: '<user>',
  category: 'general',
  guildOnly: false,
  args: false,
  mod: false,
  execute(message, args, client, time, final, prefix) {
    if (!message.mentions.users.size) {
      const tagged = message.author;
      final.addField('STATS', `**Username** - ${tagged.username}\n**Created** - ` + `${tagged.createdAt}`.substring(0,16) + `\n**ID** - ${tagged.id}\n\n`)
      .addBlankField()
      .addField('AVATAR', 'v')
      .setImage(tagged.displayAvatarURL);

      message.channel.send(final);
      console.log(`[${time}] ${message.author.username} got their own stats.`);
    }

    else {
      const tagged = message.mentions.users.first();
      final.addField('STATS', `**Username** - ${tagged.username}\n**Created** - ` + `${tagged.createdAt}`.substring(0,16) + `\n**ID** - ${tagged.id}\n\n`)
      .addBlankField()
      .addField('AVATAR', 'v')
      .setImage(tagged.displayAvatarURL);

      message.channel.send(final);
      console.log(`[${time}] ${message.author.username} got the stats of ${tagged.username}.`);
    }
  },
};
