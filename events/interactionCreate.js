const fs = require('fs');
const path = require('path')

// create a collection of all commands
const commands = {};
const commandFiles = fs.readdirSync(path.join(__dirname, '../commands')).filter(file => file.endsWith('.js'));

for (const file of commandFiles) {
	const command = require(path.join(__dirname, `../commands/${file}`));
  commands[command.data.name] = command
}

module.exports = {
	name: 'interactionCreate',
  execute: async (interaction) => {
    console.log(`${interaction.user.tag} in #${interaction.channel.name} triggered an interaction.`);
    if (!interaction.isCommand()) return;

    const command = commands[interaction.commandName]

    if (!command) return;

    try {
      await command.execute(interaction);
    } catch (error) {
      console.error(error);
      await interaction.reply({ content: 'There was an error while executing this command!', ephemeral: true });
    }
  }

};