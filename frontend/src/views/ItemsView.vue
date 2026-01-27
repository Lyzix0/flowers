<script setup>
import { products } from '../data/products.js'
import FlowerCard from '../components/FlowerCard.vue'

// Пробрасываем событие клика наверх в App.vue, чтобы открыть модалку
defineEmits(['open-product'])
</script>

<template>
  <div class="items-page">
    <h1 class="main-title">ТОВАРЫ</h1>
    <div class="category-block">
      <div class="category-header">
        <span class="category-title">АМАРИЛЛИСЫ В ВОСКЕ</span>
        <div class="category-line"></div>
      </div>
      <div class="catalog">
        <FlowerCard
          v-for="item in products"
          :key="item.id"
          :flower="item"
          @click="$emit('open-product', item)"
        />
      </div>
    </div>
  </div>
</template>