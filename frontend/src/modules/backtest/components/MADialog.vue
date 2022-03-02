<template>

    <v-dialog v-model="dialog" activator="parent" :retain-focus="false">

        <v-card min-width="500"> 

            <v-toolbar color="primary">Cruce de Medias Moviles</v-toolbar>

            <v-card-title>
                Configuracion
            </v-card-title>

            <v-card-text>
                    <v-list two-line>
                        <v-list-subheader inset>Medias Moviles</v-list-subheader>
                            <v-list-item
                                v-for="(item, index) in indicators.config" :key="index"
                                prepend-icon="mdi-finance"
                                :title="item.MA"
                                :subtitle="'Periodo: '+item.period"
                            >
                                <template v-slot:append>
                                    <v-list-item-avatar right>
                                        <v-btn variant="text" color="grey lighten-1" icon="mdi-delete-circle"></v-btn>
                                    </v-list-item-avatar>
                                </template>
                            </v-list-item>
                    </v-list>
                
                <v-select v-model="MA" :items="listMA" label="Tipo"></v-select>

                <v-text-field min=0 type="number" v-model="periodo" label="Periodo" required>
                </v-text-field>

                <v-btn @click="addMA" color="primary" icon="mdi-plus-circle">
                </v-btn>

            </v-card-text>
    
            <v-card-actions>

                <v-btn color="success" class="ma-2" @click="saveIndicator">
                    Guardar
                </v-btn>

                <v-btn color="primary" text @click="dialog = !dialog">
                    Volver
                </v-btn>

            </v-card-actions>

        </v-card>

    </v-dialog>
            
</template>

<script setup>
    import { ref } from 'vue'
    import { useStore } from 'vuex'

    const store = useStore()
    const listMA =  [ 'Media movil simple', 'Media movil exponencial' ]
    const MA = ref("")
    const periodo = ref(0)
    const dialog = ref(false)

    const indicators = ref({
        indicatorName: "MACD",
        config: []
    })

    const addMA = () => {
        indicators.value.config.push(
            {
                "MA":MA.value,
                "period":periodo.value
            }
        )

        MA.value = ""
        periodo.value =  0
    }
  
    const saveIndicator = () => {
        dialog.value = false
        store.dispatch("backtest/addIndicator", indicators.value )
    }
 
    

</script>

<style scoped>

</style>