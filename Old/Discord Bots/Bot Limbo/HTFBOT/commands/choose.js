const Discord = require('discord.js');

module.exports = {
  name: 'choose',
  description: 'Make the bot choose between two or more items!',
  usage: '<choice 1>, <choice 2>, [choice 3]...',
  category: 'general',
  guildOnly: false,
  args: false,
  mod: false,
  execute(message, args, client, time, final, prefix, start) {
    args[0] = args[0].substring(1);

    if (!args[1] || args[1] == '') {
      return message.channel.send(`You didnt\'t provide the necesarry arguments!\nThe proper usage would be \`--choose <choice 1>, <choice 2>, [choice 3]...\``);
    }

    var randInt = Math.floor(Math.random() * args.length);

    final.setTitle('Options')
    .setDescription(args.join('\n'))
    .addField('My Choice', args[randInt]);
    message.channel.send(final);
    console.log(`[${time}] ${message.author.username} made the bot make a choice.`);
  },
};
