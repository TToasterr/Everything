const Discord = require('discord.js');

module.exports = {
  name: 'choose',
  description: 'Make the bot choose between two or more items!',
  usage: '<choice 1>, <choice 2>, [choice 3]...',
  category: 'general',
  guildOnly: false,
  args: false,
  mod: false,
  execute(message, args, client) {
    args[0] = args[0].substring(1);

    if (!args[1] || args[1] == '') {
      return message.channel.send(`You didnt\'t provide the necesarry arguments!\nThe proper usage would be \`--choose <choice 1>, <choice 2>, [choice 3]...\``);
    }

    var randInt = Math.floor(Math.random() * args.length);

    const final = new Discord.RichEmbed()
    .setColor('#00ff00')
    .setAuthor('YABOT (Yet Another Bot Of Toaster\'s)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')
    .setTitle('Options')
    .setDescription(args.join(', '))
    .addField('My Choice', args[randInt]);
    message.channel.send(final);
    console.log(`${message.author.username} made the bot make a choice.`);
  },
};
