$(document).ready(function () {

  const patientsUrl = "/templates/patients.html";
  const ourDoctorUrl = "/templates/ourDoctor.html";
  const loginUrl = "/";

  const navbar = `
      <a class="patient" href="${patientsUrl}">Inicio</a>
      <a class="doctor" href="${ourDoctorUrl}">Doctors</a>
      <a class="login" href="${loginUrl}">Iniciar sesión</a>
    `;
    const compiledNavbar = Handlebars.compile(navbar);
    const html = compiledNavbar();

    $('.navbar').append(html);
    
$('.navbar a').on('click', function(e) {
  e.preventDefault();
  var href = $(this).attr('href');
  window.location.href = href;
})
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

