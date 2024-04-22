const registerButton = document.getElementById("register");
const loginButton = document.getElementById("login");
const forgotPass = document.getElementById("forgotPasswordButton");
const container = document.getElementById("container");

registerButton.addEventListener("click", () => {
  container.classList.add("right-panel-active");
});

loginButton.addEventListener("click", () => {
  container.classList.remove("right-panel-active");
});

forgotPass.addEventListener("click", () => {
  container.classList.add("left-panel-active");
});


/*const forgotPasswordContainer = document.querySelector(".forgot-password-container");
const forgotPasswordButton = document.getElementById("forgotPasswordButton");
forgotPasswordButton.addEventListener("click", (e) => {
  e.preventDefault(); 
  container.addEventListener("transitionend", () => {
    container.classList.add("right-panel-active");
  }, { once: true }); 
  container.classList.remove("right-panel-active");
});*/
/*const forgotPasswordButton = document.getElementById("forgotPasswordButton");
const forgotPasswordContainer = document.querySelector(".forgot-password-container");

forgotPasswordButton.addEventListener("click", (e) => {
  e.preventDefault(); // Prevent the default link behavior

  // Show the forgot password form
  forgotPasswordContainer.style.display = "block";
});*/

document.addEventListener("DOMContentLoaded", () => {
  const forgotPasswordButton = document.getElementById("forgotPasswordButton");
  const forgotPasswordContainer = document.querySelector(".forgot-password-container");

  forgotPasswordButton.addEventListener("click", (e) => {
    e.preventDefault(); 
    if (forgotPasswordContainer.style.display === "block") {
      forgotPasswordContainer.style.display = "none";
    } else {
      forgotPasswordContainer.style.display = "block";
    }
  });
});
