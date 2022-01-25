<template>

<div class="d-grid gap-2">

    <button type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#indicatorModalToggle">
        <i class="bi bi-plus-circle-fill"><span class="ms-2"> Agregar otro indicador</span></i>
    </button>

    <div class="modal fade" id="indicatorModalToggle" aria-hidden="true" aria-labelledby="exampleModalToggleLabel" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">

                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalToggleLabel">Indicadores</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>

                <div class="modal-body">

                    <div class="row mb-3">
                        <label for="inputIndicator" class="col-sm-3 col-form-label">Indicador:</label>
                        <div class="col-sm-9">
                            <select v-model="indicator" @change="imprime" class="form-select">
                                <option selected value="MAVue">Cruce de medias moviles</option>
                                <option value="IchimokuVue">Nubes de Ichimoku</option>
                            </select>
                        </div>
                    </div>

                </div>

                <div class="modal-footer">
                    <button class="btn btn-primary" data-bs-target="#indicatorInputs" data-bs-toggle="modal">
                        Seleccionar
                    </button>
                </div>

            </div>
        </div>
    </div>

    <div class="modal fade" id="indicatorInputs" aria-hidden="true" aria-labelledby="indicatorInputsModalToggleLabel" tabindex="-1">
        <component :is="indicator"></component>
    </div>

</div>
    
</template>

<script>

import { ref, defineAsyncComponent } from 'vue'

export default {

    components:{
        MAVue: defineAsyncComponent(() =>
            import("@/modules/backtest/components/MA.vue")
        ),
        IchimokuVue: defineAsyncComponent(() =>
            import("@/modules/backtest/components/Ichimoku.vue")
        ),
    },

    setup() {

        const indicator = ref("MAVue")

        return {
            indicator,
        }
    }

}

</script>

<style>

</style>