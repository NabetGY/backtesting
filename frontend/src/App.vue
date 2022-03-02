<template>
    <v-app>
        <v-app-bar app absolute color="deep-purple">

            <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
            <v-toolbar-title>Dashboard</v-toolbar-title>
        </v-app-bar>

        <v-navigation-drawer app v-model="drawer" absolute temporary>
            <v-list nav dense>
                <v-list-item-group v-model="group" active-class="deep-purple--text text--accent-4">

                    <v-list-item prepend-icon="mdi-home" title="Inicio"></v-list-item>
                    <v-list-item prepend-icon="mdi-account" title="Cuenta"></v-list-item>
                    
                </v-list-item-group>
            </v-list>
        </v-navigation-drawer>

        <v-main>
            <router-view ></router-view>
        </v-main>

    </v-app>

</template>

<script setup>

import { ref } from "vue";

    const intViewportHeight = ref("")
    const height = window.innerHeight-64
    intViewportHeight.value = `${height}px`

    const setHeightApp = () => { 
        let height = window.innerHeight-64
        intViewportHeight.value = `${height}px`
    };

    window.addEventListener('resize', setHeightApp);

    const drawer = ref(false)
    const group = ref(null)
    
</script>

<style>

html { overflow-y: hidden }

.height-app{
    height: v-bind(intViewportHeight);
    overflow-y: auto;
}

</style>