document.addEventListener("DOMContentLoaded", function() {
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
    });

});   
window.addEventListener("scroll", function() {
    let offset = window.pageYOffset;
    document.querySelector(".parallax").style.backgroundPositionY = offset * 0.5 + "px";
});
    

