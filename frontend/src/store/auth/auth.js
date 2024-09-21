import axios from "../../axios/index.js";
import i18n from "../../locales/index.js";
import {toast} from "vue3-toastify";
import router from "../../router/index.js";

export default {
    state() {
        return {
            currentUser:{},
        }
    },
    getters: {
        getCurrentUser(state){
            return state.currentUser
        },
    },
    mutations: {
        updateCurrentUser(state, data){
            state.currentUser = data;
        },
    },
    actions: {
        sendRegister(context, params){
            axios.post(`auth/register`, params.form).then(res=> {
                localStorage.setItem('grow-token', res.data.access_token)
                context.commit('updateCurrentUser', res.data.user)
                router.push({name: 'admin-page'})
                toast.success(i18n.t('You have successfully registered!'))
            }).catch(error=> {
                toast.error(error.message)
            })
        },
        sendLogin(context, params){
            axios.post(`auth/login`, params.form).then(res=> {
                localStorage.setItem('grow-token', res.data.access_token)
                context.dispatch('loadCurrentUser')
                router.push({name: 'admin-page'})
                toast.success(i18n.t('You have successfully logged in!'))
            }).catch(error=> {
                toast.error(error.message)
            })
        },
        loadCurrentUser(context, params){
            axios.get(`auth/current-user`, {
                headers: {
                    Authorization: `${localStorage.getItem('grow-token')}`
                }
            }).then(res=> {
                context.commit('updateCurrentUser', res.data.user)
            }).catch(error=> {
                localStorage.removeItem('grow-token');
            })
        },
    }
}