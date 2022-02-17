<template>

    <div class="modal-dialog modal-size  modal-dialog-centered">
        <div class="modal-content">

            <div class="modal-header">
                <h5 class="modal-title" id="indicatorInputsModalToggleLabel">Cruce de Medias Moviles</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>

            <div class="modal-body">

                <div class="row mb-3">

                    <label for="inputMA" class="col-sm-1 col-md-1 col-form-label">Tipo:</label>
                    <div class="col-sm-5 col-md-5">
                        <select id="inputMA" class="form-select">
                            <option selected value="1">Media movil simple</option>
                            <option value="2">Media movil exponencial</option>
                        </select>
                    </div>

                    <label for="inputMAPeriod" class="col-sm-2 col-md-2 col-form-label">Periodo:</label>
                    <div class="col-sm-3 col-md-3">
                        <input v-model="data.rapido" id="inputMAPeriod" type="number" min="0" class="form-control" >
                    </div>

                </div>
                
                

<!--                 <div class="row mb-3">
                    <label for="inputIndicator" class="col-sm-5 col-form-label text-end">Periodo Lento:</label>
                    <div class="col-sm-7">
                        <input v-model="data.lento" type="number" min="0" class="form-control" >
                    </div>
                </div> -->

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

<style scoped>

    .modal-size{
        max-width: 50%;
    }

</style>