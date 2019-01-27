const Discord = require('discord.js');
const fs = require('fs');

module.exports = {
  name: 'addresponse',
  description: 'Add an autoresponder trigger and response to the current server!',
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
      autoresponses = false;
    }

    // -----------------------------------------------------------------------------

    let trigger = args[0].substring(1);
    let response = args[1];

    let object = {};

    if (autoresponses) {
      object = JSON.parse(autoresponses);
    }
    else {
      object = {}
    }

    object[trigger] = response

    let JSONObject = JSON.stringify(object);

    // -----------------------------------------------------------------------------

    fs.writeFileSync(`./autoresponders/${message.guild.name}.json`, JSONObject, (err) => {
      if (err) throw err;
    });

    final.setTitle('Sucessfully added trigger and response!')
    .setDescription(`**Trigger:** ${trigger}\n**Response:** ${response}`);

    message.channel.send(final);
    console.log(`[${time}] ${message.author.username} made an autoresponder for ${message.guild.name}.`);
  },
};
