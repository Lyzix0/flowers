<script setup>
import '../styles/flowerCard.css'

defineProps(['flower']);
defineEmits(['click']);
</script>

<template>
  <div class="card" @click="$emit('click')">
    <div class="card-info">
      <span class="flower-name">{{ flower.name.toUpperCase() }}</span>
      <span class="flower-price">₽{{ flower.price }} / шт.</span>
    </div>
    <div class="img-container">
      <img :src="flower.image" :alt="flower.name" />
    </div>
  </div>
</template>