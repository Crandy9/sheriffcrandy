import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

// add custom views here
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/music',
    name: 'music',
    component: () => import('../views/MusicView.vue')
  },
  {
    path: '/flps',
    name: 'flps',
    component: () => import('../views/FlpView.vue')
  },
  {
    path: '/contact',
    name: 'contact',
    component: () => import('../views/ContactView.vue')
  },
  {
    path: '/tools',
    name: 'tools',
    component: () => import('../views/ToolsView.vue')
  },
  {
    path: '/bio',
    name: 'bio',
    component: () => import('../views/BioView.vue')
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
