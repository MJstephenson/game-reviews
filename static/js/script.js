window.onload = function () {
    document.getElementById("testElement").innerHTML = "JavaScript is working!";

    const datepickerWithLimits = document.getElementById('datepicker-with-limits');
    new Datepicker(datepickerWithLimits, {
        min: new Date(2020, 5, 10),
        max: new Date(2023, 5, 20)
    });

    
}

