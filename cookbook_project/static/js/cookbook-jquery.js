$(document).ready(function() {
	
	$('#discard_changes').click( function(event) {
		if (confirm('Are you sure you want to stop editing? (Any unsaved changes will be lost)')) {
			var url = (window.location.href).toString();
			url = url.substring(0, url.length-5);
			$( location ).attr("href", url);
		}
	});
	
	// Stars for users to press to rate recipes
	$(function() {
		// Get the users previous rating
		var rating = $('.stars').attr('data-initial');
		// Display the users previous rating
		$("#star-" + rating).prop("checked",true)
	});
	
	
	// Stars for displaying the recipe rating in the list
	// Displays star rating on recipe detail
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
	
});

