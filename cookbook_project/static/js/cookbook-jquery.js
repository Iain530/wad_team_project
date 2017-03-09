$(document).ready(function() {
	
	$("#about-btn").click( function(event) {
		alert("You clicked the button using JQuery!");
	});
	
	$("p").hover( function() {
		$(this).css('color', 'red');
		},
		function() {
		$(this).css('color', 'blue');
	});
	
	$("#about-btn").click( function(event) {
		msgstr = $("#msg").html()
		msgstr = msgstr + "ooo"
		$("#msg").html(msgstr)
	});
		
});