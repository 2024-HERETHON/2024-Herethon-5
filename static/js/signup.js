function goBack() {
    window.history.back();
  }
  
  function toggleCheckboxes(event) {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    const isChecked = event.target.checked;
  
    checkboxes.forEach((checkbox, index) => {
        if (index !== 0) {
            checkbox.checked = isChecked;
        }
    });
  }
  
  document.addEventListener('DOMContentLoaded', function () {
  const emailInput = document.getElementById('email');
  const passwordInput = document.getElementById('password1');
  const repasswordInput = document.getElementById('password2');
  const nameInput = document.getElementById('name');
  const ageInput = document.getElementById('age');
  const sexInputs = document.querySelectorAll('input[name="gender"]');
  const lawInputs = document.querySelectorAll('input[name="law"]');
  const submitButton = document.querySelector('.signupsubmit input[type="submit"]');
  const form = document.getElementById('signupForm');
  
  function checkInputs() {
      const emailValue = emailInput.value.trim();
      const passwordValue = passwordInput.value.trim();
      const repasswordValue = repasswordInput.value.trim();
      const nameValue = nameInput.value.trim();
      const ageValue = ageInput.value.trim();
      const sexChecked = Array.from(sexInputs).some(input => input.checked);
      const lawChecked = Array.from(lawInputs).some(input => input.checked && input.value === 'use');
  
      if (emailValue && passwordValue && repasswordValue && nameValue && ageValue && sexChecked && lawChecked) {
          submitButton.disabled = false;
          submitButton.classList.add('active');
      } else {
          submitButton.disabled = true;
          submitButton.classList.remove('active');
      }
  }
  
  emailInput.addEventListener('input', checkInputs);
  passwordInput.addEventListener('input', checkInputs);
  repasswordInput.addEventListener('input', checkInputs);
  nameInput.addEventListener('input', checkInputs);
  ageInput.addEventListener('input', checkInputs);
  sexInputs.forEach(input => input.addEventListener('change', checkInputs));
  lawInputs.forEach(input => input.addEventListener('change', checkInputs));
  
  form.addEventListener('submit', function (e) {
      if (submitButton.disabled) {
          e.preventDefault(); // 폼이 제출되지 않도록 방지
      }
  });
  });
  
  document.addEventListener('DOMContentLoaded', function () {
  const emailInput = document.getElementById('email');
  const passwordInput = document.getElementById('password1');
  const repasswordInput = document.getElementById('password2');
  const nameInput = document.getElementById('name');
  const ageInput = document.getElementById('age');
  const sexInputs = document.querySelectorAll('input[name="gender"]');
  const lawInputs = document.querySelectorAll('input[name="law"]');
  const submitButton = document.querySelector('.signupsubmit input[type="submit"]');
  const form = document.getElementById('signupForm');
  const passwordMatchMessage = document.getElementById('password-match');
  const passwordMatchSuccessMessage = document.getElementById('password-match-success');
  
  function checkInputs() {
      const emailValue = emailInput.value.trim();
      const passwordValue = passwordInput.value.trim();
      const repasswordValue = repasswordInput.value.trim();
      const nameValue = nameInput.value.trim();
      const ageValue = ageInput.value.trim();
      const sexChecked = Array.from(sexInputs).some(input => input.checked);
      const lawChecked = Array.from(lawInputs).some(input => input.checked && input.value === 'use');
  
      if (passwordValue !== repasswordValue) {
          passwordMatchMessage.style.display = 'block';
          passwordMatchSuccessMessage.style.display = 'none';
      } else if (passwordValue === repasswordValue && passwordValue !== "") {
          passwordMatchMessage.style.display = 'none';
          passwordMatchSuccessMessage.style.display = 'block';
      } else {
          passwordMatchMessage.style.display = 'none';
          passwordMatchSuccessMessage.style.display = 'none';
      }
  
      if (emailValue && passwordValue && repasswordValue && nameValue && ageValue && sexChecked && lawChecked && passwordValue === repasswordValue) {
          submitButton.disabled = false;
          submitButton.classList.add('active');
      } else {
          submitButton.disabled = true;
          submitButton.classList.remove('active');
      }
  }
  
  emailInput.addEventListener('input', checkInputs);
  passwordInput.addEventListener('input', checkInputs);
  repasswordInput.addEventListener('input', checkInputs);
  nameInput.addEventListener('input', checkInputs);
  ageInput.addEventListener('input', checkInputs);
  sexInputs.forEach(input => input.addEventListener('change', checkInputs));
  lawInputs.forEach(input => input.addEventListener('change', checkInputs));
  
  form.addEventListener('submit', function (e) {
      if (submitButton.disabled) {
          e.preventDefault(); // 폼이 제출되지 않도록 방지
      }
  });
  });