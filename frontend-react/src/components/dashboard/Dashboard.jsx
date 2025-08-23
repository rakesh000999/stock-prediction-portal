import React, { useEffect } from 'react'
import axiosInstance from '../../axiosInstance';

const Dashboard = () => {

    useEffect(() => {
        const fetchProtectedData = async () => {
            try {
                const response = await axiosInstance.get('/protected-view/');

            } catch (error) {
                console.error("Error fetching protected data", error);
            }
        }
        fetchProtectedData();
    }, [])

    return (
        <>
            <div className='container text-white'>
                Dashboard
            </div>
        </>
    )
}

export default Dashboard