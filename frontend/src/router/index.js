/*
 * router/index.js
 *    Declare application routes and page components to render
 */

import { createRouter, createWebHistory } from 'vue-router';

import Dashboard from '../pages/Dashboard.vue';
import Class from '../pages/Class.vue';

const routes = [
  {
    path: '/',  
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/class', 
    name: 'Class',
    component: Class
  }
]

const router = createRouter({
  history: createWebHistory("/"),
  routes
})

export default router;
