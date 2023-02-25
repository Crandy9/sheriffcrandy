import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'
import { toast } from 'bulma-toast'

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
    component: () => import('../views/SignUpView.vue'),
    // prevent users from accessing the signup page if they are already logged in
    meta: {
      requireLogout: true
    }
  },
  {
    path: '/login',
    name: 'LogIn',
    component: () => import('../views/LogInView.vue'),
    // prevent users from accessing the login page if they are already logged in
    meta: {
      requireLogout: true
    }
  },
  {
    path: '/logout',
    name: 'LogOut',
    component: () => import('../views/LogOutView.vue'),
    // prevent users from accessing the logout page if they are not logged in
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/myaccount',
    name: 'MyAccount',
    component: () => import('../views/MyAccountView.vue'),
    // prevent users from accessing the logout page if they are not logged in
    meta: {
      requiresAuthAccount: true
    }
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to,from,next) => {
  // prevent unauthenticated users from accessing logout view. Redirect to homepage
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ path: '/' });
  } 
  // prevent authenticated users from accessing login/signup views. Redirect to homepage
  if (to.matched.some(record => record.meta.requireLogout) && store.state.isAuthenticated){
    next({ path: '/' });
  }
  // prevent unauthenticated users from accessing MyAccount view. Redirect to login
  if (to.matched.some(record => record.meta.requiresAuthAccount) && !store.state.isAuthenticated){

    toast({
      message: 'Please login',
      type: 'is-danger',
      dismissible: true,
      pauseOnHover: true,
      duration: 3000,
      position: 'top-center',
      animate: { in: 'fadeIn', out: 'fadeOut' },
    })
    next({name:'LogIn', query: {to:to.path}});
  }
  else {
    next()
  }
})

export default router
