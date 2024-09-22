<script>
export default {
  name: "SvgMap",
  props: {
    activeDistrict: Object,
    getFillColor: {
      type: Function,
      required: true
    }
  },
  methods: {
    setActiveDistrict(id){
      this.$emit("setActiveDistrict", id);
    }
  }
}
</script>

<template>
  <div class="block w-full h-full">
    <svg
        class="max_md:mt-7 w-full h-full min-h-[80vh] max-h-[650px]"
        version="1.1"
        id="map2"
        viewBox="0 0 1637.3333 1738.6667"
        sodipodi:docname="tashkent-map.svg"
        inkscape:version="1.3.2 (091e20e, 2023-11-25, custom)"
        xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
        xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
        xmlns:xlink="http://www.w3.org/1999/xlink"
        xmlns="http://www.w3.org/2000/svg"
        xmlns:svg="http://www.w3.org/2000/svg">
      <defs
          id="defs1">
        <filter id="dropShadow" x="0" y="0" width="200%" height="200%">
          <feOffset result="offOut" in="SourceAlpha" dx="2" dy="2"/>
          <feGaussianBlur result="blurOut" in="offOut" stdDeviation="2"/>
          <feBlend in="SourceGraphic" in2="blurOut" mode="normal"/>
        </filter>
        <linearGradient
            id="swatch15"
            inkscape:swatch="solid">
          <stop
              style="stop-color:#ffffff;stop-opacity:1;"
              offset="0"
              id="stop15"/>
        </linearGradient>
        <linearGradient
            id="swatch14"
            inkscape:swatch="solid">
          <stop
              style="stop-color:#ffffff;stop-opacity:1;"
              offset="0"
              id="stop14"/>
        </linearGradient>
        <linearGradient
            id="swatch13"
            inkscape:swatch="solid">
          <stop
              style="stop-color:#ffffff;stop-opacity:1;"
              offset="0"
              id="stop13"/>
        </linearGradient>
        <linearGradient
            id="swatch12"
            inkscape:swatch="solid">
          <stop
              style="stop-color:#ffffff;stop-opacity:1;"
              offset="0"
              id="stop12"/>
        </linearGradient>
        <linearGradient
            id="swatch11"
            inkscape:swatch="solid">
          <stop
              style="stop-color:#ffffff;stop-opacity:1;"
              offset="0"
              id="stop11"/>
        </linearGradient>
        <linearGradient
            id="swatch10"
            inkscape:swatch="solid">
          <stop
              style="stop-color:#ffffff;stop-opacity:1;"
              offset="0"
              id="stop10"/>
        </linearGradient>
        <linearGradient
            id="swatch9"
            inkscape:swatch="solid">
          <stop
              style="stop-color:#ffffff;stop-opacity:1;"
              offset="0"
              id="stop9"/>
        </linearGradient>
        <linearGradient
            id="swatch8"
            inkscape:swatch="solid">
          <stop
              style="stop-color:#ffffff;stop-opacity:1;"
              offset="0"
              id="stop8"/>
        </linearGradient>
        <linearGradient
            id="swatch7"
            inkscape:swatch="solid">
          <stop
              style="stop-color:#ffffff;stop-opacity:1;"
              offset="0"
              id="stop7"/>
        </linearGradient>
        <linearGradient
            id="swatch6"
            inkscape:swatch="solid">
          <stop
              style="stop-color:#ffffff;stop-opacity:1;"
              offset="0"
              id="stop6"/>
        </linearGradient>
        <linearGradient
            id="swatch5"
            inkscape:swatch="solid">
          <stop
              style="stop-color:#ffffff;stop-opacity:1;"
              offset="0"
              id="stop5"/>
        </linearGradient>
        <linearGradient
            id="swatch4"
            inkscape:swatch="solid">
          <stop
              style="stop-color:#ffffff;stop-opacity:1;"
              offset="0"
              id="stop4"/>
        </linearGradient>
        <linearGradient
            id="swatch3"
            inkscape:swatch="solid">
          <stop
              style="stop-color:#ffffff;stop-opacity:1;"
              offset="0"
              id="stop3"/>
        </linearGradient>
        <linearGradient
            id="swatch2"
            inkscape:swatch="solid">
          <stop
              style="stop-color:#ffffff;stop-opacity:1;"
              offset="0"
              id="stop2"/>
        </linearGradient>
        <linearGradient
            inkscape:collect="always"
            xlink:href="#swatch2"
            id="linearGradient2"
            x1="620.92144"
            y1="465.47138"
            x2="1626.0608"
            y2="465.47138"
            gradientUnits="userSpaceOnUse"/>
        <linearGradient
            inkscape:collect="always"
            xlink:href="#swatch3"
            id="linearGradient3"
            x1="442.63661"
            y1="692.56827"
            x2="715.36614"
            y2="692.56827"
            gradientUnits="userSpaceOnUse"/>
        <linearGradient
            inkscape:collect="always"
            xlink:href="#swatch4"
            id="linearGradient4"
            x1="597.13985"
            y1="845.69728"
            x2="918.41263"
            y2="845.69728"
            gradientUnits="userSpaceOnUse"/>
        <linearGradient
            inkscape:collect="always"
            xlink:href="#swatch5"
            id="linearGradient5"
            x1="471.86695"
            y1="912.34144"
            x2="666.03994"
            y2="912.34144"
            gradientUnits="userSpaceOnUse"/>
        <linearGradient
            inkscape:collect="always"
            xlink:href="#swatch6"
            id="linearGradient6"
            x1="531.3675"
            y1="1079.6566"
            x2="1176.2619"
            y2="1079.6566"
            gradientUnits="userSpaceOnUse"/>
        <linearGradient
            inkscape:collect="always"
            xlink:href="#swatch7"
            id="linearGradient7"
            x1="256.24832"
            y1="835.11268"
            x2="531.58771"
            y2="835.11268"
            gradientUnits="userSpaceOnUse"/>
        <linearGradient
            inkscape:collect="always"
            xlink:href="#swatch8"
            id="linearGradient8"
            x1="373.16969"
            y1="1003.4139"
            x2="575.69421"
            y2="1003.4139"
            gradientUnits="userSpaceOnUse"/>
        <linearGradient
            inkscape:collect="always"
            xlink:href="#swatch9"
            id="linearGradient9"
            x1="189.43611"
            y1="974.42004"
            x2="427.97658"
            y2="974.42004"
            gradientUnits="userSpaceOnUse"/>
        <linearGradient
            inkscape:collect="always"
            xlink:href="#swatch10"
            id="linearGradient10"
            x1="64.424197"
            y1="1043.8535"
            x2="266.42674"
            y2="1043.8535"
            gradientUnits="userSpaceOnUse"/>
        <linearGradient
            inkscape:collect="always"
            xlink:href="#swatch11"
            id="linearGradient11"
            x1="100.96212"
            y1="1115.7068"
            x2="390.39471"
            y2="1115.7068"
            gradientUnits="userSpaceOnUse"/>
        <linearGradient
            inkscape:collect="always"
            xlink:href="#swatch12"
            id="linearGradient12"
            x1="188.91414"
            y1="1198.8714"
            x2="427.19363"
            y2="1198.8714"
            gradientUnits="userSpaceOnUse"
            gradientTransform="translate(-1.5659112,-0.44041253)"/>
        <linearGradient
            inkscape:collect="always"
            xlink:href="#swatch13"
            id="linearGradient13"
            x1="268.51462"
            y1="1281.4561"
            x2="499.22554"
            y2="1281.4561"
            gradientUnits="userSpaceOnUse"/>
        <linearGradient
            inkscape:collect="always"
            xlink:href="#swatch14"
            id="linearGradient14"
            x1="387.0019"
            y1="1226.0179"
            x2="777.95774"
            y2="1226.0179"
            gradientUnits="userSpaceOnUse"/>
        <linearGradient
            inkscape:collect="always"
            xlink:href="#swatch15"
            id="linearGradient15"
            x1="331.67304"
            y1="1504.3611"
            x2="484.61037"
            y2="1504.3611"
            gradientUnits="userSpaceOnUse"/>
        <linearGradient
            inkscape:collect="always"
            xlink:href="#swatch21"
            id="linearGradient21"
            x1="895.25"
            y1="1064.75"
            x2="981.5"
            y2="1064.75"
            gradientUnits="userSpaceOnUse"/>
        <linearGradient
            inkscape:collect="always"
            xlink:href="#swatch22"
            id="linearGradient22"
            x1="567.27642"
            y1="1205.9706"
            x2="633.03735"
            y2="1205.9706"
            gradientUnits="userSpaceOnUse"/>
      </defs>
      <sodipodi:namedview
          id="namedview1"
          pagecolor="#ffffff"
          bordercolor="#000000"
          borderopacity="0.25"
          inkscape:showpageshadow="2"
          inkscape:pageopacity="0.0"
          inkscape:pagecheckerboard="0"
          inkscape:deskcolor="#d1d1d1"
          showgrid="false"
          inkscape:zoom="0.5"
          inkscape:cx="684"
          inkscape:cy="824"
          inkscape:window-width="1920"
          inkscape:window-height="991"
          inkscape:window-x="-9"
          inkscape:window-y="-9"
          inkscape:window-maximized="1"
          inkscape:current-layer="g1"/>
      <g
          inkscape:groupmode="layer"
          inkscape:label="Image"
          id="g1">
        <a @click="setActiveDistrict('KYZ-D')" data-id="KYZ-D"
           id="okrug-5"
           class="okrug-5 map-tab-link district hover:opacity-90 transition-all duration-300 ease-in-out"
           data-color="#ed9988">
          <path
              class="district-path transition-all duration-300 ease-in-out"
              :class="{
                          'active': activeDistrict && activeDistrict.district_id === 'KYZ-D',
                          'opacity-10': activeDistrict && activeDistrict.district_id && activeDistrict.district_id !== 'KYZ-D',
                      }"
              :fill="getFillColor('KYZ-D')"
              style="fill-opacity:1;stroke-width:3.26929;stroke-linecap:butt;stroke-linejoin:bevel;stroke-dasharray:none;stroke:url(#linearGradient3)"
              d="m 465.59158,771.35001 -7.02622,21.63997 6.79924,-17.31117 3.82746,12.70617 -7.50639,4.11373 5.28809,5.41512 -2.18614,2.35232 -1.567,3.481 -6.57697,4.51797 -2.87657,3.08877 -3.42192,4.62139 11.28201,11.58165 -10.33575,-8.9327 11.92783,10.18282 0.0764,8.93098 7.33979,3.51718 1.94516,5.55409 1.65074,-1.68947 1.49006,5.23112 -3.33246,4.36253 -1.82689,9.83588 -4.43675,6.8998 5.48069,3.6701 19.57389,-2.49567 36.53793,-2.49567 35.75497,-51.67507 10.17842,-2.49567 13.31025,5.72536 23.48866,3.96372 2.34887,-21.72702 2.60985,-7.63382 9.39547,-9.10186 0.26098,-38.46269 1.30493,-6.01897 -6.52463,-7.34021 39.14778,-63.56621 -12.2663,-9.10186 -2.87084,-7.48701 0.78296,-3.22969 16.18108,-9.54227 6.52463,-16.73568 16.18108,-16.88248 14.87616,-24.80991 7.0466,-14.97402 7.0466,-9.68908 2.87083,-22.16743 -10.4394,-22.02062 -1.04394,-5.13815 -10.17843,12.47835 -19.05192,9.24867 -25.83753,4.99134 -20.61783,16.73568 -8.09054,12.33155 -31.57921,27.45238 -10.17843,25.83753 -21.66177,10.86351 -13.31024,-0.58722 -21.66177,19.67176 -9.65646,14.68042 4.17577,13.21238 11.48335,11.30392 3.3928,1.17443 -7.0466,13.50599 -1.30492,3.6701 c 3.30581,3.32756 -47.34879,-22.01356 -1.17813,0.36504 l -8.2573,5.61723 -2.73708,3.61627 -1.86157,0.74015 -5.8008,1.99286 -6.78561,7.48701 -4.09094,3.65176 -4.19249,3.61016 -3.96738,5.55531 -2.87981,4.66226 -1.48232,5.58468 -0.42043,3.94535 2.52748,7.44175 -2.48214,5.47507 -3.81634,0.0339 -5.40457,1.96153 z"
              id="KYZ-D"
              inkscape:label="кибрайский"/>
        </a>
        <a @click="setActiveDistrict('tashkent')" data-id="tashkent"
           id="okrug-15"
           class="okrug-15 map-tab-link district hover:opacity-90 transition-all duration-300 ease-in-out"
           data-color="#ed9988">
          <path
              class="district-path transition-all duration-300 ease-in-out"
              :class="{
                          'active': activeDistrict && activeDistrict.district_id === 'tashkent',
                          'opacity-10': activeDistrict && activeDistrict.district_id && activeDistrict.district_id !== 'tashkent',
                        }"
              :fill="getFillColor('tashkent')"
              style="fill-opacity:1;stroke-width:3.26929;stroke-linecap:butt;stroke-linejoin:bevel;stroke-dasharray:none;stroke:url(#linearGradient3)"
              d="m 292.38865,792.31315 17.32412,10.6066 22.27386,10.6066 2.12133,3.88909 5.65685,-9.19239 v -22.98097 l 25.45584,-25.80939 12.37437,-7.07107 16.61701,-3.18198 17.32412,11.31371 16.61701,-2.12133 5.65685,-1.06066 1.06066,10.60661 21.92031,12.72792 12.72792,8.48528 -2.47487,-17.32412 8.83884,-4.59619 6.0104,-1.76777 1.76777,-3.18198 10.25305,0.35356 4.94975,-7.77818 -4.94975,-9.19239 -28.63783,-15.9099 -1.41421,-5.3033 12.02082,-2.82843 9.54594,4.5962 18.38477,-0.35356 5.3033,-5.3033 -2.12132,-8.83883 5.3033,-7.42462 12.02082,5.65685 17.32412,-3.88909 3.88908,-6.0104 -1.41421,-4.94975 -29.69849,-10.6066 -5.65685,4.59619 -4.59619,-1.41421 -5.3033,0.7071 -0.70711,1.76777 h -13.08148 l -0.35355,-3.18198 -1.41421,-1.76777 -8.48529,2.47488 -14.84924,2.47487 -13.08147,-4.59619 -1.06066,6.0104 -3.88909,4.24264 -0.35355,3.18199 -2.47488,-1.76777 -4.94975,5.3033 -3.18198,2.82843 -1.76776,-0.35356 -7.07107,7.77818 -7.77818,6.71751 -5.3033,-3.88909 -7.07106,-6.0104 -5.65686,-4.5962 -5.65685,2.47488 -7.07107,-9.8995 -3.18198,1.41422 v 1.76776 h -5.3033 l -0.35355,3.18198 -5.30331,-3.18198 -3.88908,3.88909 -4.24264,-0.70711 -2.47488,3.53554 -5.65685,3.88908 -13.78858,9.8995 v 3.53553 l -2.12132,-3.88908 -6.71752,2.12132 3.18198,3.53553 -3.18198,1.76777 -4.94975,-1.06066 -1.76776,1.76776 1.41421,3.88909 4.94975,0.70711 4.24264,11.31371 2.82843,5.65685 4.59619,0.35355 0.35355,1.76777 -4.94974,-0.35355 0.35355,4.94974 -3.88909,-0.35355 -3.18198,4.94975 -0.70711,2.47487 -3.88908,-5.3033 -9.19239,2.12132 -4.5962,2.47488 -5.65685,-1.76777 -5.65685,2.47487 -3.18198,10.6066 v 8.13173 z"
              id="tashkent"
              inkscape:label="ташкентский"/>
        </a>
        <a @click="setActiveDistrict('PARK-D')" data-id="PARK-D"
           id="okrug-8"
           class="okrug-8 map-tab-link district hover:opacity-90 transition-all duration-300 ease-in-out"
           data-color="#ffd17f">
          <path
              class="district-path transition-all duration-300 ease-in-out"
              :class="{
                          'active': activeDistrict && activeDistrict && activeDistrict.district_id === 'PARK-D',
                          'opacity-10': activeDistrict && activeDistrict.district_id && activeDistrict.district_id !== 'PARK-D',
                      }"
              :fill="getFillColor('PARK-D')"
              style="fill-opacity:1;stroke-width:3.26929134;stroke-linecap:butt;stroke-linejoin:bevel;stroke-dasharray:none;stroke:url(#linearGradient4);paint-order:normal;stroke-miterlimit:154.3"
              d="m 609.66714,825.64626 -12.26631,42.57321 -0.26098,23.19506 v 17.17609 l 9.13448,0.88082 9.65645,-19.81856 17.22503,3.96371 15.65911,2.49567 2.60985,2.93608 -0.78296,16.73568 7.82956,11.15712 4.17576,3.5233 0.26099,7.63381 -11.74433,13.06558 -9.13449,3.22969 -8.35152,9.54227 -5.48069,4.25732 3.13182,7.78062 0.52197,5.13815 14.0932,6.45938 17.74699,-17.7633 2.60986,-1.17444 5.74167,1.61485 7.0466,1.46804 5.48069,7.34021 9.65645,3.81691 4.17577,10.42309 15.13714,19.09678 11.48335,1.7617 3.3928,-0.4405 5.21971,-9.689 16.96404,-8.22107 16.44206,-4.40413 8.09055,-15.41443 11.22236,-6.8998 12.00532,-13.79959 6.78561,-7.19341 9.65646,-0.1468 4.43674,-3.81691 -3.13182,-9.68908 12.52729,-18.64413 9.91744,-6.75299 12.2663,0.14681 1.04394,-11.89114 11.74434,-17.02929 1.82689,-17.17608 -6.52463,-11.45073 1.04395,-55.34517 12.78827,-14.38681 1.56591,-14.68042 0.78296,-6.45939 6.52463,-1.32123 20.87881,4.55093 4.17577,-8.36784 9.91743,-3.5233 -4.69773,-60.48332 6.52463,-10.5699 -6.26364,-3.81691 -12.52729,7.0466 -12.26631,2.64247 -25.83753,0.44042 -21.66177,9.10186 -6.78562,6.31258 -7.30759,6.31257 -3.13182,11.45073 -15.39812,12.91877 -7.04661,4.25732 -1.04394,26.13114 -3.65379,8.22104 -8.61251,3.96371 -24.27162,18.93774 -14.61518,0.44041 -14.87615,-5.87217 -10.96138,-10.86351 -10.96138,-1.61484 -27.14246,8.80825 -9.91744,-2.34887 -6.78561,3.96371 -4.43675,8.36784 -7.30759,7.92743 -9.65645,-1.90846 -2.87084,-6.60618 18.26897,-29.65445 12.52729,-8.80825 18.52995,0.88083 3.91477,-9.98269 -6.00265,-13.65279 -41.75764,-1.76165 -3.65379,3.3765 0.52197,7.48701 -2.60985,4.11052 -1.30493,33.03094 -7.82955,7.1934 -12.52729,6.31258 -7.30759,8.07423 z"
              id="PARK-D"
              inkscape:label="паркентский"/>
        </a>
        <a
            @click="setActiveDistrict('YUK-D')" data-id="YUK-D"
            class="okrug-14 map-tab-link district hover:opacity-90 transition-all duration-300 ease-in-out"
            id="okrug-14"
            :class="{'active': activeDistrict && activeDistrict.district_id === 'YUK-D'}"
            data-color="#9ed765"
        >
          <path
              class="district-path transition-all duration-300 ease-in-out"
              :class="{
                          'active': activeDistrict && activeDistrict.district_id === 'YUK-D',
                          'opacity-10': activeDistrict && activeDistrict.district_id && activeDistrict.district_id !== 'YUK-D',
                      }"
              :fill="getFillColor('YUK-D')"
              style="fill-opacity:1;stroke-width:4.40314961;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:154.3;stroke-dasharray:none;paint-order:normal;stroke:url(#linearGradient5)"
              d="m 471.86695,877.98929 10.43941,10.12948 5.74167,0.44042 0.52197,20.25897 -15.65911,19.52496 -0.78295,15.26763 9.65645,2.34887 11.48335,-5.72536 0.78295,-8.66145 4.69774,-2.78928 16.44207,9.83588 2.87083,13.65279 22.70572,-1.76165 0.26098,10.42309 4.43675,13.21238 57.93871,-2.20206 3.6538,26.57155 12.00532,4.55089 9.39546,0.2937 3.39281,3.2296 15.9201,0.1468 18.26896,-19.67171 -3.39281,-14.0932 -16.18108,14.53361 -15.65911,-6.01897 -2.87084,-12.33155 8.61251,-10.27629 8.8735,-8.80825 6.52463,-3.08289 9.91744,-11.45073 -3.39281,-5.72536 -8.8735,-10.5699 -0.52197,-20.55259 -30.79625,-5.43175 -9.91744,16.00165 -11.48335,-0.1468 -0.78295,-39.04991 10.96138,-42.1328 -13.83222,-4.40412 -19.3129,-5.57856 -9.65646,0.58721 -36.01595,54.46435 z"
              id="YUK-D"
              inkscape:label="юкоричирчикский"/>
        </a>
        <a @click="setActiveDistrict('AK-D')" data-id="AK-D"
           class="okrug-6 map-tab-link district hover:opacity-90 transition-all duration-300 ease-in-out"
           id="okrug-6"
           data-color="#00d990">
          <path
              class="district-path transition-all duration-300 ease-in-out"
              :class="{
                          'active': activeDistrict && activeDistrict.district_id === 'AK-D',
                          'opacity-10': activeDistrict && activeDistrict.district_id && activeDistrict.district_id !== 'AK-D',
                      }"
              :fill="getFillColor('AK-D')"
              style="fill-opacity:1;stroke-width:4.02519685;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:154.3;stroke-dasharray:none;paint-order:normal;stroke:url(#linearGradient6)"
              d="m 545.19972,974.83845 56.89477,-2.05526 2.87084,27.45241 15.13714,5.4317 8.35152,-0.8808 5.21971,4.1105 17.22502,-2.202 16.70305,-16.88253 -2.34886,-14.82722 0.52197,-4.11052 13.57123,4.69774 3.91478,6.01897 9.13448,3.22969 4.17576,10.12949 19.05192,20.55258 h 10.43941 l 8.09054,-10.5699 32.88414,-11.45072 10.17842,-16.29527 14.61517,-10.5699 11.48335,-14.82722 13.31024,-2.64247 4.17577,-4.99135 -3.91478,-9.54227 15.65911,-20.55258 6.78562,-3.5233 12.78827,0.73402 2.34887,-14.97403 11.22236,-14.82722 0.52197,-18.64413 0.78296,-3.6701 19.83487,-3.67011 12.26631,-0.58721 32.62315,15.12083 8.87349,6.60618 15.39813,5.43176 4.69774,2.93608 14.35418,-9.39547 22.70571,4.84454 5.21975,12.47836 9.6564,3.5233 6.5246,-6.16578 38.6258,1.32124 10.7004,-2.05526 23.2277,-19.81856 14.8762,-5.72537 27.9254,-5.13814 4.6977,12.77196 -14.6151,26.13114 1.8269,22.02063 6.5246,12.62516 7.8295,11.59753 2.3489,4.55093 -8.3515,6.31258 25.5765,26.71836 12.7883,9.39547 3.1318,7.0466 -10.4394,9.24869 -9.6564,30.5352 -17.747,-3.3765 -18.791,6.019 -6.7856,8.9551 1.8269,12.9187 -4.4367,-1.7616 3.1318,8.955 -0.261,8.9551 -12.0053,15.4144 v 11.4508 l -4.4368,7.487 -5.4806,4.4041 -1.044,9.3955 3.1318,11.1571 -3.6538,13.9464 -8.3515,7.9274 -13.5712,3.2297 -13.3103,3.0829 -19.5738,9.8359 -4.4368,10.7167 -14.8762,8.0742 -17.48596,9.8359 -14.61517,0.2936 -9.91744,-7.3402 -13.31025,2.6425 -4.95871,5.1381 -2.60986,10.1295 -7.30758,11.4507 -21.40079,19.6718 -9.39547,11.0103 -18.52994,8.6614 -13.83222,11.7444 -10.70039,2.0552 -27.14246,3.0829 -19.57389,21.4334 -8.61252,-1.1744 -20.35684,-11.8912 -8.35153,1.9085 -6.52463,7.0466 -14.35418,-5.2849 -16.18109,-9.1019 -3.91477,-10.2763 -10.96138,-8.5146 -11.48335,-9.1019 -16.18108,-16.5889 -13.31025,-23.4886 -27.92542,-23.0483 -1.56591,-13.7996 -20.61783,-31.2693 -24.53261,-11.3039 -24.27162,-2.4957 -16.96404,-7.7806 -1.8269,-6.3126 -8.35152,-29.3608 -15.39813,-12.1848 -11.48335,-16.0016 -8.61251,-21.1398 -1.56591,-22.3142 1.56591,-20.8462 1.30493,-13.94643 z"
              id="AK-D"
              inkscape:label="ахангаранский"/>
        </a>
        <a @click="setActiveDistrict('ZAN-D')" data-id="ZAN-D"
           class="okrug-11 map-tab-link district hover:opacity-90 transition-all duration-300 ease-in-out"
           id="okrug-11"
           data-color="#5d77c7">
          <path
              class="district-path transition-all duration-300 ease-in-out"
              :class="{
                          'active': activeDistrict && activeDistrict.district_id === 'ZAN-D',
                          'opacity-10': activeDistrict && activeDistrict.district_id && activeDistrict.district_id !== 'ZAN-D',
                      }"
              :fill="getFillColor('ZAN-D')"
              style="fill-opacity:1;stroke-width:2.89133858;stroke-linecap:butt;stroke-linejoin:round;stroke-miterlimit:154.3;stroke-dasharray:none;paint-order:normal;stroke:url(#linearGradient7)"
              d="m 319.40674,863.59269 -0.78296,-8.07423 6.78562,-10.71671 4.17576,-10.7167 0.26099,-9.24866 7.30758,-4.99135 -3.68723,-6.19757 c -17.46589,-8.78335 -17.51269,-9.02423 -27.10902,-12.44654 l -8.35153,-5.57855 -8.8735,-3.81691 -21.40078,29.21403 -8.09054,11.59753 -1.04394,14.24 -2.34887,26.13115 10.70039,17.32289 5.21971,50.64744 26.88147,2.93608 10.7004,-1.32123 8.87349,13.35918 15.39813,1.46804 6.78561,3.22969 4.95872,7.78062 14.87616,4.11052 32.36216,-4.11052 32.10118,-12.18475 -5.2197,-24.95671 -1.30493,-20.25897 -6.00266,0.44041 -16.44206,12.91877 2.87083,9.68907 -0.52197,7.19341 -14.61517,-1.17444 -3.39281,5.43176 -6.26364,-7.19341 7.56857,-12.77196 -3.91478,-0.73402 -21.66177,1.90845 -6.52463,1.02763 8.09054,-7.63381 3.91478,-2.64248 -0.52197,-6.89979 -6.26364,4.40412 4.17576,-8.22103 5.48069,-7.92743 -3.39281,-2.78928 11.22236,-16.88248 v -2.78928 l -19.3129,24.07589 -0.52197,5.28495 -4.17576,-4.84454 -12.78828,-18.79093 -3.91478,-2.78928 -4.43675,-8.51465 0.78296,-7.0466 -9.13448,8.66145 -4.17577,-1.02763 z"
              id="ZAN-D"
              inkscape:label="зангиатинский"/>
        </a>
        <a @click="setActiveDistrict('URTA-D')" data-id="URTA-D"
           class="okrug-12 map-tab-link district hover:opacity-90 transition-all duration-300 ease-in-out"
           id="okrug-12"
           data-color="#6250b9">
          <path
              class="district-path transition-all duration-300 ease-in-out"
              :class="{
                          'active': activeDistrict && activeDistrict.district_id === 'URTA-D',
                          'opacity-10': activeDistrict && activeDistrict.district_id && activeDistrict.district_id !== 'URTA-D',
                      }"
              :fill="getFillColor('URTA-D')"
              style="fill-opacity:1;stroke-width:2.89134;stroke-linecap:butt;stroke-linejoin:round;stroke-miterlimit:154.3;stroke-dasharray:none;paint-order:normal;stroke:url(#linearGradient8)"
              d="m 420.14703,908.43158 8.61251,-8.07423 2.87083,-4.99134 5.21971,4.55093 2.08788,-6.31258 9.65645,1.32123 1.8269,-16.14846 7.56857,1.46805 3.13182,-5.43176 11.22237,5.43176 8.87349,9.39546 h 6.26365 v 17.76331 l -16.18109,20.993 v 17.02928 l 12.00532,1.76165 9.13449,-5.43175 2.60985,-9.24867 3.91478,-3.08289 14.35418,11.01032 1.56591,10.7167 2.08788,2.78928 21.92276,-0.58721 v 11.30392 l 3.13182,7.48701 -9.65645,13.06557 -2.34886,7.0466 -0.78296,44.62844 7.56857,26.4248 15.39813,22.0206 13.31024,10.8635 10.17843,29.214 -8.35153,6.4594 -20.61783,-10.7167 -27.40345,-14.0932 -13.31024,-3.5233 -8.8735,-2.202 -1.04394,10.8635 -2.08788,17.0293 -5.21971,2.7892 -19.57389,-13.2123 -14.61517,-17.0293 -5.74167,-10.7167 -9.91744,-4.1105 -17.48601,-1.7617 -11.48335,-0.4404 -14.35418,10.4231 -18.52995,3.2297 -3.6538,-0.2936 4.17577,-11.3039 -2.34887,-5.285 8.61251,-7.3402 -3.65379,-6.8998 -3.65379,-2.2021 1.30492,-5.2849 10.7004,0.8808 3.65379,-11.3039 -0.78296,-8.5147 -7.30758,-2.7892 -9.39547,-0.7341 -1.56591,-12.4783 10.70039,-18.0569 10.43941,-1.6149 15.65911,-3.9637 9.91744,-18.49731 8.8735,-12.77196 -1.8269,-14.68042 -6.00266,-27.89279 z"
              id="URTA-D"
              inkscape:label="уртачирчикский"/>
        </a>
        <a @click="setActiveDistrict('YAN-D')" data-id="YAN-D"
           id="okrug-13"
           class="okrug-13 map-tab-link district hover:opacity-90 transition-all duration-300 ease-in-out"
           data-color="#4d94db">
          <path
              class="district-path transition-all duration-300 ease-in-out"
              :class="{
                        'active': activeDistrict && activeDistrict.district_id === 'YAN-D',
                          'opacity-10': activeDistrict && activeDistrict.district_id && activeDistrict.district_id !== 'YAN-D',
                      }"
              :fill="getFillColor('YAN-D')"
              style="fill-opacity:1;stroke-width:2.89134;stroke-linecap:butt;stroke-linejoin:round;stroke-miterlimit:154.3;stroke-dasharray:none;paint-order:normal;stroke:url(#linearGradient9)"
              d="m 254.68241,873.19858 -21.1398,20.11217 2.60985,22.16743 -17.74699,-2.64248 -28.96936,30.53527 8.35152,37.43507 -0.26098,33.61816 14.87616,1.0276 9.13448,-7.0466 7.82955,3.2297 0.52197,16.2953 4.69774,3.3765 18.79093,-2.7893 6.78562,-10.8635 3.39281,-1.6149 4.17576,4.551 -3.65379,11.1571 -9.13449,13.3592 12.26631,3.5233 -8.09054,16.1484 3.65379,7.7806 12.52729,3.0829 8.35153,-7.0466 10.17842,-17.7633 14.35418,-15.708 23.48867,-10.8635 11.22237,-2.0553 19.57389,-9.9827 6.52463,-15.1208 14.0932,-2.20206 0.26098,11.01036 25.57655,-5.4318 9.65645,-17.61651 9.39547,-12.77196 -2.60985,-11.74433 -23.22768,7.92742 -9.39547,3.96372 -32.62315,4.55093 -15.65911,-3.2297 -7.0466,-11.45072 -20.61783,-2.20207 -7.82956,-11.89113 -28.44739,-2.05526 -10.96138,-1.46804 -3.91477,-51.82188 z"
              id="YAN-D"
              inkscape:label="янгиюльский"/>
        </a>
        <a @click="setActiveDistrict('CHA-D')" data-id="CHA-D"
           class="okrug-4 map-tab-link district hover:opacity-90 transition-all duration-300 ease-in-out"
           id="okrug-4"
           data-color="#1f77b4">
          <path
              class="district-path transition-all duration-300 ease-in-out"
              :class="{
                          'active': activeDistrict && activeDistrict.district_id === 'CHA-D',
                          'opacity-10': activeDistrict && activeDistrict.district_id && activeDistrict.district_id !== 'CHA-D',
                      }"
              :fill="getFillColor('CHA-D')"
              style="fill-opacity:1;stroke-width:2.89134;stroke-linecap:butt;stroke-linejoin:round;stroke-miterlimit:154.3;stroke-dasharray:none;paint-order:normal;stroke:url(#linearGradient10)"
              d="m 186.82626,945.64154 -30.79626,38.75631 -9.13448,19.96535 -23.22768,34.0586 -6.78562,18.4973 -2.34886,19.8186 -16.181087,16.1484 -13.04926,5.1382 -10.178423,3.9637 -3.392808,0.734 -7.307585,8.221 9.395467,16.4421 26.359506,14.6804 24.79359,-0.2936 25.83754,-10.7167 15.39813,-11.1571 23.22768,-4.9913 20.87881,-19.9654 12.78828,-13.506 16.96404,-10.5699 13.83221,-24.5163 9.13448,-16.0016 3.39281,-8.2211 -3.65379,-3.3765 -7.82956,10.8635 -20.87881,4.6978 -6.78562,-4.1106 -0.26098,-17.176 -4.95872,-2.7893 -9.39547,8.221 -12.00532,-1.7616 -7.0466,-2.2021 3.39281,-31.7097 z"
              id="CHA-D"
              inkscape:label="чиназский"/>
        </a>
        <a @click="setActiveDistrict('QUI-D')" data-id="QUI-D"
           class="okrug-10 map-tab-link district hover:opacity-90 transition-all duration-300 ease-in-out"
           id="okrug-10"
           data-color="#ff7f0e">
          <path
              class="district-path transition-all duration-300 ease-in-out"
              :class="{
                          'active': activeDistrict && activeDistrict.district_id === 'QUI-D',
                          'opacity-10': activeDistrict && activeDistrict.district_id && activeDistrict.district_id !== 'QUI-D',
                      }"
              :fill="getFillColor('QUI-D')"
              style="fill-opacity:1;stroke-width:2.89134;stroke-linecap:butt;stroke-linejoin:round;stroke-miterlimit:154.3;stroke-dasharray:none;paint-order:normal;stroke:url(#linearGradient11)"
              d="m 100.96212,1144.7741 3.6538,15.1208 -2.87084,14.5336 3.13182,4.8445 13.83222,-7.9274 3.65379,6.019 -7.0466,9.9827 -0.78295,7.9274 15.65911,-2.9361 16.18108,7.3402 10.43941,1.9085 23.74965,13.3592 5.74168,18.6441 11.74433,-12.3316 3.91478,-4.2573 27.92541,-5.7253 17.747,-28.9205 12.52729,-5.7253 18.26896,-1.7617 15.9201,-17.1761 8.61251,-8.5146 31.31822,-14.6804 8.09055,-11.4508 8.35152,-8.0742 22.18374,-17.4697 2.60986,-9.6891 -2.08789,-6.1657 9.13449,-7.1934 -5.48069,-6.1658 -4.17577,-2.3489 3.39281,-7.487 11.22237,0.4404 2.87083,-7.9274 v -8.6614 l -15.13714,-4.2574 -4.43675,-14.3868 10.43941,-15.708 -1.04394,-10.12951 -9.65645,0.44041 -3.91478,12.772 -13.83222,7.9274 -11.22236,4.9913 -11.22236,2.3489 -22.9667,12.6252 -10.96138,12.9187 -9.65645,16.0017 -10.17842,8.6614 -15.65912,-2.7893 -2.34886,-9.3954 5.74167,-13.3592 -8.35153,-3.8169 -13.83221,24.2227 -19.83488,13.7996 -30.27428,31.8565 -27.66443,5.7253 -19.83488,13.3592 -19.3129,8.3679 z"
              id="QUI-D"
              inkscape:label="куйичирчикский"/>
        </a>
        <a @click="setActiveDistrict('AKK-D')" data-id="AKK-D"
           class="okrug-7 map-tab-link district hover:opacity-90 transition-all duration-300 ease-in-out"
           id="okrug-7"
           data-color="#2ca02c">
          <path
              class="district-path transition-all duration-300 ease-in-out"
              :class="{
                          'active': activeDistrict && activeDistrict.district_id === 'AKK-D',
                          'opacity-10': activeDistrict && activeDistrict.district_id && activeDistrict.district_id !== 'AKK-D',
                      }"
              :fill="getFillColor('AKK-D')"
              style="fill-opacity:1;stroke:url(#linearGradient12);stroke-width:4.7811;stroke-linecap:butt;stroke-linejoin:round;stroke-miterlimit:154.3;stroke-dasharray:none;paint-order:normal"
              d="m 187.34823,1234.765 13.31024,-16.5888 29.49133,-5.8722 17.48601,-29.3608 11.48335,-4.6978 20.09586,0.2936 25.57655,-29.3608 31.57921,-12.3315 9.13448,-16.0017 25.31556,-22.461 23.22769,-0.4405 15.39812,-12.1847 16.18109,1.6148 -3.6538,19.525 1.56591,6.4594 -15.65911,21.8738 3.6538,32.5905 -3.91478,5.8722 -17.22503,2.0553 -12.52729,-1.7617 -8.35152,5.1382 -17.747,-5.1382 -7.56857,-6.3126 -13.57123,6.1658 -5.48069,13.2124 -10.96137,9.3954 -1.30493,12.9188 -6.26365,3.9637 -12.2663,11.1571 4.69773,13.2124 4.95872,12.038 -0.78295,-7.3402 1.30492,9.3954 -4.43675,3.6701 -13.83221,4.551 -2.34887,11.7443 6.52463,7.3402 15.39813,-1.1744 5.74167,-1.1745 2.08788,10.4231 -8.09054,7.6338 -14.35418,8.8083 -17.22503,6.6062 -5.74167,0.8808 -17.48601,-12.0379 -17.48601,-0.1468 -6.52463,-24.0759 v -6.3126 l -9.91743,-22.3142 -10.17843,-0.4404 z"
              id="AKK-D"
              inkscape:label="аккурганский"/>
        </a>
        <a @click="setActiveDistrict('BUK-D')" data-id="BUK-D"
           class="okrug-3 map-tab-link district hover:opacity-90 transition-all duration-300 ease-in-out"
           id="okrug-3"
           data-color="#d62728">
          <path
              class="district-path transition-all duration-300 ease-in-out"
              :class="{
                        'active': activeDistrict && activeDistrict.district_id === 'BUK-D',
                        'opacity-10': activeDistrict && activeDistrict.district_id && activeDistrict.district_id !== 'BUK-D',
                      }"
              :fill="getFillColor('BUK-D')"
              style="fill-opacity:1;stroke-width:4.7811;stroke-linecap:butt;stroke-linejoin:round;stroke-miterlimit:154.3;stroke-dasharray:none;paint-order:normal;stroke:url(#linearGradient13)"
              d="m 270.08054,1316.0285 -1.56592,28.7736 17.22503,1.1744 12.00532,-1.7616 -8.8735,17.0293 28.44739,1.3212 10.4394,2.4957 4.95872,3.3765 -5.48069,13.2123 14.0932,10.8636 7.04661,-6.019 25.05457,0.5872 6.52463,-8.3678 10.96138,-10.7167 36.27695,-0.7341 21.1398,-7.3402 11.48335,-8.5146 4.95871,-16.1485 1.30493,-15.1208 1.04394,-19.2314 8.61251,-2.7892 5.48069,-10.5699 2.87084,-12.038 15.13714,-18.4973 -19.83487,2.6425 -18.00798,-8.6615 -14.35419,3.8169 -6.78561,-1.6148 -3.91478,-18.4973 8.35152,-6.019 8.35153,-2.2021 5.48069,-8.3678 7.30759,-11.5975 -10.17843,-7.6339 -12.2663,-4.4041 -8.61251,6.8998 -13.31025,3.9637 -12.2663,-2.9361 -8.35153,-12.4783 -7.82956,0.2936 -6.26364,-6.6062 -5.2197,-8.3678 -6.26365,2.6424 -3.91478,4.4042 -20.61783,-7.3402 -5.74167,-4.551 -13.31025,6.3126 -4.69773,13.9464 -10.43941,6.4594 -1.30493,14.24 -18.00797,12.4784 5.48069,16.0016 4.95871,12.4784 -6.26364,5.5785 -11.74433,2.9361 -2.60986,9.1019 4.69774,6.0189 22.18374,-1.1744 1.04394,13.506 -8.09054,8.221 z"
              id="BUK-D"
              inkscape:label="букинский"/>
        </a>
        <a @click="setActiveDistrict('PIS-D')" data-id="PIS-D"
           class="okrug-9 map-tab-link district hover:opacity-90 transition-all duration-300 ease-in-out"
           id="okrug-9"
           data-color="#9467bd">
          <path
              class="district-path transition-all duration-300 ease-in-out"
              :class="{
                        'active': activeDistrict && activeDistrict.district_id === 'PIS-D',
                        'opacity-10': activeDistrict && activeDistrict.district_id && activeDistrict.district_id !== 'PIS-D',
                      }"
              :fill="getFillColor('PIS-D')"
              style="fill-opacity:1;stroke-width:4.7811;stroke-linecap:butt;stroke-linejoin:round;stroke-miterlimit:154.3;stroke-dasharray:none;paint-order:normal;stroke:url(#linearGradient14)"
              d="m 387.0019,1178.6002 5.74168,8.6614 9.13448,0.1468 9.13448,14.9741 11.22237,1.468 11.74433,-3.5233 7.56857,-7.3402 21.40079,7.0466 3.39281,6.753 -11.74434,19.2313 -9.91744,4.551 -6.78561,5.7253 3.91478,16.2953 7.0466,1.7616 12.78827,-5.2849 15.39813,8.221 21.40079,-2.6424 8.87349,-12.4784 23.22769,-3.3765 41.49664,15.1208 13.04926,-0.1468 15.13714,15.7081 9.39547,21.4334 1.56591,13.506 17.48601,18.3505 15.9201,14.5336 10.96138,0.1468 6.52463,18.7909 11.74433,8.3679 30.0133,-1.7617 11.48335,-15.5612 16.44207,-32.4437 9.91743,-4.551 19.05192,4.551 17.22503,-12.038 -24.7936,-9.689 -8.09054,-18.057 -24.53261,-17.0292 -15.39813,-17.9102 -12.2663,-20.8461 -29.49133,-22.6079 -0.78295,-14.8272 -19.31291,-28.3332 -20.61783,-10.8635 -24.79359,-4.9914 -20.35685,-10.2763 -11.48335,6.6062 -32.36216,-17.3229 -18.79094,-9.689 -15.39812,-2.7893 -3.13183,25.8375 -7.0466,5.4318 -8.09054,-3.5233 -14.87615,-13.0656 -14.0932,-17.1761 -6.78562,-10.8635 -17.48601,-3.3765 -2.60985,18.9377 2.60985,8.2211 -16.70305,20.6994 3.39281,32.0033 -7.30759,8.955 z"
              id="PIS-D"
              inkscape:label="пскентский"/>
        </a>
        <a @click="setActiveDistrict('BEKA-D')" data-id="BEKA-D"
           class="okrug-1 map-tab-link district hover:opacity-90 transition-all duration-300 ease-in-out"
           id="okrug-1"
           data-color="#8c564b">
          <path
              class="district-path transition-all duration-300 ease-in-out"
              :class="{
                        'active': activeDistrict && activeDistrict.district_id === 'BEKA-D',
                        'opacity-10': activeDistrict && activeDistrict.district_id && activeDistrict.district_id !== 'BEKA-D',
                      }"
              :fill="getFillColor('BEKA-D')"
              style="fill-opacity:1;stroke-width:4.7811;stroke-linecap:butt;stroke-linejoin:round;stroke-miterlimit:154.3;stroke-dasharray:none;paint-order:normal;stroke:url(#linearGradient15)"
              d="m 342.11245,1394.7718 4.43675,12.4783 -12.00532,3.3765 1.30493,9.3955 10.96137,-4.2573 7.56857,4.1105 -1.04394,2.0553 -10.4394,7.1934 3.91477,25.5439 -8.35152,15.1208 4.17576,5.1382 17.22502,-1.6149 -3.65379,7.9274 -10.96138,5.1382 -1.82689,7.1934 8.87349,2.6425 16.18109,20.8462 0.78295,19.2313 -8.8735,15.4145 -15.39812,1.7616 -11.22237,6.1658 4.43675,12.4783 6.52463,9.2487 -1.82689,9.6891 -10.7004,13.2123 -0.52197,12.9188 14.0932,18.4973 3.91478,17.9102 19.57389,14.974 14.35419,16.2952 10.70039,13.7996 19.57389,3.2297 23.48867,1.0277 8.09054,4.6977 10.70039,-4.2573 -13.31024,-28.0396 -11.48335,-5.1382 -12.26631,-3.8169 -2.60985,-7.6338 2.60985,-6.6062 -4.43674,-9.1018 2.08788,-5.5786 8.61251,-0.2936 27.92542,0.8808 11.74433,-12.6251 -0.26099,-14.3869 4.95872,-4.2573 0.26099,-15.5612 -9.13448,-7.487 -10.96138,-10.7167 0.52197,-15.2677 -7.0466,-10.4231 3.13182,-13.6528 -6.52463,-2.0552 -14.35419,-33.765 v -7.3402 l 7.56858,-11.5975 -1.30493,-9.9827 -26.09852,-31.5629 3.91478,-13.2124 18.79093,-12.1847 17.747,-0.2936 24.27162,-0.7341 0.52197,-8.5146 8.09054,-9.6891 h 4.17576 l 1.30493,-14.5336 -2.87084,-12.9187 -6.00266,-19.3782 -1.30492,-30.3885 v -14.3868 l -5.74168,2.0553 -2.60985,35.967 -4.95872,11.0103 -10.17842,8.5147 -19.57389,8.0742 -38.36483,2.7893 -14.87615,16.442 -5.48069,3.0829 -22.18374,-1.468 z"
              id="BEKA-D"
              inkscape:label="бекабадский"/>
        </a>
        <a @click="setActiveDistrict('BOS-D')" data-id="BOS-D"
           class="okrug-2 map-tab-link district hover:opacity-90 transition-all duration-300 ease-in-out"
           :class="{'active': activeDistrict && activeDistrict.district_id === 'BOS-D'}"
           id="okrug-2"
           data-color="#522e9a"
        >
          <path
              class="district-path transition-all duration-300 ease-in-out"
              :class="{
                        'active': activeDistrict && activeDistrict.district_id === 'BOS-D',
                        'opacity-10': activeDistrict && activeDistrict.district_id && activeDistrict.district_id !== 'BOS-D',
                      }"
              :fill="getFillColor('BOS-D')"
              style="fill-opacity:1;stroke:url(#linearGradient2);stroke-width:3.26929134;stroke-dasharray:none;stroke-linecap:butt;stroke-linejoin:bevel"
              d="m 1626.0608,106.39561 -13.0079,-8.013783 -7.0201,-3.251972 -48.3151,-41.346499 -7.846,-3.368114 -16.5179,-0.696851 -14.0403,-6.852369 -9.4978,-5.574809 -15.8985,3.832681 -8.8784,3.484256 -4.5425,0.812993 -7.846,8.478355 -7.846,6.852369 -16.518,0.232284 -8.8784,-3.832681 -7.6395,5.110241 -19.6151,26.3642 -4.1295,4.297249 -2.8906,1.045277 -3.5101,3.251971 -8.259,0.58071 -8.259,5.923232 -9.4978,6.85237 -12.5949,2.32284 -7.6396,-6.3878 -5.7813,-3.13583 -2.4776,-1.74213 -5.3684,2.09055 -9.0849,10.68505 -9.4978,8.12993 -4.3359,8.5945 -5.1619,6.15552 -5.3683,4.41339 -5.7813,5.69095 -4.5425,10.33662 -11.356,9.40749 -7.0202,7.08466 -8.6719,16.02757 0.8259,8.24607 -8.4655,17.42128 -5.9877,17.30514 -8.6719,21.48624 -5.3684,13.70474 -11.9755,2.7874 -12.182,-8.59449 -8.259,-6.73623 -7.846,-2.78741 -2.4777,-6.73622 1.6518,-24.9705 -5.9877,-9.40749 -13.6273,-4.76182 -1.8583,-5.22638 -6.8137,1.04528 -44.5984,-37.74611 -5.9878,-3.60039 -6.6072,1.50984 -8.4654,11.3819 -1.4454,16.84057 -1.4453,10.22048 -11.769,6.38781 -7.2266,10.68505 -1.6518,5.34252 -11.9755,6.62009 -7.6396,5.11024 -2.6841,10.33662 2.8906,19.39569 0.6194,15.91144 v 7.54922 l -11.1496,7.7815 -7.846,2.7874 -5.8665,0.28262 -5.3683,7.31693 -8.6719,2.78741 -8.4655,1.3937 -8.0525,5.11024 -7.0201,10.91734 -11.14964,9.40749 -11.97552,19.62797 -8.0525,19.39569 -8.8784,18.35041 -18.16975,9.05906 -23.3316,8.01379 -3.30359,5.57481 -13.62731,8.12993 -11.3561,30.89373 -4.54243,3.94883 -7.63956,-1.50985 -2.47769,-10.33662 -2.47769,-7.08466 -4.33596,-3.60039 -8.25898,1.97441 -5.16186,5.34252 -19.82154,47.61816 -34.27475,16.49215 h -8.67193 l -8.8784,-8.01379 -15.2791,-8.01379 -10.11725,3.48426 -12.18199,10.10434 -15.42235,1.54662 -12.18199,2.7874 -8.8784,-1.50984 -5.98775,3.01969 1.44532,8.71064 8.8784,13.82088 0.20647,13.24017 -3.09712,12.7756 -13.00788,20.67325 -13.00789,24.85436 -11.14962,12.31103 -12.38846,17.53742 -3.71654,8.47836 -16.9309,8.71064 6.19423,10.68505 10.32372,8.24607 -10.32372,16.49214 -29.52584,44.48233 7.2266,10.68505 -2.68416,8.71064 -0.61943,38.32681 8.46545,-4.9941 7.22661,-10.91733 1.23884,-32.51972 1.6518,-3.6004 -0.8259,-5.22638 4.74891,-2.67126 44.18553,-0.11615 5.5748,16.37601 -4.95538,11.26576 -13.21436,-0.11615 -10.73667,3.48426 -10.73667,11.03347 -11.97552,24.04137 7.02013,9.05906 10.73667,-11.84647 2.06475,-9.1752 8.67192,-4.18111 8.46545,3.01969 12.18199,-5.34253 14.04026,-3.83268 11.76904,2.2067 4.12949,2.20669 3.30359,3.94883 6.60718,5.11024 15.89853,6.62008 11.14962,-1.16142 14.65968,-11.3819 11.56257,-9.75591 6.60718,-3.01969 1.65179,-3.83268 2.27122,-2.90355 -0.41295,-26.13191 8.25898,-3.01969 15.48558,-16.95671 2.47769,-6.38781 6.40071,-6.85236 0.61942,-3.48426 9.49782,-6.85237 17.55033,-6.96851 10.32372,-1.62599 24.1575,0.34843 4.74892,-2.55512 9.08487,-2.43898 6.40071,-4.52953 8.46545,4.1811 -7.63956,12.77561 1.85827,23.22837 0.8259,11.3819 1.44532,24.38979 -2.47769,3.01969 -9.49782,2.32283 -3.71654,8.94293 -21.06039,-5.22639 -5.78129,4.18111 -2.47769,17.7697 -10.73667,15.21459 -3.30359,52.80389 4.54244,7.89764 17.13737,-4.76181 17.7568,-0.69685 11.3561,3.25197 22.29923,11.96261 10.11725,7.08465 16.9309,4.64568 3.09711,2.7874 12.18199,-8.01379 24.98341,4.41339 5.78125,13.5886 6.8137,1.3937 4.7489,-3.71654 37.7848,-0.92913 13.0079,-2.55512 11.3561,-7.66536 15.2791,-13.24018 11.9755,-2.7874 0.6194,-36.00397 4.9554,-4.18111 13.0079,0.23228 28.287,-23.69293 16.1721,-24.00265 2.2712,-16.14372 -0.6194,-9.29135 -13.8338,-1.85827 -10.3237,-16.14372 -5.3683,-8.36221 -1.6518,-3.6004 -8.8784,-4.29725 -4.1295,-3.36811 -9.0849,-11.84647 -8.0525,-7.31693 -11.769,-0.58071 -6.8137,-7.31694 -8.6719,-16.72443 -15.2791,-8.71064 -20.2345,-5.45866 -19.2021,2.55512 -8.8784,3.48425 -33.65536,-3.83268 -6.19423,-6.15552 -3.30359,-42.39177 7.63955,-15.09844 14.86616,-7.78151 17.96327,-5.45866 7.6396,2.20669 26.2222,-18.69884 14.2467,1.27756 c 0,0 11.7691,-3.13583 14.2468,-5.80709 2.4777,-2.67126 24.1575,-29.1516 24.1575,-29.1516 l 25.8093,-14.63388 29.1129,-15.44686 11.9755,-16.49215 4.7489,-18.35041 0.4129,-18.46655 12.3885,-13.5886 12.182,-5.45867 19.8215,-11.49804 10.9432,-10.91733 5.7813,-15.44687 15.8985,-9.11714 10.9431,-24.73821 22.5058,-17.42128 13.2143,-3.13583 17.5503,1.62599 8.672,-14.86616 13.8208,8.93712 22.2993,0.69685 18.1697,-18.23427 1.2389,-27.87405 -11.5626,-14.63387 3.0971,-10.45277 10.7367,-9.87206 2.0647,-10.5689 13.8338,-8.47836 18.1698,8.12993 26.8416,8.12993 15.2791,-4.87796 4.749,0.58071 11.9755,-13.35631 16.105,-6.03938 20.028,-24.62207 8.6719,-3.6004 33.2424,-29.50003 18.7756,-9.53137 13.6273,-0.11614 9.4978,3.60039 8.8784,-6.85237 15.8986,-9.29134 2.2712,-15.33073 z"
              id="BOS-D"
              inkscape:label="бостанлыкский"/>
        </a>
      </g>
    </svg>
  </div>
</template>

<style>
.district-path:hover {
  filter: drop-shadow(0px 0px 20px black);
}

.district-path.active {
  filter: drop-shadow(0px 0px 20px black);
}

.district:hover path {
  transform: scale(1.01)
}

.district-path.active:hover {
  transform: none
}
</style>