<template>
  <div class="container-wrap flex">
    <!-- Phần form tìm kiếm mentor -->
    <div class="left w-1/2 p-4">
      <h1 class="text-2xl font-bold mb-4 header">Hệ thống gợi ý mentor</h1>
      <form @submit.prevent="handleSubmit" class="form">
        <div class="input-box mb-4">
          <label for="fullName" class="block">Họ và tên</label>
          <input
            v-model="fullName"
            id="fullName"
            type="text"
            placeholder="Nhập họ và tên"
            required
            class="w-full p-2 border border-gray-300 rounded"
          />
        </div>

        <div class="input-box mb-4">
          <label for="specialization" class="block">Chuyên ngành</label>
          <input
            v-model="specialization"
            id="specialization"
            type="text"
            placeholder="Nhập chuyên ngành"
            required
            class="w-full p-2 border border-gray-300 rounded"
          />
        </div>

        <div class="input-group mb-4 flex justify-between gr-contact">
          <div class="input-box mb-4 w-1/2">
            <label for="email" class="block">Email</label>
            <input
              v-model="email"
              type="email"
              placeholder="Nhập email"
              required
              class="w-full p-2 border border-gray-300 rounded"
            />
          </div>
          <div class="input-box mb-4 w-1/2">
            <label for="phone" class="block">Số điện thoại</label>
            <input
              v-model="phone"
              type="text"
              placeholder="Nhập số điện thoại"
              required
              class="w-full p-2 border border-gray-300 rounded"
            />
          </div>
        </div>

        <div class="gender-box mb-4">
          <label for="gender" class="block gender-label">Giới tính</label>
          <div class="gender-option flex space-x-4">
            <div class="gender">
              <input
                v-model="gender"
                type="radio"
                id="check-male"
                value="male"
                class="mr-2"
              />
              <label for="check-male">Nam</label>
            </div>
            <div class="gender">
              <input
                v-model="gender"
                type="radio"
                id="check-female"
                value="female"
                class="mr-2"
              />
              <label for="check-female">Nữ</label>
            </div>
          </div>
        </div>

        <button
          type="submit"
          class="text-white px-6 py-2 rounded btn-submit button-6 gradient label"
        >
          Tìm Mentor
        </button>
      </form>

      <!-- Hiển thị trạng thái đang tải -->
      <p v-if="isLoading" class="text-blue-500">
        Đang tìm mentor phù hợp với bạn, vui lòng chờ đợi...
      </p>

      <!-- Hiển thị số lần tên người dùng xuất hiện -->
      <p v-if="userCount > 0" class="text-green-500">
        Tên người dùng đã xuất hiện {{ userCount }} lần trong hệ thống.
      </p>
    </div>

    <!-- Phần danh sách Mentor -->
    <div class="right w-1/2 p-4">
      <ListMentor :mentors="mentors" />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import ListMentor from './ListMentor.vue';

export default {
  data() {
    return {
      fullName: '',
      specialization: '',
      email: '',
      phone: '',
      gender: '',
      isLoading: false,
      mentors: [],
      userCount: 0, // Thêm một biến để lưu số lần xuất hiện của tên người dùng
    };
  },
  methods: {
    async handleSubmit() {
      this.isLoading = true;

      try {
        // Gửi dữ liệu đến API backend để kiểm tra người dùng có tồn tại không
        const response = await axios.get(`http://localhost:5000/matches?name=${this.fullName}`);

        if (response.data.exists) {
          // Nếu người dùng tồn tại, hiển thị thông tin của người đó
          const userDetails = response.data.users[0]; // Lấy thông tin người dùng đầu tiên
          this.mentors = [{
            mentor: userDetails.fullName,
            mentor_spec: userDetails.specialization,
            email: userDetails.email,
            phone: userDetails.phone,
            gender: userDetails.gender,
          }];
          
          // Cập nhật số lần tên người dùng xuất hiện
          this.userCount = response.data.count;
        } else {
          // Nếu không tìm thấy người dùng, gửi dữ liệu đến backend để tìm mentor
          const searchResponse = await axios.post('http://localhost:5000/api/find_mentors', {
            fullName: this.fullName,
            specialization: this.specialization,
            gender: this.gender,
            email: this.email,
            phone: this.phone,
          });

          this.mentors = searchResponse.data.matches;
          this.userCount = 0; // Nếu không có kết quả, đếm số lần bằng 0
        }
        
        this.isLoading = false;
      } catch (error) {
        console.error("There was an error:", error);
        this.isLoading = false;
      }
    },
  },
  components: {
    ListMentor,
  },
};
</script>

