const Discord = require('discord.js');

module.exports = {
  name: 'verynotthis',
  description: 'VERY Disagrees with a message.',
  usage: '<amount of messages up>',
  category: 'this',
  guildOnly: true,
  args: false,
  mod: false,
  execute(message, args, client, time) {
    var amount;
    var noarg;
    if (args == '') {
      amount = 1;
      noarg = 1;
    } else {
      amount = parseInt(args[0].substring(1), 10);
      noarg = 1;
    }

    const author = message.author;
    message.delete(1000);

    message.channel.fetchMessages({
      limit: amount + noarg,
    }).then((messages) => {
      var i = 0;
      messages.forEach(function(message) {
        var a = 0;
        if (message.author.bot) {
          var a = 1;
        }
        i++;
        if (i >= (amount + noarg) && a == 0) {
          message.channel.send(`${author} HATES ${message.author}'s message,\n\`${message.content}\``);
        }
      })
    });
    console.log(`[${time}] ${message.author.username} VERY disagreed with a message.`);
  },
};
