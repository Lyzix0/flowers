<script setup>
import About from '../components/About.vue'
defineEmits(['contact'])
</script>

<template>
  <About @contact="$emit('contact')" />
</template>