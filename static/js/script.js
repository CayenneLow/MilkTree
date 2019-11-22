document.addEventListener("DOMContentLoaded", function(event) {
    let numJobs = 1;
    let cloneStatic = $("#job-card-1").clone();
    
    $("#new-job-button").on('click', addJobBox);
    
    $("#" + numJobs + "-select-skills").select2({width:'style'});
    
    $("#" + numJobs + "-select-skills").change(function(e) {
        dropDown(e);
    });
    
    function addJobBox() {
        let clone = cloneStatic.clone();
        numJobs++;
        $("#job-list").append(clone);
        //clone.appendTo($("#job-list"));
        clone.prop("id", `job-card-${numJobs}`);
        var jobCardId = "#job-card-" + numJobs;
        $(jobCardId + ' #role').attr("name", numJobs + "-role");
        $(jobCardId + ' #description').attr("name", numJobs + "-description");
        $(jobCardId + ' #budget-min').attr("name", numJobs + "-budget-min");
        $(jobCardId + ' #budget-max').attr("name", numJobs + "-budget-max");
        $("#numJob").val(Number($("#numJob").val()) + 1);
        $("#job-card-" + numJobs + ' #currency').attr("name", numJobs + "-currency");
        $(jobCardId + '  #1-select-skills').prop("id", numJobs + "-select-skills");
        $(jobCardId + " #" + numJobs + "-select-skills").select2({width:'style'});
        $(jobCardId + " #" + numJobs + "-select-skills").change(function (e) {
            dropDown(e);
        });
    }
   
    function dropDown(event) {
        let index = $(event.delegateTarget).prop("id").split("-")[0];
        var skill = $("#" + index + "-select-skills option:selected").text();
        if (skill == "Select Skill"){
            return;
        }
        let alreadyThere = 0;
        $('#job-card-' + index + ' #skill-results').children('li').each(function () {
            if (skill == this.innerText) {
                alreadyThere = 1;
                return;
            }
        });
        if (alreadyThere) {
            return;
        }

        var cur_value = $("#hidden-skills").val();
        console.log(cur_value);
        $("#hidden-skills").val(cur_value + "|" + skill);
        skillElement = document.createElement("li")
        skillElement.className = "badge badge-warning list-inline-item"
        skillElement.innerText = skill;
        $('#job-card-' + index + ' #skill-results').append(skillElement);
    }
});
