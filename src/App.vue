<template>
  <div id="app">
    <nav>
      <router-link to="/" class="navbar__link">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          width="24"
          height="24"
        >
          <path d="M12 3l10 9-1.5 1.5L17 12v10h-4V14H9v8H5V12L2.5 13.5 12 3z" />
        </svg>
        <span>Home</span>
      </router-link>
      <router-link to="/rcm" class="navbar__link">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          width="24"
          height="24"
        >
          <path
            d="M12 2L2 7v10l10 5 10-5V7l-10-5zm0 4.66l4 2v5.68l-4 2-4-2V8.66l4-2zm0 0l4 2V7l-4-2-4 2v1.66l4-2z"
          />
        </svg>
        <span>Recomments mentor-mentee</span>
      </router-link>

      <router-link to="/cmt" class="navbar__link">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          width="24"
          height="24"
        >
          <path
            d="M12 2L2 7v10l10 5 10-5V7l-10-5zm0 4.66l4 2v5.68l-4 2-4-2V8.66l4-2zm0 0l4 2V7l-4-2-4 2v1.66l4-2z"
          />
        </svg>
        <span>Classifications Comments System</span>
      </router-link>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style lang="scss" scoped>
$borderRadius: 10px;
$spacer: 5px;
$primary: #c4151c;
$text: #fff;
$linkHeight: $spacer;
$timing: 250ms;
$transition: $timing ease all;
$linkWidth: 10rem;

@import url("https://fonts.googleapis.com/css2?family=Open+Sans:wght@600&display=swap");

body {
  background-size: cover;
  font-family: "Open Sans", sans-serif;
}

nav {
  background: #000 no-repeat center center;
  display: flex;
  gap: 1rem;
  padding: $spacer;
  justify-content: center;
}

.navbar__link {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: $text;
  text-decoration: none;
  padding: $spacer;
  transition: $transition;
  svg {
    fill: $text;
    transition: fill $timing ease;
  }
  span {
    margin-top: 0.4rem;
    font-size: 1rem;
    text-transform: uppercase;
    font-weight: 600;
  }

  &:hover {
    color: $primary;
    svg {
      fill: $primary;
    }
  }
}
</style>
