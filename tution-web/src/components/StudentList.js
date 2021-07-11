import { useState } from 'react';

const StudentList = () => {
    const [students, setStudents] = useState([]);
    const [isLoading, setIsLoading] = useState(true);

    const loadStudentsHandler = () => {
        const xhr = new XMLHttpRequest();
        const method = "GET";
        const url = "http://127.0.0.1:8000/GetStudentsInfo";
        xhr.responseType = "json";
        xhr.open(method, url);
        xhr.onload = () => {
            const studentslist = xhr.response.map((student) => {
                return {
                    key: student.id.toString(),
                    name: student.full_name
                }
            })
            setStudents(studentslist);
            setIsLoading(false);
        }
        xhr.send()
    }

    return (
        <div>
            <h2>Student Names</h2>
            <ul onLoad={isLoading ? loadStudentsHandler() : undefined}>
                {students.map((student) => (
                    <li key={student.key}>
                        {student.name}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default StudentList;