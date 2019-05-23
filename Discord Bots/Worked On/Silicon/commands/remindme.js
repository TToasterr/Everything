const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'remindme',
	description: 'Set a reminder for a time in the future, in seconds!',
	usage: '[time][s, m, or h], [reminder]',
	category: 'general',
	passThrough: false,
	autoExec: false,
	guildOnly: false,
	args: true,
	mod: false,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final, client) {
		let timee = args[0].slice(1);
		let type = args[0].slice(args[0].length - 1);


		// console.log(timee, type);


		try {
			timee = parseInt(timee);
		}
		catch (err) {
			final.setTitle(`__**Whoops!**__`)
				.setDescription(`You didn't use a number as the first argument!\n(Excluding the s (for seconds), m (for minutes), or h (for hours))`);

			channel.send(final);
			return console.log(`[${time}] ${authorName} tried to set a reminder, but didn't use a number as the time.`);
		}

		if (timee < 5 && type == 's') {
			final.setTitle(`__**Whoops!**__`)
				.setDescription(`You used too small a number! \nPlease enter a time more than 5 seconds.`);

			channel.send(final);
			return console.log(`[${time}] ${authorName} tried to set a reminder, but made the time less than 5s.`);
		}

		if (!args[1] || args[1] == '') {
			final.setTitle(`__**Whoops!**__`)
				.setDescription(`You didn't enter a reminder! \nPlease enter a message for me to remind you with!`);

			channel.send(final);
			return console.log(`[${time}] ${authorName} tried to set a reminder, but didn't set a message.`);
		}



		if (type == 's') {
			type = 'seconds';
		}
		else if (type == 'm') {
			type = 'minutes';
		}
		else if (type == 'h') {
			type = 'hours'
		}



		if (type.length < 5) {
			final.setTitle(`__**Whoops!**__`)
				.setDescription(`You didn't enter a correct time type! \nPlease enter s (for seconds), m (for minutes), or h (for hours).`);

			channel.send(final);
			return console.log(`[${time}] ${authorName} tried to set a reminder, but didn't use s m or h.`);
		}



		final.setTitle('__**Reminder set!**__')
			.setDescription(`I will remind you:\n'${args[1]}'\nin ${timee} ${type}.`);



		if (type == 'seconds') {
			setTimeout(function() {
				channel.send(`<@${author.id}>\n${args[1]}`);
			}, timee * 1000);
		}
		else if (type == 'minutes') {
			setTimeout(function() {
				channel.send(`<@${author.id}>\n${args[1]}`);
			}, (timee * 60) * 1000);
		}
		else {
			setTimeout(function() {
				channel.send(`<@${author.id}>\n${args[1]}`);
			}, ((timee * 60) * 60) * 1000);
		}



		channel.send(final);
		console.log(`[${time}] ${authorName} set a reminder for ${timee} ${type}.`);
	},
};