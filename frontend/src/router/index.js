import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../pages/HomePage.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage,
    meta: {
      title: 'Blue Box - Login'
    }
  },
  {
    path: '/index',
    name: 'index',
    component: HomePage,
    meta: {
      title: 'Blue Box - Dashboard'
    }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from) => {
  document.title = to.meta.title || 'Blue Box'
  return true
})

export default router