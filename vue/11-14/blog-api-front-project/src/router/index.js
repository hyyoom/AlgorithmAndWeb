import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import PostListView from '@/views/PostListView.vue'
import CategoryView from '@/views/CategoryView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Main',
      component: MainView
    },
    {
      path: '/postlist',
      name: 'PostList',
      component: PostListView
    },
    {
      path: '/createcategory',
      name: 'category',
      component: CategoryView
    },
  ]
})

export default router
