<template>
  <div>
    <hr>
    <span :class="{ completed : todo.isCompleted}">
      {{ todo.content }}
    </span>
    <hr>
  </div>
</template>

<script setup>
  defineProps({
    todo:Object
  })
</script>

<style scoped>
  .completed{
    text-decoration: line-through;
  }
</style>