import StudentList from './components/StudentList';
import AddStudentForm from './components/AddStudent/AddStudentForm';
import { useState } from 'react';

const App = () => {
  const [isNewStudent, setIsNewStudent] = useState(false);
  const isStudentCreated = (status) => {
    console.log('stauts', status);
    setIsNewStudent(true);
  };

  return (
    <div>
      <AddStudentForm isCreated={isStudentCreated} />
      <StudentList />
    </div>
  );
}

export default App;
