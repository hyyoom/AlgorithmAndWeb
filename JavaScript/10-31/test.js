const formTag = document.querySelector('#follow_form');
formTag.addEventListener('submit', function(event){
  event.preventDefault();
});
console.log(formTag);
axios({
    //url : `/accounts/${}/follow/`,
    method : 'post',
    })
    .then((response)=>{
        console.log(response)
    })
    .catch((error)=>{
        console.log(error)
    })

document.querySelectorAll('.likes-forms')

const formTags = document.querySelectorAll('.likes-forms')

const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
formTags.forEach((formTag)=>{
  formTag.addEventListener('submit', function (event){
    event.defaultPrevented
    axios({
        url: `/articles/${}/likes/`,
        method: 'post',
        headers: { 'X-CSRFToken': csrftoken }
    })
  })
})

  
formTag.addEventListener('submit', function(event) {
  event.preventDefault();
  console.log(formTag.dataset);
  
  axios({
    url: `/accounts/${userId}/follow/`,
    method: 'post',
    headers: { 'X-CSRFToken': csrftoken }
  })
  .then((response) => {
    console.log(response);
  })
  .catch((error) => {
    console.log(error);
  });
});

const articleId = formTag.dataset.articleId
