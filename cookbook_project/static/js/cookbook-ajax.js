

$('#save_button').click(function(){
	var user;
	var slug;
	slug = $(this).attr("data-slug");
	user = $(this).attr("data-user");
	$.get('/cookbook/save_recipe/', {user: user, slug: slug}, function(data){
		if (data === 'True') {
			$('#save_button').html('Remove');
		} else {
			$('#save_button').html('Save')
		}
	});
});