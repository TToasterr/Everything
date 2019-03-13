const fs = require(`fs`);
const Discord = require(`discord.js`);
const client = new Discord.Client();

// -----------------------------------------------------------------------------

client.once(`ready`, () => {
        console.log(`\n\n\n\n\n\n\n\n\n\n\n\n\n`);
        console.log(`SILICON IS RUNNING\nVISIBLE USERS: ${client.users.size}\nVISIBLE CHANNELS: ${client.channels.size}\nVISIBLE SERVERS: ${client.guilds.size}\n`);
});