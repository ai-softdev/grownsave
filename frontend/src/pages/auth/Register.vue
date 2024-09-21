<script>
import MainInput from "../../components/ui/MainInput.vue";
import Breadcrumbs from "../../components/ui/Breadcrumbs.vue";
import {MAIN_ROUTE} from "../../assets/paths.js";
import Loading from "../../components/ui/Loading.vue";
import MainButton from "../../components/ui/MainButton.vue";
import {mapActions} from "vuex";

export default {
  name: "Register",
  components: {MainButton, Loading, Breadcrumbs, MainInput},
  data(){
    return {
      formValues: {
        email: '',
        password: '',
        password_repeat: ''
      },
      errorPassword: false,
      disableButton: false,
      showPopup: false,
      breadcrumbs: [
        { label: 'Main', path: MAIN_ROUTE },
        { label: 'Регистрация '},
      ]
    }
  },
  methods:{
    ...mapActions(['sendRegister']),
    validatePasswords(){
      this.disableButton = true;
      if (this.formValues.password === this.formValues.password_repeat) {
        this.errorPassword = false;
        this.sendRegister({form: this.formValues});
      } else {
        this.errorPassword = true;
        this.showPopup = true;
        setTimeout(() => this.showPopup = false, 600);
        this.disableButton = false;
      }
    },
    handleSubmit() {
      // try {
      //   await store.dispatch('user/register', formValues.value);
      // } catch (error) {
      //   console.error('Registration failed:', error);
      // }
    }
  }
}
</script>

<template>
  <section class="flex items-center justify-start">
    <div class="relative container min-h-[100vh] z-10 flex items-center justify-between">
      <div class="flex items-center gap-[24px] absolute top-5 left-0 max_sm:flex-col max_sm:items-start max_xl:left-4 max_sm:left-10">
        <router-link
            to="/#main"
            class="bg-white bg-opacity-[0.08] py-3 px-4 rounded-[100px] text-white flex items-center gap-2 font-medium">
          <img src="/img/light-back.svg" alt="light-back">
          {{ $t('Back') }}
        </router-link>
        <Breadcrumbs
            :breadcrumbItems="breadcrumbs"
        />
      </div>
      <div class="w-5/12 mt-20 bg-white rounded-[32px] max_lg:mx-auto max_lg:w-8/12 max_sm:w-full p-12 max_sm:px-8 flex flex-col items-center max_md:w-9/12 shadow-feedback">
        <h1 class="font-bold text-[32px] mb-[40px] text-center max_sm:text-2xl">
          {{ $t('Registration') }}
        </h1>
        <form @submit.prevent="validatePasswords()" class="w-full flex flex-col gap-[16px]">
          <MainInput
              id="email-input"
              name="email"
              label="Email"
              type="email"
              required
              placeholder="name@example.com"
              v-model="formValues.email"
          />
          <MainInput
              id="password-input"
              name="password"
              label="Password"
              type="password"
              :placeholder="$t('Come up with a password')"
              :class="{'text-red-500': errorPassword}"
              v-model="formValues.password"
          />
          <MainInput
              id="password-input-repeat"
              name="password_repeat"
              label="Repeat the password"
              type="password"
              :placeholder="$t('Repeat the password')"
              :class="{'text-red-500': errorPassword}"
              v-model="formValues.password_repeat"
          />
          <MainButton
              type="submit"
              :disabled="disableButton"
          >
            {{ $t('Register') }}
            <Loading v-if="disableButton" />
          </MainButton>
          <p class="mt-[8px] text-center">
            {{ $t('Do you have an account? Log in') }}
            <router-link to="/login" class="text-forest font-bold"> {{ $t('here') }}</router-link>
          </p>
        </form>
      </div>
    </div>
    <img
        class="absolute object-cover w-full h-full top-0 left-0 right-0 bottom-0"
        src="/img/register-bg.webp"
        alt="registration"
    />
  </section>
</template>

<style scoped>

</style>