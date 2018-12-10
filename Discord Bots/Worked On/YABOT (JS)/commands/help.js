const { prefix } = require('../config.json');
const Discord = require('discord.js');

module.exports = {
  name: 'help',
  description: 'Get some help.',
  usage: '',
  category: 'general',
  guildOnly: false,
  args: false,
  mod: false,
  execute(message, args, client) {

    if (args == '') {
      var general = [];
      var thiss = [''];
      var suggestions = [''];
      var commands = message.client.commands.map(command => command);

      for (var i = 0; i < commands.length; i++) {
        if (commands[i].category == 'general' || commands[i].category == '') {
          general.push(commands[i].name);
        }
        else if (commands[i].category == 'this') {
          thiss.push(commands[i].name);
        }
        else if (commands[i].category == 'sugg') {
          suggestions.push(commands[i].name);
        }
      }

      const final = new Discord.RichEmbed()
      .setColor('#00ff00')
      .setAuthor('YABOT (Yet Another Bot Of Toaster\'s)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')
      .setTitle('__**Here are all of my commands!**__')
      .addField('General', '```' + general.join('\n') + '```')
      .addField('This', '```' + thiss.join('\n') + '```')
      .addField('Suggestions', '```' + suggestions.join('\n') + '```')
      .addField(`You can send \`${prefix}help <command name>\` to get info on a specific command!`, 'Have fun!');

      message.channel.send(final);
      return console.log(`${message.author.username} got help.`);
    }

    const name = args[0].toLowerCase().substring(1);
    const command = message.client.commands.get(name);

    if (!command) {
        return message.channel.send('That\'s not a valid command!');
    }

    const final = new Discord.RichEmbed()
    .setColor('#ff0000')
    .setAuthor('YABOT (Yet Another Bot Of Toaster\'s)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')
    .setTitle('**Name**')
    .setDescription(command.name)
    .addField('**Description**', command.description)
    .addField('**Usage**', `${prefix}${command.name} ${command.usage}`);

    message.channel.send(final);
    console.log(`${message.author.username} got help.`);
  },
};
