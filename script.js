// Sample job data
const jobs = [
    {
        title: "Software Engineer",
        company: "TechCorp",
        location: "Remote"
    },
    {
        title: "Data Scientist",
        company: "AI Solutions",
        location: "San Francisco, CA"
    },
    {
        title: "Software Engineer",
        company: "DevWorks",
        location: "San Francisco, CA"
    },
    {
        title: "Data Scientist",
        company: "Machine Learning Inc.",
        location: "Remote"
    }
];

// Function to display jobs
function displayJobs(filteredJobs) {
    const jobListings = document.getElementById('job-listings');
    jobListings.innerHTML = ''; // Clear existing job listings
    filteredJobs.forEach(job => {
        const jobDiv = document.createElement('div');
        jobDiv.classList.add('job');
        jobDiv.innerHTML = `
            <h3>${job.title}</h3>
            <p>Company: ${job.company}</p>
            <p>Location: ${job.location}</p>
            <button>Apply Now</button>
        `;
        jobListings.appendChild(jobDiv);
    });
}

// Function to filter jobs based on selected category and location
function filterJobs() {
    const category = document.getElementById('category').value;
    const location = document.getElementById('location').value;
    
    const filteredJobs = jobs.filter(job => {
        return (category === 'All' || job.title === category) &&
               (location === 'All' || job.location === location);
    });
    
    displayJobs(filteredJobs);
}

// Initial job display
filterJobs();

// Event listeners for filter changes
document.getElementById('category').addEventListener('change', filterJobs);
document.getElementById('location').addEventListener('change', filterJobs);
