const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'togglerandomradial',
	description: 'With this on, every message the bot recieves has a 1/500 chance of \ngetting responded to with a random image from r/radialblurredimages',
	usage: '',
	category: 'random',
	passThrough: false,
	autoExec: false,
	guildOnly: true,
	args: false,
	mod: true,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final) {
		let toggled = `on`;

		if (serverSettings[`randomRadial`]) {
			if (serverSettings.randomRadial == `on`) {
				toggled = `off`;
				serverSettings[`randomRadial`] = toggled;
			}
			else {
				toggled = `on`;
				serverSettings[`randomRadial`] = toggled;
			}
		}
		else {
			serverSettings[`randomRadial`] = toggled;
		}

		final.setTitle(`__**Deletion of the top 10 most used words has been turned ${toggled}!**__`)
			.setDescription(`Have fun!`);

		serverSettings = JSON.stringify(serverSettings);
		fs.writeFileSync(`./servers/${guild.id} Settings.json`, serverSettings, (err) => {
			if (err) console.log(`Error writing to '${guildName}'s settings file:\n${err}\n`);
		});

		channel.send(final);
		console.log(`[${time}] ${authorName} turned randomRadial ${toggled} in ${guildName}.`);
	},
};