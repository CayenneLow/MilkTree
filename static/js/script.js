document.addEventListener("DOMContentLoaded", function(event) {
    function addJobBox(){
        // const lastJob = document.getElementById('last-job')

        var newJob = "<div class=\"card\" id=\"job-list\">\
        <label for=\"jobs\" class=\"card-header w-100\">Job</label>\
        <ul class=\"list-group list-group-flush\">\
            <div class=\"job-info-box\">\
                <li class=\"list-group-item\">\
                    <label for=\"role\">Role</label>\
                    <input class=\"form-control\" type=\"text\" name=\"{{jobs|length|string}}-role\" />\
                </li>\
                <li class=\"list-group-item\">\
                    <label for=\"description\">Description</label>\
                    <textarea class=\"form-control\" type=\"text\" name=\"{{jobs|length|string}}-description\"></textarea>\
                </li>\
                <li class=\"list-group-item\">\
                    <label for=\"budget\">Budget</label>\
                    <input class=\"form-control\" type=\"number\" name=\"{{jobs|length|string}}-budget\" />\
                </li>\
                <li class=\"list-group-item\">\
                    <select class=\"custom-select\">\
                        <option selected> Currency </option>\
                        <option value=\"AUD\">AUD</option>\
                        <option value=\"USD\">USD</option>\
                        <option value=\"EUR\">EUR</option>\
                    </select>\
                </li>\
                <li class=\"list-group-item\">\
                    <select class=\"custom-select\">\
                        <option selected> Skills </option>\
                        <option value=\"AUD\">SEO</option>\
                        <option value=\"USD\">Digital Marketing</option>\
                        <option value=\"EUR\">Front-end web developemtn</option>\
                    </select>\
                </li>\
            </div>\
        </li>\
    </div>"

        $("#job-list").append(newJob)
    }

    const newJobButton = document.getElementById('new-job-button');

    newJobButton.addEventListener("click", addJobBox);

});
