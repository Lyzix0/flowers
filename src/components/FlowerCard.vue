<script setup>
import '../styles/flowerCard.css'

defineProps(['flower']);
defineEmits(['click']);
</script>

<template>
  <div class="card" @click="$emit('click')">
    <!-- СНАЧАЛА КАРТИНКА -->
    <div class="img-container">
      <img :src="flower.image" :alt="flower.name" />
    </div>
    
    <!-- ПОТОМ ТЕКСТ (теперь он будет снизу) -->
    <div class="card-info">
      <span class="flower-name">{{ flower.name.toUpperCase() }}</span>
      <span class="flower-price">₽{{ flower.price }} / шт.</span>
    </div>
  </div>
</template>