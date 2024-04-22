$(document).ready(() => {
    $('#login-form').submit((e) => {
        e.preventDefault();

        const formData = JSON.stringify({"user":$('#user-id').val()});
        //const serializedData = $.param(formData);
        console.log(formData);
        $.ajax({
            type: 'POST',
            url: '/login',
            contentType: 'application/json',
            data: formData,
            success: function(response) {
                window.location.href = response.redirect;
                //$('body').html(response);
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