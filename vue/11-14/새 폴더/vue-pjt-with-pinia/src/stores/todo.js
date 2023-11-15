import { defineStore } from "pinia";
import { computed,ref } from "vue";

export const useTodoStore = defineStore('todo',()=>{
  const todos = ref([])

  const completedTodos = computed(()=>{
    return todos.value.filter((todo)=>{
      return todo.isCompleted
    })
  })
  function setTodos(todo){
    todos.value = todo
  }

  function addTodo(todo){
    todos.value.push(todo)
  }
  return { todos, completedTodos, addTodo, setTodos }
})