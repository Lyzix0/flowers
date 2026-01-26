<template>
  <footer class="footer">
    <div class="footer-content">
      <div class="footer-section">
        <h3 class="footer-logo">Floramania®</h3>
        <p class="footer-text">Уникальные амариллисы в воске</p>
      </div>

      <div class="footer-section">
        <h4 class="footer-title">FAQ</h4>
        <div class="faq-list">
          <div 
            v-for="(item, index) in faqItems" 
            :key="index"
            class="faq-item"
          >
            <button 
              class="faq-question"
              @click="toggleFaq(index)"
              :class="{ active: openFaqIndex === index }"
            >
              {{ item.question }}
              <span class="faq-icon">{{ openFaqIndex === index ? '−' : '+' }}</span>
            </button>
            <Transition name="faq">
              <div v-if="openFaqIndex === index" class="faq-answer">
                {{ item.answer }}
              </div>
            </Transition>
          </div>
        </div>
      </div>

      <div class="footer-section">
        <h4 class="footer-title">Контакты</h4>
        <!-- Обертка для кнопок -->
        <div class="footer-buttons-container">
          <button class="footer-button footer-button-primary" @click="$emit('contact')">
            Связаться с нами
          </button>
          <button class="footer-button footer-button-avito" @click="openAvito">
            Мы на Авито
          </button>
        </div>
        <p class="footer-copyright">
          © {{ new Date().getFullYear() }} Floramania®. Все права защищены.
        </p>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { ref } from 'vue'
import '../styles/footer.css'

defineEmits(['contact'])

const openFaqIndex = ref(null)

const toggleFaq = (index) => {
  openFaqIndex.value = openFaqIndex.value === index ? null : index
}

const openAvito = () => {
  window.open('https://www.avito.ru/moskva/rasteniya/amarillis_lukovitsy_v_voske_optroznitsa_7816560257', '_blank')
}

const faqItems = [
    {
    question: 'Как сделать заказ?',
    answer: 'Для заказа свяжитесь с нами через форму, нажав кнопку "Оставить заявку", или купите товар на avito. Мы ответим в ближайшее время и поможем выбрать идеальный амариллис для вас.'
  },
  {
    question: 'Как вы доставляете товары?',
    answer: 'Мы осуществляем доставку через СДЭК, курьерскими сервисами или иными способами. Подробности можно уточнить при оформлении заказа.'
  },
  {
    question: 'Как ухаживать за амариллисом в воске?',
    answer: 'Амариллисы в воске практически не требуют ухода. Просто поставьте их в хорошо освещенное место, но избегайте прямых солнечных лучей. Их не нужно поливать или удобрять. Клубень содержит все необходимые питательные вещества для длительного цветения.'
  },
]
</script>