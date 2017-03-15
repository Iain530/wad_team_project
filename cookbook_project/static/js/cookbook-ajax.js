

$('#save_button').click(function(event){
	var user;
	var slug;
	slug = $(this).attr("data-slug");
	user = $(this).attr("data-user");
	$.get('/cookbook/save_recipe/', {user: user, slug: slug}, function(data){
		if (data === 'True') {
			$('#save_button').html('Remove');
		} else if (data == 'False') {
			$('#save_button').html('Save');
		} else {
			alert('Could not save/remove recipe');
		}
	});
});

$('.delete_button').click(function(event) {
	if (confirm('Are you sure you want to delete this comment?')) {
		var comment_id;
		var comment_div;
		comment_id = $(this).attr('id');
		comment_div = $(this).parent().attr('id');
		$.get('/cookbook/delete_comment/', {comment_id: comment_id}, function(data){
			if (data == 'True') {
				$('#'+comment_div).remove();
			} else {
				alert('Comment could not be deleted');
			}
		});
	}
});

// Posting comments (unfinished)

// $('#post_comment').click(function() {
	// var user;
	// var slug;
	// var comment;
	
	// slug = $(this).attr("data-slug");
	// user = $(this).attr("data-user");
	// comment = $(#'comment_text').val()
	
	// if (val != '') {
		// $.get('/cookbook/post_comment', {user: user, slug: slug, text: comment}, function(data){
			
			
		// });
		
	// }
// });