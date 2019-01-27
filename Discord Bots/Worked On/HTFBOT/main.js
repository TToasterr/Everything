const fs = require(`fs`);
const Discord = require(`discord.js`);
const client = new Discord.Client();
const prefix = `..`

// -----------------------------------------------------------------------------

client.once(`ready`, () => {
  console.log(`\n\n\n\n\n\n\n`);
  console.log(`Bot has started! \nUSERS: ${client.users.size} \nCHANNELS: ${client.channels.size} \nSERVERS: ${client.guilds.size}\n`);
})

// -----------------------------------------------------------------------------

client.on(`guildCreate`, guild => {
  console.log(`New server joined! \nNAME: ${guild.name} \nMEMBERS: ${guild.memberCount}`);
});

client.on(`guildDelete`, guild => {
  console.log(`Removed from server! \nNAME: {$guild.name} \nMEMBERS: ${guild.memberCount}`);
});



// -----------------------------------------------------------------------------
// -----------------------------------------------------------------------------



function notEnoughArgs(command, message, time) {
  let final = new Discord.RichEmbed()
  .setColor(`#00ff00`)
  .setAuthor(`HTFBOT (Hopefully The Final Bot Of Toasters)`, `https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048`, `https://discordapp.com/api/oauth2/authorize?client_id=537774698809786368&permissions=8&scope=bot`)
  .setTitle(`__**Oops!**__`)
  .setDescription(`You didnt provide the necesarry arguments!`);

  if (command.usage !== ``) {
    final.addField(`Usage`, `${prefix}${command.name} ${command.usage}`);
  }

  message.channel.send(final);
  console.log(`[${time}] ${message.author.username} tried to do a command, but didnt use enough arguments.`);
}



// -----------------------------------------------------------------------------
// -----------------------------------------------------------------------------



client.on(`message`, message => {
  let final = new Discord.RichEmbed()
  .setColor(`#00ff00`)
  .setAuthor(`HTFBOT (Hopefully The Final Bot Of Toasters)`, `https://cdn.discordapp.com/avatars/184474965859368960/5325a0eed911e9f09e24fd277e886846.png?size=2048`, `https://discordapp.com/api/oauth2/authorize?client_id=537774698809786368&permissions=8&scope=bot`)

  // -----------------------------------------------------------------------------

  let date = new Date();
  let day = date.toString().substring(0,3);
  let mdy = date.toString().substring(4,15);
  let time = date.toString().substring(16,24);

  // -----------------------------------------------------------------------------

  client.commands = new Discord.Collection();

  const commandFiles = fs.readdirSync(`./commands`).filter(file => file.endsWith(`.js`));

  for (const file of commandFiles) {
    const command = require(`./commands/${file}`);
    client.commands.set(command.name, command);
  }

  // -----------------------------------------------------------------------------

  if (!message.content.startsWith(prefix) || message.author.bot) return;

  // -----------------------------------------------------------------------------

  const entire = message.content.slice(prefix.length).toLowerCase();
  const commandName = entire.split(` `)[0];
  const args = entire.slice(commandName.length).split(`, `);

  if (!client.commands.has(commandName)) return;

  const command = client.commands.get(commandName);

  // -----------------------------------------------------------------------------

  if (command.args && args == ``) {
    final.setTitle(`__**Oops!**__`)
    .setDescription(`You didnt provide any arguments!`);

    if (command.usage !== ``) {
      final.addField(`Usage`, `${prefix}${command.name} ${command.usage}`);
    }

    message.channel.send(final);
    return console.log(`[${time}] ${message.author.username} tried to do a command, but didnt use any arguments.`);
  }

  if (command.guildOnly && message.channel.type !== `text`) {
    final.setTitle(`__**Oops!**__`)
    .setDescription(`That command only works in servers!`);

    message.channel.send(final);
    return console.log(`[${time}] ${message.author.username} tried to do a guild only command outside of a guild.`);
  }

  if (command.mod && !message.member.roles.some(r => [`Administrator`, `Moderator`, `Mod`, `Admin`, `Owners`, `Toaster`, `EPIC GAMERS`, `COOL KIDS`].includes(r.name))) {
    final.setTitle(`__**Oops!**__`)
    .setDescription(`Sorry, you dont have permission to do this command!`);

    message.channel.send(final);
    return console.log(`[${time}] ${message.author.username} tried to do a command, but didnt have the right permission.`);
  }

  // -----------------------------------------------------------------------------

  try {
    command.execute(message, args, client, time, final, prefix);
  }
  catch (err) {
    final.setTitle(`__**Oops!**__`)
    .setDescription(`There was an error executing that command!\nThe bot owner has been notified.`);

    message.channel.send(final);

    let client = message.channel.client;
    let toaster = client.fetchUser(`184474965859368960`).then(toaster => {
      toaster.send(`${message.author.username} got an error using the ${command.name} command. \nCheck console my guy!`);
    });
    return console.log(err + `\n`);
  }
});



// -----------------------------------------------------------------------------
// -----------------------------------------------------------------------------



client.login(process.argv[2]);