$(document).ready(() => {
    $('#sumbit-patient').click(function(e) {
        e.preventDefault();

        const formData = {
            Name: $('#name').val(),
            Last_Name: $('#last_name').val(),
            Address: $('#address').val(),
            Age: parseInt($('#age').val()),
            Phone: $('#phone'.val()),
            Email: $('#email').val()
        };

        $.ajax({
            type: 'POST',
            url: `${APP_URl}/patients/add`,
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: function(response){
                
            }
        })
    })
})