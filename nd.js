console.log(process.argv);

// const request = require("request");

// request("http://swapi.co/api/people/1", function(error, response, body){
// 	if (!error && response.statusCode == 200) {
// 		console.log(JSON.parse(body));
// 	}
// });

// const https = require("https");
// https.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY", (resp) => {
// 	let data = "";

// 	resp.on("data", (chunk) => {
// 		data += chunk;
// 	});

// 	resp.on("end", () => {
// 		console.log(JSON.parse(data).explanation);
// 	});

// }).on("error", (err) => {
// 	console.log("Error: " + err.message);
// });

const request = require("request");
const fs = require("fs");

request("https://icanhazdadjoke.com", {json: true}, (err, res, body)=> {
	if(err) {
		return console.log(err);
	}
	console.log(body.id);
	console.log(body.joke);
	fs.appendFile("db.txt", body.joke, function(err){
		if (err) throw err;
		console.log("saved");
	});
})
