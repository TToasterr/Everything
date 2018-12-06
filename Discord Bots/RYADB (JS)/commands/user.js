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
      .addBlankField()
      .addField('Username', tagged.username, true)
      .addField('Creation Date', `${tagged.createdAt}`.substring(0,16), true)
      .addBlankField()
      .addField('ID', tagged.id, true)
      .addField('Avatar', 'v', true)
      .setImage(tagged.displayAvatarURL);

      message.channel.send(final);
      // message.channel.send(`**Username:** ${tagged.username}\n**Account Creation Date:** ${tagged.createdAt}\n**ID:** ${tagged.id}\n**Avatar:** ${tagged.displayAvatarURL}`);
      console.log(`${message.author.username} got their own stats.`);
    }

    else {
      const tagged = message.mentions.users.first();
      const final = new Discord.RichEmbed()
      .setColor('#00ff00')
      .setAuthor('YABOT (Yet Another Bot Of Toasters)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')
      .addBlankField()
      .addField('Username', tagged.username, true)
      .addField('Creation Date', `${tagged.createdAt}`.substring(0,16), true)
      .addBlankField()
      .addField('ID', tagged.id, true)
      .addField('Avatar', 'v', true)
      .setImage(tagged.displayAvatarURL);

      message.channel.send(final);
      // message.channel.send(`**Username:** ${tagged.username}\n**Account Creation Date:** ${tagged.createdAt}\n**ID:** ${tagged.id}\n**Avatar:** ${tagged.displayAvatarURL}`);
      console.log(`${message.author.username} got the stats of ${tagged.username}.`);
    }
  },
};
