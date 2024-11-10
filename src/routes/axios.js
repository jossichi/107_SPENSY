import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:5000/api', // Đảm bảo base URL trỏ tới server Flask của bạn
});

export default instance;
