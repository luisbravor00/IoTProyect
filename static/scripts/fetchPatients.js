$(document).ready(() => {
    const doctor_id = $('#doctor-id').data('id');
        $.ajax({
            type: 'GET',
            url: `${APP_URL}/doctorInterface/${doctor_id}`,
            contentType: 'application/json',
            success: function(response) {
                const patientList = $('#patients');
                patientList.empty();

                response.forEach(function(patient) {
                    const patientEntry = $('<li>').text(patient.patientId + ' ' +  patient.name + ' ' + patient.last_name + ' ' + patient.age + ' ' + patient.phone);
                    patientList.append(patientEntry); 
                });
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
