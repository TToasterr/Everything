const discord = require('discord.js');
const fs = require('fs');
const pup = require('random-puppy');

module.exports = {
	name: 'Random Radial',
	description: 'Every message has a 1/500 chance of getting responded to with an image from r/radialblurredimages, if toggled on.',
	usage: '',
	category: 'random',
	passThrough: false,
	autoExec: true,
	guildOnly: true,
	args: false,
	mod: false,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final) {
		if (serverSettings.randomRadial == `on`) {
			pup(`radialblurredimages`).then(data => {
				channel.send(data);
			});
		}
	}
};