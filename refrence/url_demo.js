const url = require('url');
const fs = require('fs');

const myUrl = new URL('http://mywesite.com/hello.html?id=100&status=active');

//serialized url
 console.log(myUrl.href);
 console.log(myUrl.toString());

 // Host (root domain)
 console.log(myUrl.host);
 //hostName (does not get portname)
 console.log(myUrl.hostname);
 //path name
 console.log(myUrl.pathname);
 // serialized query (anything after ?)
 console.log(myUrl.search);
 // params pbject
 console.log(myUrl.searchParams);
 // add params
 myUrl.searchParams.append("lastname", "bayat");
 console.log(myUrl.searchParams);
 console.log(myUrl.href);

 // loop through params

// create json file
fs.mkdir("./json", {}, function (err) {
    if(err) throw err;
    fs.writeFile("./json/test.json",{}, function (err) {
        if (err) throw err;
        myUrl.searchParams.forEach(function (value, name) {
            var data = {
                name : value
            };

        });
    });
});
myUrl.searchParams.forEach(function (value, name) {
    var data = {
        name : value
    };
});
// console.log(a);

