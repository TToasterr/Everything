const Discord = require('discord.js');
const fs = require('fs');

module.exports = {
  name: 'responses',
  description: 'List all autoresponse triggers and responses!',
  usage: '',
  category: 'autoresp',
  guildOnly: true,
  args: false,
  mod: false,
  execute(message, args, client, time, final, prefix, start) {
    final.setTitle('__All Suggestions__');

    // -----------------------------------------------------------------------------

    let autoresponses;

    try {
      let autoresponses = fs.readFileSync(`./autoresponders/${message.guild.name}.json`, (err) => {
        if (err) {
          final.setTitle(`Oops!`)
          .setDescription(`There are no autoresponse triggers for this server!`);

          message.channel.send(final);
          return console.log(`[${time}] ${message.author.username} tried to list autoresponse triggers for ${message.guild.name}, but there werent any.`);
          throw err;
        }
      });
    }
    catch (err) {
      final.setTitle(`Oops!`)
      .setDescription(`There are no autoresponse triggers for this server!`);

      message.channel.send(final);
      return console.log(`[${time}] ${message.author.username} tried to list autoresponse triggers for ${message.guild.name}, but there werent any.`);
      throw err;
    }

    if (autoresponses == `{}` || autoresponses == {}) {
      final.setTitle(`Oops!`)
      .setDescription(`There are no autoresponse triggers for this server!`);

      message.channel.send(final);
      return console.log(`[${time}] ${message.author.username} tried to list autoresponse triggers for ${message.guild.name}, but there werent any.`);
    }

    // -----------------------------------------------------------------------------

    autoresponses = JSON.parse(autoresponses);
    let keys = Object.keys(autoresponses);
    let description = `__*Trigger and response are shown.*__\n\n`;

    for (var key of keys) {
      description += `**${key}** - ${autoresponses[key]}\n`;
    }

    final.setDescription(description);

    message.channel.send(final);
    console.log(`[${time}] ${message.author.username} listed autoresponse triggers and responses for ${message.guild.name}.`);
  },
};
