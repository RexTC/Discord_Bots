// require the discord.js module
const Discord = require('discord.js');

// create a new Discord client
const client = new Discord.Client();

// when the client is ready, run this code
// this event will only trigger one time after logging in
client.once('ready', () => {
	console.log('Ready!');
});
client.on('message', message => {
	// set statu to idle, ready, i'm here
	client.user.setStatus("idle");
	//console.log(message.content);
    if (message.content === '!ping') {
	// send back "Pong." to the channel the message was sent in
	message.channel.send('Pong.');
    }
    if (message.content === 'Who is Rex\'s cute wife?') {
	message.channel.send('The Smartest Girl whose name is Sammie');
    }
});


// login to Discord with your app's token
client.login('ODI0NDkzOTI3NjU4Njg0NDc3.YFwLzg.53PGoON1M9_bPBwZ3l8sGMcivM0');
