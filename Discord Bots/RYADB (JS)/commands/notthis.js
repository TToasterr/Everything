const Discord = require('discord.js');

module.exports = {
  name: 'notthis',
  description: 'Disagrees with a message.',
  usage: '<amount of messages up>',
  guildOnly: true,
  args: false,
  execute(message, args) {
    var amount;
    var noarg;
    if (args == '') {
      amount = 1;
      noarg = 1;
    } else {
      amount = parseInt(args[0].substring(1), 10);
      noarg = 1;
    }

    const author = message.author.username;
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
          // message.react('✅').catch(console.error);
          message.channel.send(`${author} doesn't like ${message.author}'s message,\n\`${message.content}\``);
        }
      })
    });
    // message.channel.send('');
    // message.channel.send(`Amount: ${amount}\nNoarg: ${noarg}\nFinal: ${amount + noarg}`)
    console.log(`${message.author.username} disagreed with a message.`);
  },
};
