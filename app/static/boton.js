$(document).ready(function(){


  $('#search').click(function(){

    var txt = $("input").val();
    $.post("/resultado", {palabra: txt}, function(result){
		
	console.log(result)

      $(".result").html(result);
    });

});
});
