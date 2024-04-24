$(document).ready(function () {
    $('#contact-form').on("submit", function (event) {
        event.preventDefault();
        const nombre = $("#clientName").val();
        const email = $("#emailField").val();
        const message = $("#messageField").val();
        const validation = $("#checkTyC").is(":checked");
        let formValues = {
                "name":nombre,
                "email":email,
                "message":message,
                "validation":validation
        }
        if(formValues['validation']){
            $.ajax({
                type: 'POST',
                url: '/contact',
                contentType: 'application/json',
                data: JSON.stringify(formValues),
                success: function(response) {
                    alert('Your message have been received');
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
        }else{
            $('#TyC-Alert').removeClass("visually-hidden");
            alert('Acepta terminos y condiciones para continuar');
        }
    });
});