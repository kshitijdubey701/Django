// static/js/validation.js

// static/js/internship.js

document.getElementById('internshipForm').addEventListener('submit', function(event) {
    var fullName = document.getElementById('id_full_name').value.trim();
    var email = document.getElementById('id_email').value.trim();
    var whatsapp = document.getElementById('id_whatsapp_number').value.trim();
    var collegeName = document.getElementById('id_college_name').value.trim();
    var qualification = document.getElementById('id_qualification').value.trim();
    var lastQualificationYear = document.getElementById('id_last_qualification_year').value.trim();
    var resume = document.getElementById('resume').files.length; // Check if a file is uploaded

    if (fullName === "" || email === "" || whatsapp === "" || collegeName === "" || qualification === "" || lastQualificationYear === "" || resume === 0) {
        alert("Please fill out all required fields and upload your resume.");
        event.preventDefault();  // Stop the form from submitting
    }
});
