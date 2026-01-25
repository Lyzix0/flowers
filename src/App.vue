<script setup>
import { ref } from 'vue'
import { products } from './data/products.js'
import FlowerCard from './components/FlowerCard.vue'
import About from './components/About.vue'
import Footer from './components/Footer.vue'
import './styles/app.css'

const currentPage = ref('products') // 'products', 'about', 'contacts'
const selectedProduct = ref(null)
const isModalOpen = ref(false)

const openModal = (product) => {
  selectedProduct.value = product
  isModalOpen.value = true
  document.body.style.overflow = 'hidden'
}

const closeModal = () => {
  isModalOpen.value = false
  selectedProduct.value = null
  document.body.style.overflow = ''
}

const openTelegram = () => {
  window.open('https://t.me/xlsx_csv', '_blank')
}

const openAvito = () => {
  window.open('https://www.avito.ru', '_blank')
}

const setPage = (page) => {
  currentPage.value = page
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const handleContact = () => {
  openTelegram()
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
        
        <div class="layout-grid">
          <aside class="sidebar">
            <p>АМАРИЛЛИСЫ<br>В ВОСКЕ</p>
          </aside>
          
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

      <!-- Страница "Контакты" -->
      <div v-if="currentPage === 'contacts'" class="contacts-page">
        <h1 class="main-title">КОНТАКТЫ</h1>
        <div class="contacts-content">
          <div class="contact-section">
            <h2 class="contact-title">Свяжитесь с нами</h2>
            <p class="contact-description">
              Мы всегда рады ответить на ваши вопросы и помочь с выбором 
              идеального амариллиса для вас или в подарок.
            </p>
            <button class="contact-button" @click="openTelegram">
              Написать в Telegram
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Подвал -->
    <Footer @contact="handleContact" />

    <!-- Модальное окно -->
    <Transition name="modal">
      <div v-if="isModalOpen" class="modal-overlay" @click="closeModal">
        <div class="modal-content" @click.stop>
          <button class="modal-close" @click="closeModal">×</button>
          <div class="modal-image">
            <img :src="selectedProduct?.image" :alt="selectedProduct?.name" />
          </div>
          <div class="modal-info">
            <h2 class="modal-title">{{ selectedProduct?.name.toUpperCase() }}</h2>
            <p class="modal-price">₽{{ selectedProduct?.price }} / шт.</p>
            <p class="modal-description">{{ selectedProduct?.description }}</p>
            <div class="modal-buttons">
              <button class="contact-button" @click="openTelegram">
                Связаться
              </button>
              <button class="contact-button avito-button" @click="openAvito">
                Купить на Avito
              </button>
            </div>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>