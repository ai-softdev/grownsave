<template>
  <div class="flex flex-wrap relative">
    <label
        class="relative w-full text-black dark:text-iron text-lg font-medium mb-2 transition-all duration-300 ease-in-out"
        :class="{ required: required }"
        :for="name"
    >
      {{ $t(label) }}
      <div v-if="name === 'password' || name === 'password_repeat'"  @click="$refs.password.type= $refs.password.type === 'password'?'text':'password'; changePassword()"
           class="absolute z-10 top-[45px] right-5 w-6 h-6 cursor-pointer"
      >
        <svg v-if="show_password" fill="#374957" width="25px" height="25px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg">
          <g id="SVGRepo_bgCarrier" stroke-width="0"/>
          <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
          <g id="SVGRepo_iconCarrier"> <path d="M16.108 10.044c-3.313 0-6 2.687-6 6s2.687 6 6 6 6-2.686 6-6-2.686-6-6-6zM16.108 20.044c-2.206 0-4.046-1.838-4.046-4.044s1.794-4 4-4c2.206 0 4 1.794 4 4s-1.748 4.044-3.954 4.044zM31.99 15.768c-0.012-0.050-0.006-0.104-0.021-0.153-0.006-0.021-0.020-0.033-0.027-0.051-0.011-0.028-0.008-0.062-0.023-0.089-2.909-6.66-9.177-10.492-15.857-10.492s-13.074 3.826-15.984 10.486c-0.012 0.028-0.010 0.057-0.021 0.089-0.007 0.020-0.021 0.030-0.028 0.049-0.015 0.050-0.009 0.103-0.019 0.154-0.018 0.090-0.035 0.178-0.035 0.269s0.017 0.177 0.035 0.268c0.010 0.050 0.003 0.105 0.019 0.152 0.006 0.023 0.021 0.032 0.028 0.052 0.010 0.027 0.008 0.061 0.021 0.089 2.91 6.658 9.242 10.428 15.922 10.428s13.011-3.762 15.92-10.422c0.015-0.029 0.012-0.058 0.023-0.090 0.007-0.017 0.020-0.030 0.026-0.050 0.015-0.049 0.011-0.102 0.021-0.154 0.018-0.090 0.034-0.177 0.034-0.27 0-0.088-0.017-0.175-0.035-0.266zM16 25.019c-5.665 0-11.242-2.986-13.982-8.99 2.714-5.983 8.365-9.047 14.044-9.047 5.678 0 11.203 3.067 13.918 9.053-2.713 5.982-8.301 8.984-13.981 8.984z"/> </g>
        </svg>
        <svg v-else width="25px" height="25px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <g id="SVGRepo_bgCarrier" stroke-width="0"/>
          <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
          <g id="SVGRepo_iconCarrier"> <path d="M2.99902 3L20.999 21M9.8433 9.91364C9.32066 10.4536 8.99902 11.1892 8.99902 12C8.99902 13.6569 10.3422 15 11.999 15C12.8215 15 13.5667 14.669 14.1086 14.133M6.49902 6.64715C4.59972 7.90034 3.15305 9.78394 2.45703 12C3.73128 16.0571 7.52159 19 11.9992 19C13.9881 19 15.8414 18.4194 17.3988 17.4184M10.999 5.04939C11.328 5.01673 11.6617 5 11.9992 5C16.4769 5 20.2672 7.94291 21.5414 12C21.2607 12.894 20.8577 13.7338 20.3522 14.5" stroke="#374957" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/> </g>
        </svg>
      </div>
      <svg
          v-if="name !== 'password' && name !== 'password_repeat' && modelValue.length"
          @click="clearModelValue"
          class="absolute z-10 top-12 right-4 cursor-pointer fill-doveGrey transition-all ease-in-out duration-300" width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path fill-rule="evenodd" clip-rule="evenodd" d="M13.7071 1.70711C14.0976 1.31658 14.0976 0.683418 13.7071 0.292893C13.3166 -0.0976311 12.6834 -0.0976311 12.2929 0.292893L7 5.58579L1.70711 0.292893C1.31658 -0.0976311 0.683419 -0.0976311 0.292894 0.292893C-0.0976298 0.683417 -0.0976298 1.31658 0.292894 1.70711L5.58579 7L0.292893 12.2929C-0.097631 12.6834 -0.097631 13.3166 0.292893 13.7071C0.683418 14.0976 1.31658 14.0976 1.70711 13.7071L7 8.41421L12.2929 13.7071C12.6834 14.0976 13.3166 14.0976 13.7071 13.7071C14.0976 13.3166 14.0976 12.6834 13.7071 12.2929L8.41421 7L13.7071 1.70711Z" />
      </svg>
    </label>
    <input
        :ref="type"
        :id="name"
        :class="{ '!border-red !text-red': errors, 'border-mercury': !errors, '!pr-14': name === 'password' || name === 'password_repeat' }"
        class="border bg-romance border-mercury bg-porcelain rounded-[1000px] w-full pr-12 h-[46px] px-5 outline-none focus:!border text-[16px] text-black max-h-[60px] transition-all duration-300 ease-in-out"
        :type="type"
        :placeholder="placeholder ? $t(placeholder) : ''"
        :value="modelValue"
        :v-model="modelValue"
        :name="name"
        @input="$emit('update:modelValue', $event.target.value)"
        :required="necessary"
        :min="min"
    />
    <span v-if="helpTextIs" class="text-doveGrey dark:text-primary mt-1 ml-1 capitalize">
      {{ $t(helpText) }}
    </span>
    <Transition name="left-fade">
      <div
          v-if="errors"
          class="absolute -top-8 left-0 flex flex-col gap-0.5"
      >
        <div
            v-for="(item, index) in errors"
            :key="index"
            :class="getClass()"
            class="shadow-simple w-full gap-x-2 mt-4 px-4 py-2 text-red text-lg flex items-center rounded-xl bg-white"
        >
        <span
            class="w-7 h-7 rounded-full border-red border-2 flex items-center justify-center font-bold"
        >!</span
        >
          <span class="w-full"> {{ $t(item) }}</span>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script>
