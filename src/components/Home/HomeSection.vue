<template>
  <li class="l-section section section--is-active">
    <div class="intro">
      <div class="intro--banner">
        <h1>Your next<br>interactive<br>experience</h1>
        <button class="cta" @click="hireUs">Hire Us
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 150 118" class="icon">
            <g transform="translate(0.000000,118.000000) scale(0.100000,-0.100000)">
              <path d="M870,1167c-34-17-55-57-46-90c3-15,81-100,194-211l187-185l-565-1c-431,0-571-3-590-13c-55-28-64-94-18-137c21-20,33-20,597-20h575l-192-193C800,103,794,94,849,39c20-20,39-29,61-29c28,0,63,30,298,262c147,144,272,271,279,282c30,51,23,60-219,304C947,1180,926,1196,870,1167z"/>
            </g>
          </svg>
          <span class="btn-background"></span>
        </button>
        <img src="assets/img/introduction-visual.png" alt="Welcome">
      </div>
      <div class="intro--options">
        <div v-for="(option, index) in introOptions" :key="index">
          <a href="#0">
            <h3>{{ option.title }}</h3>
            <p>{{ option.description }}</p>
          </a>
        </div>
      </div>
    </div>
  </li>
</template>

<script>
export default {
  name: "HomeSection",
  data() {
    return {
      introOptions: [
        {
          title: "Metiew & Smith",
          description: "Lorem ipsum dolor sit amet, consectetur adipisicing elit sed do.",
        },
        {
          title: "Fantasy interactive",
          description: "Lorem ipsum dolor sit amet, consectetur adipisicing elit sed do.",
        },
        {
          title: "Paul & Shark",
          description: "Lorem ipsum dolor sit amet, consectetur adipisicing elit sed do.",
        },
      ],
    };
  },
  methods: {
    hireUs() {
      console.log("Hire Us button clicked");

    },
  },
};
</script>