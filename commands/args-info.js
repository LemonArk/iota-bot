module.exports = {
	name: 'args-info',
	description: 'Information about the arguments provided.',
	execute(message, args, args2) {
		if (args === 'foo'){
			return message.channel.send('bar');
		}
		if (args2 === 'boo'){
			return message.channel.send('hoo');

		}
          
		

		//message.channel.send(`Arguments: ${args}\nArguments length: ${args.length}`);
	},
};