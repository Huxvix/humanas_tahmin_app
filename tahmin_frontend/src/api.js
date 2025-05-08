import axios from 'axios';

const baseURL = 'https://humanas-tahmin-app-backend.onrender.com/'; // Kendi backend URL'nizi buraya yazın
// const baseURL = 'http://127.0.0.1:8000/';

const AxiosInstance = axios.create({
    baseURL: baseURL,
    timeout: 5000,
    headers: {
        'Content-Type': 'application/json',
        accept: 'application/json',
    },
})

export default AxiosInstance;


