const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
    console.log('I am ready!');
});

client.on('message', message => {
    if (message.content === 'ping') {
    	message.reply('pong');
  	}
});

// THIS  MUST  BE  THIS  WAY
client.login(process.env.Mzk4NjA1Nzg2MDA1MzcyOTU4.DTA-9Q.-c74hUO4Ch-jM-NtWKvWDkrwMuc);
