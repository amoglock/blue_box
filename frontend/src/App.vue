<template>
  <div class="app">
    <div class="content">
      <router-view />
    </div>
  </div>
</template>

<script setup>
</script>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Russo One', sans-serif;
    background-color: #f0f0f0;
}

.content {
    min-height: 100vh;
}
</style>