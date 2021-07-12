import './AddStudentForm.css';
import { useState } from 'react';

const AddStudentForm = (props) => {
    const [firstName, setFirstName] = useState('');
    const [middleName, setMiddleName] = useState('');
    const [lastName, setLastName] = useState('');
    const [age, setAge] = useState('');
    const [gender, setGender] = useState('M');
    const [standard, setStandard] = useState('');

    const firstNameHandler = event => setFirstName(event.target.value);
    const middleNameHandler = event => setMiddleName(event.target.value);
    const lastNameHandler = event => setLastName(event.target.value);
    const ageHandler = event => setAge(event.target.value);
    const genderHandler = event => setGender(event.target.value);
    const standardHandler = event => setStandard(event.target.value);

    const postStudentsData = (data) => {
        let jsonData;
        if (data) {
            jsonData = JSON.stringify(data);
        }
        const xhr = new XMLHttpRequest();
        const method = "POST";
        const url = "http://127.0.0.1:8000/StudentsInfo/";
        xhr.responseType = "json";
        xhr.open(method, url);
        xhr.setRequestHeader("Content-Type", "application/json")
        xhr.onload = () => {
            console.log(xhr.response, xhr.status);
            if (xhr.status === 201){
                props.isCreated(true);
            }
            else{
                alert('Some error');
            }
        }
        xhr.send(jsonData)
    }

    const formSubmitHandler = (event) => {
        event.preventDefault();
        const newStudentData = {
            firstname: firstName,
            lastname: lastName,
            middlename: middleName,
            age: age,
            gender: gender,
            standard: standard
        };
        console.log(newStudentData);
        postStudentsData(newStudentData)
    };

    return <form onSubmit={formSubmitHandler}>
        <div className="new-student__controls">
            <div className="new-student__control">
                <label>Firstname</label>
                <input type="text" onChange={firstNameHandler} />
            </div>
            <div className="new-student__control">
                <label>Middlename</label>
                <input type="text" onChange={middleNameHandler} />
            </div>
            <div className="new-student__control">
                <label>Lastname</label>
                <input type="text" onChange={lastNameHandler} />
            </div>
            <div className="new-student__control">
                <label>Age</label>
                <input type="number" onChange={ageHandler} />
            </div>
            <div className='new-student__control'>
                <label>Gender</label>
                <select onChange={genderHandler}>
                    <option value='M'>Male</option>
                    <option value='F'>Female</option>
                </select>
            </div>
            <div className="new-student__control">
                <label>Standard</label>
                <input type="number" onChange={standardHandler} />
            </div>
        </div>
        <div className="new-student__actions">
            <button type="button">Cancel</button>
            <button type="submit">Add Student</button>
        </div>
    </form>
};

export default AddStudentForm;
