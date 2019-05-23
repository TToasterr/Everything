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
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final, client) {
		if (args == '') {
			var general = [];
			var autoresponder = [];
			var marv = [];
			var dnd = [];
			var random = [];
			var commands = message.client.commands.map(command => command);

			for (var i = 0; i < commands.length; i++) {
				if (commands[i].name !== '' && !(commands[i].autoExec)) {
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
				.addField('General', serverPrefix + general.join(`\n${serverPrefix}`))
				.addField('Autoresponder', serverPrefix + autoresponder.join(`\n${serverPrefix}`))
				.addField('Marv', serverPrefix + marv.join(`\n${serverPrefix}`))
				.addField('DND', serverPrefix + dnd.join(`\n${serverPrefix}`))
				.addField('Random', serverPrefix + random.join(`\n${serverPrefix}`))
				.addField(`You can send \`${serverPrefix}help <command name>\` to get info on a specific command!`, '*Message `Toaster#0403` to suggest commands or changes!*');

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