const Discord = require('discord.js');

module.exports = {
  name: 'user',
  description: 'Get data for a user!',
  usage: '<user>',
  guildOnly: false,
  args: false,
  execute(message, args) {
    if (!message.mentions.users.size) {
      const tagged = message.author;
      const final = new Discord.RichEmbed()
      .setColor('#00ff00')
      .setAuthor('YABOT (Yet Another Bot Of Toasters)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')
      .addField('STATS', `**Username** - ${tagged.username}\n**Created** - ` + `${tagged.createdAt}`.substring(0,16) + `\n**ID** - ${tagged.id}\n\n`)
      .addBlankField()
      .addField('AVATAR', 'v')
      .setImage(tagged.displayAvatarURL);

      message.channel.send(final);
      console.log(`${message.author.username} got their own stats.`);
    }

    else {
      const tagged = message.mentions.users.first();
      const final = new Discord.RichEmbed()
      .setColor('#00ff00')
      .setAuthor('YABOT (Yet Another Bot Of Toasters)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')
      .addField('STATS', `**Username** - ${tagged.username}\n**Created** - ` + `${tagged.createdAt}`.substring(0,16) + `\n**ID** - ${tagged.id}\n\n`)
      .addBlankField()
      .addField('AVATAR', 'v')
      .setImage(tagged.displayAvatarURL);

      message.channel.send(final);
      console.log(`${message.author.username} got the stats of ${tagged.username}.`);
    }
  },
};
