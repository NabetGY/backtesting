<template>

  <div class="scroll">
    <router-view />
  </div>

</template>

<script>

export default {
}

</script>

<style scoped>

    .scroll {
        overflow-y: scroll;
        height: calc(100vh);
    }

</style>