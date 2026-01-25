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
  window.open('https://www.avito.ru', '_blank');
};
</script>

<template>
  <Transition name="modal">
    <div v-if="isOpen" class="modal-overlay" @click="$emit('close')">
      <div class="modal-content" @click.stop>
        <button class="modal-close" @click="$emit('close')">×</button>
        <div class="modal-image">
          <img :src="product?.image" :alt="product?.name" />
        </div>
        <div class="modal-info">
          <h2 class="modal-title">{{ product?.name.toUpperCase() }}</h2>
          <p class="modal-price">₽{{ product?.price }} / шт.</p>
          <p class="modal-description">{{ product?.description }}</p>
          <div class="modal-buttons">
            <button class="contact-button" @click="handleContact">
              Связаться
            </button>
            <button class="contact-button avito-button" @click="handleAvito">
              Купить на Avito
            </button>
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  padding: 20px;
}

.modal-content {
  background: white;
  border-radius: 15px;
  max-width: 700px;
  width: 100%;
  display: flex;
  overflow: hidden;
  position: relative;
  max-height: 95vh;
  overflow-y: auto;
}

.modal-close {
  position: absolute;
  top: 15px;
  right: 15px;
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  color: #333;
  z-index: 10;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color 0.2s;
}

.modal-close:hover {
  color: #000;
}

.modal-image {
  width: 40%;
  height: 100%;
  overflow: hidden;
  border-radius: 15px 0 0 15px;
}

.modal-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.modal-info {
  padding: 30px;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.modal-title {
  font-size: 1.5rem;
  font-weight: 800;
  color: #222;
  margin: 0 0 10px 0;
  letter-spacing: 0.5px;
}

.modal-price {
  font-size: 1.1rem;
  color: #4e4e4e;
  font-weight: 400;
  margin: 0 0 15px 0;
}

.modal-description {
  font-family: "Outfit";
  font-size: 1.1rem;
  color: #383838;
  line-height: 1.6;
  margin: 0 0 30px 0;
  flex-grow: 1;
}

.modal-buttons {
  display: flex;
  gap: 15px;
  flex-direction: column;
}

.contact-button {
  flex: 1;
  font-family: 'Outfit';
  padding: 15px 30px;
  background: #070707;
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 1.2rem;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.2s;
  letter-spacing: 0.5px;
}

.contact-button:hover {
  background: #333;
}

.avito-button {
  background: #008539;
}

.avito-button:hover {
  background: #005a26;
}

/* Анимация модального окна */
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-to,
.modal-leave-from {
  opacity: 1;
}

/* Адаптивность */
@media (max-width: 768px) {
  .modal-content {
    flex-direction: column;
  }

  .modal-image {
    width: 100%;
    height: 250px;
    border-radius: 15px 15px 0 0;
  }

  .modal-info {
    padding: 20px;
  }

  .modal-title {
    font-size: 1.3rem;
  }

  .modal-price {
    font-size: 1rem;
  }

  .modal-description {
    font-size: 0.95rem;
  }

  .contact-button {
    font-size: 1rem;
    padding: 12px 20px;
  }
}

@media (max-width: 480px) {
  .modal-overlay {
    padding: 10px;
  }

  .modal-content {
    border-radius: 10px;
    max-height: 95vh;
  }

  .modal-image {
    height: 200px;
    border-radius: 10px 10px 0 0;
  }

  .modal-info {
    padding: 15px;
  }

  .modal-title {
    font-size: 1.1rem;
    margin-bottom: 8px;
  }

  .modal-price {
    font-size: 0.9rem;
    margin-bottom: 10px;
  }

  .modal-description {
    font-size: 0.85rem;
    margin-bottom: 15px;
  }

  .contact-button {
    font-size: 0.9rem;
    padding: 10px 15px;
  }

  .modal-close {
    font-size: 1.5rem;
    top: 10px;
    right: 10px;
  }
}
</style>
