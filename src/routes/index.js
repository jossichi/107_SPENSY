// src/routes/index.js
import { createRouter, createWebHistory } from 'vue-router';
import DisplayRCM from "../components/DisplayRCM.vue";
import MasterPage from "@/components/MasterPage.vue";
// import App from '@/App.vue';
import CommentsSystem from "../components/CommentsSystem.vue"
import PoststingStatus from '@/components/Status/PoststingStatus.vue';
import TablesAdmin from '@/components/Status/TablesAdmin.vue';
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
  {
    path: "/cmt",
    component: CommentsSystem,
  },
  {
    path: "/posting",
    component: PoststingStatus,
  },
  {
    path: "/admin",
    component: TablesAdmin,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
