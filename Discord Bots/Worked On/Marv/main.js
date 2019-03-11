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
	var sent = [];
	var done = false;
	for (var i = 5000; i >= 0; i--) {
		if (!done) {
			if (i < 10) {
				i = `00${i}`;
			}
			else if (i < 100) {
				i = `0${i}`;
			}

			// var splitMessage = message.content.split(i);
			// var numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

			// console.log(`${i}	-	${splitMessage}`)

			let final = new Discord.RichEmbed()
			.setColor(`#000000`)
			.setAuthor(`Marv`, `https://images.discordapp.net/avatars/538173713162567690/07187402dab82f0fd34348a0a5202ecc.png?size=512`, `https://discordapp.com/api/oauth2/authorize?client_id=554490018752626708&permissions=8&scope=bot`)

			// if (message.content.includes(`&{i}`) && !(numbers.includes(splitMessage[0][-1])) && !(numbers.includes(splitMessage[1][0]))) {
			if (message.content.includes(`SCP-${i}`)) {
				// console.log(splitMessage[0][-1])
				// console.log(splitMessage[1][0])
				final.setDescription(`[\`SCP-${i}\`](http://www.scp-wiki.net/scp-${i})`);
				message.channel.send(final);
				done = true;
			}
		}
	}
});

// -----------------------------------------------------------------------------

client.login(process.argv[2]);