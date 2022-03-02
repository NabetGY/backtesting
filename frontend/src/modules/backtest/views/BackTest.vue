<template>
    <v-row >

        <TickerFormVue />
        
        <v-col cols="12" sm="8" class="mx-8">
        
            <IndicatorInfoCardVue v-for="item in indicators" :key="item.indicator" :indicator="item" />

            <IndicatorDialogVue />

        </v-col>

    </v-row>
    
</template>

<script>

import { computed, defineAsyncComponent, ref } from 'vue'
import { useStore } from 'vuex'

export default {
    components:{
        IndicatorDialogVue: defineAsyncComponent( () => import('@/modules/backtest/components/IndicatorDialog.vue')),
        TickerFormVue: defineAsyncComponent( () => import('@/modules/backtest/components/TickerForm.vue')),
        IndicatorInfoCardVue: defineAsyncComponent( () => import('@/modules/backtest/components/IndicatorInfoCard.vue')),

    },
    
    setup() {

        const store = useStore()
        const date = ref(new Date())
        const dateLimit = ref(new Date())
        

        return{
            tickers: computed( () => store.state.backtest.tickers ),
            indicators: computed( () => store.state.backtest.indicators ),
            selectItem: ( item ) =>{
                console.log(item.symbol)
            },
            date,
            dateLimit,
            muestra: ( date ) => {
                console.log( date )
            }
        }
    }
}

</script>

<style scoped>

    .box-indicator{
        height: 570px;
        overflow-y: scroll;
        border-radius: 5px;
        background-color: rgb(227, 224, 224);
    }


</style>