$(document).ready(function(){

  $("#min, #med, #max, #con").attr('disabled','disabled');

  $(".bin").children("img, .name").click(
    function() {
      $(".bin").children("img").animate({ opacity: "0" }, 500);
      $(".bin").children(".name, .bin_type").animate({ top: "-50px"},500);
      $(".bin_type").animate({opacity: "1"},500);
    });

  $("#yani").click(
    function(){
      //get
      $("#yani, #pik").attr('disabled','disabled');
      $("#yani, #pik, .bin").css("background-color","#aeaeae");
      $("#min, #med, #max, #con").prop('disabled',false);
      $(".noize, .noize_type").css("background-color","#717ece");
    });

  $("#pik").click(
    function(){
      //get
      $("#yani, #pik").attr('disabled','disabled');
      $("#yani, #pik, .bin").css("background-color","#aeaeae");
      $("#min, #med, #max, #con").prop('disabled',false);
      $(".noize, .noize_type").css("background-color","#717ece");
      $(".pik").prop('disabled',true);
    });

    $(".noize").children("img, .name").click(
    function() {
      $(".noize").children("img").animate({ opacity: "0" }, 500);
      $(".noize").children(".name, .noize_type").animate({ top: "-50px"},500);
      $(".noize_type").animate({opacity: "1"},500);
    });
});