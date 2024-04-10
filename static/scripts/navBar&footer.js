$(document).ready(function () {

    let navbar = `
                <a href="./patients.html">Inicio</a>
                <a href="./doctors.html">Doctors</a>
                <a href="./login.html">Iniciar sesión</a>
                `;
    $('.navbar').append(navbar).css('justify-content', 'space-evenly');

    let footer = `
                <p>CareMinder S.A de C.V</p>
                <div class="icons">
                  <a target="_blank" href="https://web.telegram.org/a/"><i class="footer-icon fa-brands fa-telegram"></i></a>
                  <a target="_blank" href="https://www.facebook.com/"><i class="footer-icon fa-brands fa-facebook"></i></a>
                  <a target="_blank" href="https://twitter.com/?lang=es"><i class="footer-icon fa-brands fa-x-twitter"></i></a>
                  <a target="_blank" href="https://www.twitch.tv/illojuan"><i class="footer-icon fa-brands fa-twitch"></i></a>
                  <a target="_blank" href="https://www.tumblr.com/"><i class="footer-icon fa-brands fa-tumblr"></i></a>
                  <a target="_blank" href="https://www.youtube.com/@jluiselvira"><i class="fa-brands fa-youtube"></i></a>
                </div>
                `;
    $('footer').append(footer);
});