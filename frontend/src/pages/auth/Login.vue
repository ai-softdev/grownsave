<script>
import { Swiper, SwiperSlide } from 'swiper/vue';
import {Pagination, Autoplay} from "swiper/modules";
import 'swiper/css';
import 'swiper/css/pagination';
import MainInput from "../../components/ui/MainInput.vue";
import MainButton from "../../components/ui/MainButton.vue";
import {mapActions} from "vuex";

export default {
  name: "Login",
  components: {
    MainButton,
    MainInput,
    Swiper,
    SwiperSlide,
  },
  data() {
    return {
      slides: ['img/swiper/1.webp', 'img/swiper/2.webp', 'img/swiper/3.webp', 'img/swiper/4.webp'],
      formValues: {
        email: '',
        password: ''
      },
      disableButton: false
    };
  },
  setup() {
    const onSwiper = (swiper) => {
    };
    const onSlideChange = () => {
    };
    return {
      onSwiper,
      modules: [Pagination, Autoplay],
      onSlideChange,
    };
  },
  methods: {
    ...mapActions(['sendLogin']),
  },
  mounted() {
  }
}
</script>

<template>
  <div class="relative">
    <swiper
        class="h-full max-h-[100vh]"
        :modules="modules"
        :pagination="{ clickable: true }"
        :autoplay="{ delay: 3000 }"
        loop
        @swiper="onSwiper"
        @slideChange="onSlideChange"
    >
      <swiper-slide
          v-for="(slide, index) in slides"
          :key="index"
          class="max-h-[100vh] h-full"
      >
        <img class="w-full h-full min-h-[100vh] max-h-[100vh] object-cover" :src="slide" alt="img"/>
      </swiper-slide>
    </swiper>

    <div class="container w-full flex items-center justify-center min-h-[100vh] absolute top-0 left-0 right-0 bottom-0 z-10">
      <div class="w-full flex items-center justify-center max_md:w-full max_md:mx-auto max_md:min-h-[100vh]">
        <div class="w-5/12 max_lg:w-8/12 max_sm:w-full bg-white p-12 max_sm:px-8 rounded-[32px] shadow-feedback flex flex-col items-center justify-center max_md:w-9/12">
          <h1 class="font-bold text-[32px] mb-[40px] text-center max_sm:text-2xl">
            {{ $t('Welcome') }}
          </h1>
          <form @submit.prevent="sendLogin({form: formValues})" class="w-full flex flex-col gap-[16px]">
            <MainInput
                id="email-input"
                name="email"
                label="Email"
                placeholder="name@example.com"
                type="email"
                :required="true"
                v-model="formValues.email"
            />
            <MainInput
                id="password-input"
                name="password"
                label="Password"
                type="password"
                placeholder="Password"
                required
                v-model="formValues.password"
            />
            <MainButton :disabled="disableButton">
              {{ $t('Entrance') }}
            </MainButton>
            <p class="mt-[8px] text-center">
              {{ $t("Don't you have an account? Register") }} <router-link to="/register" class="text-forest font-bold">{{ $t('here') }}</router-link>
            </p>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.swiper-pagination {
  width: 100%;
  position: absolute;
  bottom: 32px;
  height: 30px !important;
  z-index: 1000;
  display: flex;
  gap: 8px;
  align-items: center;
  justify-content: center;
}

.swiper-pagination-bullet {
  width: 14px;
  height: 14px;
  display: block !important;
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 100%;
}

.swiper-pagination-bullet-active {
  background-color: #598F3D;
}
</style>