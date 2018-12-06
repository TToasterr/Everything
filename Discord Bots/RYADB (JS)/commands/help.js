const { prefix } = require('../config.json');
const Discord = require('discord.js');

module.exports = {
  name: 'help',
  description: 'Get some help.',
  usage: '',
  guildOnly: false,
  args: false,
  execute(message, args) {
    // const data = [];

    if (args == '') {
      // data.push('Here\'s a list of all my commands!\n\`');
      // data.push(message.client.commands.map(command => command.name).join('\n'));
      // data.push(`\`\nYou can send \`${prefix}help <command name> \` to get info on a specific command!`);
      const final = new Discord.RichEmbed()
      .setColor('#00ff00')
      .setAuthor('YABOT (Yet Another Bot Of Toasters)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')
      .setTitle('Here are all of my commands!')
      .setDescription('```' + message.client.commands.map(command => command.name).join('\n') + '```')
      .addField(`You can send \`${prefix}help <command name>\` to get info on a specific command!`, 'Have fun!');

      // message.channel.send(data, { split: true });
      message.channel.send(final);
      return console.log(`${message.author.username} got help.`);
    }

    const name = args[0].toLowerCase().substring(1);
    const command = message.client.commands.get(name);

    // console.log(command);

    if (!command) {
        return message.channel.send('That\'s not a valid command!');
    }

    // data.push(`**Name:** ${command.name}`);
    // data.push(`**Description:** ${command.description}`);
    // data.push(`**Usage:** ${prefix}${command.name} ${command.usage}`);
    const final = new Discord.RichEmbed()
    .setColor('#ff0000')
    .setAuthor('YABOT (Yet Another Bot Of Toasters)', 'https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048', 'https://discordapp.com/api/oauth2/authorize?client_id=519640938667048960&permissions=8&scope=bot')
    .setTitle('**Name**')
    .setDescription(command.name)
    .addField('**Description**', command.description)
    .addField('**Usage**', `${prefix}${command.name} ${command.usage}`);

    // message.channel.send(data, { split: true });
    message.channel.send(final);
    console.log(`${message.author.username} got help.`);
  },
};
