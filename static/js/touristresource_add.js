const addImageFormBtn = document.querySelector("#add-image-form");
const submitFormBtn = document.querySelector('[type="submit"]');
const imageForm =document.getElementsByClassName("image-form");
const mainForm =document.querySelector("#listImage");
const totalForms = document.querySelector("#id_form-TOTAL_FORMS")
  
let formCount  = imageForm.length;
  
  
function updateNameAndIDObject(_element,_count){
    if (_element.nodeName!="#text" && _element.nodeName!="BR"){
        const formRegexName = RegExp('form-(\\d+)-','g');
        const formRegexID = RegExp('id_form-(\\d+)-','g');
        if(_element.hasAttribute('name')){
            var name = _element.getAttribute('name');
            name = name.replace(formRegexName,'form-'+_count+'-');
            _element.setAttribute('name',name);
        }
        if(_element.hasAttribute('id')){
            var id = _element.getAttribute('id'); 
            id = id.replace(formRegexID,'id_form-'+_count+'-');
            _element.setAttribute('id',id);
        }
    }
        
    var childs = _element.childNodes;
    for(var i =0;i<childs.length;i++){
        updateNameAndIDObject(childs[i],_count);
    } 
}
  
function updateForm(){
    let count = 0;
    for (let form of imageForm){
        updateNameAndIDObject(form,count);
        count++;
    }
}  
  

addImageFormBtn.addEventListener("click",function(event){
    event.preventDefault();
    const newImageForm = imageForm[0].cloneNode(true);
    const formRegex = RegExp('form-(\\d+)-','g');
    newImageForm.innerHTML = newImageForm.innerHTML.replace(formRegex,'form-'+formCount+'-');
    mainForm.insertBefore(newImageForm,addImageFormBtn);
    formCount++;
    totalForms.setAttribute('value',formCount);
});
  

mainForm.addEventListener("click",function(event){
        if(event.target.classList.contains("delete-image-form") && formCount>=2){
          event.preventDefault();
          event.target.parentElement.parentElement.remove();
          formCount--;
          totalForms.setAttribute('value',formCount);
          updateForm();
        }else if(event.target.classList.contains("delete-image-form-icon") && formCount>=2){
          event.preventDefault();
          event.target.parentElement.parentElement.parentElement.remove();
          formCount--;
          totalForms.setAttribute('value',formCount);
          updateForm();
        }
      });


function hasImageChange(_element){
    if ($(_element)[0].checked == true){
        $("#tabImages").show();
    }else{
        $("#tabImages").hide();
    }
}