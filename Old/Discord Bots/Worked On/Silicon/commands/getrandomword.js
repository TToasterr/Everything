const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'getrandomword',
	description: 'Get a random word from this server!',
	usage: '',
	category: 'random',
	passThrough: false,
	autoExec: false,
	guildOnly: true,
	args: false,
	mod: false,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final, client) {
		let serverwordcount;
		let wordarray = [];
		let finalarray = [];

		try {
			serverwordcount = fs.readFileSync(`./servers/${guild.id} wordcounts.json`, (err) => {
				if (err) throw err;
			});
		}
		catch (err) {
			serverwordcount = `{}`;
		}
		serverwordcount = JSON.parse(serverwordcount);

		let keys = Object.keys(serverwordcount);
		let array = [];
		for (let word in serverwordcount) {
			array.push([word, serverwordcount[word]]);
		}

		let randint = Math.floor(Math.random() * array.length)
		finalarray.push(`**${array[randint][0]}** - ${array[randint][1]}`);

		final.setTitle(`__**A random word from ${guildName}:**__`)
			.setDescription(finalarray.join(`\n`));

		channel.send(final);
		console.log(`[${time}] ${authorName} got a random word from ${guildName}.`);
	},
};