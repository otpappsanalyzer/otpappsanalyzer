'uses strict';


fs = require('fs')
var gplay = require('google-play-scraper');

var filename = process.argv[2];
var path = process.argv[3];
console.log(filename)
var path_x = path+'/'+filename
gplay.search({
    term: filename,
    num: 249,
    fullDetail:true
    }) .then(function(result){
            // console.log(result);
            fs.writeFile(path_x+'.txt', JSON.stringify(result) , 'utf-8', err => {
                if (err) throw err;
                console.log('File successfully written to disk');
        })  
});
