<script>
export default {
  name: "Burger",
  props: {
    isActiveBurger: Boolean
  },
  methods:{
    toggleBurger(){
      this.$emit("toggleBurger");
    }
  }
}
</script>

<template>
  <button @click="toggleBurger"
          :class="['burger', 'hidden', 'max_lg:block', { active: isActiveBurger }]">
    <div></div>
  </button>
</template>

<style scoped>
.burger {
  top: 10px;
  right: 15px;
  position: absolute;
  width: 40px;
}

.burger:before,
.burger:after,
.burger div {
  background: white;
  content: "";
  display: block;
  height: 3px;
  border-radius: 3px;
  margin: 7px 0;
  transition: 0.5s;
}
.burger.active:before {
  background: #598F3D;
  transform: translateY(8px) rotate(135deg);
}
.burger.active:after {
  background: #598F3D;
  transform: translateY(-12px) rotate(-135deg);
}
.burger.active div {
  transform: scale(0);
}
</style>