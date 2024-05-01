$(document).ready(() => {
    const urlParams = new URLSearchParams(window.location.search);
    const doctorId = urlParams.get('doctor_id');
        $.ajax({
            type: 'GET',
            url: `${APP_URL}/doctorInterface/${doctorId}`,
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
