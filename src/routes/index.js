// src/routes/index.js
import { createRouter, createWebHistory } from 'vue-router';
import DisplayRCM from "../components/DisplayRCM.vue";
import MasterPage from "@/components/MasterPage.vue";
// import App from '@/App.vue';
// import thêm các components khác nếu có

const routes = [
  {
    path: "/",
    name: "Home",
    component: MasterPage,
  },
  {
    path: "/rcm",
    component: DisplayRCM,
  },
  // Thêm các route khác nếu có
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
