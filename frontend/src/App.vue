<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import Footer from './components/Footer.vue'
import ProductModal from './components/ProductModal.vue'
import './styles/app.css'

const selectedProduct = ref(null)
const isModalOpen = ref(false)

// Трекинг (срабатывает 1 раз при загрузке любой страницы сайта)
const logVisit = async () => {
  try {
    await axios.post('/api/visit', {
      screen_resolution: `${window.screen.width}x${window.screen.height}`,
      referrer: document.referrer || 'direct',
      platform: navigator.platform,
      user_agent: navigator.userAgent
    })
  } catch (e) { console.error('Stat error:', e) }
}

onMounted(() => { logVisit() })

const openModal = (product) => {
  selectedProduct.value = product
  isModalOpen.value = true
  document.body.style.overflow = 'hidden'
}

const closeModal = () => {
  isModalOpen.value = false
  setTimeout(() => { selectedProduct.value = null }, 300)
  document.body.style.overflow = ''
}

const handleContact = () => {
  window.open(import.meta.env.VITE_TELEGRAM_LINK, '_blank')
}
</script>

<template>
  <div class="page">
    <header class="header">
      <div class="logo">Floramania®</div>
      <nav class="nav">
        <!-- router-link автоматически добавляет класс active, когда мы на нужной странице -->
        <router-link to="/items" active-class="active">ТОВАРЫ</router-link>
        <router-link to="/about" active-class="active">О НАС</router-link>
      </nav>
    </header>

    <main class="main-content">
      <!-- Здесь будет меняться контент (ItemsView или AboutView) -->
      <router-view
        @open-product="openModal"
        @contact="handleContact"
      />
    </main>

    <Footer @contact="handleContact" />

    <ProductModal
      :is-open="isModalOpen"
      :product="selectedProduct"
      @close="closeModal"
    />
  </div>
</template>