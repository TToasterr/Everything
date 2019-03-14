const fs = require(`fs`);
const Discord = require(`discord.js`);
const client = new Discord.Client();



// -----------------------------------------------------------------------------



client.once(`ready`, () => {
        console.log(`\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n`);
        console.log(`XENON IS LIVE\nOBERVABLE USERS: ${client.users.size}\nOBSERVABLE CHANNELS: ${client.channels.size}\nOBSERVED SERVERS: ${client.guilds.size}\n`);
        client.user.setActivity(`rd.help`);
});

// -----------------------------------------------------------------------------

client.on(`guildCreate`, guild => {
        console.log(`\nNEW SERVER OBSERVED: ${guild.name}\nNEW USERS OBSERVABLE: ${guild.memberCount}\n`);
});

client.on(`guildDelete`, guild => {
        console.log(`\nLOST SIGHT OF ${guild.name}\nOBSERVABLE USERS LOST: ${guild.memberCount}`);
});



// -----------------------------------------------------------------------------



client.defaultCommands = new Discord.Collection();
client.tCommands = new Discord.Collection();
client.jCommands = new Discord.Collection();
client.nCommands = new Discord.Collection();
client.lCommands = new Discord.Collection();

const defaultCommandFiles = fs.readdirSync(`./default`).filter(file => file.endsWith(`.js`));
const tCommandFiles = fs.readdirSync(`./toaster`).filter(file => file.endsWith(`.js`));
const jCommandFiles = fs.readdirSync(`./jonathan`).filter(file => file.endsWith(`.js`));
const nCommandFiles = fs.readdirSync(`./nate`).filter(file => file.endsWith(`.js`));
const lCommandFiles = fs.readdirSync(`./liam`).filter(file => file.endsWith(`.js`));

for (var file of defaultCommandFiles) {
        var command = require(`./default/${file}`);
        client.defaultCommands.set(command.name, command);
}
for (var file of tCommandFiles) {
        var command = require(`./toaster/${file}`);
        client.tCommands.set(command.name, command);
}
for (var file of jCommandFiles) {
        var command = require(`./jonathan/${file}`);
        client.jCommands.set(command.name, command);
}
for (var file of nCommandFiles) {
        var command = require(`./nate/${file}`);
        client.nCommands.set(command.name, command);
}
for (var file of lCommandFiles) {
        var command = require(`./liam/${file}`);
        client.lCommands.set(command.name, command);
}



// -----------------------------------------------------------------------------



var profPic = `https://cdn.discordapp.com/attachments/539116623261466635/555604369068785664/600px-Radiation_warning_symbol.svg.png`;
var invLink = `https://discordapp.com/api/oauth2/authorize?client_id=555556786908954624&permissions=8&scope=bot`;



// -----------------------------------------------------------------------------



client.on(`message`, message => {
        if (message.author.bot || !message.content.startsWith('rd')) return;
        // time and final defining
        var entire;
        var date = new Date();
        var time = date.toString().substring(16, 24);
        var final = new Discord.RichEmbed()
                .setColor(`#FF0000`);

        // -----------------------------------------------------------------------------

        // entire defining
        if (message.content[2] == `.`) {
                entire = message.content.slice(3).toLowerCase();
        } else {
                entire = message.content.slice(4).toLowerCase();
        }

        // -----------------------------------------------------------------------------



        // variable defining
        var commandName = entire.split(` `)[0];
        var args = entire.slice(commandName.length).split(`, `);
        var command;
        var prefix;
        if (!client.defaultCommands.has(commandName) && !client.tCommands.has(commandName) && !client.jCommands.has(commandName) && !client.nCommands.has(commandName) && !client.lCommands.has(commandName)) return;


        // getting command from the right collection
        if (message.content[2] == `.`) {
                command = client.defaultCommands.get(commandName);
                prefix = 'rd.';
                final.setAuthor(`Radon`, profPic, invLink);
        } else if (message.content[2] == `t`) {
                command = client.tCommands.get(commandName);
                prefix = 'rdt.';
                final.setAuthor(`Radon (Toaster)`, profPic, invLink);
        } else if (message.content[2] == `j`) {
                command = client.jCommands.get(commandName);
                prefix = 'rdj.';
                final.setAuthor(`Radon (Jonathan)`, profPic, invLink);
        } else if (message.content[2] == `n`) {
                command = client.nCommands.get(commandName);
                prefix = 'rdn.';
                final.setAuthor(`Radon (Nate)`, profPic, invLink);
        } else if (message.content[2] == `l`) {
                command = client.lCommands.get(commandName);
                prefix = 'rdl.';
                final.setAuthor(`Radon (Liam)`, profPic, invLink);
        } else {
                return;
        }



        // -----------------------------------------------------------------------------



        // if args and if guildonly
        if (command.args && args == ``) {
                final.setTitle(`__**Oops!**__`)
                        .setDescription(`You didnt provide any arguments!`);

                if (command.usage !== ``) {
                        final.addField(`Usage`, `${prefix}${command.name} ${command.usage}`);
                }

                message.channel.send(final);
                return console.log(`[${time}] ${message.author.username} FAILED TO USE ARGUMENTS`);
        }

        if (command.guildOnly && message.channel.type !== `text`) {
                final.setTitle(`__**Oops!**__`)
                        .setDescription(`That command only works in servers!`);

                message.channel.send(final);
                return console.log(`[${time}] ${message.author.username} MESSAGED ME DIRECTLY WHEN DISALLOWED`);
        }



        // -----------------------------------------------------------------------------



        // executing the command
        try {
                command.execute(message, args, client, time, final);
        } catch (err) {
                final.setTitle(`__**Oops!**__`)
                        .setDescription(`Radon got an error.\n*Owners have been notified.*`)

                message.channel.send(final);

                let client = message.channel.client;
                let toaster = client.fetchUser(`184474965859368960`).then(toaster => {
                        toaster.send(`\`${message.author.username}\` got an error using \`${command.name}\`.`)
                });
                throw err;
        }
});



// -----------------------------------------------------------------------------



client.login(process.argv[2]);