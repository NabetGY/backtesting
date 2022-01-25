<template>

    <div class="col-3 me-5 pt-3">
        
        <span class="fw-bold">Selecciona un Ticker:</span>
        <SimpleTypeahead
            placeholder="APPL"
            :items="tickers"
            :minInputLength="1"
            @selectItem="selectItem"
            :itemProjection="
                (item) => { 
                    return item.symbol;
            }"
        />

        <div class="mt-5 mb-3">
            <span class="fw-bold">Fecha inicial: </span>
            <datepicker v-model="dateStart" :upper-limit="dateLimit"/>
        </div>

        <div class="mb-3">
            <span class="fw-bold">Fecha final: </span>
            <datepicker v-model="dateEnd" :upper-limit="dateLimit"/>
        </div>

        <div class="form-floating mt-5 mb-3">
            <select v-model="tickerData.interval" class="form-select" id="floatingSelect" aria-label="Floating label select example">
                <option value="1min">1 min</option>
                <option value="5min">5 min</option>
                <option value="60min">60 min</option>
            </select>
            <label for="floatingSelect">Periodo</label>
        </div>

        <div class="d-grid gap-2 mt-5 col-6 mx-auto">
            <button @click="startBacktest" class="btn btn-primary" type="button">Iniciar</button>
            <button class="btn btn-danger" type="button">Limpiar</button>
        </div>

    </div>
    
</template>

<script>
import { computed, ref } from 'vue'
import { useStore } from 'vuex';
import SimpleTypeahead from 'vue3-simple-typeahead'
import 'vue3-simple-typeahead/dist/vue3-simple-typeahead.css' //Optional default CSS
import Datepicker from 'vue3-datepicker'

export default {
    components:{
        SimpleTypeahead,
        Datepicker
    }, 
    setup() {

        const store = useStore()
        const dateLimit = ref(new Date())
        const dateStart = ref(new Date())
        const dateEnd = ref(new Date())


        const tickerData = ref(
            {
                ticker: "",
                dateStart: "",
                dateEnd: "",
                interval: "",
            }
        )

        const dateFormat= ( date ) => {
            return date.getUTCFullYear() + "-" +
            ("0" + (date.getUTCMonth()+1)).slice(-2) + "-" +
            ("0" + date.getUTCDate()).slice(-2) + " " +
            ("0" + date.getUTCHours()).slice(-2) + ":" +
            ("0" + date.getUTCMinutes()).slice(-2) + ":" +
            ("0" + date.getUTCSeconds()).slice(-2)
        }

        return {
            tickerData,
            dateLimit,
            dateStart,
            dateEnd,
            tickers: computed( () => store.state.backtest.tickers ),
            selectItem: ( item ) =>{
                tickerData.value.ticker = item.symbol
            },
            startBacktest: () => {
                tickerData.value.dateStart = dateFormat( dateStart.value )
                tickerData.value.dateEnd = dateFormat( dateEnd.value )
                store.dispatch("backtest/startBacktest", tickerData.value )
            }
        }
    }
}
</script>

<style>

</style>