<template>

    <v-col cols="12"  sm="3" class="my-5 border" >
        
        <span class="font-weight-bold">Selecciona un Ticker:</span>
        <SimpleTypeahead
            class="mb-5 "
            placeholder="APPL"
            :items="tickers"
            :minInputLength="1"
            @selectItem="selectItem"
            :itemProjection="
                (item) => { 
                    return item.symbol;
            }"
        />

        <div class="mb-1">
            <v-text-field min=0 type="number" v-model="tickerData.capital" label="Capital" required>
            </v-text-field>
        </div>

        <div class="mb-1">
            <v-text-field min=0 type="number" v-model="tickerData.margen" label="Margen" required>
            </v-text-field>
        </div>

        <div class="mb-1">
            <span class="font-weight-bold">Fecha inicial: </span>
            <datepicker v-model="dateStart" :upper-limit="dateLimit" typeable />
        </div>

        <div class="mb-7">
            <span class="font-weight-bold">Fecha final: </span>
            <datepicker v-model="dateEnd" :upper-limit="dateLimit" typeable />
        </div>

        <div class="mb-1">
            <v-select v-model="tickerData.interval" :items="listPeriod" label="Periodo"></v-select>
        </div>

        <div class="d-flex flex-column">
            <v-btn @click="startBacktest" color="primary">Iniciar</v-btn>
            <v-btn class="mt-2" color="warning">Limpiar</v-btn>
        </div>

    </v-col>
    
</template>

<script>
import { computed, ref } from 'vue'
import { useStore } from 'vuex';
import SimpleTypeahead from 'vue3-simple-typeahead'
import 'vue3-simple-typeahead/dist/vue3-simple-typeahead.css' //Optional default CSS
import Datepicker from 'vue3-datepicker'
import { useRouter } from 'vue-router'
import Swal from 'sweetalert2'



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
        const router = useRouter()


        const tickerData = ref(
            {
                capital:0,
                margen:0,
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
            listPeriod: ['30min', '60min', 'Diario', 'Semanal'],
            tickerData,
            dateLimit,
            dateStart,
            dateEnd,
            tickers: computed( () => store.state.backtest.tickers ),
            selectItem: ( item ) =>{
                tickerData.value.ticker = item.symbol
            },
            startBacktest: async() => {
                tickerData.value.dateStart = dateFormat( dateStart.value )
                tickerData.value.dateEnd = dateFormat( dateEnd.value )
                console.log(tickerData)
                const { ok, message } = await store.dispatch("backtest/startBacktest", tickerData.value )

                if ( !ok ) {
                   Swal.fire('Error', message, 'error')
               } 
               else  {
                   Swal.fire(
                    {
                        title:'Baktest Exitoso',
                        icon:'success',
                        allowEscapeKey:false,
                        allowOutsideClick:false
                    }
                    ).then((result) => 
                        {
                            if (result.isConfirmed) {
                               router.push({ name: 'backtestResult' }) 
                            } 
                        }
                    )
                }
            }
        }
    }
}
</script>

<style>

    .bg-gray{
        background-color: #EFEFEF;
    }

    
    .simple-typeahead-input, div.v3dp__input_wrapper input{
        height: 45px;
        padding-left: 20px;
        width: 100%;
        background-color: #EFEFEF;
        border-bottom: 1px solid #9D9D9D;
        transition: 0.3s;

    }

    .simple-typeahead-input:hover, div.v3dp__input_wrapper input:hover{

        background-color: #cfcece;

    }

</style>