<script>
export default {
  name: "NavigationLinks",
  props: {
    navLinks: Array
  }
}
</script>

<template>
  <nav class="max_lg:w-full">
    <ul class="flex items-center gap-5 max_lg:flex-col max_lg:items-start">
      <li v-for="(link, index) in navLinks" :key="index" class="cursor-pointer">
        <router-link
            :to="link.link"
            class="text-white"
        >
          {{ $t(link.name) }}
        </router-link>
      </li>
    </ul>
  </nav>
</template>

<style scoped>

</style>