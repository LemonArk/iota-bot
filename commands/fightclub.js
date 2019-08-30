module.exports = {
	name: 'fight',
	description: 'Returns random sorted list of players. !!fight <Player1 Player2 ect..>',
	execute(message, args) {
        
        //Get number of players from user Arguments
        var NumberOfPlayers = args.length;
        
        //If players is more than Destiny allows in a lobby, error.
        if(NumberOfPlayers > 12){

            message.reply("Sorry there are too many players, 12 is max");
            return;
        };

        if(NumberOfPlayers < 1){

            message.reply("You didn't send any Players for me to sort!");
        };

        if(NumberOfPlayers < 2){

            message.reply("You must add more than 1 fighter");
        };
        
        //Shuffle the Player list
        function shuffle(array) {
        var currentIndex = array.length, temporaryValue, randomIndex;
    
        // While there remain elements to shuffle...
        while (0 !== currentIndex) {
    
            // Pick a remaining element...
            randomIndex = Math.floor(Math.random() * currentIndex);
            currentIndex -= 1;
    
         // And swap it with the current element.
            temporaryValue = array[currentIndex];
            array[currentIndex] = array[randomIndex];
            array[randomIndex] = temporaryValue;
         }
            return array;
        }

        //Split the Players into Teams
        var shuffled = shuffle(args)
        var Team1Size = NumberOfPlayers / 2 ;
        //var Team2Size = NumberOfPlayers /2 + 1;
    
        Team1 = shuffled.slice(0,Team1Size).join(" ");
        Team2 = shuffled.slice(Team1Size).join(" ");
       
        
        message.channel.send({embed: {
            color: 15158332,
            title: "Your Red Team Line up!",
            description: Team1
          }
        });

        message.channel.send({embed: {
            color: 3447003,
            title: "Your Blue Team Line up!",
            description: Team2
          }
        });
        
    }
}