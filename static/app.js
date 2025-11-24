// Global state
let resumeData = null;
let jobsData = [];
let applicationsData = [];
let currentJob = null;
let currentCoverLetter = '';

// Dark mode
const darkModeToggle = document.getElementById('darkModeToggle');
const htmlElement = document.documentElement;

// Load dark mode preference
if (localStorage.getItem('darkMode') === 'true') {
    htmlElement.classList.add('dark');
}

darkModeToggle.addEventListener('click', () => {
    htmlElement.classList.toggle('dark');
    localStorage.setItem('darkMode', htmlElement.classList.contains('dark'));
});

// Tab switching
function switchTab(tabName) {
    // Hide all tabs
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.add('hidden');
    });
    
    // Remove active class from all buttons
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('bg-gradient-to-r', 'from-blue-500', 'to-purple-600', 'text-white', 'shadow-md');
        btn.classList.add('text-slate-600', 'dark:text-slate-400');
    });
    
    // Show selected tab
    document.getElementById(`${tabName}Tab`).classList.remove('hidden');
    
    // Add active class to selected button
    const activeBtn = document.querySelector(`[data-tab="${tabName}"]`);
    activeBtn.classList.add('bg-gradient-to-r', 'from-blue-500', 'to-purple-600', 'text-white', 'shadow-md');
    activeBtn.classList.remove('text-slate-600', 'dark:text-slate-400');
    
    // Update tracker if switching to it
    if (tabName === 'tracker') {
        renderApplications();
    }
}

// Initialize first tab
switchTab('upload');

// Load data from localStorage
function loadLocalData() {
    const savedResume = localStorage.getItem('resumeData');
    const savedJobs = localStorage.getItem('jobsData');
    const savedApps = localStorage.getItem('applicationsData');
    
    if (savedResume) {
        resumeData = JSON.parse(savedResume);
        displayResume();
    }
    
    if (savedJobs) {
        jobsData = JSON.parse(savedJobs);
    }
    
    if (savedApps) {
        applicationsData = JSON.parse(savedApps);
    }
}

loadLocalData();

// File upload
async function handleFileUpload() {
    const fileInput = document.getElementById('resumeFile');
    const file = fileInput.files[0];
    
    if (!file) return;
    
    // Show loading
    document.getElementById('uploadIcon').classList.add('hidden');
    document.getElementById('loadingIcon').classList.remove('hidden');
    document.getElementById('uploadText').textContent = 'Processing resume...';
    
    const formData = new FormData();
    formData.append('resume', file);
    
    try {
        const response = await fetch('/upload-resume', {
            method: 'POST',
            body: formData
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Upload failed');
        }
        
        resumeData = await response.json();
        localStorage.setItem('resumeData', JSON.stringify(resumeData));
        
        displayResume();
        alert('Resume processed successfully!');
        
    } catch (error) {
        alert('Error: ' + error.message);
        
        // Reset UI
        document.getElementById('uploadIcon').classList.remove('hidden');
        document.getElementById('loadingIcon').classList.add('hidden');
        document.getElementById('uploadText').textContent = 'Click to upload resume';
    }
}

function displayResume() {
    if (!resumeData) return;
    
    // Hide upload section, show resume section
    document.getElementById('uploadSection').classList.add('hidden');
    document.getElementById('resumeSection').classList.remove('hidden');
    
    // Update header
    document.getElementById('resumeInfo').classList.remove('hidden');
    document.getElementById('userName').textContent = resumeData.name;
    document.getElementById('skillCount').textContent = resumeData.skills.length;
    
    // Fill resume details
    document.getElementById('resumeName').textContent = resumeData.name;
    document.getElementById('resumeEmail').textContent = resumeData.email;
    document.getElementById('resumePhone').textContent = resumeData.phone;
    document.getElementById('skillsCount').textContent = resumeData.skills.length;
    
    // Display skills
    const skillsList = document.getElementById('skillsList');
    skillsList.innerHTML = resumeData.skills.map(skill => 
        `<span class="px-3 py-1 bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200 rounded-full text-sm font-medium">${skill}</span>`
    ).join('');
    
    // Display experience
    if (resumeData.experience && resumeData.experience.length > 0) {
        document.getElementById('experienceSection').classList.remove('hidden');
        const experienceList = document.getElementById('experienceList');
        experienceList.innerHTML = resumeData.experience.map(exp => 
            `<li>• ${exp}</li>`
        ).join('');
    }
}

function clearResume() {
    if (confirm('Are you sure you want to remove your resume?')) {
        resumeData = null;
        localStorage.removeItem('resumeData');
        
        document.getElementById('uploadSection').classList.remove('hidden');
        document.getElementById('resumeSection').classList.add('hidden');
        document.getElementById('resumeInfo').classList.add('hidden');
        document.getElementById('resumeFile').value = '';
        
        // Reset upload UI
        document.getElementById('uploadIcon').classList.remove('hidden');
        document.getElementById('loadingIcon').classList.add('hidden');
        document.getElementById('uploadText').textContent = 'Click to upload resume';
    }
}

// Job search
async function searchJobs() {
    if (!resumeData) {
        document.getElementById('resumeWarning').classList.remove('hidden');
        return;
    }
    
    document.getElementById('resumeWarning').classList.add('hidden');
    
    const query = document.getElementById('searchQuery').value.trim();
    if (!query) {
        alert('Please enter job keywords');
        return;
    }
    
    // Show loading
    document.getElementById('searchIcon').classList.add('hidden');
    document.getElementById('searchLoading').classList.remove('hidden');
    
    try {
        const response = await fetch('/search-jobs', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                query: query,
                skills: resumeData.skills
            })
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Search failed');
        }
        
        jobsData = await response.json();
        localStorage.setItem('jobsData', JSON.stringify(jobsData));
        
        displayJobs();
        
    } catch (error) {
        alert('Error: ' + error.message);
    } finally {
        document.getElementById('searchIcon').classList.remove('hidden');
        document.getElementById('searchLoading').classList.add('hidden');
    }
}

