const fs = require(`fs`);
const Discord = require(`discord.js`);
const hrtime = require('process');
const client = new Discord.Client();



// -----------------------------------------------------------------------------



client.once(`ready`, () => {
  console.log(`\n\n\n\n\n\n\n`);
  console.log(`Bot has started! \nUSERS: ${client.users.size} \nCHANNELS: ${client.channels.size} \nSERVERS: ${client.guilds.size}\n`);
})



// -----------------------------------------------------------------------------



client.on(`guildCreate`, guild => {
  console.log(`\n-----------------------------\nNew server joined! \nNAME: ${guild.name} \nMEMBERS: ${guild.memberCount}\n-----------------------------\n`);
});

client.on(`guildDelete`, guild => {
  console.log(`\n-----------------------------\nRemoved from server! \nNAME: ${guild.name} \nMEMBERS: ${guild.memberCount}\n-----------------------------\n`);
});



// -----------------------------------------------------------------------------



client.on(`message`, message => {
	if (message.author.bot) return;

	var sent = [];
	var includesSCP = false;

	var splitMessage = message.content.split(" ");

	var finalDesc = [];

	let final = new Discord.RichEmbed()
	.setColor(`#000000`)
	.setAuthor(`Marv`, `https://images.discordapp.net/avatars/538173713162567690/07187402dab82f0fd34348a0a5202ecc.png?size=512`, `https://discordapp.com/api/oauth2/authorize?client_id=554490018752626708&permissions=8&scope=bot`)

	for (var i = 0; i < splitMessage.length; i++) {
		if (splitMessage[i].includes("SCP-")) {
			finalDesc.push(`[${splitMessage[i]}](http://www.scp-wiki.net/${splitMessage[i]})`);
			includesSCP = true;
		}

		if (splitMessage[i].includes("TALE-")) {
			finalDesc.push(`[${splitMessage[i].substring(5).split("-").join(" ")}](http://www.scp-wiki.net/${splitMessage[i].substring(5)})`);
			includesSCP = true;
		}
	}

	if (includesSCP) {
		final.setDescription(finalDesc.join("\n"));
		message.channel.send(final);
	}



	// -----------------------------------------------------------------------------



	// for (var i = 5000; i >= 0; i--) {
	// 	if (!done) {
	// 		if (i < 10) {
	// 			i = `00${i}`;
	// 		}
	// 		else if (i < 100) {
	// 			i = `0${i}`;
	// 		}
	//
	// 		let final = new Discord.RichEmbed()
	// 		.setColor(`#000000`)
	// 		.setAuthor(`Marv`, `https://images.discordapp.net/avatars/538173713162567690/07187402dab82f0fd34348a0a5202ecc.png?size=512`, `https://discordapp.com/api/oauth2/authorize?client_id=554490018752626708&permissions=8&scope=bot`)
	//
	// 		if (message.content.includes(`SCP-${i}`)) {
	// 			final.setDescription(`[\`SCP-${i}\`](http://www.scp-wiki.net/scp-${i})`);
	// 			message.channel.send(final);
	// 			done = true;
	// 		}
	// 	}
	// }
});

// -----------------------------------------------------------------------------

client.login(process.argv[2]);