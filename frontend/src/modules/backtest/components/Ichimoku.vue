<template>

    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">

            <div class="modal-header">
                <h5 class="modal-title" id="indicatorInputsModalToggleLabel">Nubes de Ichimoku</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>

            <div class="modal-body">
                
                <div class="row mb-3">
                    <label for="inputIndicator" class="col-sm-5 col-form-label text-end">Linea de conversion:</label>
                    <div class="col-sm-7">
                        <input type="number" v-model="data.conversion" min="0" class="form-control" >
                    </div>
                </div>

                <div class="row mb-3">
                    <label for="inputIndicator" class="col-sm-5 col-form-label text-end">Linea Base:</label>
                    <div class="col-sm-7">
                        <input type="number" v-model="data.base" min="0" class="form-control" >
                    </div>
                </div>

                <div class="row mb-3">
                    <label for="inputIndicator" class="col-sm-5 col-form-label text-end">Linea de Retraso:</label>
                    <div class="col-sm-7">
                        <input type="number" v-model="data.retraso" min="0" class="form-control" >
                    </div>
                </div>

                <div class="row mb-3">
                    <label for="inputIndicator" class="col-sm-5 col-form-label text-end">Span A:</label>
                    <div class="col-sm-7">
                        <input type="number" v-model="data.spanA" min="0" class="form-control" >
                    </div>
                </div>

                <div class="row mb-3">
                    <label for="inputIndicator" class="col-sm-5 col-form-label text-end">Span B:</label>
                    <div class="col-sm-7">
                        <input type="number" v-model="data.spanB" min="0" class="form-control" >
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
import { ref } from 'vue';
import { useStore } from 'vuex'

export default {
    props: {
        modelValue: Array,
    },
    setup() {

        const store = useStore()

        const data = ref({
            indicator: "Ichimoku",
            conversion: "",
            base:"",
            retraso:"",
            spanA:"",
            spanB:"",
        })


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