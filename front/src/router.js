import { createRouter, createWebHistory } from "vue-router";
import UrlForm from "@/components/UrlForm"

const routes = [
    { path: "/", component: UrlForm, name: "UrlForm" },
]

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;