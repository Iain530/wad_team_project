$(document).ready(function() {
	
	// Check if username is available
	$('#id_username').keyup(function(event){
		var username = $(this).val();
		if (username.length > 0) {
			$.get('/cookbook/username_check/', {username: username}, function(data){
				if (data === 'True') {
					$('#username_check').html('&#10004;');
					$('#username_check').css('color', 'lightgreen')
					$('#register_button').prop('disabled', false);
				} else {
					$('#username_check').html('&#10006;')
					$('#username_check').css('color', 'crimson')
					$('#register_button').prop('disabled', true);
				}
			});
		} else {
			$('#username_check').html('')
			$('#username_check').css('color', '#f2f2f2')
			$('#register_button').prop('disabled', true);
		}
	});

	// Rate a recipe
	$('input.star').click(function(event){
		var recipe_id;
		var value;
		recipe_id = $(this).attr("data-recipe_id");
		value = parseInt($(this).attr("data-value"));
		$.get('/cookbook/rate_recipe/', {recipe_id: recipe_id, value: value}, function(data){
			var rating = parseFloat(data);
			$('#this_rating').html(rating);
			$('#this_rating').stars();
		});
	});


	// Save/Unsave a recipe
	$('#save_button').click(function(event){
		var user;
		var slug;
		// Get the recipe slug and user
		slug = $(this).attr("data-slug");
		user = $(this).attr("data-user");
		// Send get request to save/unsave the recipe
		$.get('/cookbook/save_recipe/', {user: user, slug: slug}, function(data){
			if (data === 'True') {
				// If recipe was saved then change button text to remove
				$('#save_button').html('Remove');
			} else if (data == 'False') {
				// Else if recipe was unsaved change button text to save
				$('#save_button').html('Save');
			} else {
				// Else display an error message
				alert('Could not save/remove recipe');
			}
		});
	});

	// Delete a recipe
	$('.delete_recipe_button').click(function(event) {
		// Get the name of the recipe
		var name;
		name = $(this).attr('data-name');
		// Require a confimation
		if (confirm('Do you really want to delete ' + name + '. (This cannot be undone)')) {
			var recipe_id;
			var recipe_div;
			// Get the recipe id and the id of the recipe's div
			recipe_id = $(this).attr('id');
			recipe_div = '#' + $(this).parent().attr('id');
			// Send get to the server to delete the recipe
			$.get('/cookbook/delete_recipe/', {recipe_id: recipe_id}, function(data){
				if (data == 'True') {
					// If recipe was deleted then remove the recipe's div
					$(recipe_div).fadeOut("normal", function() { $(this).remove(); });
				} else {
					// Otherwise display an error message
					alert('Recipe could not be deleted');
				}
			});
		}
	});

	// Delete a comment
	$('.delete_comment_button').click(function(event) {
		// Require a confimation
		if (confirm('Are you sure you want to delete this comment? (This cannot be undone)')) {
			var comment_id;
			var comment_div;
			// Get the comment id and id of comment's div
			comment_id = $(this).attr('id');
			comment_div = '#' + $(this).parent().attr('id');
			// Send get request to delete the comment
			$.get('/cookbook/delete_comment/', {comment_id: comment_id}, function(data){
				if (data == 'True') {
					// If comment was deleted then remove the comment's div
					$(comment_div).fadeOut("normal", function() { $(this).remove(); });
				} else {
					// Else display a error message
					alert('Comment could not be deleted');
				}
			});
		}
	});
	
	
});