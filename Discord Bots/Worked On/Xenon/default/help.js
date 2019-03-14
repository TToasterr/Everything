const Discord = require('discord.js');

module.exports = {
        name: 'help',
        description: 'Get some help.',
        usage: '',
        guildOnly: false,
        args: false,
        mod: false,
        execute(message, args, client, time, final) {
                final.setTitle('__**About the bot:**__')
                        .setDescription('*This bot is made by 4 sepearate people, each of which will make their own commands.*\n\nOther valid prefixes are rdt, rdj, rdn, and rdl.')

                message.channel.send(final);
                console.log(`[${time}] ${message.author.username} got help.`);
        },
};