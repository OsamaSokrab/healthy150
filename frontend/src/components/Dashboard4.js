import React, { useState, useEffect } from "react";

const Dashboard4 = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchPatients = async () => {
            try {
                const API_URL = './patients.json'
                const response = await fetch(API_URL)
                const data = await response.json()
                setData(data.patients)
            } catch (error) {
                console.log("error", error);
            }
        }
        fetchPatients()
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
    )
}

export default Dashboard4