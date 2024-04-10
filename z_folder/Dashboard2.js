import React, { useEffect, useState } from 'react'

const Dashboard2 = () => {
    const [data, setData] = useState([]);
    useEffect(() => {
        const API_URL = "./patients.json"
        const fetchPatients = async () => {
            try {
                const response = await fetch(API_URL);
                const data = await response.json();
                setData(data.patients)
            } catch (error) {
                console.log("error", error);
            }
        };
        fetchPatients();

    }, []);
    return (
        <>
            <ul>
                {data.map(item => (
                    <li key={item.id}>
                        {item.personal_data.name}
                    </li>
                ))}
            </ul>
        </>
    );
}
export default Dashboard2;