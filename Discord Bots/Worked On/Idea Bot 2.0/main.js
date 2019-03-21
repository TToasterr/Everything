const fs = require('fs');
const discord = require('discord.js');
const client = new discord.Client();

// -----------------------------------------------------------------------------

client.once(`ready`, () => {
        console.log(`\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n`);
        console.log(`IDEABOT STARTED\n\nUSERS: ${client.users.size}\nCHANNELS: ${client.channels.size}\nSERVERS: ${client.guilds.size}\n`);
});

client.on(`guildCreate`, guild => {
        console.log(`\nNEW SERVER\n${guild.name}\nMEMBERS: ${guild.memberCount}\n`);
});

client.on(`guildDelete`, guild => {
        console.log(`\nLOST SERVER\n${guild.name}\nMEMBERS: ${guild.memberCount}\n`);
});

// -----------------------------------------------------------------------------


const ideaCategories = [`NEWS`, `CWN`, `ARTICLE`, `GENERAL`, `JOKE`];


client.on(`message`, message => {
        if (message.author.bot) return;

        function send(msg) {
                message.channel.send(msg);
        }

        function debug(msg) {
                message.channel.send(`[DEBUG]\n\n${msg}`);
        }

        if (message.content.startsWith(`./ping`)) {
                send(`Wow, the bot exists.\nNeat`);
                console.log(`The bot was pinged by ${message.author.username}`);
        } else if (message.content == `thanks for existing, bot`) {
                send(`no problemo xd`);
                console.log(`The bot was thanked for existing by ${message.author.username}`);
        } else if (message.content.startsWith(`./help`)) {
                send(`**Commands:**\n\n\`./help\n./ping\n./invite\n./descriptions\n\n./idea [category], [alias], [idea]\n./listideas [category]\n./showratings [category], [alias]\n./delidea [category], [alias]\n./rate [category], [alias], [rating]\``);
                console.log(`${message.author.username} just got help.`);
        } else if (message.content.startsWith(`./invite`)) {
                send(`Wow you must really like me\n\nhttps://discordapp.com/api/oauth2/authorize?client_id=496529456178003987&permissions=8&scope=bot`);
                console.log(`An invite link was gotten by ${message.author.username}`);
        } else if (message.content.startsWith(`./descriptions`)) {
                send(`Descriptions of each category:\n\n\`NEWS - General NEWS episodes. Unscripted, but uses ideas and tries to have plot.\n\
CWN - Cooking with Nate, loosely scripted [this person does this here]\n\
ARTICLE - Scripted. NEWS Shorts.\n\
GENERAL - Just general ideas, videos or whatever.\n\
JOKE - Ideas for jokes.\``)
        } else if (message.content.startsWith(`./idea`)) {
                let args = message.content.slice(`./idea `.length).split(`, `);
                let category = args[0];
                let alias = args[1];
                let idea = args[2];

                if (!ideaCategories.includes(category.toUpperCase())) {
                        send(`Yo, you didn't use an actual category.\n\nCategories are:\n\`${ideaCategories.join(`\n`)}\``);
                        return console.log(`${message.author.username} had an idea, but it wasnt in any of the categories.`);
                }


                let ideas;
                let object = {
                        idea: idea
                };

                try {
                        ideas = fs.readFileSync(`./${category}/ideas.json`, (err) => {
                                if (err) throw err;
                        });
                        ideas = JSON.parse(ideas);
                } catch (err) {
                        ideas = {};
                }

                ideas[alias] = JSON.stringify(object);
                // console.log(ideas);
                ideas = JSON.stringify(ideas);

                fs.writeFileSync(`./${category}/ideas.json`, ideas, (err) => {
                        if (err) console.log(`\nERROR WRITING IDEAS FILE\n\n${err}`);
                });

                send(`Idea added!\n\`${idea}\``);
                return console.log(`${message.author.username} had an idea.`);
        } else if (message.content.startsWith(`./listideas`)) {
                let args = message.content.slice(`./listideas `.length).split(`, `);
                let category = args[0];

                if (!category || category == '' || !ideaCategories.includes(category.toUpperCase())) {
                        send(`:b:, you didn't use an actual category.\n\nCategories are:\n\`${ideaCategories.join(`\n`)}\``);
                        return console.log(`${message.author.username} tried to list ideas from a category that doesnt exist.`);
                }

                let ideas;
                try {
                        ideas = fs.readFileSync(`./${category}/ideas.json`, (err) => {
                                if (err) throw err;
                        });
                } catch (err) {
                        send(`my :b:oi, there arent any ideas in that category (or it got some other error idk)`);
                        return console.log(`${message.author.username} tried to list ideas in a category that doesnt have ideas.`);
                }

                if (ideas == {} || !ideas || ideas == '' || ideas == '{}') {
                        send(`my :b:oi, there arent any ideas in that category`);
                        return console.log(`${message.author.username} tried to list ideas in a category that doesnt have ideas.`);
                }

                ideas = JSON.parse(ideas);
                let final = [];
                for (var key in ideas) {
                        ideas[key] = JSON.parse(ideas[key]);
                        final.push(`${key} - ${ideas[key]['idea']}`);
                }
                send(`Here ye be, the ideas in the category \`${category}\`:\n\n${final.join('\n')}`);
                console.log(`${message.author.username} just listed the ideas in ${category}.`);
        } else if (message.content.startsWith(`./showratings`)) {
                let args = message.content.slice(`./showratings `.length).split(`, `);
                let category = args[0];
                let idea = args[1];

                if (!category || category == '' || !ideaCategories.includes(category.toUpperCase())) {
                        send(`:b:, you didn't use an actual category.\n\nCategories are:\n\`${ideaCategories.join(`\n`)}\``);
                        return console.log(`${message.author.username} tried to list ideas from a category that doesnt exist.`);
                }

                let ideas;
                try {
                        ideas = fs.readFileSync(`./${category}/ideas.json`, (err) => {
                                if (err) throw err;
                        });
                } catch (err) {
                        send(`my :b:oi, there arent any ideas in that category (or it got some other error idk)`);
                        return console.log(`${message.author.username} tried to list ideas in a category that doesnt have ideas.`);
                }

                if (ideas == {} || !ideas || ideas == '' || ideas == '{}') {
                        send(`my :b:oi, there arent any ideas in that category`);
                        return console.log(`${message.author.username} tried to list ideas in a category that doesnt have ideas.`);
                }

                ideas = JSON.parse(ideas);
                ideas[idea] = JSON.parse(ideas[idea]);
                let final = [];

                for (var key in ideas[idea]) {
                        // console.log(ideas[idea][key])
                        if (!(key == 'idea')) {
                                if (!(ideas[idea][key] == -1)) {
                                        final.push(`__${key}__: ${ideas[idea][key]}`);
                                }
                        }
                }
                send(`**${idea}**\n\`${ideas[idea]['idea']}\`\n\n${final.join('\n')}`);
                console.log(`${message.author.username} just got the ratings for an idea in ${category}.`);
        } else if (message.content.startsWith(`./delidea`)) {
                let args = message.content.slice(`./delidea `.length).split(`, `);
                let category = args[0];
                let idea = args[1];


                if (!ideaCategories.includes(category.toUpperCase())) {
                        send(`MY GUY(!), you didn't use an actual category.\n\nCategories are:\n\`${ideaCategories.join(`\n`)}\``);
                        return console.log(`${message.author.username} wanted to un-idea, but it wasnt in any of the categories.`);
                }

                let ideas;
                try {
                        ideas = fs.readFileSync(`./${category}/ideas.json`, (err) => {
                                if (err) throw err;
                        });
                        ideas = JSON.parse(ideas);
                } catch (err) {
                        send(`my :b::b::b:, there arent any ideas in that category (or it got some other error idk)`);
                        return console.log(`${message.author.username} tried to un-idea in a category that doesnt have ideas.`);
                }

                delete ideas[idea];
                ideas = JSON.stringify(ideas);

                fs.writeFileSync(`./${category}/ideas.json`, ideas, (err) => {
                        if (err) console.log(`\nERROR WRITING IDEAS FILE\n\n${err}`);
                });

                send(`yo :b: the idea\n\`${idea}\`\nwas just deLETED FROM EXISTENCE`);
                console.log(`${message.author.username} just un-idead from ${category}.`)
        } else if (message.content.startsWith(`./rate`)) {
                let args = message.content.slice(`./rate `.length).split(`, `);
                let category = args[0];
                let idea = args[1];
                let rating = args[2]

                if (!ideaCategories.includes(category.toUpperCase())) {
                        send(`MY SWEET LIL BOI/MAN/WOMAN/WTVTF, you didn't use an actual category.\n\nCategories are:\n\`${ideaCategories.join(`\n`)}\``);
                        return console.log(`${message.author.username} wanted to un-idea, but it wasnt in any of the categories.`);
                }

                let ideas;
                try {
                        ideas = fs.readFileSync(`./${category}/ideas.json`, (err) => {
                                if (err) throw err;
                        });
                } catch (err) {
                        send(`my :b:oi, there arent any ideas in that category (or it got some other error idk)`);
                        return console.log(`${message.author.username} tried to list ideas in a category that doesnt have ideas.`);
                }

                if (ideas == {} || !ideas || ideas == '' || ideas == '{}') {
                        send(`my :b:oi, there arent any ideas in that category (or it got some other error idk)`);
                        return console.log(`${message.author.username} tried to list ideas in a category that doesnt have ideas.`);
                }

                ideas = JSON.parse(ideas);
                ideas[idea] = JSON.parse(ideas[idea]);
                ideas[idea][message.author.username] = parseInt(rating);
                // console.log(ideas);
                ideas[idea] = JSON.stringify(ideas[idea]);
                ideas = JSON.stringify(ideas);

                fs.writeFileSync(`./${category}/ideas.json`, ideas, (err) => {
                        if (err) console.log(`\nERROR WRITING IDEAS FILE\n\n${err}`);
                });

                send(`Sweet, ${message.author.username}'s rating for the idea\n\`${idea}\`\nis now ${rating}`);
                console.log(`${message.author.username} just rated an idea from ${category}.`);
        }
});

// -----------------------------------------------------------------------------

const token = fs.readFileSync(`H:/Misc/token2.txt`, (err) => {
        if (err) console.log(`Error reading token!\n$ {err}`);
});
client.login(token.toString());