<template>
  <div class="row">

        <TickerSelectionVue />

      <div class="col-8 pt-3">
        
        <IndicatorInfoVue v-for="item in indicators" :key="item.indicator" :indicator="item" />

        <div class="row py-3 mb-4">

            <IndicatorModalVue />

        </div>

      </div>

  </div>
</template>

<script>

import { computed, defineAsyncComponent, ref } from 'vue'
import { useStore } from 'vuex'

export default {
    components:{
        IndicatorModalVue: defineAsyncComponent( () => import('@/modules/backtest/components/IndicatorModal.vue')),
        TickerSelectionVue: defineAsyncComponent( () => import('@/modules/backtest/components/TickerSelection.vue')),
        IndicatorInfoVue: defineAsyncComponent( () => import('@/modules/backtest/components/IndicatorInfo.vue')),
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

<style>

    .box-indicator{
        border-radius: 5px;
        background-color: rgb(227, 224, 224);
    }

</style>