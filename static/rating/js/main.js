
var Subscribe = {
	init: function() {
		this.$container = $('.art-container');
		this.render();
		this.bindEvents();
	},

	render: function() {

	},

	bindEvents: function() {
		$('.btn-like', this.$container).on('click', function(e) {
			e.preventDefault();

			var self = $(this);
			var url = $(this).attr('href');
			$.getJSON(url, function(result) {
				if (result.success) {
					$('.fa-thumbs-o-up', self).toggleClass('active');
				}
			});

			return false;
		});
	}
};

$(document).ready(function() {
	Subscribe.init();
});


