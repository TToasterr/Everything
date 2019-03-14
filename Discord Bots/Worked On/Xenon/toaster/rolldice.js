const Discord = require('discord.js');

module.exports = {
        name: 'rolldice',
        description: 'Roll some dice, with a variable amount of sides!',
        usage: '<amount of sides>',
        category: '',
        guildOnly: false,
        args: true,
        mod: false,
        execute(message, args, client, time, final) {
                final.setTitle(`Rolling a die with ${args[0].substring(1)} sides..`)
                        .setDescription(`I rolled a(n) ${Math.floor(Math.random() * args[0].substring(1)) + 1}`)
                // .addField('', '');
                message.channel.send(final);
                console.log(`[${time}] ${message.author.username} rolled a die with ${args[0].substring(1)} sides.`);
        },
};
