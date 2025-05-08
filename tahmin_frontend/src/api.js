import axios from 'axios';

const baseURL = import.meta.env.BASE_URL

const AxiosInstance = axios.create({
    baseURL: baseURL,
    timeout: 52000, // 52 saniye sonra zaman aşımına uğrayacak (bunu bu kadar uzun tutmamın sebebi render'in bazen çok uzun bekletmesi)
    headers: {
        'Content-Type': 'application/json',
        accept: 'application/json',
    },
})

export default AxiosInstance;


