const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'Top 10 Deleter',
	description: 'Removes messages that include the top 10 most used words, if toggled on.',
	usage: '',
	category: 'random',
	passThrough: false,
	autoExec: true,
	guildOnly: true,
	args: false,
	mod: false,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final) {
		if (serverSettings.top10channels) {
			if (serverSettings.top10channels.includes(channelID)) {
				let serverwordcount;
				let wordarray = [];
				let finalarray = [];

				try {
					serverwordcount = fs.readFileSync(`./servers/${guildName} wordcounts.json`, (err) => {
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

				for (var i = 0; i < 10; i++) {
					if (content.includes(` ${wordarray[i][0]} `) || content == wordarray[i][0]) {
						message.delete();
					}
				}
			}
		}
	}
};