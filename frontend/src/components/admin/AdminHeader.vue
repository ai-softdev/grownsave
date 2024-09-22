<script>
import Header from "../main/Header.vue";

export default {
  name: "AdminHeader",
  components: {Header}
}
</script>

<template>
  <header class="header flex h-[70px] items-center justify-center w-full">
    <router-link :to="{name: 'main-page'}">
      <img src="/img/logo-dark.svg" class="logo mx-auto w-[170px] h-[60px] object-contain font-bold"/>
    </router-link>
  </header>
</template>

<style scoped>
.header {
  background: url("/img/bg.png");
}
</style>