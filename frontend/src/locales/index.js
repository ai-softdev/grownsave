import en from './en.json'
import ru from './ru.json'
import uz from './uz.json'
import {createI18n} from "vue-i18n"
const msg = {
    en:en,
    ru: ru,
    uz: uz,
}

const i18n = new createI18n({
    locale:'ru',
    fallbackLocale:'en',
    messages:msg
})

export default i18n;