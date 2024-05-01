$(document).ready(() => {
    //const queryString = window.location.search;
    //const urlParams = new URLSearchParams(queryString);

    $('#submit-prescription').click(function(e) {
        e.preventDefault();

        const formData = {
            ID_Doctor: $('#doctor-id').data('id'),
            ID_Patient: parseInt($('#patient').val()),
            Date_Prescribed: $('#date').val()
        };

        $.ajax({
            type: 'POST',
            url: `${APP_URL}/prescriptions/add`,
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: function(response) {
                const formData2 = {
                    ID_Prescription: response.newId,
                    ID_Medication: parseInt($('#medicine').val().split(',')[0]),
                    Dose: parseInt($('#dosage_form').val()),
                    Times_Per_Day: parseInt($('#TimesPerDay').val())
                };
                $.ajax({
                    type: 'POST',
                    url: `${APP_URL}/prescriptionDetails/add`,
                    contentType: 'application/json',
                    data: JSON.stringify(formData2),
                    success: function(response2) {
                        console.log('Prescription added successfully');
                        console.log(response2);
                        alert(response2.success);
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