export default {
  props: {
    name: {
      type: String,
      required: true,
    },
    error: {
      type: Boolean,
    },
    errors: {
      type: Array,
    },
    label: {
      type: String,
      required: true,
    },
    modelValue: {
      type: String,
      required: true,
    },
    placeholder: {
      type: String,
      required: false,
    },
    type: {
      type: String,
      required: true,
    },
    required: {
      type: Boolean,
      required: true,
    },
    helpTextIs: {
      type: Boolean,
      required: false,
    },
    helpText: {
      type: String,
      required: false
    },
    necessary: {
      type: Boolean,
      required: false
    },
    min: {
      type: Number,
      required: false
    }
  },
  data(){
    return {
      show_password: false,
    }
  },
  computed: {},
  methods: {
    clearModelValue() {
      this.$emit('update:modelValue', '')
    },
    getClass() {
      if (window.outerWidth > 1280) return "error";
      return "";
    },
    changePassword(){
      this.show_password = !this.show_password
    }
  },
  mounted() {
    if(this.name === 'password' || this.name === 'password_repeat'){
      this.show_password = true
    }
  }
};
</script>

<style scoped>
.required::after {
  content: "*";
  color: #598F3D;
}

.error::before {
  content: "";
  width: 13.74px;
  height: 22.69px;
  background: white;
  position: absolute;
  z-index: -1;
  transform-origin: center;
  transform: translateX(-150%) rotate(45deg);
}

input::-webkit-datetime-edit-fields-wrapper {
  color: #6562F9;
  transition: 0.3s ease-in-out;
}

.dark input::-webkit-datetime-edit-fields-wrapper {
  color: white;
}

input::-webkit-calendar-picker-indicator {
  filter: invert(31%) sepia(87%) saturate(1168%) hue-rotate(220deg) brightness(105%) contrast(95%);
  transition: 0.3s ease-in-out;
}

.dark input::-webkit-calendar-picker-indicator {
  filter: invert(1);
}

</style>
