<script setup>
defineProps({
  isOpen: Boolean,
  product: Object
});

defineEmits(['close', 'contact', 'avito']);

const handleContact = () => {
  window.open('https://t.me/xlsx_csv', '_blank');
};

const handleAvito = () => {
  window.open('https://www.avito.ru/moskva/rasteniya/amarillis_lukovitsy_v_voske_optroznitsa_7816560257', '_blank');
};
</script>

<template>
  <Transition name="modal">
    <!-- Оверлей -->
    <div v-if="isOpen" class="modal-overlay" @click="$emit('close')">
      <!-- Контент модалки -->
      <div class="modal-content" @click.stop>
        <button class="modal-close" @click="$emit('close')">×</button>
        <div class="modal-body">
          <div class="modal-image-col">
            <div class="image-wrapper">
              <img :src="product?.image" :alt="product?.name" />
            </div>
          </div>
          <div class="modal-info-col">
            <div class="info-sticky">
              <span class="modal-subtitle">COLLECTION 2026</span>
              <h2 class="modal-title">{{ product?.name }}</h2>
              <p class="modal-price">₽{{ product?.price }}</p>
              
              <div class="divider"></div>
              
              <p class="modal-description">{{ product?.description }}</p>
              
              <!-- Кнопки теперь внутри scroll-контейнера, но липкие снизу -->
              <div class="modal-buttons">
                <button class="contact-button primary" @click="handleContact">
                  Telegram
                </button>
                <button class="contact-button secondary" @click="handleAvito">
                  Avito
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>

<style scoped>
/* Modal Overlay */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(62, 50, 41, 0.6); /* Чуть темнее фон для контраста */
  backdrop-filter: blur(8px);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2000;
  padding: 40px;
}

.modal-content {
  background: #F2F0EB;
  border-radius: 12px;
  width: 100%;
  max-width: 1100px;
  height: 85vh;
  position: relative;
  overflow: hidden;
  box-shadow: 0 30px 60px rgba(0,0,0,0.2);
}

.modal-close {
  position: absolute;
  top: 20px;
  right: 20px;
  background: #F2F0EB; /* Фон чтобы было видно на картинке */
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  font-size: 1.8rem;
  cursor: pointer;
  color: #3E3229;
  z-index: 20;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.modal-close:hover {
  background: #3E3229;
  color: #fff;
}

.modal-body {
  display: flex;
  height: 100%;
}

.modal-image-col {
  flex: 1.2;
  background: #EBE8E1;
  height: 100%;
  overflow: hidden;
  position: relative;
}

.image-wrapper {
  width: 100%;
  height: 100%;
}

.image-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.modal-info-col {
  flex: 1;
  overflow-y: auto; /* Скроллится только правая часть */
  height: 100%;
  position: relative;
}

.info-sticky {
  display: flex;
  flex-direction: column;
  min-height: 100%; /* Растягиваем контент */
  padding: 60px;
  box-sizing: border-box;
}

.modal-subtitle {
  font-family: 'Raleway', sans-serif;
  font-size: 0.8rem;
  letter-spacing: 2px;
  color: #BC8F8F;
  font-weight: 700; /* Жирнее */
  text-transform: uppercase;
  margin-bottom: 10px;
  display: block;
}

.modal-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: 3.5rem;
  font-weight: 600; /* Жирнее */
  font-style: italic;
  color: #3E3229;
  margin: 0 0 10px 0;
  line-height: 1;
}

.modal-price {
  font-family: 'Raleway', sans-serif;
  font-size: 1.8rem;
  color: #5C5550;
  font-weight: 600; /* Жирнее */
  margin: 0;
}

.divider {
  height: 2px;
  background: #B0B7A6;
  width: 50px;
  margin: 30px 0;
}

.modal-description {
  font-family: 'Raleway', sans-serif;
  font-size: 1.1rem;
  color: #3E3229;
  font-weight: 500; /* Жирнее для читаемости */
  line-height: 1.7;
  margin-bottom: 40px;
  flex-grow: 1;
}

.modal-buttons {
  display: flex;
  gap: 15px;
  margin-top: auto;
  background: #F2F0EB;
  padding-top: 20px;
}

.contact-button {
  padding: 20px 30px;
  border-radius: 12px;
  font-family: 'Raleway', sans-serif;
  font-weight: 700; /* Жирнее */
  text-transform: uppercase;
  letter-spacing: 1px;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.3s;
}

.primary {
  flex: 2;
  background: #3E3229;
  color: #F2F0EB;
  border: 1px solid #3E3229;
}

.secondary {
  flex: 1;
  background: transparent;
  color: #3E3229;
  border: 1px solid #3E3229;
}

.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.4s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-active .modal-content {
  transition: transform 0.4s cubic-bezier(0.19, 1, 0.22, 1);
}

.modal-enter-from .modal-content,
.modal-leave-to .modal-content {
  transform: translateY(50px) scale(0.95);
}

/* --- MOBILE --- */
@media (max-width: 900px) {
  .modal-overlay {
    padding: 0;
    align-items: flex-end; /* Шторка снизу */
  }

  .modal-content {
    border-radius: 20px 20px 0 0;
    height: 90vh; /* Высота на мобильном */
    max-height: 90vh;
  }

  .modal-body {
    flex-direction: column;
    overflow-y: hidden; /* Скроллим только нижнюю часть */
  }

  .modal-image-col {
    flex: none;
    height: 35%; /* Уменьшил высоту картинки, чтобы был виден текст */
    min-height: 250px;
  }

  .modal-info-col {
    padding: 0;
    flex: 1;
    overflow-y: auto; /* Скролл только тут */
  }
  
  .info-sticky {
    padding: 30px 20px;
  }

  .modal-title {
    font-size: 2.5rem;
  }
  
  .modal-close {
    top: 15px;
    right: 15px;
  }
  
  /* Липкие кнопки для мобилки */
  .modal-buttons {
    position: sticky;
    bottom: -1px; /* Чтобы перекрыть возможный зазор */
    padding: 20px 0 10px 0; /* Отступ сверху и снизу */
    background: linear-gradient(to bottom, rgba(242, 240, 235, 0.8), #F2F0EB 40%);
    backdrop-filter: blur(5px);
    z-index: 10;
  }
}
</style>