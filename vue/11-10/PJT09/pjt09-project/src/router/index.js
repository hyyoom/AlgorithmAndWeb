import { createRouter, createWebHistory } from 'vue-router'
import CartView from '@/views/CartView.vue';
import HomeView from '@/views/HomeView.vue';
import ProductDetailView from '@/views/ProductDetailView.vue';


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/cart',
      name: 'cart',
      component: CartView
    },
    {
      path: '/detail/:productId',
      name: 'productDetail',
      component: ProductDetailView
    },
  ]
})

export default router
