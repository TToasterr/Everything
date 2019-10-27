const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'roll',
	description: 'Roll a dice.',
	usage: '[amount (can be 6, 2d20, or percentile)]',
	category: 'dnd',
	passThrough: true,
	autoExec: false,
	guildOnly: true,
	args: true,
	mod: false,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final, client) {
		if (serverSettings[`DNDChannels`][`inCharacter`].includes(channelID)) message.delete();

		args[0] = args[0].slice(1);
		let number;

		if (args[0] == `e`) {
			let output;
			try {
				output = eval(args[1]);
			}
			catch (err) {
				output = err;
			}
			final.setTitle(`*spooky*`)
				.setDescription(output);
		}
		else if (args[0] == `percentile`) {
			number = (Math.round(Math.random() * 9) + 1) * 10;
			final.setTitle(`__**${authorName} rolled percentile.**__`)
				.setDescription(`They got ${number}`);
		}
		else if (args[0].includes('d')) {
			let finalNumbers = [];
			let amountToRoll = args[0].split('d')[0];
			let maxAmount;
			if (args[0].includes('+')) {
				maxAmount = args[0].split('d')[1].split('+')[0];
			}
			else if (args[0].includes('-')) {
				maxAmount = args[0].split('d')[1].split('-')[0];
			}
			else {
				maxAmount = args[0].split('d')[1];
			}
			for (var i = 0; i < amountToRoll; i++) {
				number = (Math.round(Math.random() * (maxAmount - 1)) + 1);
				if (args[0].includes('+')) {
					number = parseInt(number) + parseInt(args[0].split('+')[1]);
				}
				else if (args[0].includes('-')) {
					number = parseInt(number) - parseInt(args[0].split('-')[1]);
				}
				finalNumbers.push(number);
			}

			if (`**They got:**\n${finalNumbers.join(", ")}`.length > 2048) {
				final.setTitle(`__**${authorName} tried to roll a d${maxAmount} ${amountToRoll} time(s).**__`)
					.setDescription(`The character amount exceeded 2,048 characters.\nPlease don't break me ;(`);
			}
			else {
				if (args[0].includes('+')) {
					final.setTitle(`__**${authorName} rolled a d${maxAmount} ${amountToRoll} time(s) with a modifier of +${args[0].split('+')[1]}.**__`);
				}
				else if (args[0].includes('-')) {
					final.setTitle(`__**${authorName} rolled a d${maxAmount} ${amountToRoll} time(s) with a modifier of -${args[0].split('-')[1]}.**__`);
				}
				else {
					final.setTitle(`__**${authorName} rolled a d${maxAmount} ${amountToRoll} time(s).**__`);
				}
				final.setDescription(`**They got:**\n${finalNumbers.join(", ")}`);

				if (amountToRoll > 1) {
					let total = 0;
					for (let number of finalNumbers) {
						total += parseInt(number);
					}
					final.addField(`Stats:`, `**Average:** ${total/parseInt(amountToRoll)}\n**Total:** ${total}`);
				}
			}
		}
		else {
			number = Math.round(Math.random() * (args[0] - 1)) + 1;
			final.setTitle(`__**${authorName} rolled a d${args[0]}.**__`)
				.setDescription(`They got ${number}`);
		}

		channel.send(final);
		console.log(`[${time}] ${authorName} rolled a die.`);
	},
};