function displayJobs() {
    const jobsList = document.getElementById('jobsList');
    const noJobs = document.getElementById('noJobs');
    
    if (jobsData.length === 0) {
        jobsList.innerHTML = '';
        noJobs.classList.remove('hidden');
        return;
    }
    
    noJobs.classList.add('hidden');
    
    jobsList.innerHTML = jobsData.map(job => `
        <div class="bg-white dark:bg-slate-800 rounded-xl shadow-lg p-6 hover:shadow-xl transition-all">
            <div class="flex justify-between items-start mb-4">
                <div class="flex-1">
                    <div class="flex items-center gap-3 mb-2">
                        <h3 class="text-xl font-bold text-slate-800 dark:text-white">${job.title}</h3>
                        ${job.fitScore >= 70 ? `
                            <span class="flex items-center gap-1 px-2 py-1 bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200 rounded-full text-xs font-semibold">
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2">
                                    <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
                                </svg>
                                ${job.fitScore}% Match
                            </span>
                        ` : ''}
                    </div>
                    <p class="text-slate-600 dark:text-slate-400 font-medium">${job.company}</p>
                    <p class="text-sm text-slate-500 dark:text-slate-500">${job.location} • ${job.salary}</p>
                </div>
            </div>
            
            ${job.fitReason ? `
                <div class="bg-blue-50 dark:bg-blue-900/30 border border-blue-200 dark:border-blue-800 rounded-lg p-3 mb-4">
                    <p class="text-sm text-blue-800 dark:text-blue-200"><strong>Why this fits:</strong> ${job.fitReason}</p>
                </div>
            ` : ''}
            
            <p class="text-slate-700 dark:text-slate-300 mb-4">${job.description}</p>
            
            <div class="mb-4">
                <p class="text-sm font-semibold text-slate-700 dark:text-slate-300 mb-2">Requirements:</p>
                <div class="flex flex-wrap gap-2">
                    ${job.requirements.slice(0, 5).map(req => 
                        `<span class="px-2 py-1 bg-slate-100 dark:bg-slate-700 text-slate-700 dark:text-slate-300 rounded text-xs">${req}</span>`
                    ).join('')}
                </div>
            </div>
            
            <div class="flex gap-3">
                <button onclick='generateCoverLetter(${JSON.stringify(job).replace(/'/g, "&apos;")})' 
                        class="flex-1 bg-blue-500 text-white py-2 rounded-lg font-medium hover:bg-blue-600 transition-all flex items-center justify-center gap-2">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                        <polyline points="14 2 14 8 20 8"></polyline>
                        <line x1="16" y1="13" x2="8" y2="13"></line>
                        <line x1="16" y1="17" x2="8" y2="17"></line>
                        <polyline points="10 9 9 9 8 9"></polyline>
                    </svg>
                    Generate Cover Letter
                </button>
                <button onclick='addApplication(${JSON.stringify(job).replace(/'/g, "&apos;")})' 
                        class="flex-1 bg-gradient-to-r from-green-500 to-emerald-600 text-white py-2 rounded-lg font-medium hover:shadow-lg transition-all flex items-center justify-center gap-2">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <line x1="12" y1="5" x2="12" y2="19"></line>
                        <line x1="5" y1="12" x2="19" y2="12"></line>
                    </svg>
                    Mark as Applied
                </button>
            </div>
        </div>
    `).join('');
}

