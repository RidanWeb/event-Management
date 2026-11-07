

//   document.addEventListener('DOMContentLoaded', () => {
//     const menuBtn = document.getElementById('mobile-menu-btn');
//     const mobileMenu = document.getElementById('mobile-menu');
//     const hamburgerIcon = document.getElementById('hamburger-icon');
//     const closeIcon = document.getElementById('close-icon');

//     menuBtn.addEventListener('click', () => {
//       const isExpanded = menuBtn.getAttribute('aria-expanded') === 'true';
      
//       // Toggle menu container visibility
//       mobileMenu.classList.toggle('hidden');

//       // Toggle icons (hamburger vs cross)
//       hamburgerIcon.classList.toggle('hidden');
//       closeIcon.classList.toggle('hidden');

//       // Update accessibility state
//       menuBtn.setAttribute('aria-expanded', !isExpanded);
//     });
//   });





const menuBtn = document.getElementById('mobile-menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

menuBtn.addEventListener('click', () => {
  mobileMenu.classList.toggle('hidden');
});

// const links = document.querySelectorAll('.dashEventGrid');


// links.forEach(link => {

//   link.addEventListener('click', function() {
    

//     links.forEach(item => item.classList.remove('active'));
    
//     this.classList.add('active');

//   });

// });