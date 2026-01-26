<script setup>
import { ref } from 'vue';

const props = defineProps({
  isOpen: Boolean,
  product: Object
});

defineEmits(['close', 'contact', 'avito']);

const showForm = ref(false);
const isSending = ref(false); // Состояние загрузки

const formData = ref({
  name: '',
  phone: '',
  telegram: ''
});

const handleOpenForm = () => {
  showForm.value = true;
};

const handleCloseForm = () => {
  showForm.value = false;
  resetForm();
};

const resetForm = () => {
  formData.value = {
    name: '',
    phone: '',
    telegram: ''
  };
};

const handleSubmitForm = async () => {
  if (!formData.value.name || !formData.value.phone || !formData.value.telegram) {
    alert('Пожалуйста, заполните все поля');
    return;
  }

  isSending.value = true;

  const BOT_TOKEN = import.meta.env.VITE_BOT_TOKEN;
  const CHAT_ID = import.meta.env.VITE_CHAT_ID;
  console.log(BOT_TOKEN)
  console.log(CHAT_ID)
  
  const message = `
<b>🚀 Новая заявка с сайта!</b>
<b>📦 Товар:</b> ${props.product?.name || 'Не указан'}
<b>💰 Цена:</b> ${props.product?.price || '—'} руб.

<b>👤 Имя:</b> ${formData.value.name}
<b>📞 Телефон:</b> ${formData.value.phone}
<b>✈️ Telegram:</b> ${formData.value.telegram}
  `.trim();

  try {
    const response = await fetch(`https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        chat_id: CHAT_ID,
        text: message,
        parse_mode: 'HTML'
      }),
    });

    if (response.ok) {
      alert('Спасибо! Ваша заявка отправлена. Мы свяжемся с вами в ближайшее время.');
      handleCloseForm();
    } else {
      throw new Error('Ошибка при отправке');
    }
  } catch (error) {
    console.error('Ошибка:', error);
    alert('Произошла ошибка при отправке сообщения. Попробуйте связаться с нами напрямую.');
  } finally {
    isSending.value = false;
  }
};

const handleAvito = () => {
  const avitoLink = import.meta.env.VITE_AVITO_ORDER;
  window.open(avitoLink, '_blank');
};
</script>

<template>
  <!-- Модальное окно с товаром -->
  <Transition name="modal">
    <div v-if="isOpen" class="modal-overlay" @click="$emit('close')">
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
              
              <div class="modal-buttons">
                <button class="contact-button primary" @click="handleOpenForm">
                  Оставить заявку
                </button>
                <button class="contact-button secondary" @click="handleAvito">
                  Купить на Avito
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </Transition>

  <!-- Форма заявки -->
  <Transition name="modal">
    <div v-if="showForm" class="form-overlay" @click="handleCloseForm">
      <div class="form-content" @click.stop>
        <button class="form-close" @click="handleCloseForm">×</button>
        <h2 class="form-title">Оставить заявку</h2>
        <p class="form-subtitle">Заполните форму и мы свяжемся с вами</p>
        
        <form @submit.prevent="handleSubmitForm" class="application-form">
          <div class="form-group">
            <label for="name" class="form-label">Имя</label>
            <input 
              id="name"
              v-model="formData.name" 
              type="text" 
              class="form-input" 
              placeholder="Ваше имя"
              required
              :disabled="isSending"
            />
          </div>

          <div class="form-group">
            <label for="phone" class="form-label">Номер телефона</label>
            <input 
              id="phone"
              v-model="formData.phone" 
              type="tel" 
              class="form-input" 
              placeholder="+7 (999) 999-99-99"
              required
              :disabled="isSending"
            />
          </div>

          <div class="form-group">
            <label for="telegram" class="form-label">Telegram</label>
            <input 
              id="telegram"
              v-model="formData.telegram" 
              type="text" 
              class="form-input" 
              placeholder="@telegram_id"
              required
              :disabled="isSending"
            />
          </div>

          <button type="submit" class="form-submit" :disabled="isSending">
            {{ isSending ? 'Отправка...' : 'Отправить заявку' }}
          </button>
        </form>
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
  background: rgba(62, 50, 41, 0.6);
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
  background: #F2F0EB;
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
  overflow-y: auto;
  height: 100%;
  position: relative;
}

.info-sticky {
  display: flex;
  flex-direction: column;
  min-height: 100%;
  padding: 60px;
  box-sizing: border-box;
}

.modal-subtitle {
  font-family: 'Raleway', sans-serif;
  font-size: 0.8rem;
  letter-spacing: 2px;
  color: #BC8F8F;
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 10px;
  display: block;
}

.modal-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: 3.5rem;
  font-weight: 600;
  font-style: italic;
  color: #3E3229;
  margin: 0 0 10px 0;
  line-height: 1;
}

.modal-price {
  font-family: 'Raleway', sans-serif;
  font-size: 1.8rem;
  color: #5C5550;
  font-weight: 600;
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
  font-weight: 500;
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
  font-weight: 700;
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
    align-items: flex-end;
  }

  .modal-content {
    border-radius: 20px 20px 0 0;
    height: 90vh;
    max-height: 90vh;
  }

  .modal-body {
    flex-direction: column;
    overflow-y: hidden;
  }

  .modal-image-col {
    flex: none;
    height: 35%;
    min-height: 250px;
  }

  .modal-info-col {
    padding: 0;
    flex: 1;
    overflow-y: auto;
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
  
  .modal-buttons {
    position: sticky;
    bottom: -1px;
    padding: 20px 0 10px 0;
    background: linear-gradient(to bottom, rgba(242, 240, 235, 0.8), #F2F0EB 40%);
    backdrop-filter: blur(5px);
    z-index: 10;
  }
}

/* --- ФОРМА ЗАЯВКИ --- */
.form-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(62, 50, 41, 0.6);
  backdrop-filter: blur(8px);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 3000;
  padding: 40px;
}

.form-content {
  background: #F2F0EB;
  border-radius: 12px;
  width: 100%;
  max-width: 500px;
  padding: 60px;
  box-shadow: 0 30px 60px rgba(0,0,0,0.2);
  position: relative;
}

.form-close {
  position: absolute;
  top: 20px;
  right: 20px;
  background: transparent;
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  font-size: 1.8rem;
  cursor: pointer;
  color: #3E3229;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.form-close:hover {
  background: #3E3229;
  color: #F2F0EB;
}

.form-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: 2.5rem;
  font-weight: 600;
  font-style: italic;
  color: #3E3229;
  margin: 0 0 10px 0;
  text-align: center;
}

.form-subtitle {
  font-family: 'Raleway', sans-serif;
  font-size: 0.95rem;
  color: #5C5550;
  text-align: center;
  margin-bottom: 30px;
}

.application-form {
  display: flex;
  flex-direction: column;
  gap: 25px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-label {
  font-family: 'Raleway', sans-serif;
  font-size: 0.9rem;
  font-weight: 600;
  color: #3E3229;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.form-input {
  padding: 15px 20px;
  border: 2px solid #B0B7A6;
  border-radius: 8px;
  font-family: 'Raleway', sans-serif;
  font-size: 1rem;
  color: #3E3229;
  background: #FFFFFF;
  transition: all 0.3s;
}

.form-input:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.form-input::placeholder {
  color: #B0B7A6;
}

.form-input:focus {
  outline: none;
  border-color: #3E3229;
  box-shadow: 0 0 0 3px rgba(62, 50, 41, 0.1);
}

.form-submit {
  padding: 18px 30px;
  border-radius: 8px;
  font-family: 'Raleway', sans-serif;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-size: 0.9rem;
  cursor: pointer;
  background: #3E3229;
  color: #F2F0EB;
  border: 1px solid #3E3229;
  transition: all 0.3s;
  margin-top: 10px;
}

.form-submit:hover:not(:disabled) {
  background: #F2F0EB;
  color: #3E3229;
}

.form-submit:disabled {
  opacity: 0.7;
  cursor: wait;
}

/* --- МОБИЛЬНАЯ ВЕРСИЯ ФОРМЫ --- */
@media (max-width: 600px) {
  .form-overlay {
    padding: 20px;
    align-items: flex-end;
  }

  .form-content {
    width: 100%;
    max-width: none;
    border-radius: 20px 20px 0 0;
    padding: 40px 25px 60px 25px;
    max-height: 90vh;
    overflow-y: auto;
  }

  .form-title {
    font-size: 1.8rem;
  }

  .form-subtitle {
    font-size: 0.85rem;
    margin-bottom: 25px;
  }

  .application-form {
    gap: 20px;
  }

  .form-input {
    padding: 12px 15px;
    font-size: 0.95rem;
  }
}
</style>