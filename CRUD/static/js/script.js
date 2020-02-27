$( "form" ).submit(function( event ) {
    event.preventDefault();
    var form = $(this);
  $.ajax({
    url: form.attr("action"),
    data: form.serialize(),
    type: form.attr("method"),
    success: function (data) {
    console.log(data)
    },
    error:function(data) {
        console.log("No se ha podido obtener la información");
    }
  });
});