document.addEventListener("DOMContentLoaded", function(event) {
    const jobItem = $('.job-item')[0];

    function addJobBox(){
        // const lastJob = document.getElementById('last-job')

        var newJob = "<li class=\"job-item\"><div class=\"job-info-box\">\
                <label for=\"role\">Role</label>\
                <input type=\"text\" name=\"{{jobs|length|string}}-role\" />\
                <label for=\"description\">Description</label>\
                <input type=\"text\" name=\"{{jobs|length|string}}-description\" />\
                <label for=\"budget\">Budget</label>\
                <input type=\"number\" name=\"{{jobs|length|string}}-budget\" />\
                <label for=\"currency\">Currency</label>\
                <select name=\"currency\">\
                  <option value=\"AUD\">AUD</option>\
                  <option value=\"USD\">USD</option>\
                  <option value=\"EUR\">EUR</option>\
                </select>\
                <label for=\"skills\">Skills</label>\
                <select name=\"skills\">\
                  <option value=\"AUD\">SEO</option>\
                  <option value=\"USD\">Digital Marketing</option>\
                  <option value=\"EUR\">Front-end web developemtn</option>\
                </select>\
            </div>\
        </li>"

        $("#job-list").append(newJob)
    }

    const newJobButton = document.getElementById('new-job-button');

    newJobButton.addEventListener("click", addJobBox);

    $("#select-skills").select2();

    $("#select-skills").on('change', function() {
        console.log("IN HERE");
        var skill = $("#select2-select-skills-container").text();
        console.log("SKILL")
        console.log(skill);
        skillElement = document.createElement("p")
        skillElement.innerText = skill;
        $("#skill-results").append(skillElement);
    });

});
