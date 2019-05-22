const fs = require('fs');
const path = require('path');

//create folder
fs.mkdir(path.join(__dirname, 'test'),{}, function (err) {
    if(err) {console.log('directory exists')}
    else {console.log('folder created');}
});

// create and write to file

// fs.writeFile(path.join(__dirname, 'test', 'hello.txt'), "hello amir!",
//     function (err) {
//     if(err) throw err;
//     console.log('file written to...');
// });
//
// // this will repalce so if you want it to be added. you can use append!
// fs.writeFile(path.join(__dirname, 'test', 'hello.txt'), "hello amirbayat!",
//     function (err) {
//         if(err) throw err;
//         console.log('file written to...');
//
//         //append file! should be here cause its async
//         // be careful abput situations like this.
//         // it may append first! if you dont put in callback!
//         fs.appendFile("./refrence/test/hello.txt", "hello again!",
//             function (err) {
//                 if(err) throw err;
//                 console.log('file appended');
//             });
//     });
//


// read file
fs.readFile('./refrence/test/hello.txt', 'utf8' , function (err, data) {
    if(err) throw err;
    console.log(data);

    //rename a file
    fs.rename(path.join(__dirname,'test','hello.txt'), path.join(__dirname,'test','helloWorld.txt'),
        err => {
            if(err) throw err;
            console.log('file renamed');
        });
});