// Cover letter
async function generateCoverLetter(job) {
    currentJob = job;
    
    // Show modal
    document.getElementById('coverLetterModal').classList.remove('hidden');
    document.getElementById('coverLetterLoading').classList.remove('hidden');
    document.getElementById('coverLetterContent').classList.add('hidden');
    
    try {
        const response = await fetch('/generate-cover-letter', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ job })
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Generation failed');
        }
        
        const data = await response.json();
        currentCoverLetter = data.coverLetter;
        
        document.getElementById('coverLetterContent').textContent = currentCoverLetter;
        document.getElementById('coverLetterLoading').classList.add('hidden');
        document.getElementById('coverLetterContent').classList.remove('hidden');
        
    } catch (error) {
        alert('Error: ' + error.message);
        closeCoverLetterModal();
    }
}

function closeCoverLetterModal() {
    document.getElementById('coverLetterModal').classList.add('hidden');
    currentJob = null;
    currentCoverLetter = '';
}

function copyCoverLetter() {
    navigator.clipboard.writeText(currentCoverLetter);
    alert('Cover letter copied to clipboard!');
}

function applyAndTrack() {
    if (currentJob) {
        addApplication(currentJob);
    }
    closeCoverLetterModal();
}

// Applications
function addApplication(job) {
    const app = {
        id: Date.now().toString(),
        jobId: job.id,
        jobTitle: job.title,
        company: job.company,
        status: 'applied',
        appliedDate: new Date().toISOString()
    };
    
    applicationsData.push(app);
    localStorage.setItem('applicationsData', JSON.stringify(applicationsData));
    
    switchTab('tracker');
}

function updateApplicationStatus(appId, newStatus) {
    applicationsData = applicationsData.map(app => 
        app.id === appId ? { ...app, status: newStatus } : app
    );
    localStorage.setItem('applicationsData', JSON.stringify(applicationsData));
    renderApplications();
}

function renderApplications() {
    const statuses = ['applied', 'screening', 'interview', 'offer', 'rejected'];
    const noApps = document.getElementById('noApplications');
    
    if (applicationsData.length === 0) {
        noApps.classList.remove('hidden');
        statuses.forEach(status => {
            document.getElementById(`${status}Count`).textContent = '0';
            document.getElementById(`${status}Column`).innerHTML = '';
        });
        return;
    }
    
    noApps.classList.add('hidden');
    
    statuses.forEach(status => {
        const apps = applicationsData.filter(app => app.status === status);
        document.getElementById(`${status}Count`).textContent = apps.length;
        
        const column = document.getElementById(`${status}Column`);
        column.innerHTML = apps.map(app => `
            <div class="bg-white dark:bg-slate-800 rounded-lg p-3 shadow-sm border border-slate-200 dark:border-slate-700">
                <p class="font-semibold text-slate-800 dark:text-white text-sm mb-1">${app.jobTitle}</p>
                <p class="text-xs text-slate-600 dark:text-slate-400 mb-2">${app.company}</p>
                <select onchange="updateApplicationStatus('${app.id}', this.value)" 
                        class="w-full text-xs px-2 py-1 border border-slate-300 dark:border-slate-600 dark:bg-slate-700 dark:text-white rounded">
                    ${statuses.map(s => 
                        `<option value="${s}" ${s === app.status ? 'selected' : ''}>${s.charAt(0).toUpperCase() + s.slice(1)}</option>`
                    ).join('')}
                </select>
            </div>
        `).join('');
    });
}