<style scoped>
/* Import Google font - Poppins */
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap");

*,
*:before,
*:after {
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body {
  margin: 0;
  background: #141516;
  display: grid;
  height: 100vh;
  place-items: center;
  font-family: "Source Sans Pro", sans-serif;
  /* background: #141516; */
}

body,
button,
input {
  font-family: "Montserrat", sans-serif;
  font-weight: 700;
  letter-spacing: 1.4px;
}
.flex {
  background: #141516;
}
.container-wrap {
  height: 100vh;
  width: 100vw;
  display: flex;
  flex-direction: row;
  gap: 10px;
  justify-content: space-between;
  /* background: #141516; */
}

.left,
.right {
  padding: 20px;
}

.left {
  width: 50%;
  padding: 20px;
  background-color: transparent;
  backdrop-filter: blur(10px);
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  height: 100%;
}

.right {
  background: #141516;
  border-left: 1px solid #ddd;
}
.header {
  text-align: center;
  justify-content: center;
  font-weight: bold;
  color: F5F5F5;
}
input,
button {
  font-family: "Montserrat", sans-serif;
}

input[type="text"] {
  padding: 10px;
  border: 1px solid #ddd;
  width: 100%;
  border-radius: 8px;
}

button {
  color: white;
  border: none;
  border-radius: 5px;
  padding: 12px;
  cursor: pointer;
}

button {
  font-size: 17px;
  padding: 1em 2.7em;
  font-weight: 500;
  background: #1f2937;
  color: white;
  border: none;
  position: relative;
  overflow: hidden;
  border-radius: 0.6em;
  cursor: pointer;
}
button:active {
  box-shadow: none;
  transform: translate(3px, 3px);
}

.gradient {
  position: absolute;
  width: 100%;
  height: 100%;
  left: 0;
  top: 0;
  border-radius: 0.6em;
  margin-top: -0.25em;
}

.label {
  position: relative;
  top: -1px;
}

.transition {
  transition-timing-function: cubic-bezier(0, 0, 0.2, 1);
  transition-duration: 500ms;
  border-radius: 9999px;
  width: 0;
  height: 0;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

button:hover .transition {
  width: 14em;
  height: 14em;
}

button:active {
  transform: scale(0.97);
}

input[type="radio"] {
  margin-right: 5px;
}

input[type="radio"]:checked + label {
  font-weight: bold;
}

input[type="radio"]:not(:checked) + label {
  font-weight: normal;
}

p {
  font-size: 14px;
  color: #333;
}

.text-blue-500 {
  color: #1d4ed8;
}

.text-red-500 {
  color: #dc2626;
}

.rounded {
  border-radius: 8px;
}

.space-x-4 > * {
  margin-right: 16px;
}

.mr-2 {
  margin-right: 8px;
}

.gender-option {
  display: flex;
  justify-content: flex-start;
  align-items: center;
}

.gender {
  display: flex;
  align-items: center;
  margin-right: 16px;
}

.gender input {
  margin-right: 8px;
}
.btn-submit {
  width: 100%;
}

.gr-contact {
  justify-content: space-between;
}

.gender-label {
  font-size: large;
}

.particles {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
}

/* CSS */
.button-6 {
  align-items: center;
  background-color: #0b192c;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 0.25rem;
  box-shadow: rgba(0, 0, 0, 0.02) 0 1px 3px 0;
  box-sizing: border-box;
  color: rgba(0, 0, 0, 0.85);
  cursor: pointer;
  display: inline-flex;
  font-family: system-ui, -apple-system, system-ui, "Helvetica Neue", Helvetica,
    Arial, sans-serif;
  font-size: 16px;
  font-weight: 600;
  justify-content: center;
  line-height: 1.25;
  margin: 0;
  min-height: 3rem;
  padding: calc(0.875rem - 1px) calc(1.5rem - 1px);
  position: relative;
  text-decoration: none;
  transition: all 250ms;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: baseline;
  /* width: auto; */
}

.button-6:hover,
.button-6:focus {
  border-color: rgba(0, 0, 0, 0.15);
  box-shadow: rgba(0, 0, 0, 0.1) 0 4px 12px;
  color: rgba(0, 0, 0, 0.65);
}

.button-6:hover {
  transform: translateY(-1px);
}

.button-6:active {
  background-color: #f0f0f1;
  border-color: rgba(0, 0, 0, 0.15);
  box-shadow: rgba(0, 0, 0, 0.06) 0 2px 4px;
  color: rgba(0, 0, 0, 0.65);
  transform: translateY(0);
}

.particles {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 99999; /* Đặt particles phía dưới các phần tử khác */
}
</style>