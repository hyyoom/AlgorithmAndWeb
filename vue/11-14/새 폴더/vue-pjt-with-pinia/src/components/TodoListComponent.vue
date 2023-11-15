<template>
  <div>
    <h1>여기에 Todo 표시</h1>
    <TodoListItemComponent
    v-for="todo of store.todos"
    :key="todo.id"
    :todo="todo"/>
  </div>
</template>

<script setup>
import TodoListItemComponent from '@/components/TodoListItemComponent.vue';
import { useTodoStore } from '@/stores/todo'
const store = useTodoStore()
</script>
<style scoped>
</style>