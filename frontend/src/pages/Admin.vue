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
  Profile page
</template>

<style scoped>

</style>