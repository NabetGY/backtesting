<template>

    <v-card :color="color" theme="dark" class="mb-3 zoom" :elevation="isHovering ? 24 : 6">

        <div class="d-flex flex-no-wrap justify-space-between">

            <div>
                <v-card-title class="text-h5">
                    {{ indicator.indicatorName }}
                </v-card-title>

                <v-card-subtitle class="ps-10">
                    <ul>
                        <li v-for="item in listConfig" :key="item">
                        {{ item }}
                        </li>
                    </ul>
        
                </v-card-subtitle>

                <v-card-actions class="ps-5">
                    <v-btn class="ml-2" icon="mdi-cog" variant="outlined"></v-btn>
                </v-card-actions>
            </div>

            <v-avatar class="ma-3" size="150" rounded="0">
                <v-img class="rounded-xl" :src="img_card"></v-img>
            </v-avatar>

        </div>

    </v-card>

</template>

<script setup>
import { computed, defineProps, ref } from 'vue'

    const props = defineProps(['indicator'])
    const listConfig = ref([])
    let color = "#952175"
    let img_card = ""

    const configSTR = computed( () => {
        const lista = []
        if(  props.indicator.indicatorName === "MACD"){
            color = "blue-grey"
            img_card = "https://res.cloudinary.com/lumayo/image/upload/v1645910477/ma_lybvuq.png"
            for (const iterator of props.indicator.config) {
                
                lista.push(macdResumen(iterator))
                
            }
        }else if(  props.indicator.indicatorName === "Ichimoku"){
            color = "red-darken-3"
            img_card ="https://res.cloudinary.com/lumayo/image/upload/v1645909786/ichimoku_mglko7.png"
            for (const iterator of props.indicator.config) { 
                console.log(iterator)
                lista.push(ichimokuResumen(iterator)) 
            }
        }
        else if(  props.indicator.indicatorName === "DonchianChannels"){
            color = "amber-lighten-1"
            img_card ="https://res.cloudinary.com/lumayo/image/upload/v1646446457/donchianchannels_waircd.png"
            for (const iterator of props.indicator.config) { 
                console.log(iterator)
                lista.push(donchianChannelsResumen(iterator)) 
            }
        }
        return lista
    })

    function ichimokuResumen( config ) {
        let resumen = `
        Linea de conversion: ${ config.conversion} periodos.
        linea base: ${ config.base } periodos.
        linea de retraso: ${ config.lagging } periodos.
        Span A: ${ config.spanA }.
        Span B: ${ config.spanB} .
        `
        return resumen
    }

    function macdResumen( config ) {
        let resumen = `Tipo: ${ config.MA }, periodos: ${ config.period }.`
        return resumen
    }

    function donchianChannelsResumen( config ) {
        let resumen = `Tamaño del Periodo: ${ config.period }.`
        return resumen
    }

    listConfig.value =  configSTR.value

    console.log(listConfig.value)

</script>

<style scoped>
    .zoom {
        will-change: transform;
        transition: transform 450ms;
    }
    .zoom:hover{
        transition: transform 125ms;
        transform: scale(1.02);
    }
</style>