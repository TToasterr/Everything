const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'listallusers',
	description: 'List all users in the server!',
	usage: '',
	category: 'management',
	passThrough: false,
	autoExec: false,
	guildOnly: true,
	args: false,
	mod: true,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final, client) {
		let members = message.guild.members.map(member => member.user.username).join('\n');

		if (members.length > 2048) {
			let thing1 = members.slice(0, 2047);
			let thing2 = members.slice(2047);
			final.setDescription(thing1);
			if (thing2.length > 1024) {
				let half2half1 = thing2.slice(0, 1023);
				let half2half2 = thing2.slice(1023);
				final.addField('*(2048 character limit break)*', half2half1)
					.addField('*(1024 character limit break)*', half2half2);
			}
			else {
				final.addField('*(2048 character limit break)*', thing2);
			}
		}
		else {
			final.setDescription(members);
		}

		final.setTitle(`__**All users in ${guildName}:**__`)
		// .setDescription(`${members.join('\n')}`);
		// .addField('', '');

		// serverSettings = JSON.stringify(serverSettings);
		// fs.writeFileSync(`./servers/${guild.id}Settings.json`, serverSettings, (err) => {
		// 	if (err) console.log(`Error writing to '${guildName}'s settings file:\n${err}\n`);
		// });

		channel.send(final);
		console.log(`[${time}] ${authorName} listed all users in ${guildName}.`);
	},
};