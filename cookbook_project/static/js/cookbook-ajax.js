

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