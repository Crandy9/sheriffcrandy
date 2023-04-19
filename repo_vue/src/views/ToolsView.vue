<template>
    <section class="tools-section">
        <div class="tools-title-div">
            <h3 class="tools-title has-text-white">
                {{$t('toolsview.toolsiuse')}}
            </h3>
        </div>
        <ul class="my-tools-unordered-list">
            <li class="list-item">
                <div class="tool-list-title">
                    DAW: FL Studio Producer Edition
                </div>
            </li>
            <li class="list-item">
                <div class="tool-list-title">
                    Yamaha CLP-645B Clarinova
                </div>
                <img class="my-tools-img yamaha-img" src="@/assets/images/yamaha_clp_645b.jpg" alt="">
            </li>
            <li class="list-item">
                <div class="tool-list-title">
                    Beyerdynamic DT770 PRO Headset - 80 OHM
                </div>
                <img class="my-tools-img headphones-img" src="@/assets/images/dt_770_pro.png" alt="">
            </li>
            <li class="list-item">
                <div class="tool-list-title">
                    Alesis v49 Midi Controller
                </div>
                <img class="my-tools-img alesis-img" src="@/assets/images/alesis_v49.png" alt="">
            </li>
        </ul>
    </section>
</template>

<script>

export default {
    name: 'Tools',
    data() {
        return {
        }
    },
    mounted() {
      document.title = 'Tools' 
    }
}
</script>