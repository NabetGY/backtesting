<template>
    <v-app>
        <v-app-bar app absolute color="deep-purple" density="compact" class="px-15">

            <v-app-bar-nav-icon color="deep-purple" @click="drawer = !drawer"></v-app-bar-nav-icon>
            <v-app-bar-title>G-BACKTEST</v-app-bar-title>
            <v-spacer></v-spacer>
            
        </v-app-bar>

        <template v-if="isAuthenticated !== 'no-authenicate'">

            <v-navigation-drawer app v-model="drawer" absolute temporary>

                <v-list nav dense>

                    <v-list-item-group v-model="group" active-class="deep-purple--text text--accent-4">

                        <v-list-item prepend-icon="mdi-account-circle" :title="username"></v-list-item>

                        <v-divider></v-divider>

                        <v-list-item prepend-icon="mdi-home" title="Inicio"></v-list-item>
                        <v-list-item prepend-icon="mdi-account" title="Cuenta"></v-list-item>
                        
                    </v-list-item-group>

                </v-list>

                <template v-slot:append>
                    <div class="pa-2">
                        <v-btn @click="onLogout" block color="warning" >
                            Cerrar sesion
                        </v-btn>
                    </div>
                </template>

            </v-navigation-drawer>

        </template>

        <v-main>
            <router-view ></router-view>
        </v-main>

    </v-app>

</template>

<script setup>

import { computed, ref } from "vue";
import { useStore } from "vuex";
import useAuth from '@/modules/auth/composables/useAuth'
import { useRouter } from "vue-router";

    
    const drawer = ref(false)
    const group = ref(null)

    const  { username, logout } = useAuth()

    const store = useStore()
    const router = useRouter()
    
    const isAuthenticated = computed( () => store.state.auth.status )

    const intViewportHeight = ref("")
    const height = window.innerHeight-64
    intViewportHeight.value = `${height}px`

    const setHeightApp = () => { 
        let height = window.innerHeight-64
        intViewportHeight.value = `${height}px`
    };

    window.addEventListener('resize', setHeightApp);

    

    const onLogout = () => {
        router.push({name : 'login'})
        logout()
    }
    
</script>

<style>

html { overflow-y: hidden }

.height-app{
    height: v-bind(intViewportHeight);
    overflow-y: auto;
}

</style>