document.addEventListener("DOMContentLoaded", function(event) {
    // function addJobBox(){
    //     // const lastJob = document.getElementById('last-job')
    //
    //     var newJob = "<div class=\"card\">\
    //     <label for=\"jobs\" class=\"card-header w-100\">Job</label>\
    //     <ul class=\"list-group list-group-flush\">\
    //         <div class=\"job-info-box\">\
    //             <li class=\"list-group-item\">\
    //                 <label for=\"role\">Role</label>\
    //                 <input class=\"form-control\" type=\"text\" name=\"{{jobs|length|string}}-role\" />\
    //             </li>\
    //             <li class=\"list-group-item\">\
    //                 <label for=\"description\">Description</label>\
    //                 <textarea class=\"form-control\" type=\"text\" name=\"{{jobs|length|string}}-description\"></textarea>\
    //             </li>\
    //             <li class=\"list-group-item\">\
    //                 <label for=\"budget\">Budget</label>\
    //                 <input class=\"form-control\" type=\"number\" name=\"{{jobs|length|string}}-budget\" />\
    //             </li>\
    //             <li class=\"list-group-item\">\
    //                 <select class=\"custom-select\">\
    //                     <option selected> Currency </option>\
    //                     <option value=\"AUD\">AUD</option>\
    //                     <option value=\"USD\">USD</option>\
    //                     <option value=\"EUR\">EUR</option>\
    //                 </select>\
    //             </li>\
    //             <li class=\"list-group-item\">\
    //                 <select class=\"custom-select\">\
    //                     <option selected> Skills </option>\
    //                     <option value=\"AUD\">SEO</option>\
    //                     <option value=\"USD\">Digital Marketing</option>\
    //                     <option value=\"EUR\">Front-end web developemtn</option>\
    //                 </select>\
    //             </li>\
    //         </div>\
    //     </li>\
    // </div>"
    //
    //     $("#job-list").append(newJob)
    // }

    var numJobs = 1;
    function addJobBox() {
        numJobs++;
        let clone = $("#job-card-1").clone();
        $("#job-list").append(clone);
        //clone.appendTo($("#job-list"));
        clone.prop("id", `job-card-${numJobs}`);
        var jobCardId = "#job-card-" + numJobs;
        $("#job-card-" + numJobs + ' #role').attr("name", numJobs + "-role");
        $("#job-card-" + numJobs + ' #description').attr("name", numJobs + "-description");
        $("#job-card-" + numJobs + ' #budget-min').attr("name", numJobs + "-budget-min");
        $("#job-card-" + numJobs + ' #budget-max').attr("name", numJobs + "-budget-max");

    }

    const newJobButton = document.getElementById('new-job-button');

    newJobButton.addEventListener("click", addJobBox);

    $("#select-skills").select2();

    $("#select-skills").on('change', function() {
        var skill = $("#select2-select-skills-container").text();
        if (skill == "Select Skill"){
            return;
        }
        var alreadyThere = 0;
        $('#skill-results').children('p').each(function () {
            if (skill == this.innerText) {
                alreadyThere = 1;
            }
        });
        if (alreadyThere) {
            return;
        }

        skillElement = document.createElement("p")
        skillElement.innerText = skill;
        $("#skill-results").append(skillElement);
    });

});
