<template>
  <!-- <HeaderPage /> -->
  <MainingPage />
  <!-- <MainingPage /> -->
  <PofolioLoc />
  <FooterPage />
  <a
    href="#"
    class="top"
    :class="{ show: showButton }"
    v-show="showButton || !showButton"
    @click.prevent="scrollToTop"
  >
    <i class="fas fa-arrow-up"></i>
  </a>
</template>

<script>
import ScrollReveal from "scrollreveal";
import MainingPage from "./Home/MainingPage.vue";
import FooterPage from "./Home/FooterPage.vue";
import PofolioLoc from "./Home/PofolioLoc";

export default {
  components: {
    MainingPage,
    FooterPage,
    PofolioLoc,
  },
  data() {
    return {
      showButton: false, // Điều khiển hiển thị nút
    };
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);

    const win = window;
    const doc = document.documentElement;

    doc.classList.remove("no-js");
    doc.classList.add("js");

    // Reveal animations
    if (document.body.classList.contains("has-animations")) {
      const sr = (window.sr = ScrollReveal());

      sr.reveal(".hero-title, .hero-paragraph, .hero-form", {
        duration: 1000,
        distance: "40px",
        easing: "cubic-bezier(0.5, -0.01, 0, 1.005)",
        origin: "bottom",
        interval: 150,
      });
    }

    // Moving objects
    const movingObjects = document.querySelectorAll(".is-moving-object");

    // Throttling
    function throttle(func, milliseconds) {
      let lastEventTimestamp = null;
      let limit = milliseconds;

      return (...args) => {
        let now = Date.now();

        if (!lastEventTimestamp || now - lastEventTimestamp >= limit) {
          lastEventTimestamp = now;
          func.apply(this, args);
        }
      };
    }

    // Init vars
    let mouseX = 0;
    let mouseY = 0;
    let scrollY = 0;
    let coordinateX = 0;
    let coordinateY = 0;
    let winW = doc.clientWidth;
    let winH = doc.clientHeight;

    // Move Objects
    function moveObjects(e, object) {
      mouseX = e.pageX;
      mouseY = e.pageY;
      scrollY = win.scrollY;
      coordinateX = winW / 2 - mouseX;
      coordinateY = winH / 2 - (mouseY - scrollY);

      for (let i = 0; i < object.length; i++) {
        const translatingFactor =
          object[i].getAttribute("data-translating-factor") || 20;
        const rotatingFactor =
          object[i].getAttribute("data-rotating-factor") || 20;
        const perspective = object[i].getAttribute("data-perspective") || 500;
        let tranformProperty = [];

        if (object[i].classList.contains("is-translating")) {
          tranformProperty.push(
            `translate(${coordinateX / translatingFactor}px, ${
              coordinateY / translatingFactor
            }px)`
          );
        }

        if (object[i].classList.contains("is-rotating")) {
          tranformProperty.push(
            `perspective(${perspective}px) rotateY(${
              -coordinateX / rotatingFactor
            }deg) rotateX(${coordinateY / rotatingFactor}deg)`
          );
        }

        if (
          object[i].classList.contains("is-translating") ||
          object[i].classList.contains("is-rotating")
        ) {
          tranformProperty = tranformProperty.join(" ");
          object[i].style.transform = tranformProperty;
          object[i].style.transition = "transform 1s ease-out";
          object[i].style.transformStyle = "preserve-3d";
          object[i].style.backfaceVisibility = "hidden";
        }
      }
    }

    // Call function with throttling
    if (movingObjects) {
      win.addEventListener(
        "mousemove",
        throttle(function (e) {
          moveObjects(e, movingObjects);
        }, 150)
      );
    }
  },
  beforeUnmount() {
    // Sử dụng Vue 3 lifecycle hook
    window.removeEventListener("scroll", this.handleScroll);
  },
  methods: {
    handleScroll() {
      this.showButton = window.scrollY > 300; // Hiển thị khi cuộn > 300px
    },
    scrollToTop() {
      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });
    },
  },
};
</script>

<style scoped>
@import "../assets/dist/css/style.css";
html {
  line-height: 1.15;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
  /* background: #141516; */
}
article,
aside,
footer,
header,
nav,
section {
  display: block;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
figcaption,
figure,
main {
  display: block;
}
.site-footer {
  position: relative;
  font-size: 14px;
  line-height: 20px;
  letter-spacing: 0px;
}
.site-footer a {
  color: #768696;
  text-decoration: none;
}
.site-footer a:hover,
.site-footer a:active {
  color: #fff;
  text-decoration: underline;
}
.footer-bg,
.footer-dots {
  display: none;
}
.site-footer-inner {
  position: relative;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  padding-top: 32px;
  padding-bottom: 32px;
}
.footer-social-links,
.footer-copyright {
  flex: none;
  width: 100%;
  display: inline-flex;
  justify-content: center;
}
.footer-copyright {
  margin-bottom: 24px;
}
.footer-social-links {
  margin-bottom: 0;
}
.footer-social-links li {
  display: inline-flex;
}
.footer-social-links li + li {
  margin-left: 16px;
}
.footer-social-links li a {
  padding: 8px;
}
@media (min-width: 641px) {
  .site-footer::before {
    height: 202px;
  }
  .footer-bg,
  .footer-dots {
    display: block;
    position: absolute;
  }
  .footer-bg {
    bottom: 0;
    right: 0;
  }
  .footer-dots {
    bottom: 124px;
    right: 127px;
  }
  .site-footer-inner {
    justify-content: space-between;
  }
  .footer-social-links,
  .footer-copyright {
    flex: 50%;
  }
  .footer-copyright {
    margin-bottom: 0;
    justify-content: flex-start;
  }
  .footer-social-links {
    justify-content: flex-end;
  }
}
.container,
.container-sm {
  width: 100%;
  margin: 0 auto;
  padding-left: 16px;
  padding-right: 16px;
}
@media (min-width: 481px) {
  .container,
  .container-sm {
    padding-left: 24px;
    padding-right: 24px;
  }
}
.container {
  max-width: 1128px;
}
.container-sm {
  max-width: 848px;
}
.container .container-sm {
  max-width: 800px;
  padding-left: 0;
  padding-right: 0;
}

.top {
  position: fixed;
  bottom: -50px;
  right: 20px;
  background-color: transparent;
  backdrop-filter: blur(20px); /* Làm mờ nền */
  -webkit-backdrop-filter: blur(20px); /* Hỗ trợ Safari */
  border: 1px solid rgba(255, 255, 255, 0.3); /* Đường viền mờ */
  color: white;
  border: none;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: background-color 0.3s ease;
  font-size: 20px;
  transition: bottom 0.5s ease, opacity 0.5s ease; /* Animation cho vị trí và độ mờ */
  opacity: 0;
}

.top:hover {
  background-color: rgba(255, 255, 255, 0.3);
}

.top i {
  pointer-events: none; /* Đảm bảo click hoạt động đúng */
}
.top.show {
  bottom: 20px; /* Vị trí cố định khi hiển thị */
  opacity: 1;
  transform: translateY(0);
}
.top.hide {
  transform: translateY(50px); /* Fly down khi ẩn */
  opacity: 0; /* Ẩn đi */
}
</style>
