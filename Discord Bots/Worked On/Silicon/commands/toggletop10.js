const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'toggletop10',
	description: 'Toggle the usage of the top 10 most used words in this channel!',
	usage: '',
	category: 'random',
	passThrough: false,
	autoExec: false,
	guildOnly: true,
	args: false,
	mod: true,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final) {
		let toggled = `on`;

		if (serverSettings[`top10channels`]) {
			if (serverSettings[`top10channels`].includes(channelID)) {
				let index = serverSettings[`top10channels`].indexOf(channelID);
				serverSettings[`top10channels`].splice(index, 1);
				toggled = `off`;
			}
			else {
				serverSettings[`top10channels`].push(channelID);
			}
		}
		else {
			serverSettings[`top10channels`] = [channelID];
		}

		final.setTitle(`__**Usage of the top 10 most used words has been turned ${toggled} in this channel!**__`)
			.setDescription(`Have fun!`);

		serverSettings = JSON.stringify(serverSettings);
		fs.writeFileSync(`./servers/${guildName}Settings.json`, serverSettings, (err) => {
			if (err) console.log(`Error writing to '${guildName}'s settings file:\n${err}\n`);
		});

		channel.send(final);
		console.log(`[${time}] ${authorName} turned top10words in ${channelName} ${toggled}.`);
	},
};