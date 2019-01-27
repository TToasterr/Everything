const Discord = require('discord.js');
const fs = require('fs');

module.exports = {
  name: 'delresponse',
  description: 'Delete an autoresponder trigger and response from the current server!',
  usage: '<trigger>, <response>',
  category: 'autoresp',
  guildOnly: true,
  args: true,
  mod: false,
  execute(message, args, client, time, final, prefix) {
    let autoresponses = false;
    try {
      autoresponses = fs.readFileSync(`./autoresponders/${message.guild.name}.json`, (err) => {
        if (err) throw err;
      });
    }
    catch (err) {
      final.setTitle(`Oops!`)
      .setDescription(`There are no autoresponses for this server, or the bot got an error trying to fetch them!`);

      message.channel.send(final);
      return console.log(`[${time}] ${message.author.usename} tried to delete an autoresponse, but there werent any for the server they were in.`);
    }

    // -----------------------------------------------------------------------------

    let trigger = args[0].substring(1);
    let response = args[1];
    let object = JSON.parse(autoresponses);

    if (object[trigger]) {
      if (object[trigger] == response) {
        delete object[trigger];
      }
      else {
        final.setTitle(`Oops!`)
        .setDescription(`There was a trigger with that name, but the response was different!\nDid you mean ${object[trigger]}?`);

        message.channel.send(final);
        return console.log(`[${time}] ${message.author.username} tried to delete an autoresponse, but there werent any with the response they gave!`);
      }
    }
    else {
      final.setTitle(`Oops!`)
      .setDescription(`There was no trigger with that name on this server!`);

      message.channel.send(final);
      return console.log(`[${time}] ${message.author.username} tried to delete an autoresponse, but there werent any with the trigger they gave!`);
    }

    let JSONObject = JSON.stringify(object);

    // -----------------------------------------------------------------------------

    fs.writeFileSync(`./autoresponders/${message.guild.name}.json`, JSONObject, (err) => {
      if (err) throw err;
    });

    final.setTitle('Sucessfully deleted trigger and response!')
    .setDescription(`**Trigger:** ${trigger}\n**Response:** ${response}`);

    message.channel.send(final);
    console.log(`[${time}] ${message.author.username} deleted an autoresponder for ${message.guild.name}.`);
  },
};
