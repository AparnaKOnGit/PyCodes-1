// scripts.js
document.addEventListener('DOMContentLoaded', function() {
    const footer = document.querySelector('footer');
    const currentDate = new Date();
    footer.textContent = `© ${currentDate.getFullYear()} My Blog`;
});
