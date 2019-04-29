const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'togglerandom',
	description: 'Toggle on/off the random commands that the community makes!',
	usage: '',
	category: 'random',
	passThrough: true,
	autoExec: false,
	guildOnly: true,
	args: false,
	mod: true,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final) {
		let state;

		if (serverSettings[`random`]) {
			state = `off`;
			serverSettings[`random`] = false;
		}
		else {
			state = `on`;
			serverSettings[`random`] = true;
		}

		final.setTitle(`__**Community Commands Toggled!**__`)
			.setDescription(`Community commands are now ${state}.`);

		serverSettings = JSON.stringify(serverSettings);
		fs.writeFileSync(`./servers/${guildName}Settings.json`, serverSettings, (err) => {
			if (err) console.log(`Error writing to '${guildName}'s settings file:\n${err}\n`);
		});

		channel.send(final);
		console.log(`[${time}] ${authorName} toggled community commands ${state} for '${guildName}'.`);
	},
};