const Discord = require('discord.js');
const ytdl = require('ytdl-core');

module.exports = {
        name: 'play',
        description: 'it does a thing with sound',
        usage: '<video link>',
        guildOnly: true,
        args: false,
        mod: false,
        execute(message, args, client, time, final) {
		var connection;
		if (message.member.voice.channel) {
			connection = await message.member.voice.channel.join();
		} else {
			final.setTitle('__**wow ur so bad xd**__');
				.setDescription('wow what a nerd you arent even in a noise place');
			return console.log(`[${time}] ${message.author.username} tried to add the bot to a voice channel.`);
		}
		
		connection.play(ytdl(args[0].substring(1), { filter: 'audioonly' }));
                
                final.setTitle(`__**Joined voice channel!**__`)
                	.setDescription(`Now playing song ${args[0].substring(1)}`);
                // .addField(``, ``);
                message.channel.send(final);
                console.log(`[${time}] ${message.author.username} added the bot to a voice channel.`);
        },
};
