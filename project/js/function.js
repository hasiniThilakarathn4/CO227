/* code by webdevtrick ( https://webdevtrick.com ) */
$(".btn").click(function(){
    $(".input").toggleClass("active").focus;
    $(this).toggleClass("animate");
    $(".input").val("");
  });