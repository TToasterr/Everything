const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'mostusedwords',
	description: 'Get the most used words in this server!',
	usage: '',
	category: 'random',
	passThrough: false,
	autoExec: false,
	guildOnly: true,
	args: false,
	mod: false,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final) {
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
		array.sort(function(a, b) {
			return a[1] - b[1];
		});

		wordarray = array.reverse();

		try {
			for (var i = 0; i < 10; i++) {
				finalarray.push(`**${wordarray[i][0]}** - ${wordarray[i][1]}`);
			}
		}
		catch (err) {
			finalarray = [`Whoops!`, `There arent even 10 different words used yet!`, `Talk some more, and then try again!`];
		}

		final.setTitle(`__**Top 10 most used words on ${guildName}:**__`)
			.setDescription(finalarray.join(`\n`));

		channel.send(final);
		console.log(`[${time}] ${authorName} listed the most used words in ${guildName}.`);
	},
};