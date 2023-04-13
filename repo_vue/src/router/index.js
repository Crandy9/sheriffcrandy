import { createRouter, createWebHistory, RouterView } from 'vue-router'
import store from '../store'
import { toast } from 'bulma-toast'

// import components/views here
import HomeView from '../views/HomeView.vue'
import FlpView from '../views/FlpView.vue'

// import i18n
import i18n from '@/i18n'


// russian demo: https://www.youtube.com/watch?v=ZLCMv_rdlsY
// indian demo: 
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes: [
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
      {
        path: '/thankyou',
        name: 'ThankYou',
        component: () => import('../views/ThankYouView.vue'),
        // prevent users from accessing the logout page if they are not logged in
        meta: {
          readyForCheckout: true
        }
      },
  ]
})

router.beforeEach((to,from,next) => {

  if (store.state.currentTrackPlaying) {
    if (to.name === 'Music') {
      // if navigating to the Music view, use the #slidebar element but wait for DOM to load view 
      // before trying to access the slidebar div, otherwise it will pass null to the mutation
      document.addEventListener('DOMContentLoaded', () => {
        store.commit('updateSlideBarBackground', document.getElementById('slidebar'))
      })

    } else {
      // otherwise, use the #persist-mini-slideBar element
      store.commit('updateSlideBarBackground', document.getElementById('persist-mini-slideBar'))
    }
  }
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
      message: this.$t('modals.pleaselogin'),
      type: 'is-danger',
      dismissible: true,
      pauseOnHover: true,
      duration: 2000,
      position: 'top-center',
      animate: { in: 'fadeIn', out: 'fadeOut' },
    })
    next({name:'LogIn', query: {to:to.path}});
  }

  // check if user is authenticated before proceeding to checkout page
  if (to.matched.some(record => record.meta.readyForCheckout) && !store.state.isAuthenticated){
    next({ path: '/' });
  }


  else {
    next()
  }
})

export default router
