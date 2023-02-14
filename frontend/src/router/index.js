import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '../pages/Dashboard.vue'
import Test from '../pages/Test.vue'
import Login from '../components/Login.vue'

const routes = [
  {
    path: '/',  
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/test', 
    name: 'Test',
    component: Test
  }
]

const router = createRouter({
  history: createWebHistory("/"),
  routes
})

export default router
