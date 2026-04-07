<template>
  <div class="home-page">
    <!-- Форма входа по центру сверху -->
    <div class="user-entry russo-one-regular">
      <div>USERNAME</div>
      <input type="text" v-model="username" @keyup.enter="handleLogin">
      <div>PASSWORD</div>
      <input type="password" v-model="password" @keyup.enter="handleLogin">
      <div style="cursor: pointer;" @click="handleLogin" :class="{ loading: loading }">
        {{ loading ? 'LOGGING IN...' : 'LOGIN' }}
      </div>
    </div>

    <!-- Контент с анимацией -->
    <div class="content">
      <div class="content-header">
        <div class="company-name russo-one-regular">BLUE BOX</div>
        <div class="content-header-text russo-one-regular">
          Blue box it is a platform for managing and optimizing your production.
        </div>
        <div class="red-bar"></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const username = ref('')
const password = ref('')
const loading = ref(false)

const handleLogin = async () => {
  loading.value = true

  // Здесь будет логика авторизации
  console.log('Login attempt:', username.value, password.value)

  // Имитация запроса к API
  setTimeout(() => {
    loading.value = false
    // router.push('/dashboard')
  }, 1000)
}
</script>

<style scoped>
.home-page {
  height: 100vh;
  width: 100%;
  overflow: hidden;
  position: relative;
}

.russo-one-regular {
  font-family: "Russo One", serif;
  font-weight: 400;
  font-style: normal;
}

.user-entry {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 5vh;
  position: absolute;
  top: 5%;
  left: 50%;
  transform: translateX(-50%);
  gap: 5px;
  font-size: 12px;
  color: #9DB1CC;
  z-index: 10;
}

.user-entry input {
  margin-bottom: 5px;
  padding: 5px 10px;
  border: 1px solid #9DB1CC;
  border-radius: 3px;
  background: rgba(255, 255, 255, 0.1);
  color: #9DB1CC;
}

.user-entry input:focus {
  outline: none;
  border-color: #fff;
}

.user-entry div:last-child {
  margin-top: 10px;
  padding: 5px 20px;
  background-color: #9DB1CC;
  color: #fff;
  border-radius: 3px;
  transition: all 0.3s;
}

.user-entry div:last-child:hover {
  background-color: #7a8ea8;
  transform: scale(1.05);
}

.user-entry div:last-child.loading {
  background-color: #6c757d;
  cursor: wait;
  opacity: 0.7;
}

.content {
  margin-top: 70vh;
  user-select: none;
  transform: translateX(-100%);
  animation: slideIn 0.5s forwards;
}

@keyframes slideIn {
  to {
    transform: translateX(0);
  }
}

.company-name {
  font-size: 48px;
  padding-left: 50px;
  color: #9DB1CC;
  opacity: 0.9;
}

.content-header-text {
  font-size: 24px;
  padding-left: 50px;
  color: #9DB1CC;
  opacity: 0.9;
  margin-top: 20px;
}

.red-bar {
  width: 90%;
  height: 20px;
  background-color: red;
  margin-top: 20px;
  margin-left: 50px;
}

@media (max-width: 768px) {
  .company-name {
    font-size: 32px;
    padding-left: 20px;
  }

  .content-header-text {
    font-size: 18px;
    padding-left: 20px;
  }

  .red-bar {
    margin-left: 20px;
    height: 10px;
  }

  .user-entry {
    width: 80%;
  }
}
</style>