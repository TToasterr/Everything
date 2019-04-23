const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'Word Counter (Background Script)',
	description: 'Not a command!\nThe word counter counts the amount of times a word has been used in a server.\nUsing the mostusedwords command, you can list them!',
	usage: '',
	category: 'random',
	passThrough: false,
	autoExec: true,
	guildOnly: true,
	args: false,
	mod: false,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final) {
		let split = content.split(' ');
		let serverwordcount;

		try {
			serverwordcount = fs.readFileSync(`./servers/${guildName} wordcounts.json`, (err) => {
				if (err) throw err;
			});
		}
		catch (err) {
			serverwordcount = `{}`;
		}
		serverwordcount = JSON.parse(serverwordcount);

		for (let word of split) {
			word = word.replace(/`/g, '')
				.replace(/\~/g, '')
				.replace(/\!/g, '')
				.replace(/\^/g, '')
				.replace(/\*/g, '')
				.replace(/\(/g, '')
				.replace(/\)/g, '')
				.replace(/\[/g, '')
				.replace(/\]/g, '')
				.replace(/\{/g, '')
				.replace(/\}/g, '')
				.replace(/\:/g, '')
				.replace(/\'/g, '')
				.replace(/\"/g, '')
				.replace(/\,/g, '')
				.replace(/\./g, '')
				.replace(/\</g, '')
				.replace(/\>/g, '')
				.replace(/\//g, '')
				.replace(/\\/g, '')
				.replace(/\_/g, '')
				.replace(/\+/g, '')
				.replace(/\-/g, '')
				.replace(/\=/g, '')

			if (serverwordcount[word.toLowerCase()]) {
				serverwordcount[word.toLowerCase()]++;
			}
			else {
				serverwordcount[word.toLowerCase()] = 1;
			}
		}

		serverwordcount = JSON.stringify(serverwordcount);
		fs.writeFileSync(`./servers/${guildName} wordcounts.json`, serverwordcount, (err) => {
			if (err) console.log(`Error writing to '${guildName}'s wordcount file:\n${err}\n`);
		});
	},
};