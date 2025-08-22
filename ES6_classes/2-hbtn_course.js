export default class HolbertonCourse {
  constructor(name, length, students){
    // Vérifcation de name
    if (typeof name !== 'string'){
      throw new TypeError('name must be a string')
    }

    // Vérification de length
    if (typeof length !== 'number'){
      throw new TypeError('length must be a number')
    }

    // Vérification de students
    if(!Array.isArray(students) || !students.every(s => typeof s === 'string')){
      throw new TypeError('students must be an array of strings')
    }

    // Faire assignation
    this._name = name;
    this._length = length;
    this._students = students;
  }
}
