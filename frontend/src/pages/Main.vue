<script>
import Header from "../components/main/Header.vue";
import Footer from "../components/main/Footer.vue";
import Intro from "../components/main/sections/Intro.vue";
import InteractiveMap from "../components/main/sections/InteractiveMap.vue";
import Tariffs from "../components/main/sections/Tariffs.vue";

export default {
  name: "Main",
  components: {Tariffs, InteractiveMap, Intro, Footer, Header}
}
</script>

<template>
  <Header/>
  <Intro/>
  <InteractiveMap/>
  <Tariffs/>
  <Footer/>
</template>

<style scoped>

</style>