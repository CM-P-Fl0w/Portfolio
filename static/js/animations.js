/*document.addEventListener("DOMContentLoaded", function() {
    // Smooth fade-in effect for sections
    gsap.utils.toArray(".fade-in").forEach(section => {
        gsap.fromTo(section, 
            { opacity: 0, y: 50 },
            { opacity: 1, y: 0, duration: 1.2, ease: "power3.out", scrollTrigger: { trigger: section, start: "top 80%" } }
        );
    });

    // Navbar Shrink on Scroll
    const navbar = document.querySelector(".navbar");
    window.addEventListener("scroll", function() {
        if (window.scrollY > 50) {
            navbar.classList.add("navbar-shrink");
        } else {
            navbar.classList.remove("navbar-shrink");
        }
    }); */

document.addEventListener("DOMContentLoaded", function() {
    const toggleButton = document.getElementById("dark-mode-toggle");
    const body = document.body;
    
        // Function to update the button text based on the current mode
    function updateButtonText() {
        if (body.classList.contains("dark-mode")) {
            toggleButton.textContent = "☀️ Light Mode";
        } else {
            toggleButton.textContent = "🌙 Dark Mode";
        }
    }
    
        // Check saved mode in local storage
    if (localStorage.getItem("dark-mode") === "enabled") {
        body.classList.add("dark-mode");
    }
    
    updateButtonText(); // Update button text on page load
    
    toggleButton.addEventListener("click", function() {
        body.classList.toggle("dark-mode");
    
            // Save mode to local storage
        if (body.classList.contains("dark-mode")) {
            localStorage.setItem("dark-mode", "enabled");
        } else {
            localStorage.setItem("dark-mode", "disabled");
        }
    
        updateButtonText(); // Update button text after toggling
    });
});
    
window.addEventListener("scroll", function() {
    let offset = window.pageYOffset;
    document.querySelector(".parallax").style.backgroundPositionY = offset * 0.5 + "px";
});
    
});
