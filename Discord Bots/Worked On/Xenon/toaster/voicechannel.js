const Discord = require('discord.js');
const ytdl = require('ytdl-core');
const fs = require('fs');

module.exports = {
        name: 'play',
        description: 'it does a thing with sound',
        usage: '<video link>',
        category: 'testing',
        guildOnly: true,
        args: true,
        mod: false,
        execute(message, args, client, time, final) {
                var connection;

                if (message.member.voiceChannel) {
                        // ytdl(args[0].substring(1)).pipe(fs.createWriteStream('./music/song.mp3'));
                        //
                        // connection = message.member.voiceChannel.join().then(connection => {
                        //         var dispatcher = connection.playFile('./music/song.mp3');
                        //
                        //         dispatcher.on('end', end => {
                        //                 message.member.voiceChannel.leave();
                        //         });
                        // }).catch(err => console.log(err));;

                        const streamOptions = {
                                seek: 0,
                                volume: 1
                        };
                        var voiceChannel = message.member.voiceChannel;
                        voiceChannel.join().then(connection => {
                                // console.log("joined channel");
                                const stream = ytdl(args[0].substring(1), {
                                        filter: 'audioonly'
                                });
                                const dispatcher = connection.playStream(stream, streamOptions);
                                dispatcher.on("end", end => {
                                        // console.log("left channel");
                                        voiceChannel.leave();
                                });
                        }).catch(err => console.log(err));

                } else {
                        final.setTitle('__**wow ur so bad xd**__')
                                .setDescription('wow what a nerd you arent even in a noise place');
                        message.channel.send(final);
                        return console.log(`[${time}] ${message.author.username} tried tomake the bot play a song outside of a voice channel.`);
                }

                final.setTitle(`__**Joined voice channel!**__`)
                        .setDescription(`Now playing song ${args[0].substring(1)}`);

                message.channel.send(final);
                console.log(`[${time}] ${message.author.username} made the bot play a song.`);
        },
};