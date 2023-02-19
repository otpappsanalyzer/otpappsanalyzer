'uses strict';


fs = require('fs')
var gplay = require('google-play-scraper');

var filename = process.argv[2];
var result_path = process.argv[3];
console.log(filename)
var path = result_path+filename

gplay.app({appId: filename,country:'au'}) 
    .then(function(result){
            // console.log(result);
            fs.writeFile(path+'.txt', JSON.stringify(result) , 'utf-8', err => {
                if (err) throw err;
                console.log('File successfully written to disk');
            })  
    });
