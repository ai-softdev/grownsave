<script>
import Header from "../components/main/Header.vue";
import Footer from "../components/main/Footer.vue";
import AdminHeader from "../components/admin/AdminHeader.vue";

export default {
  name: "Index",
  components: {AdminHeader, Footer, Header}
}
</script>

<template>
  <AdminHeader/>
  Profile
<!--  <Transition name="blur-fade">-->
<!--    <router-view/>-->
<!--  </Transition>-->
</template>

<style scoped>

</style>