$(document).ready(() => {
    $('#sumbit-patient').click(function(e) {
        e.preventDefault();

        const formData = {
            Name: $('#name').val(),
            Last_Name: $('#last_name').val(),
            Address: $('#address').val(),
            Age: $('#age').val(),
            Phone: $('#phone').val(),
            Email: $('#email').val()
        };

        $.ajax({
            type: 'POST',
            url: `${APP_URL}/patients/add`,
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: function(response){
                const formData2 = {
                    ID_Doctor: $('#doctor-id').data('id'),
                    ID_Patient: response.newId,
                    Date_Prescribed: $('#date').val()
                };
                $.ajax({
                    type: 'POST',
                    url: `${APP_URL}/prescriptions/add`,
                    contentType: 'application/json',
                    data: JSON.stringify(formData2),
                    success: function(response2) { 
                        console.log('Patient added successfully');
                        console.log(response2.success);
                        alert('Patient added successfully, please refresh page to view them.');
                    },
                    error: function(err) {
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
            },
            error: function(err) {
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