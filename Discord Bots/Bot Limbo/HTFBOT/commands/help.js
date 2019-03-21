const Discord = require('discord.js');

module.exports = {
  name: 'help',
  description: 'Get some help.',
  usage: '',
  category: 'general',
  guildOnly: false,
  args: false,
  mod: false,
  execute(message, args, client, time, final, prefix, start) {

    if (args == '') {
      var general = [];
      var suggestions = [``];
      var autoresp = [``];
      var commands = message.client.commands.map(command => command);

      for (var i = 0; i < commands.length; i++) {
        if (commands[i].category == 'general' || commands[i].category == '') {
          general.push(commands[i].name);
        }
        else if (commands[i].category == 'sugg') {
          suggestions.push(commands[i].name);
        }
        else if (commands[i].category == `autoresp`) {
          autoresp.push(commands[i].name);
        }
      }

      final.setTitle('__**Here are all of my commands!**__')
      .setDescription('*Arguments must be seperated with a comma and space or it will return an error.*')
      .addField('General', '```' + general.join('\n') + '```')
      .addField('Suggestions', '```' + suggestions.join('\n') + '```')
      .addField('Autoresponder', '```' + autoresp.join('\n') + '```')
      .addField(`You can send \`${prefix}help <command name>\` to get info on a specific command!`, '[`My Github`](https://github.com/TToasterr/Everything/tree/master/Discord%20Bots/Worked%20On/HTFBOT)');

      message.channel.send(final);
      return console.log(`[${time}] ${message.author.username} got help.`);
    }

    const name = args[0].toLowerCase().substring(1);
    const command = message.client.commands.get(name);

    if (!command) {
        return message.channel.send('That\'s not a valid command!');
    }

    final.setTitle('**Name**')
    .setDescription('*Arguments must be seperated with a comma and space or it will return an error.*')
    .setDescription(command.name)
    .addField('**Description**', command.description)
    .addField('**Usage**', `${prefix}${command.name} ${command.usage}`);

    message.channel.send(final);
    console.log(`[${time}] ${message.author.username} got help.`);
  },
};
