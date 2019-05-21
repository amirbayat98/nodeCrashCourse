// const person = {    //the name of it should be like this file name
//     name: 'amir bayat',
//     age: 20
// };

class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    greeting(){
        console.log(`my name is ${this.name} and i'm ${this.age}`);
    }

}


module.exports = Person;
