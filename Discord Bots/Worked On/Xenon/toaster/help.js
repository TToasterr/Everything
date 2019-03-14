const Discord = require('discord.js');

module.exports = {
        name: 'help',
        description: 'Get some help.',
        usage: '',
        guildOnly: false,
        args: false,
        mod: false,
        execute(message, args, client, time, final) {

                if (args == '') {
                        var general = [];
                        var commands = message.client.tCommands.map(command => command);

                        for (var i = 0; i < commands.length; i++) {
                                general.push(commands[i].name);
                        }

                        final.setTitle('__**Here are all of Toasters commands!**__')
                                .setDescription('*Arguments must be seperated with a comma and space or it will return an error.*')
                                .addField('__Commands:__', '`' + general.join('\n') + '`')
                                .addField(`You can send \`rdt.help <command name>\` to get info on a specific command!`, '[`My Github`](https://github.com/TToasterr/Everything/tree/master/Discord%20Bots/Worked%20On/Xenon)');

                        message.channel.send(final);
                        return console.log(`[${time}] ${message.author.username} got help.`);
                }

                const name = args[0].toLowerCase().substring(1);
                const command = message.client.tCommands.get(name);

                if (!command) {
                        return message.channel.send('That\'s not a valid command!');
                }

                final.setTitle('**Specific Command Help**')
                        .setDescription(command.name)
                        .addField('**Description**', command.description)
                        .addField('**Usage**', `rdt.${command.name} ${command.usage}`);

                message.channel.send(final);
                console.log(`[${time}] ${message.author.username} got Toaster help.`);
        },
};