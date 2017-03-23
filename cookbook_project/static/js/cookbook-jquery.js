$(document).ready(function() {
	
	// Disable delete account button until confirm is checked
	// (Account still cannot be deleted due to the form even if button wasn't disabled)
	$('#id_confirm').change( function(event) {
		var conf = $(this).is(':checked');
		if (conf) {
			$('#delete_account_button').prop('disabled', false);
		} else {
			$('#delete_account_button').prop('disabled', true);
		}
	});
	
	// filtering
	$('.filter').change( function(event) {
		// get the filters wanted
		var vegetarian = $('#vegetarian').is(":checked");
		var vegan = $('#vegan').is(":checked");
		var glutenfree = $('#gluten-free').is(":checked");
		var dairyfree = $('#dairy-free').is(":checked");
		
		// show all recipes
		$('.recipe_detail').show();
		
		// hide unwanted recipes
		if (vegan) {
			// converting true to 'True'
			var s_vegan = String(vegan).charAt(0).toUpperCase() + String(vegan).slice(1);
			$('.recipe_detail[data-vegan!=' + s_vegan + ']').hide();
		
		} else {
			if (vegetarian){
				var s_vegetarian = String(vegetarian).charAt(0).toUpperCase() + String(vegetarian).slice(1);
				$('.recipe_detail[data-vegetarian!=' + s_vegetarian + ']').hide();
			}
			if (dairyfree) {
				var s_dairyfree = String(dairyfree).charAt(0).toUpperCase() + String(dairyfree).slice(1);
				$('.recipe_detail[data-dairyfree!=' + s_dairyfree + ']').hide();
			}
		}
	
		if (glutenfree) {
			var s_glutenfree = String(glutenfree).charAt(0).toUpperCase() + String(glutenfree).slice(1);
			$('.recipe_detail[data-glutenfree!=' + s_glutenfree + ']').hide();
		}
		
		// if all recipes were hidden then show a no results message
		if ($('.recipe_detail:visible').length === 0) {
			$('#no_results').show();
		} else {
			$('#no_results').hide();
		}
	});
	
	// Discard changes when editing recipe and redirect back to recipe
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
		$("#star-" + rating).prop("checked",true);
	});
	
	// These two functions taken from http://stackoverflow.com/questions/1987524/turn-a-number-into-star-rating-display-using-jquery-and-css
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
	};
	
});

