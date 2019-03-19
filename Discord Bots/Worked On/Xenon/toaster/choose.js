const Discord = require('discord.js');

module.exports = {
        name: 'choose',
        description: 'Choose an option from two or more arguments!',
        usage: '<option 1>, <option 2>, [option 3]...',
        category: '',
        guildOnly: false,
        args: true,
        mod: false,
        execute(message, args, client, time, final) {
                args[0] = args[0].substring(1);

                if (!args[1] || args[1] == '') {
                        final.setTitle(`__**Oops!**__`)
                                .setDescription(`You didn\'t use enough arguments!`)
                        message.channel.send(final);
                        return console.log(`[${time}] ${message.author.username} tried to make the bot choose from only one thing.`);
                }

                var randInt = Math.floor(Math.random() * args.length);

                final.setTitle(`__**Options**__`)
                        .setDescription(`\`${args.join("\n")}\``)
                        .addField(`__**My Choice**__`, `\`${args[randInt]}\``);
                message.channel.send(final);
                console.log(`[${time}] ${message.author.username} made the bot choose.`);
        },
};