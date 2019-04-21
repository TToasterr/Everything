const fs = require(`fs`);
// const request = require(`request`);
// const randomImage = require(`random-puppy`);
const Discord = require(`discord.js`);
const client = new Discord.Client();



// -----------------------------------------------------------------------------



client.once(`ready`, () => {
	console.log(`\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n`);
	console.log(`PexBot is online!\nUsers: ${client.users.size}\nServers: ${client.guilds.size}\n`);
	client.user.setActivity(`.help`);
});

// -----------------------------------------------------------------------------

client.on(`guildCreate`, guild => {
	console.log(`\nJoined a new server: ${guild.name}\nNew users: ${guild.memberCount}\n`);
});

client.on(`guildDelete`, guild => {
	console.log(`\nLeft a server: ${guild.name}\nUsers lost: ${guild.memberCount}`);
});



// -----------------------------------------------------------------------------



var profPic = `https://cdn.discordapp.com/attachments/514067788827066379/569381210539819008/DISCORD_TEAM.png`;
var invLink = `https://discordapp.com/api/oauth2/authorize?client_id=569380001447673856&permissions=8&scope=bot`;



// -----------------------------------------------------------------------------



client.on(`message`, msg => {
	if (msg.author.bot) return;

	let message = msg.content.toLowerCase();
	let final = new Discord.RichEmbed()
		.setColor(`#FFB200`);


	// -----------------------------------------------------------------------------


	// variable defining
	let command = message.split(` `)[0].slice(1);
	let args = message.slice(command.length + 1).slice(1).split(`, `);
	let prefix = '.';

	if (message == `wow this new bot is great`) {
		msg.channel.send(`hell yeah I am thanks :b:`);
		final.setTitle(`Also Ali:`)
			.setDescription(`This is a richembed.`);
		msg.channel.send(final);
	}

	if (command == `ping`) {
		final.setTitle(`Hello!`)
			.setDescription(`Yes, I exist.`);
		msg.channel.send(final);
	}
});

client.on('error', console.error);



// -----------------------------------------------------------------------------



const token = fs.readFileSync(`H:/Misc/PexBotToken.txt`, (err) => {
	if (err) console.log(`Error reading token!\n$ {err}`);
});
client.login(token.toString());