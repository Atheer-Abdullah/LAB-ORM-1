document.addEventListener('DOMContentLoaded', () => {
    
    
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 20) {
            
            navbar.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.04)';
            navbar.style.background = 'rgba(255, 255, 255, 0.95)';
        } else {
           
            navbar.style.boxShadow = 'none';
            navbar.style.background = 'rgba(255, 255, 255, 0.8)';
        }
    });


    const cards = document.querySelectorAll('.post-card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = `all 0.6s ease ${index * 0.1}s`;
        
        
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 100);
    });

    
    console.log("%c Byte. %c Minimalist Blog Active ", 
                "color: white; background: #6366f1; padding: 5px; font-weight: bold; border-radius: 4px 0 0 4px;", 
                "color: #6366f1; background: #f1f5f9; padding: 5px; border-radius: 0 4px 4px 0;");
});

const toggleBtn = document.getElementById('theme-toggle');
const themeIcon = document.getElementById('theme-icon');
const currentTheme = localStorage.getItem('theme');


if (currentTheme === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
    themeIcon.classList.replace('bi-moon-stars-fill', 'bi-sun-fill');
}

toggleBtn.addEventListener('click', () => {
    let theme = document.documentElement.getAttribute('data-theme');
    
    if (theme === 'dark') {
        
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light');
        
        themeIcon.classList.replace('bi-sun-fill', 'bi-moon-stars-fill');
    } else {
        
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
        
        themeIcon.classList.replace('bi-moon-stars-fill', 'bi-sun-fill');
    }
});