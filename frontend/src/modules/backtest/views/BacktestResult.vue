<template>

<div class="row">
    <div class="col-12">
        <ul class="nav nav-tabs justify-content-center">
            <li class="nav-item">
                <button @click="isActive = !isActive"  class="nav-link active" aria-current="page">Reporte</button>
            </li>
            <li class="nav-item">
                <button @click="isActive = !isActive" class="nav-link">Operaciones</button>
            </li>
            <li class="nav-item">
                <button @click="isActive = !isActive" class="nav-link">Grafica</button>
            </li>
        </ul>
    </div>
    <div class="col-12">

        <ReportResumenVue v-show="isActive" />

        <OperationsBacktestVue v-show="!isActive"/>
     
    </div>
</div>

</template>

<script>
import { defineAsyncComponent, ref } from '@vue/runtime-core'

export default {
    components: {
        ReportResumenVue: defineAsyncComponent( () => import('@/modules/backtest/components/ReportResumen.vue')),
        OperationsBacktestVue: defineAsyncComponent( () => import('@/modules/backtest/components/OperationsBacktest.vue')),

    },
    setup(){
        const isActive = ref(true)

        return{
            isActive,
        }
    }

}
</script>

<style>

</style>