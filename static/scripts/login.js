$(document).ready(() => {
    $('#login-form').submit((e) => {
        e.preventDefault();

        // const formData = $('#user-id').val();
        const formData = {"user":$('#user-id').val()};
        const serializedData = $.param(formData);
        console.log(formData);
        $.ajax({
            type: 'GET',
            url: '/login',
            contentType: 'application/json',
            data: formData,
            success: function(response) {
                console.log(response);
                // window.location.href = '/login.html';
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