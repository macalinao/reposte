$(function() {
  $('.date').each(function() {
    var val = $(this).text();
    $(this).text(moment.unix(val).format('MMMM Do YYYY, h:mm:ss a'));
  });
});
