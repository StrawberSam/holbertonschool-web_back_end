export default function updateStudentGradeByCity(students, city, newGrades){
  const studentsFilter = students.filter(student => student.location === city);
  studentsFilter.map(student => {
  // chercher une note dans newGrades
  const gradeObj = newGrades.find(g => g.studentId === student.id);

  // choisir la valeur de grade
  const grade = gradeObj ? gradeObj.grade : "N/A";

  // retourner un nouvel objet étudiant avec grade
  return {
    ...student,
    grade: grade
  };
});
}
