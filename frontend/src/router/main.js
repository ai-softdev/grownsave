import {ADMIN_ROUTE, LOGIN_ROUTE, MAIN_ROUTE, MAP_ROUTE, REGISTER_ROUTE} from "../assets/paths.js";
import Main from "../pages/Main.vue";
import Map from "../pages/Map.vue";
import Login from "../pages/auth/Login.vue";
import Register from "../pages/auth/Register.vue";
import Admin from "../pages/Admin.vue";

const main =  [
    {
        path: ADMIN_ROUTE,
        component: Admin,
        name: 'admin-page',
        children: [
            {
                path: MAP_ROUTE,
                component: Map,
                name: "map-page"
            }
        ]
    },
    {
        path: MAIN_ROUTE,
        component: Main,
        name: "main-page"
    },
    {
        path: LOGIN_ROUTE,
        component: Login,
        name: "login-page",
    },
    {
        path: REGISTER_ROUTE,
        component: Register,
        name: "register-page",
    }
]

export default main