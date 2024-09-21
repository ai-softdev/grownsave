import { createRouter, createWebHistory } from "vue-router";
import main from "./main.js";

const routes = [...main];

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
});

export default router;