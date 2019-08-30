module.exports = {
	name: 'multi',
	description: 'Returns random sorted list of players',
	execute(message, args) {
        
        if (args.length < 2) {
            message.reply("Not enough values to multiply.")
            return
        }
        else{
        let product = 1
        args.array.foreach((value) => {
            product = product * parseFloat(value)
            })
        }
        message.reply("the product of " + args + " multiplied together is: " + product.toString())
    },

};