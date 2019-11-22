document.addEventListener("DOMContentLoaded", function(event) {
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
        $("#job-card-" + numJobs + " #select-skills").select2();
        $("#job-card-" + numJobs + " #select-skills").change(dropDown);
    }
    
    $("#new-job-button").on('click', addJobBox);

    $("#select-skills").select2();

    $("#select-skills").on('change', dropDown);

    function dropDown() {
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
    }
});
