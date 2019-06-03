const discord = require('discord.js');
const fs = require('fs');

module.exports = {
	name: 'arandomrole',
	description: 'Assign either everyone, or everyone already in a role, a random role\neither picked using arguments, or out of every role.\n\nTo exclude a role, add it in the arguments with a \'!\' in front of it.\n\n*This command is currently in progress, and doesn\'t actually assign any roles yet.*',
	usage: '[e (everyone) or role name], <role 1 name>, <role 2 name>..',
	category: 'management',
	passThrough: false,
	autoExec: false,
	guildOnly: true,
	args: true,
	mod: true,
	execute(message, content, args, author, authorName, channel, channelName, channelID, guild, guildName, serverPrefix, time, serverSettings, final, client) {
		let role1;
		let role2;
		let arr = [];
		let startingRole;
		let everyone = false;
		let includeCount = 0;
		let excludeCount = 0;
		let includedRoles = [];
		let excludedRoles = [];
		let members = message.guild.members.map(member => member);
		let roles = message.guild.roles.map(role => role);
		args[0] = args[0].slice(1);



		function check2048(array) {
			array = array.join('\n');
			if (arr.length > 2048) {
				let half1 = array.slice(0, 2047);
				let half2 = array.slice(2047);
				final.setDescription(half1);

				if (half2.length > 1024) {
					let half2half1 = half2.slice(0, 1023);
					let half2half2 = half2.slice(1023);

					if (half2half2.length > 1024) {
						final.setDescription("Whoops, The user list is too long for me to display.\nAll the roles were changed, though!");
					} else {
						final.addField('*(2048 character limit break)*', half2half1)
							.addField('*(1024 character limit break)*', half2half2);
					}
				} else {
					final.addField('*(2048 character limit break)*', half2);
				}
			} else {
				final.setDescription(arr);
			}
		}



		if (args[0] == 'e') {
			everyone = true;
		}



		if (everyone) {
			if (!args[1]) {
				for (let member of members) {
					let num = Math.floor(Math.random() * roles.length);
					// member.addRoles(roles[num].id);
					arr.push(`**${member.user.username}:** ${roles[num].name}`);
				}

				check2048(arr);
				final.setTitle(`__**All users in the server have now been assigned random roles!**__`);
				channel.send(final);
				return console.log(`[${time}] ${authorName} gave everyone in ${guildName} a random role.`);
			} else {
				for (let num in args) {
					// console.log(num);
					// console.log(args[num]);
					if (num > 0) {
						let tempArg;
						if (args[num].includes('everyone')) {
							args[num] = args[num].replace('everyone', '@everyone');
						}
						if (args[num].startsWith('!')) {
							tempArg = args[num].slice(1);
						} else {
							tempArg = args[num];
						}
						if (message.guild.roles.find('name', tempArg)) {
							let role = message.guild.roles.find('name', tempArg);
							if (args[num].startsWith('!')) {
								excludeCount++;
								excludedRoles.push(role.name);
							} else {
								includeCount++;
								includedRoles.push(role.name);
							}
						} else {
							final.setTitle(`__**Whoops!**__`)
								.setDescription(`One of the roles you used doesnt exist in this server!\nPlease make sure you spelled everything right.`);
							channel.send(final);
							return console.log(`[${time}] ${authorName} tried to give everyone in ${guildName} a random role, but didnt input a role that existed.`);
						}
					}
				}
				if (includeCount == 0) {
					for (let member of members) {
						let num = Math.floor(Math.random() * roles.length);
						while (excludedRoles.includes(roles[num].name)) {
							num = Math.floor(Math.random() * roles.length);
						}
						// member.addRoles(roles[num].id);
						arr.push(`**${member.user.username}:** ${roles[num].name}`);
					}

					check2048(arr);
					final.setTitle(`__**All users in the server have now been assigned random roles!**__\n*Excluding: '${excludedRoles.join("', '")}'*`);
					channel.send(final);
					return console.log(`[${time}] ${authorName} gave everyone in ${guildName} a random role, excluding a few.`);
				} else if (includeCount == 1) {
					final.setTitle(`__**Whoops!**__`)
						.setDescription(`You didn\'t give me 2 roles to randomly pick from!\nYou only gave me one.`);
					channel.send(final);
					return console.log(`[${time}] ${authorName} tried to give everyone in ${guildName} a random role, but didnt give me two roles to pick from.`);
				} else {
					for (let member of members) {
						let num = Math.floor(Math.random() * roles.length);
						while (excludedRoles.includes(roles[num].name) || !includedRoles.includes(roles[num].name)) {
							num = Math.floor(Math.random() * roles.length);
						}
						// member.addRoles(roles[num].id);
						arr.push(`**${member.user.username}:** ${roles[num].name}`);
					}

					check2048(arr);
					final.setTitle(`__**All users in the server have now been assigned random roles!**__\n*Excluding: '${excludedRoles.join("', '")}'\nIncluding: '${includedRoles.join("', '")}'*`);
					channel.send(final);
					return console.log(`[${time}] ${authorName} gave everyone in ${guildName} a random role, excluding a few and including a few.`);
				}
			}
		} else {

		}

		// if (!args[1]) {
		// 	if (everyone) {
		// 		let arr = [];
		//
		// 		for (let member of members) {
		// 			let num = Math.floor(Math.random() * (roles.length));
		// 			// member.addRole(roles[num].id);
		// 			arr.push('**' + member.user.username + '**: ' + roles[num].name);
		// 		}
		//
		// 		arr = arr.join('\n');
		// 		if (arr.length > 2048) {
		// 			let half1 = arr.slice(0, 2047);
		// 			let half2 = arr.slice(2047);
		// 			final.setDescription(half1);
		//
		// 			if (half2.length > 1024) {
		// 				let half2half1 = half2.slice(0, 1023);
		// 				let half2half2 = half2.slice(1023);
		//
		// 				if (half2half2.length > 1024) {
		// 					final.setDescription("Whoops, The user list is too long for me to display.\nAll the roles were changed, though!");
		// 				} else {
		// 					final.addField('*(2048 character limit break)*', half2half1)
		// 						.addField('*(1024 character limit break)*', half2half2);
		// 				}
		// 			} else {
		// 				final.addField('*(2048 character limit break)*', half2);
		// 			}
		// 		} else {
		// 			final.setDescription(arr);
		// 		}
		//
		// 		final.setTitle(`__**All users in the server have now been assigned random roles!**__`);
		// 		channel.send(final);
		//
		// 		return console.log(`[${time}] ${authorName} gave everyone in ${guildName} a random role.`);
		// 	} else {
		// 		if (message.guild.roles.find(`name`, args[0])) {
		// 			let arr = [];
		//
		// 			let roleMembers = message.guild.roles.find(`name`, args[0])
		// 				.members.map(member => member);
		//
		// 			for (let member of roleMembers) {
		// 				let num = Math.floor(Math.random() * (roles.length));
		// 				// member.addRole(roles[num].id);
		// 				arr.push('**' + member.user.username + '**: ' + roles[num].name);
		// 			}
		//
		// 			arr = arr.join('\n');
		// 			if (arr.length > 2048) {
		// 				let half1 = arr.slice(0, 2047);
		// 				let half2 = arr.slice(2047);
		// 				final.setDescription(half1);
		//
		// 				if (half2.length > 1024) {
		// 					let half2half1 = half2.slice(0, 1023);
		// 					let half2half2 = half2.slice(1023);
		//
		// 					if (half2half2.length > 1024) {
		// 						final.setDescription("Whoops, The user list is too long for me to display.\nAll the roles were changed, though!");
		// 					} else {
		// 						final.addField('*(2048 character limit break)*', half2half1)
		// 							.addField('*(1024 character limit break)*', half2half2);
		// 					}
		// 				} else {
		// 					final.addField('*(2048 character limit break)*', half2);
		// 				}
		// 			} else {
		// 				final.setDescription(arr);
		// 			}
		//
		// 			final.setTitle(`__**All users in ${args[0]} have now been assigned random roles!**__`);
		// 			channel.send(final);
		//
		// 			return console.log(`[${time}] ${authorName} gave everyone in ${guildName} with the ${args[0]} role a random role.`);
		// 		} else {
		// 			final.setTitle(`__**Whoops!**__`)
		// 				.setDescription(`That role doesnt exist in this server!\nPlease make sure you spelled everything right.`);
		// 			channel.send(final);
		//
		// 			return console.log(`[${time}] ${authorName} tried to give everyone in ${guildName} with the ${args[0]} role a random role, but didnt input a role that existed.`);
		// 		}
		// 	}
		// }
		//
		//
		// if (!args[2]) {
		// 	final.setTitle(`__**Whoops!**__`)
		// 		.setDescription(`You need to use at least two roles for me to pick from as the second and third arguments!`);
		// 	channel.send(final);
		//
		// 	return console.log(`[${time}] ${authorName} tried to give people in ${guildName} random roles, but didnt input two roles for me to choose from.`);
		// }
		//
		// if (everyone) {
		// 	let arr = [];
		// 	let realRoles = [];
		// 	let excludedRoles = [];
		// 	let roles = [];
		//
		// 	for (i = 1; i < 100; i++) {
		// 		try {
		// 			roles.push(args[i]);
		// 		} catch (err) {
		// 			let do = "nothing";
		// 		}
		// 	}
		//
		// 	for (role of roles) {
		// 		if (role.startsWith('!')) {
		// 			excludedRoles.push(message.guild.roles.find(`name`, role.slice(1)));
		// 			realRoles.push(message.guild.roles.find(`name`, role.slice(1)));
		// 		} else if (!message.guild.roles.find(`name`, role)) {
		// 			final.setTitle(`__**Whoops!**__`)
		// 				.setDescription(`The role '${role}' does not exist on this server!`);
		// 			channel.send(final);
		//
		// 			return console.log(`[${time}] ${authorName} tried to give people in ${guildName} random roles, but one of the roles they used didnt exist.`);
		// 		} else {
		// 			realRoles.push(message.guild.roles.find(`name`, role));
		// 		}
		// 	}
		//
		// 	for (let member of members) {
		// 		let num = Math.floor(Math.random() * (realRoles.length));
		// 		while (excludedRoles.includes(realRoles[num])) {
		// 			num = Math.floor(Math.random() * (realRoles.length));
		// 		}
		//
		// 		// member.addRole(realRoles[num].id);
		// 		arr.push('**' + member.user.username + '**: ' + realRoles[num].name);
		// 	}
		//
		// 	arr = arr.join('\n');
		// 	if (arr.length > 2048) {
		// 		let half1 = arr.slice(0, 2047);
		// 		let half2 = arr.slice(2047);
		// 		final.setDescription(half1);
		//
		// 		if (half2.length > 1024) {
		// 			let half2half1 = half2.slice(0, 1023);
		// 			let half2half2 = half2.slice(1023);
		//
		// 			if (half2half2.length > 1024) {
		// 				final.setDescription("Whoops, The user list is too long for me to display.\nAll the roles were changed, though!");
		// 			} else {
		// 				final.addField('*(2048 character limit break)*', half2half1)
		// 					.addField('*(1024 character limit break)*', half2half2);
		// 			}
		// 		} else {
		// 			final.addField('*(2048 character limit break)*', half2);
		// 		}
		// 	} else {
		// 		final.setDescription(arr);
		// 	}
		//
		// 	final.setTitle(`__**All users in the server have now been assigned random roles!**__`);
		// 	channel.send(final);
		//
		// 	return console.log(`[${time}] ${authorName} gave everyone in ${guildName} a random role (either ${args[1]} or ${args[2]}).`);
		// }

		// final.setTitle('')
		// .setDescription('')
		// .addField('', '');

		// serverSettings = JSON.stringify(serverSettings);
		// fs.writeFileSync(`./servers/${guild.id}Settings.json`, serverSettings, (err) => {
		// 	if (err) console.log(`Error writing to '${guildName}'s settings file:\n${err}\n`);
		// });

		// channel.send(final);
		// console.log(`[${time}] ${authorName} did something.`);
	},
};