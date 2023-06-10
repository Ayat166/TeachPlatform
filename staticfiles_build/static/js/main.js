function setFormMassage(formElement , type, massage){
    const massageElement = formElement.querySelector(".form__massage");

    massageElement.textContent =massage;
    massageElement.classList.remove("form__massage--success","form__massage--error");
    massageElement.classList.add(`form__massage--${type}`);
}
function setInputError(inputElement, massage){
    inputElement.classList.add("form__input--error");
    inputElement.parentElement.querySelector(".form__input-error-massage").textContent=massage;

}
function clearInputError(inputElement)
{
    inputElement.classList.remove("form__input--error");
    inputElement.parentElement.querySelector(".form__input-error-massage").textContent="";

}
document.addEventListener("DOMContentLoaded",()=>{
    const loginForm = document.querySelector("#login");
    const createAccountForm = document.querySelector("#createAccount");

    document.querySelector("#linkCreateAccount").addEventListener("click",e =>{
       e.preventDefault();
        loginForm.classList.add("form--hidden");
       createAccountForm.classList.remove("form--hidden");
    });
    document.querySelector("#linkLogin").addEventListener("click",e=>{
        e.preventDefault();       
        loginForm.classList.remove("form--hidden");
        createAccountForm.classList.add("form--hidden");
     });
     loginForm.addEventListener("submit",e=>{
        e.preventDefault();

        // perform your AJAX/Fetch login

        setFormMassage(loginForm,"error","Invalid username/password compination");
     });
     document.querySelectorAll(".form__input").forEach(inputElement=>
        {
            inputElement.addEventListener("blur",e=>{
                if(e.target.id==="signupUsername"&& e.target.value.length>0&&e.target.value.length<10)
                {setInputError(inputElement,"Username must be at least 10 characters in length");}
                if(e.target.id==="Pass"&& e.target.value.length>0&&e.target.value.length<10)
                {setInputError(inputElement,"Password must be at least 10 characters in length");}
                
            });

            inputElement.addEventListener("input",e=>{
                clearInputError(inputElement);
            });
        });
});