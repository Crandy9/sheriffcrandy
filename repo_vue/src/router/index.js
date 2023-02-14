import { createRouter, createWebHistory } from 'vue-router'
// import components/views here
import HomeView from '../views/HomeView.vue'
import FlpView from '../views/FlpView.vue'
// add custom views here
const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/music',
    name: 'Music',
    // can also import components/views here using Arrow function expressions
    component: () => import('../views/MusicView.vue')
  },
  {
    path: '/flps',
    name: 'Flps',
    component: FlpView
  },
  {
    path: '/contact',
    name: 'Contact',
    component: () => import('../views/ContactView.vue')
  },
  {
    path: '/tools',
    name: 'Tools',
    component: () => import('../views/ToolsView.vue')
  },
  {
    path: '/bio',
    name: 'Bio',
    component: () => import('../views/BioView.vue')
  },
  {
    path: '/cart',
    name: 'Cart',
    component: () => import('../views/CartView.vue')
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: () => import('../views/SignUpView.vue')
  },
  {
    path: '/login',
    name: 'LogIn',
    component: () => import('../views/LogInView.vue')
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
