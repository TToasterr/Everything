const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'leastusedwords',
	description: 'Get the least used words in this server!',
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

		wordarray = array;
		let thing = false;
		let i = 0;
		let array1;
		let array2;
		let array3;
		let array4;

		// for (var i = 0; i < 10; i++) {
		// 	finalarray.push(`**${wordarray[i][0]}** - ${wordarray[i][1]}`);
		// }

		while (!thing) {
			if (wordarray[i][1] == 1) {
				finalarray.push(`${wordarray[i][0]}`);
			}
			else {
				thing = true;
			}
			i++;
		}

		if (finalarray.join('\n').length > 2048) {
			finalarray = finalarray.join(" ").slice(0, 2047).split(" ");
			array1 = finalarray.join(" ").slice(2047).split(" ");
			if (array1 !== `` && array1 !== [] && array1 !== [``] && array1.join("\n") !== '' && array1.join("\n") !== '\n') {
				final.addField(`1`, array1.join(`\n`));
			}
		}

		final.setTitle(`__**All words with only one use on ${guildName}:**__`)
			.setDescription(finalarray.join(`\n`));

		channel.send(final);
		console.log(`[${time}] ${authorName} listed the least used words in ${guildName}.`);
	},
};