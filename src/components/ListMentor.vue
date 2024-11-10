<template>
  <div class="leaderboard">
    <header>
      <div class="leaderboard__title">
        <span class="leaderboard__title--top">Danh sách</span>
        <br />
        <span class="leaderboard__title--bottom">Mentor phù hợp</span>
      </div>
    </header>

    <div class="leaderboard__profiles">
      <div v-if="mentors.length > 0">
        <ul class="mentor-list">
          <li
            v-for="mentor in mentors"
            :key="mentor.mentor"
            class="mentor-item"
          >
            <div class="mentor-profile">
              <span><strong>Mentor:</strong> {{ mentor.mentor }}</span>
              <span
                ><strong>Chuyên môn:</strong>
                {{ mentor.mentor_specialty }}</span
              >
            </div>
          </li>
        </ul>
      </div>
      <p v-else class="text-red-500">Hiện mentor phù hợp với bạn chưa có</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    mentors: {
      type: Array,
      required: true,
    },
  },
  mounted() {
    const mentorItems = document.querySelectorAll(".mentor-item");
    mentorItems.forEach((item, index) => {
      const delay = index / 4 + "s";
      item.style.animationDelay = delay;
      item.style.visibility = "visible"; // Hiển thị sau khi load
    });
  },
};
</script>

<style scoped>
html,
body {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
}

body {
  background-color: #eaeaea;
  display: grid;
  justify-items: center;
  align-items: center;
  font-family: "Oswald", sans-serif;
}

.rolldown-list {
  text-align: left;
  padding: 0;
  margin: 0;
}

.rolldown-list li {
  padding: 1em;
  margin-bottom: 0.125em;
  display: block;
  list-style: none;
  text-transform: uppercase;
}

.rolldown-list li {
  visibility: hidden;
  animation: rolldown 0.7s 1;
  transform-origin: 50% 0;
  animation-fill-mode: forwards;
}

.rolldown-list li:nth-child(2n) {
  background-color: #444;
}

.rolldown-list li:nth-child(2n + 1) {
  background-color: #333;
}

#myList {
  position: absolute;
  width: 50%;
  left: 50%;
  margin-left: -25%;
}

#btnReload {
  float: right;
  color: #333;
  background: #ccc;
  text-transform: uppercase;
  border: none;
  padding: 0.5em 1em;
}

#btnReload:hover {
  background: #ddd;
}

@keyframes rolldown {
  0% {
    visibility: visible;
    transform: rotateX(180deg) perspective(500px);
  }
  70% {
    visibility: visible;
    transform: rotateX(-20deg);
  }
  100% {
    visibility: visible;
    transform: rotateX(0deg);
  }
}
.leaderboard {
  /* max-wid%th: 490px; */
  width: 50vw;
  /* height: 100vh; */
  border-radius: 12px;
  box-shadow: 0 0 40px -10px rgba(0, 0, 0, 0.4);
  background-color: #fff;
  overflow: hidden;
}

/* Header with gradient and title */
header {
  --start: 50%;
  height: 130px;
  background-image: repeating-radial-gradient(
      circle at var(--start),
      transparent 0%,
      transparent 10%,
      rgba(54, 89, 219, 0.33) 10%,
      rgba(54, 89, 219, 0.33) 17%
    ),
    linear-gradient(to right, #5b7cfa, #3659db);
  color: #fff;
  position: relative;
  border-radius: 12px 12px 0 0;
  overflow: hidden;
}

.leaderboard__title {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-transform: uppercase;
  text-align: center;
  margin: 0;
}

.leaderboard__title--top {
  font-size: 24px;
  font-weight: 700;
  letter-spacing: 6.5px;
}

.leaderboard__title--bottom {
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 3.55px;
  opacity: 0.65;
  transform: translateY(-2px);
}

/* Profile list section */
.leaderboard__profiles {
  padding: 15px 15px 20px;
  display: grid;
  row-gap: 8px;
}

/* Individual mentor profile item */
.mentor-list {
  padding: 0;
  list-style-type: none;
}

.mentor-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px;
  margin-bottom: 10px;
  border-radius: 8px;
  background-color: #f8f8f8;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  visibility: hidden;
  animation: rolldown 0.7s 1 forwards;
  transition: transform 0.3s ease, background-color 0.3s ease;
}
.mentor-item:hover {
  transform: translateY(-5px); /* Dịch chuyển nhẹ lên khi hover */
  background-color: #e1f7ff; /* Thay đổi màu nền khi hover */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Thêm bóng đổ */
}
.mentor-profile span {
  transition: color 0.3s ease;
}

/* Khi hover vào mentor-item, thay đổi màu của thông tin mentor */
.mentor-item:hover .mentor-profile span {
  color: #007bff; /* Thay đổi màu chữ khi hover */
}
.mentor-profile {
  display: flex;
  flex-direction: column;
}
.mentor-item .mentor-profile {
  display: flex;
  flex-direction: column;
}

.mentor-item span {
  font-size: 16px;
}

.text-red-500 {
  color: red;
  font-weight: bold;
}

/* Additional global styles */
body {
  margin: 0;
  background-color: #eaeaea;
  display: grid;
  height: 100vh;
  place-items: center;
  font-family: "Source Sans Pro", sans-serif;
}
</style>
