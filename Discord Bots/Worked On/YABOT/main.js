const fs = require('fs');
const Discord = require('discord.js');
const client = new Discord.Client();
const config = require('./config.json');





client.once('ready', () => { // once the bot turns on
  for (var i = 0; i <= 100; i++) { // for i in range 100
    console.log(); // print a linebreak
  }
  console.log(`Bot has started!\nUSERS: ${client.users.size}\nCHANNELS: ${client.channels.size}\nSERVERS: ${client.guilds.size}\n`); // print the welcome message
})





client.on("guildCreate", guild => { // when the bot joines a server
  console.log(`New server joined!\nNAME: ${guild.name}.\nMEMBERS: ${guild.memberCount}`); // say it in console
});

client.on("guildDelete", guild => { // when the bot leaves a server
  console.log(`Removed from server!\nNAME: ${guild.name}\nMEMBERS: ${guild.memberCount}`); // say it in console
});





client.on('message', message => { // when the bot recieves a message
  // var toaster = client.fetchUser('184474965859368960');
  try { // try to
    client.commands = new Discord.Collection(); // make a collection of all commands

    const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js')); // read all command .js files and put them into variable commandFiles

    for (const file of commandFiles) { // for each file in commandFiles
      const command = require(`./commands/${file}`); // command = the file
      client.commands.set(command.name, command); // add the command to the discord collection of commands
    }



    if (!message.content.startsWith(config.prefix) || message.author.bot) return; // if the message doesnt start with the prefix or is sent by a bot, do nothing

    const entire = message.content.slice(config.prefix.length).toLowerCase(); // const entire is the entire message in lower case, minus the prefix
    const commandName = entire.split(' ')[0]; // const commandName is the first word of entire
    const args = entire.slice(commandName.length).split(', '); // const args are the rest of entire, split by ", "

    if (!client.commands.has(commandName)) return; // if the client doesnt have a command called commandName, stop

    const command = client.commands.get(commandName); // const command is the actual command they did

    if (command.args && args == '') { // if the command required arguments and the person gave none
      let reply = 'You didnt\'t provide the necesarry arguments!'; // set reply to say so
      if (command.usage !== '') { // if the command has a usage variable, showing how to use it
        reply += `\nThe proper usage would be \`${config.prefix}${command.name} ${command.usage}\``; // add the usage to the reply
      }
      return message.channel.send(reply); // send the reply and stop the program
    }

    if (command.guildOnly && message.channel.type !== 'text') { // if the command can only be done in guilds and they didnt do it in a guild
      return message.channel.send("That command only works in servers!"); // say so and stop the program
    }

    if(command.mod && !message.member.roles.some(r=>["Administrator", "Moderator", "Mod", "Admin", "Owner", "Toaster"].includes(r.name)) ) // if the command required mod permission and the user doesnt have it
      return message.channel.send("Sorry, you don't have permissions to use this command!"); // say so and stop the program



    try { // try to
      var date = new Date(); // get the current date
      var day = date.toString().substring(0,3); // get the day
      var mdy = date.toString().substring(4,15); // get the date (mm/dd/yy)
      var time = date.toString().substring(16,24); // get the time
      command.execute(message, args, client, time); // execute the code for the command the person did
    }
    catch (error) { // if it gets an error
      message.channel.send('There was an error executing that command! The bot owner has been notified.'); // say so into the channel
      let client = message.channel.client; // let client be the client
      let user = client.fetchUser('184474965859368960') // get me as a user
      .then(user => { // then...
        user.send(`A user got an error using the '${command.name}' command!\n\`\`\`${error}\`\`\``); // send the error to me
      })
      console.error(error); // and also put it in console.
    }
  }
  catch(error) { // if it gets an error (this one is usually syntax errors, shouldnt really send a message)
    message.channel.send('There was some unknown error! The bot owner has been notified.'); // say so
    let client = message.channel.client; // let client be the client
    let user = client.fetchUser('184474965859368960') // get me as a user
    .then(user => { // then...
      user.send(`A user got a generic error!\n\`\`\`${error}\`\`\``); // send me the error
    })
    console.error(error); // and also put it in console
  }
})

client.on('error', console.error); // more backup, on a client error, log the error in console.





client.login(process.argv[2]); // start the client with the second argument in the console as the token
