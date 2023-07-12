window.onload = function () {
    document.getElementById("testElement").innerHTML = "JavaScript is working!";

    const datepickerWithLimits = document.getElementById('datepicker-with-limits');
    new Datepicker(datepickerWithLimits, {
        min: new Date(2020, 5, 10),
        max: new Date(2023, 5, 20)
    });
}
    function confirmDelete (game_name, formId) { // get the game_name & formId parameters
        // show a confirm delete modal to the user to confirm deletion of their review
        const deleteReview = confirm("Are you sure you would like to delete your " + game_name + " review?")
        console.log("Submitting form with ID:", formId);
        if (deleteReview == true) {
            // grab the form id and call the submit from the form to delete the review
            document.getElementById(formId).submit();
        }
    }
