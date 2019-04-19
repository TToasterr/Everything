const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'help',
	description: 'Gives you help on all commands the bot has!',
	usage: '<command name>',
	category: 'general',
	passThrough: false,
	autoExec: false,
	guildOnly: false,
	args: false,
	mod: false,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final) {
		if (args == '') {
			var general = [];
			var autoresponder = [];
			var marv = [];
			var dnd = [];
			var random = [];
			var commands = message.client.commands.map(command => command);

			for (var i = 0; i < commands.length; i++) {
				if (commands[i].name !== '') {
					if (commands[i].category == 'general' || commands[i].category == '') {
						general.push(commands[i].name);
					}
					else if (commands[i].category == 'autoresponder') {
						autoresponder.push(commands[i].name);
					}
					else if (commands[i].category == `marv`) {
						marv.push(commands[i].name);
					}
					else if (commands[i].category == `dnd`) {
						dnd.push(commands[i].name);
					}
					else if (commands[i].category == `random`) {
						random.push(commands[i].name);
					}
				}
			}

			final.setTitle('__**Here are all of my commands!**__')
				.setDescription('*Arguments must be seperated with a comma and space or it will return an error.*')
				.addField('General', '-' + general.join('\n-'))
				.addField('Autoresponder', '-' + autoresponder.join('\n-'))
				.addField('Marv', '-' + marv.join('\n-'))
				.addField('DND', '-' + dnd.join('\n-'))
				.addField('Random', '-' + random.join('\n-'))
				.addField(`You can send \`${serverPrefix}help <command name>\` to get info on a specific command!`, '[`My Github`](https://github.com/TToasterr/Everything/tree/master/Discord%20Bots/Worked%20On/Silicon)');

			channel.send(final);
			return console.log(`[${time}] ${authorName} got help.`);
		}

		const name = args[0].toLowerCase().substring(1);
		const command = message.client.commands.get(name);

		if (!command) {
			final.setTitle(`__**Whoops!**__`)
				.setDescription(`That's not a valid command!`);

			channel.send(final);
			return console.log(`[${time}] ${authorName} tried to get help for a command that doesn't exist.`);
		}

		final.setTitle(`**${command.name}**`)
			.setDescription(command.description)
			.addField('**Usage**', `${serverPrefix}${command.name} ${command.usage}`);

		channel.send(final);
		console.log(`[${time}] ${authorName} got help for ${command.name}.`);
	},
};