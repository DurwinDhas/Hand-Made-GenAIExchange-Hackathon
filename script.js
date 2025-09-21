document.addEventListener('DOMContentLoaded', () => {
    // Basic Login Form Logic (Client-side simulation)
    const artisanLoginForm = document.getElementById('artisanLoginForm');
    const uploadTool = document.getElementById('upload-tool');
    const processCraftButton = document.getElementById('processCraftButton');
    const craftFileUpload = document.getElementById('craftFileUpload');
    const generatedContent = document.getElementById('generatedContent');
    const aiHeading = document.getElementById('aiHeading');
    const aiStory = document.getElementById('aiStory');
    const aiTags = document.getElementById('aiTags');
    const publishBlogButton = document.getElementById('publishBlogButton');

    if (artisanLoginForm) {
        artisanLoginForm.addEventListener('submit', (event) => {
            event.preventDefault(); // Prevent actual form submission

            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            // Simulate a successful login for demonstration
            if (username === 'artisan' && password === 'password123') {
                alert('Login successful! Welcome, Artisan!');
                artisanLoginForm.style.display = 'none'; // Hide login form
                if (uploadTool) uploadTool.style.display = 'block'; // Show upload tool
                if (generatedContent) generatedContent.style.display = 'none'; // Hide generated content initially
            } else {
                alert('Invalid username or password.');
            }
        });
    }

    // Machine Learning Model Simulation (Front-end only)
    if (processCraftButton) {
        processCraftButton.addEventListener('click', () => {
            if (craftFileUpload.files.length > 0) {
                // In a real application, you would send these files to a backend
                // where your ML model would process them.
                console.log('Files selected:', craftFileUpload.files);
                alert('Processing your craft with AI... (This is a simulation)');

                // Simulate AI generating text based on the presence of files
                const fileNames = Array.from(craftFileUpload.files).map(file => file.name).join(', ');
                aiHeading.textContent = `The Beauty of My Handcrafted Item (${fileNames})`;
                aiStory.textContent = `This piece, made with love and traditional techniques, showcases the intricate details and passion behind my work. Each element tells a story of heritage and dedication. I hope you enjoy its unique charm.`;
                aiTags.textContent = `#handmade #craftsmanship #artisan #unique #traditional #creative`;

                if (generatedContent) generatedContent.style.display = 'block';
                if (publishBlogButton) publishBlogButton.style.display = 'block';
                publishBlogButton.textContent = 'Publish Blog Post'; // Reset button text if changed
            } else {
                alert('Please upload some images or videos first!');
            }
        });
    }

    // Publish Blog Post Simulation
    if (publishBlogButton) {
        publishBlogButton.addEventListener('click', () => {
            alert('Your blog post has been published successfully!');
            // In a real app, this would send data to a database.
            // Reset fields for a new upload
            if (craftFileUpload) craftFileUpload.value = '';
            if (aiHeading) aiHeading.textContent = '';
            if (aiStory) aiStory.textContent = '';
            if (aiTags) aiTags.textContent = '';
            if (generatedContent) generatedContent.style.display = 'none';
        });
    }

    // Placeholder for craft images (for index.html)
    // You would replace this with dynamic loading from a database in a real app
    const craftImages = [
        'images/craft1.jpg',
        'images/craft2.jpg',
        'images/craft3.jpg',
        'images/craft4.jpg', // Add more placeholder images
        'images/craft5.jpg',
        'images/craft6.jpg'
    ];

    const craftGrid = document.querySelector('.craft-grid');
    if (craftGrid) {
        craftGrid.innerHTML = ''; // Clear existing examples if any
        craftImages.forEach((src, index) => {
            const craftItem = document.createElement('div');
            craftItem.classList.add('craft-item');
            craftItem.innerHTML = `
                <img src="${src}" alt="Handmade Craft ${index + 1}">
                <h4>My Unique Creation ${index + 1}</h4>
                <p>A beautiful example of handcrafted excellence, perfect for any home or collection.</p>
                <a href="#" class="view-details">View Details</a>
            `;
            craftGrid.appendChild(craftItem);
        });
    }
});