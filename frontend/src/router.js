import { createRouter, createWebHistory } from 'vue-router'
import ItemsView from './views/ItemsView.vue'
import AboutView from './views/AboutView.vue'

const routes = [
  { path: '/', redirect: '/items' }, // Редирект с главной на товары
  { path: '/items', name: '/items', component: ItemsView },
  { path: '/about', name: '/about', component: AboutView }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    return { top: 0, behavior: 'smooth' }
  }
})

export default router