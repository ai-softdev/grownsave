/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    screens: {
      sm: "640px",
      md: "768px",
      lg: "1024px",
      xl: "1280px",
      "2xl": "1536px",
      max_3xl: { max: "1660px" },
      max_2xl: { max: "1552px" },
      max_2big: {max: "1400px"},
      max_big: {max: "1300px"},
      max_xl: { max: "1279px" },
      max_lg: { max: "1023px" },
      max_md: { max: "767px" },
      max_md2: { max: "700px" },
      max_sm: { max: "639px" },
      max_lit: { max: "400px" },
    },
    extend: {
      colors: {
        romance: "#F2F2F2",
        doveGrey: "#6B6B6B",
        positive: '#30B502',
        forest: "#598F3D",
        smokey: "#737373",
        stormDust: "#626262",
        violet: "#9902D9",
        lightViolet: "rgba(153, 2, 217, 0.8)",
        dune: "#323232"
      },
      boxShadow: {
        filter: "0 3px 10px 0 rgba(0, 0, 0, 0.04)",
        chart: "0 2px 19px 2px rgba(0, 0, 0, 0.04)",
      }
    },
  },
  plugins: [],
}

