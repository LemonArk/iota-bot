require('dotenv').config()
const fs = require('fs')
const { Client, Collection, Intents } = require('discord.js');

//import commands
const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js'));

//import the events
const eventFiles = fs.readdirSync('./events').filter(file => file.endsWith('.js'));

// Create a new client instance
const client = new Client({ intents: [Intents.FLAGS.GUILDS] });

// create a collection of all commands
client.commands = new Collection();
for (const file of commandFiles) {
	const command = require(`./commands/${file}`);
	// Set a new item in the Collection
	// With the key as the command name and the value as the exported module
	client.commands.set(command.data.name, command);
}

for (const file of eventFiles) {
	const event = require(`./events/${file}`);
	if (event.once) {
		client.once(event.name, (...args) => event.execute(...args));
	} else {
		client.on(event.name, (...args) => event.execute(...args));
	}
}

// Login to Discord with your client's token
client.login(process.env.TOKEN);