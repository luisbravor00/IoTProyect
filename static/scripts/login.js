$(document).ready(() => {
    $('#login-form').submit((e) => {
        e.preventDefault();

        const formData = $('#login-form').serialize();
        

        $.ajax({
            type: 'POST',
            url: '/login',
            contentType: 'application/json',
            data: formData,
            success: function(response) {
                window.location.href = '/login.html';
            },
            error: (err) => {
                try {
                    const errorMessage = err.responseJSON.message;
                    const error = $('#error');
                    error.text(errorMessage);
                } catch (e) {
                    const error = $('#error');
                    error.text("Something went wrong");
                }
            }
        })
    })
})