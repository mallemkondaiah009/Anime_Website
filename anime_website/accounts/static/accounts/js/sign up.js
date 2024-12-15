document.addEventListener('DOMContentLoaded', () => {
    const signupForm = document.getElementById('signupForm');

    // Client-Side Validation
    signupForm.addEventListener('submit', (event) => {
        const password = document.querySelector('#id_password1').value;
        const confirmPassword = document.querySelector('#id_password2').value;

        // Validate Password Match
        if (password !== confirmPassword) {
            alert('Passwords do not match!');
            event.preventDefault();
        }

        // Additional Validations (Example: Phone Number)
        const phoneNumber = document.querySelector('#id_phone_number').value;
        const phonePattern = /^[0-9]{10}$/;
        if (!phonePattern.test(phoneNumber)) {
            alert('Please enter a valid 10-digit phone number.');
            event.preventDefault();
        }
    });
});
