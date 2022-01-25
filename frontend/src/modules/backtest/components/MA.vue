<template>

    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">

            <div class="modal-header">
                <h5 class="modal-title" id="indicatorInputsModalToggleLabel">Cruce de Medias Moviles</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>

            <div class="modal-body">
                
                <div class="row mb-3">
                    <label for="inputIndicator" class="col-sm-5 col-form-label text-end">Periodo rapido:</label>
                    <div class="col-sm-7">
                        <input v-model="data.rapido" type="number" min="0" class="form-control" >
                    </div>
                </div>

                <div class="row mb-3">
                    <label for="inputIndicator" class="col-sm-5 col-form-label text-end">Periodo Lento:</label>
                    <div class="col-sm-7">
                        <input v-model="data.lento" type="number" min="0" class="form-control" >
                    </div>
                </div>

            </div>

            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                <button type="button" class="btn btn-primary" data-bs-target="#indicatorModalToggle" data-bs-toggle="modal">Volver</button>
                <button @click="saveIndicator" type="button" class="btn btn-success" data-bs-dismiss="modal">Guardar</button>
            </div>

        </div>
    </div>

  
</template>

<script>
import { ref } from 'vue'
import { useStore } from 'vuex'

export default {
    setup() {

        const store = useStore()

        const data = ref(
            {
                indicator: "MA",
                rapido: 0,
                lento:0
            }
        )

        return {
            data,
            saveIndicator: () => {
                store.dispatch("backtest/addIndicator", data.value )
            }
        }
    }
}
</script>

<style>

</style>