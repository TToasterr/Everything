const Discord = require('discord.js');

module.exports = {
        name: 'reload',
        description: 'Reload the commands for the bot!',
        usage: '',
        guildOnly: false,
        args: false,
        mod: false,
        execute(message, args, client, time, final) {
                reloadbot()

                final.setTitle(`__**Commands have been reloaded!**__`)
                        .setDescription(`Any new changes will now show up!`)
                // .addField(``, ``);
                message.channel.send(final);
                console.log(`[${time}] ${message.author.username} reloaded the bot.`);
        },
};