function goBack() {
    window.history.back();
  }
  
  function gosign() {
    window.location.href = "http://127.0.0.1:8000/accounts/signup";
  }
  
  document.addEventListener('DOMContentLoaded', function () {
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const submitButton = document.querySelector('.loginsubmit input[type="submit"]');
    const form = document.getElementById('loginForm');
  
    function checkInputs() {
        const emailValue = emailInput.value.trim();
        const passwordValue = passwordInput.value.trim();
  
        if (emailValue && passwordValue) {
            submitButton.disabled = false;
            submitButton.classList.add('active');
        } else {
            submitButton.disabled = true;
            submitButton.classList.remove('active');
        }
    }
  
    emailInput.addEventListener('input', checkInputs);
    passwordInput.addEventListener('input', checkInputs);
  
    form.addEventListener('submit', function (e) {
        if (submitButton.disabled) {
            e.preventDefault(); // 폼이 제출되지 않도록 방지
        }
    });
  });