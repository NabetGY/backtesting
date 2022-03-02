<template>
<!-- App.vue -->

<v-app>
  <AppBarVue />

  <!-- Sizes your content based upon application components -->
  <v-main>

    <!-- Provides the application the proper gutter -->
    <v-container fluid>

      <!-- If using vue-router -->
      <router-view></router-view>
    </v-container>
  </v-main>

  <v-footer app>
    <!-- -->
  </v-footer>
</v-app>
</template>

<script>
import { defineAsyncComponent } from '@vue/runtime-core'

export default {
    name: 'App',
    components:{
      AppBarVue: defineAsyncComponent(() => import('@/modules/shared/components/AppBar.vue'))
    },

  data: () => ({
    //
  }),
}
</script>
