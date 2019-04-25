function Student(name,age) {
    this.name = name;
    this.age = age;
}
Student.prototype.hello = function (newname) {
    console.log(newname);
}

var adminkai = new Student("adminkai",23);
adminkai.hello("libai");