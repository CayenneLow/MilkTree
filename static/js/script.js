document.addEventListener("DOMContentLoaded", function(event) {

    function addJobBox(){
        const jobs = document.getElementsByClassName('job-item');
        const lastJob = jobs[jobs.length - 1];
        const newJob = document.createElement('li');
        newJob.innerText = "I'm a new job yooo";
        lastJob.appendChild(newJob)
    }

    const newJobButton = document.getElementById('new-job-button');

    newJobButton.addEventListener("click", addJobBox);

});
