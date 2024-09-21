import { createStore } from "vuex";
import auth from "./auth/auth.js";

const store = createStore({
    state: {},
    mutations: {},
    actions: {},
    getters: {
        getServerDomain() {
            return 'https://api-grownsave.ai-softdev.com/'
        },
    },
    modules: {
        auth
    }
})
export default store;