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
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final, client) {
		if (serverSettings.top10channels) {
			if (serverSettings.top10channels.includes(channelID)) {
				let serverwordcount;
				let wordarray = [];
				let finalarray = [];
				let wordUsed = false;

				try {
					serverwordcount = fs.readFileSync(`./servers/${guild.id} wordcounts.json`, (err) => {
						if (err) throw err;
					});
				} catch (err) {
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
					try {
						if (content.includes(` ${wordarray[i][0]} `) || content == wordarray[i][0] || content.startsWith(wordarray[i][0] + ' ') || content.endsWith(' ' + wordarray[i][0])) {
							message.delete();
							finalarray.push(wordarray[i][0]);
							wordUsed = true;
						}
					} catch (err) {
						final.setTitle(`__**Whoops!**__`)
							.setDescription(`You have to have sent at least 10 messages (Not commands)\nin order to use this command (Though I don't know why you'd want to)`);
						channel.send(final);
						return console.log(`[${time}] ${authorName} tried to use top10words, but there havent been 10 words!`);
					}
				}

				if (wordUsed) {
					final.setTitle(`__**Whoops!**__`)
						.setDescription(`${authorName} used the following words:\n${finalarray.join("\n")}`);
					channel.send(final)
						.then(m => {
							m.delete(5000);
						});
				}
			}
		}
	}
};