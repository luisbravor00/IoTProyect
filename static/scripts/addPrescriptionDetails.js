$(document).ready(() => {
    success: function(response) {
        console.log(response.success);
        $('#submit-prescription').click(function(e) {
            e.preventDefault();
    
            const formData = {
                prescriptionId: prescriptionId,
                medicineId: $('#medicine').val().split(',')[0],
                TimesPerDay: $('#TimesPerDay').val(),
                Dose: $('#dosage_form').val(),
            };
    
            $.ajax({
                type: 'POST',
                url: `${APP_URL}/prescriptionDetails/add`,
                contentType: 'application/json',
                data: JSON.stringify(formData),
                success: function(response) {
                    console.log('Prescription added successfully');
                    console.log(response);
                    alert(response.success);
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
    }
})