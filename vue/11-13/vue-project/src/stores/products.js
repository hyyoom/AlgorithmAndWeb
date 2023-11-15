import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useProductStore = defineStore('products', () => {

  const productList = ref([
    {
      name : '상품 1',
      ImagePath : 'src/assets/product1.png',
      price : 10000,
      isFavorite : false,
    },
    {
      name : '상품 2',
      ImagePath : 'src/assets/product2.png',
      price : 20000,
      isFavorite : false,
    },
    {
      name : '상품 3',
      ImagePath : 'src/assets/product3.png',
      price : 30000,
      isFavorite : false,
    },
    {
      name : '상품 4',
      ImagePath : 'src/assets/product4.png',
      price : 40000,
      isFavorite : true,
    },
  ])


  const CountFavorite = computed(()=>{
    return productList.value.filter(item=>{return item.isFavorite}).length
  })

  // const ChoiseFavorite = function (todoId) {
  //   // todos 배열에서 몇번째 인덱스가 삭제되었는지 검색
  //   const index = todos.value.findIndex((todo) => todo.id === todoId)
  //   // 찾은 인덱스 값을 통해 배열에서 요소를 제거 후 원본 배열 업데이트
  //   todos.value.splice(index, 1)
  // }


  const isFavorite = computed(()=>{
    return productList.value.filter((item) => item.isFavorite===true);
  })

  return { productList, CountFavorite ,isFavorite }
}, {persist:true})
