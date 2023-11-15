import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import VideoSearchView from '@/views/VideoSearchView.vue'
import VideoLaterView from '@/views/VideoLaterView.vue'
import VideoDetailView from '@/views/VideoDetailView.vue'



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/search',
      name: 'VideoSearch',
      component: VideoSearchView
    },
    {
      path: '/detail',
      name: 'VideoDetail',
      component: VideoDetailView
    },
    {
      path: '/later',
      name: 'VideoLater',
      component: VideoLaterView
    },
  ]
})

export default router
