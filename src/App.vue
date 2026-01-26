<script setup>
import { ref } from 'vue'
import { products } from './data/products.js'
import FlowerCard from './components/FlowerCard.vue'
import About from './components/About.vue'
import Footer from './components/Footer.vue'
import ProductModal from './components/ProductModal.vue' // Импортируем компонент
import './styles/app.css'

const currentPage = ref('products') 
const selectedProduct = ref(null)
const isModalOpen = ref(false)

const openModal = (product) => {
  selectedProduct.value = product
  isModalOpen.value = true
  document.body.style.overflow = 'hidden'
}

const closeModal = () => {
  isModalOpen.value = false
  setTimeout(() => { selectedProduct.value = null }, 300) // Задержка для плавной анимации
  document.body.style.overflow = ''
}

const setPage = (page) => {
  currentPage.value = page
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const handleContact = () => {
  window.open('https://t.me/xlsx_csv', '_blank')
}
</script>

<template>
  <div class="page">
    <header class="header">
      <div class="logo">Floramania®</div>
      <nav class="nav">
        <a 
          href="#" 
          @click.prevent="setPage('products')"
          :class="{ active: currentPage === 'products' }"
        >
          ТОВАРЫ
        </a>
        <a 
          href="#" 
          @click.prevent="setPage('about')"
          :class="{ active: currentPage === 'about' }"
        >
          О НАС
        </a>
      </nav>
    </header>

    <div class="main-content">
      <!-- Страница товаров -->
      <div v-if="currentPage === 'products'">
        <h1 class="main-title">ТОВАРЫ</h1>
        
        <!-- Новый блок раздела с линией -->
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
              @click="openModal(item)"
            />
          </div>
        </div>
      </div>

      <!-- Страница "О нас" -->
      <About v-if="currentPage === 'about'" @contact="handleContact" />
    </div>

    <!-- Подвал -->
    <Footer @contact="handleContact" />

    <!-- Исправленное модальное окно (через компонент) -->
    <ProductModal 
      :is-open="isModalOpen" 
      :product="selectedProduct" 
      @close="closeModal" 
    />
  </div>
</template>