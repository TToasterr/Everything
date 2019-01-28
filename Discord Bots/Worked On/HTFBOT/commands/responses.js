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
    // console.log(autoresponses + `01`);

    try {
      autoresponses = fs.readFileSync(`./autoresponders/${message.guild.name}.json`, (err) => {
        if (err) {
          // final.setTitle(`Oops!`)
          // .setDescription(`There are no autoresponse triggers for this server!`);
          //
          // message.channel.send(final);
          // return console.log(`[${time}] ${message.author.username} tried to list autoresponse triggers for ${message.guild.name}, but there werent any.`);
          // console.log(autoresponses + `02`);
          throw err;
        }
      });
      // console.log(autoresponses + `03`);
    }
    catch (err) {
      final.setTitle(`Oops!`)
      .setDescription(`There are no autoresponse triggers for this server!`);

      message.channel.send(final);
      // console.log(autoresponses + `04`);
      return console.log(`[${time}] ${message.author.username} tried to list autoresponse triggers for ${message.guild.name}, but there werent any.`);
      // throw err;
    }

    if (autoresponses == `{}`) {
      final.setTitle(`Oops!`)
      .setDescription(`There are no autoresponse triggers for this server!`);

      message.channel.send(final);
      // console.log(autoresponses + `05`);
      return console.log(`[${time}] ${message.author.username} tried to list autoresponse triggers for ${message.guild.name}, but there werent any.`);
    }

    // -----------------------------------------------------------------------------

    // console.log(autoresponses + `06`);
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
