const fs = require(`fs`);
const Discord = require(`discord.js`);
const client = new Discord.Client();

// -----------------------------------------------------------------------------

client.once(`ready`, () => {
        console.log(`\n\n\n\n\n\n\n\n\n\n\n\n\n`);
        console.log(`SILICON IS RUNNING\nVISIBLE USERS: ${client.users.size}\nVISIBLE CHANNELS: ${client.channels.size}\nVISIBLE SERVERS: ${client.guilds.size}\n`);
        client.user.setActivity(`slc.help`);
});

// -----------------------------------------------------------------------------

client.on(`guildCreate`, guild => {
        console.log(`\nNEW SERVER VISIBLE: ${guild.name}\nNEW USERS VISIBLE:  ${guild.memberCoutn}\n`);
});