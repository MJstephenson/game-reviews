    function confirmDelete (game_name, formId) { // get the game_name & formId parameters
        // show a confirm delete modal to the user to confirm deletion of their review
        const deleteReview = confirm("Are you sure you would like to delete your " + game_name + " review?");
        if (deleteReview == true) {
            // grab the form id and call the submit from the form to delete the review
            document.getElementById(formId).submit();
        }
    }
