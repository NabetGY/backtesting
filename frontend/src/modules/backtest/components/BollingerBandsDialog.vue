<template>

    <v-dialog v-model="dialog" activator="parent" :retain-focus="false">

        <v-card min-width="500"> 

            <v-toolbar color="primary">Bollinger Bandas</v-toolbar>

            <v-card-title>
                Configuracion
            </v-card-title>

            <v-card-text>
                
                <v-text-field min=0 type="number" v-model="period" label="Periodo" required>
                </v-text-field>

                <v-text-field min=0 type="number" v-model="std" label="Desviacion Estandar" required>
                </v-text-field>

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
    const period = ref(0)
    const std = ref(0)
    const dialog = ref(false)

    const indicators = ref({
        indicatorName: "BollingerBands",
        config: []
    })



    const saveIndicator = () => {
        indicators.value.config.push(
            {
                "period": period.value,
                "std": std.value
            }
        )
        dialog.value = false
        store.dispatch("backtest/addIndicator", indicators.value )
    }
 
</script>

<style scoped>

</style>