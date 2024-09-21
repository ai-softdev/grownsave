<script>
import 'animate.css'
import NavigationLinks from "../ui/NavigationLinks.vue";
import ChangeLang from "../ui/ChangeLang.vue";
import MainButton from "../ui/MainButton.vue";
import Burger from "../ui/Burger.vue";
import {mapActions, mapGetters} from "vuex";

export default {
  name: "Header",
  components: {Burger, MainButton, ChangeLang, NavigationLinks},
  data(){
    return {
      links: [
        {
          name: 'Преимущества платформы',
          link: '/#advantages'
        },
        {
          name: 'Интерактивная карта',
          link: '/#map'
        },
        {
          name: 'Тарифы',
          link: '/#tariffs'
        },
      ],
      languages: [
        {
          name: 'Russian',
          short: 'Ru',
          locale: 'ru'
        },
        {
          name: 'Uzbek',
          short: 'Uzb',
          locale: 'uz'
        },
        {
          name: 'English',
          short: 'En',
          locale: 'en'
        }
      ],
      activeLanguage: {
        name: 'English',
        short: 'En',
        locale: 'en'
      },
      showLang: false,
      activeBurger: false
    }
  },
  computed:{
    ...mapGetters(['getCurrentUser'])
  },
  methods:{
    ...mapActions(['loadCurrentUser']),
    changeShowLang(){
      this.showLang = !this.showLang
    },
    changeLanguage(lng) {
      this.changeShowLang()
      this.activeLanguage = lng
      localStorage.setItem('grow-lang', JSON.stringify(lng))
      this.$i18n.locale = lng.locale
    },
    findLanguageByLocale(locale) {
      return this.languages.find(lang => lang.locale === locale) || this.languages.find(lang => lang.locale === 'en');
    },
    toggleBurger() {
      this.activeBurger = !this.activeBurger;
    }
  },
  mounted() {
    this.loadCurrentUser()
    let storedLang = localStorage.getItem('grow-lang');
    if (storedLang) {
      try {
        storedLang = JSON.parse(storedLang);
        this.activeLanguage = this.findLanguageByLocale(storedLang.locale);
        this.$i18n.locale = storedLang.locale;
      } catch (error) {
        this.activeLanguage = this.findLanguageByLocale(this.$i18n.locale);
        this.$i18n.locale = this.activeLanguage.locale;
      }
    } else {
      this.activeLanguage = this.findLanguageByLocale(this.$i18n.locale);
      this.$i18n.locale = this.activeLanguage.locale;
    }
  }
}
</script>

<template>
  <header class="absolute top-0 left-0 right-0 z-10 header h-[70px] w-full">
    <div class="container !flex items-center justify-between">
      <RouterLink to="/#intro">
        <img src="/img/logo.svg" class="logo mx-auto w-[170px] h-[60px] object-contain font-bold"/>
      </RouterLink>
      <div
          class="flex items-center justify-between gap-[100px] max_xl:gap-[30px] max_lg:absolute max_lg:-top-[43px] max_lg:pt-[100px] max_lg:justify-start max_lg:gap-10 max_lg:p-10 max_lg:bg-white max_lg:flex-col max_lg:shadow max_lg:h-[100vh] transition-all ease-in-out duration-300"
          :class="{
          'right-0 max_sm:w-full':  activeBurger,
          '-right-[200%]': !activeBurger
        }"
      >
        <NavigationLinks
            :nav-links="links"
        />
        <div class="flex items-center gap-8">
          <ChangeLang
              :active-language="activeLanguage"
              :languages="languages"
              :show-lang="showLang"
              @changeShowLang="changeShowLang"
              @changeLanguage="changeLanguage"
          />
          <router-link v-if="getCurrentUser && !getCurrentUser.id" to="/login">
            <MainButton
                class="!text-forest bg-white !rounded-full !w-fit px-4"
            >
              {{ $t('Login/Registration') }}
            </MainButton>
          </router-link>
          <router-link to="/admin" class="font-bold flex items-center gap-3">
            <MainButton
                class="!text-forest bg-white !rounded-full !w-fit px-4"
            >
              {{ $t('Profile') }}
            </MainButton>
          </router-link>
        </div>
      </div>
      <Burger
        :is-active-burger="activeBurger"
        @toggleBurger="toggleBurger"
      />
    </div>
  </header>
</template>

<style scoped>
.header {
  min-height: 55px;
  padding-top: 40px;
}

.logo {
  animation: fadeIn;
  animation-duration: 2.5s;
}
</style>