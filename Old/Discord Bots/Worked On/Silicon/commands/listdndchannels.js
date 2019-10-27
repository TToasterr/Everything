const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'listdndchannels',
	description: 'List all DND enabled channels for this server!',
	usage: '',
	category: 'dnd',
	passThrough: true,
	autoExec: false,
	guildOnly: true,
	args: false,
	mod: false,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final, client) {
		let inCharacter = serverSettings[`DNDChannels`][`inCharacter`];
		let outOfCharacter = serverSettings[`DNDChannels`][`outOfCharacter`];
		let inCharacterList = [];
		let outOfCharacterList = [];

		if ((inCharacter == [] || inCharacter == '' || !inCharacter) && (outOfCharacter == [] || outOfCharacter == '' || !outOfCharacter)) {
			final.setTitle(`__**Whoops!**__`)
				.setDescription(`This server doesn't have any DND enabled channels!`);

			channel.send(final);
			return console.log(`[${time}] ${authorName} tried to list DND channels when there werent any.`);
		}



		if (inCharacter !== []) {
			for (var i in inCharacter) {
				inCharacterList.push(`<#${inCharacter[i]}>`);
			}
		}
		else {
			inCharacterList = [`No channels here!`];
		}


		if (outOfCharacter !== []) {
			for (var i in outOfCharacter) {
				outOfCharacterList.push(`<#${outOfCharacter[i]}>`);
			}
		}
		else {
			outOfCharacterList = [`No channels here!`];
		}

		final.setTitle(`__**All DND Enabled Channels in '${guildName}':**__`)
			.setDescription(`**In Character:**\n${inCharacterList.join("\n")}\n\n**Out of Character:**\n${outOfCharacterList.join("\n")}`)

		// serverSettings = JSON.stringify(serverSettings);
		// fs.writeFileSync(`./servers/${guildName}Settings.json`, serverSettings, (err) => {
		// 	if (err) console.log(`Error writing to '${guildName}'s settings file:\n${err}\n`);
		// });

		channel.send(final);
		console.log(`[${time}] ${authorName} listed DND channels for '${guildName}'.`);
	},
};