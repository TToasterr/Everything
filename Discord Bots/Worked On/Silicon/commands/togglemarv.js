const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'togglemarv',
	description: 'Toggle on/off the marv (SCP) commands!',
	usage: '',
	category: 'marv',
	passThrough: true,
	autoExec: false,
	guildOnly: true,
	args: false,
	mod: true,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final) {
		let state;

		if (serverSettings[`marv`]) {
			state = `off`;
			serverSettings[`marv`] = false;
		}
		else {
			state = `on`;
			serverSettings[`marv`] = true;
		}

		final.setTitle(`__**Marv Commands Toggled!**__`)
			.setDescription(`Marv commands are now ${state}.`);

		serverSettings = JSON.stringify(serverSettings);
		fs.writeFileSync(`./servers/${guild.id} Settings.json`, serverSettings, (err) => {
			if (err) console.log(`Error writing to '${guildName}'s settings file:\n${err}\n`);
		});

		channel.send(final);
		console.log(`[${time}] ${authorName} toggled marv commands ${state} for '${guildName}'.`);
	},
};