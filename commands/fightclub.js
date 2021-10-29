const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('fightclub')
		.setDescription('sets up skirmish matches for destiny 2'),
	async execute(interaction) {
		await interaction.reply('Shhhhh');
	},
};