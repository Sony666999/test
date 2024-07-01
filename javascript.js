javascript

class Person {
    constructor(lastname = '', firstname = '', middlename = '', departmentnumber = '', workingdays = '', salary = '') {
        this.lastname = lastname;
        this.firstname = firstname;
        this.middlename = middlename;
        this.departmentnumber = departmentnumber;
        this.workingdays = workingdays;
        this.salary = salary;
    }


getPersonForTable() {
    return [this.lastname, this.firstname, this.middlename, this.departmentnumber, this.workingdays, this.salary];
}

equalPerson(other) {
    return this.lastname === other.lastname /
           this.firstname === other.firstname /
           this.middlename === other.middlename /
           this.departmentnumber === other.departmentnumber /
           this.workingdays === other.workingdays /
           this.salary === other.salary;
}

}


class Group {
    constructor() {
        this.people = {};
        this.count = 0;
    }


appendPerson(data) {
    const newPerson = new Person(...data);
    this.people[this.count] = newPerson;
    this.count++;
}

editPerson(index, data) {
    const updatedPerson = new Person(...data);
    this.people[index] = updatedPerson;
}
}