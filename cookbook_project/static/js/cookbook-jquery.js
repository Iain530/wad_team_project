$(document).ready(function() {
	
	// Display star rating on page
	$(function() {
		$('span.stars').stars();
	});

	
	
	$.fn.stars = function() {
		return $(this).each(function() {
			// Get the value
			var val = parseFloat($(this).html());
			// Make sure that the value is in 0 - 5 range, multiply to get width
			var size = Math.max(0, (Math.min(5, val))) * 16;
			// Create stars holder
			var $span = $('<span />').width(size);
			// Replace the numerical value with stars
			$(this).html($span);
		});
	}
	
	
	// From TWD (not used)
	$("#about-btn").click( function(event) {
		alert("You clicked the button using JQuery!");
	});
	
	
	$("#about-btn").click( function(event) {
		msgstr = $("#msg").html()
		msgstr = msgstr + "ooo"
		$("#msg").html(msgstr)
	});
	
});

