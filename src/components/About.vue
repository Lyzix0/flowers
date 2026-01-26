<template>
  <link rel="preload" as="image" href="../images/process.png">
  <div class="about-page">
    <h1 class="main-title">О НАС</h1>
    <div class="about-content">
      <div class="about-section">
        <div class="about-columns">
          <div class="about-text">
            <p class="contact-description">
              Мы специализируемся на создании уникальных амариллисов в воске — 
              это не просто цветы, это произведения искусства, которые будут 
              радовать вас недели без особого ухода.
            </p>
            
            <p class="contact-description">
              Амариллисы в воске — это инновационный способ сохранения красоты 
              живых цветов. Восковая оболочка защищает растение и позволяет ему 
              цвести без полива. Это идеальное решение для 
              тех, кто ценит красоту и практичность.
            </p>
            <p class="contact-description">
              Мы тщательно отбираем каждый цветок, обрабатываем его по специальной 
              технологии и упаковываем в восковую оболочку. Наш процесс гарантирует 
              долговечность и красоту каждого растения.
            </p>
          </div>
          <div class="about-image">
            <img src="../images/process.png" alt="Процесс создания восковых цветов" class="process-image" loading="eager" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import '../styles/about.css'

defineEmits(['contact'])
</script>