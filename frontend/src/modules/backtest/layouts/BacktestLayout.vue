<template>
  <v-container class="height-app">
    <v-row v-if="isLoading" class="loading-position" no-gutters>
        <v-col cols="12" class="text-center">
          <v-progress-circular  :size="70" :width="7" color="purple" indeterminate>
          </v-progress-circular>
        </v-col>
    </v-row>

    <router-view v-else />
    
  </v-container>

</template>

<script>
import { computed } from "vue";
import { useStore } from 'vuex';

/* import useAuth from './modules/auth/composables/useAuth'
 */
export default {
  components: {
    
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

  .loading-position{
      position: absolute;
      top: 40%;
      right: 50%;
      left: 50%;
  }
</style>