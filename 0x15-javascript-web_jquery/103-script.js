$('document').ready(function () {
  $('INPUT#btn_translate').click(executeTranslate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        executeTranslate();
      }
    });
  });
});

function executeTranslate () {
  const url = 'https://hellosalut.stefanbohacek.dev/?';
  $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    $('DIV#hello').html(data.hello);
  });
}
