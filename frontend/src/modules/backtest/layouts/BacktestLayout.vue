<template>
  
    <div v-if="isLoading" 
    class="row justify-content-md-center">
      <div class="col-3 alert-info text-center-mt-5">
        Espere por favor...
        <h3 class="mt-2">
          <i class="fa fa-spin fa-sync"></i>
        </h3>
      </div>
    </div>

  <div v-else
   class="container-fluid overflow-hidden">
    <div class="row vh-100 overflow-auto">

      <NavBar />
      <router-view class="col d-flex h-sm-100 p-5 m-0"/>

   </div>
</div>

</template>

<script>
import { computed, defineAsyncComponent } from "vue";
import { useStore } from 'vuex';

/* import useAuth from './modules/auth/composables/useAuth'
 */
export default {
  components: {
    NavBar: defineAsyncComponent(() =>
      import("@/modules/shared/components/NavBar.vue")
    ),
  },

  setup(){
    const store = useStore()
    store.dispatch('backtest/loadTickers')

    return {
      isLoading: computed( () => store.state.backtest.isLoading )
    }
  }
};
</script>

<style scoped>


    .scroll {
        overflow-y: scroll;
        height: calc(100vh);
    }

</style>