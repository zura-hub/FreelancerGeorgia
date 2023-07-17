const desktopBtn = document.querySelector('.btn-desktop-box');
const menu = document.querySelector('.mobile-nav');
const logo = document.querySelector('.logo-box');
const burger = document.querySelector('.burger');

burger.addEventListener('click', () => {
    if (desktopBtn.style.display === 'none' || menu.style.display === 'none') {
        desktopBtn.style.display = 'block';
        menu.style.display = 'block';
        logo.style.display = 'none';
    } else {
        desktopBtn.style.display = 'none';
        menu.style.display = 'none';
        logo.style.display = 'block';
    }
});


const show = () => {
    const singbtns = document.querySelector('.signup');
    const emp = document.querySelector('.employer-employee');

    singbtns.style.display = 'none';
    emp.style.display = 'flex';
};