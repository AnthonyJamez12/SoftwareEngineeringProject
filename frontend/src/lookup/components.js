export function loadUploads(callback){
    const xhr = new XMLHttpRequest()        // xhr = SomeClass() its a Class in JavaScript
    const method = 'GET'
    const url = "http://localhost:8000/api/main"
    const responseType = "json"
    xhr.responseType = responseType 
    xhr.open(method, url)
    xhr.onload = function(){
      callback(xhr.response, xhr.status)
    }
    xhr.onerror = function(e){
      console.log(e)
      callback({"message": "The request was an error"}, 400)
    }
    xhr.send()
  }