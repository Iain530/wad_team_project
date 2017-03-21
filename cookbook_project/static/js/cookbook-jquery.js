$(document).ready(function() {
	
	
	$('.filter').change( function(event) {
		var vegetarian = $('#vegetarian').is(":checked");
		var vegan = $('#vegan').is(":checked");
		var glutenfree = $('#gluten-free').is(":checked");
		var dairyfree = $('#dairy-free').is(":checked");
		var s_vegetarian = String(vegetarian).charAt(0).toUpperCase() + String(vegetarian).slice(1)
		var s_vegan = String(vegan).charAt(0).toUpperCase() + String(vegan).slice(1)
		var s_glutenfree = String(glutenfree).charAt(0).toUpperCase() + String(glutenfree).slice(1)
		var s_dairyfree = String(dairyfree).charAt(0).toUpperCase() + String(dairyfree).slice(1)
		
		$('.recipe_detail').show();
		if (vegan) {
			$('.recipe_detail[data-vegan!=' + s_vegan + ']').hide();
		
		} else {
			if (vegetarian){
				$('.recipe_detail[data-vegetarian!=' + s_vegetarian + ']').hide();
			}
			if (dairyfree) {
				$('.recipe_detail[data-dairyfree!=' + s_dairyfree + ']').hide();
			}
		}
	
		if (glutenfree) {
			$('.recipe_detail[data-glutenfree!=' + s_glutenfree + ']').hide();
		}
		
		if ($('.recipe_detail:visible').length == 0) {
			$('#no_results').show();
		} else {
			$('#no_results').hide();
		}
	});
	
	
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

