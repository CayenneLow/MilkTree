document.addEventListener("DOMContentLoaded", function(event) {
    var numJobs = 1;
    let cloneStatic = $("#job-card-1").clone();

    function addJobBox() {
        let clone = cloneStatic.clone();
        numJobs++;
        $("#job-list").append(clone);
        //clone.appendTo($("#job-list"));
        clone.prop("id", `job-card-${numJobs}`);
        var jobCardId = "#job-card-" + numJobs;
        $("#job-card-" + numJobs + ' #role').attr("name", numJobs + "-role");
        $("#job-card-" + numJobs + ' #description').attr("name", numJobs + "-description");
        $("#job-card-" + numJobs + ' #currency').attr("name", numJobs + "-currency");
        $("#job-card-" + numJobs + ' #budget-min').attr("name", numJobs + "-budget-min");
        $("#job-card-" + numJobs + ' #budget-max').attr("name", numJobs + "-budget-max");
        $("#job-card-" + numJobs + ' #1-select-skills').prop("id", numJobs + "-select-skills");
        console.log("#job-card-" + numJobs + " #" + numJobs + "-select-skills");
        $("#job-card-" + numJobs + " #" + numJobs + "-select-skills").select2({width:'style'});
        $("#job-card-" + numJobs + " #" + numJobs + "-select-skills").change(dropDown);
        $("#numJob").val(Number($("#numJob").val()) + 1);
    }
    
    $("#new-job-button").on('click', addJobBox);

    $("#" + numJobs + "-select-skills").select2();

    $("#" + numJobs + "-select-skills").on('change', dropDown);

    function dropDown() {
        var skill = $("#" + numJobs + "-select-skills option:selected").text();
        console.log(skill);
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

        var cur_value = $("#hidden-skills").val();
        console.log(cur_value);
        $("#hidden-skills").val(cur_value + "|" + skill);
        skillElement = document.createElement("p")
        skillElement.innerText = skill;
        $("#skill-results").append(skillElement);
    }
});
