const fs = require('fs');
const Discord = require('discord.js');
const client = new Discord.Client();
const config = require('./config.json');





client.once('ready', () => {
  for (var i = 0; i <= 100; i++) {
    console.log();
  }
  console.log(`Bot has started!\nUSERS: ${client.users.size}\nCHANNELS: ${client.channels.size}\nSERVERS: ${client.guilds.size}\n`);
})





client.on("guildCreate", guild => {
  console.log(`New server joined!\nNAME: ${guild.name}.\nMEMBERS: ${guild.memberCount}`);
});

client.on("guildDelete", guild => {
  console.log(`Removed from server!\nNAME: ${guild.name}\nMEMBERS: ${guild.memberCount}`);
});





client.on('message', message => {
  // var toaster = client.fetchUser('184474965859368960');
  try {
    client.commands = new Discord.Collection();

    const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js'));

    for (const file of commandFiles) {
      const command = require(`./commands/${file}`);
      client.commands.set(command.name, command);
    }



    if (!message.content.startsWith(config.prefix) || message.author.bot) return;

    const entire = message.content.slice(config.prefix.length).toLowerCase();
    const commandName = entire.split(' ')[0];
    const args = entire.slice(commandName.length).split(', ');

    if (!client.commands.has(commandName)) return;

    const command = client.commands.get(commandName);

    if (command.args && args == '') {
      let reply = 'You didnt\'t provide the necesarry arguments!';
      if (command.usage !== '') {
        reply += `\nThe proper usage would be \`${config.prefix}${command.name} ${command.usage}\``;
      }
      return message.channel.send(reply);
    }

    if (command.guildOnly && message.channel.type !== 'text') {
      return message.channel.send("That command only works in servers!");
    }

    if(command.mod && !message.member.roles.some(r=>["Administrator", "Moderator", "Mod", "Admin", "Owner", "Toaster"].includes(r.name)) )
      return message.channel.send("Sorry, you don't have permissions to use this command!");



    try {
      command.execute(message, args, client);
    }
    catch (error) {
      message.channel.send('There was an error executing that command! The bot owner has been notified.');
      let client = message.channel.client;
      let user = client.fetchUser('184474965859368960')
      .then(user => {
        user.send(`A user got an error using the '${command.name}' command!\n\`\`\`${error}\`\`\``);
      })
      console.error(error);
    }
  }
  catch(error) {
    message.channel.send('There was some unknown error! The bot owner has been notified.');
    let client = message.channel.client;
    let user = client.fetchUser('184474965859368960')
    .then(user => {
      user.send(`A user got a generic error!\n\`\`\`${error}\`\`\``);
    })
    console.error(error);
  }
})

client.on('error', console.error);





client.login(process.argv[2]);
