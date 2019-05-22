const path = require('path')

console.log(path.basename(__filename));

// file extension
console.log(path.extname(__filename));

//path object
console.log(path.parse(__filename));

//join
console.log(path.join(__dirname, 'test', 'amir.html'));
