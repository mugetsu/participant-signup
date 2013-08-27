/**
	Django uses jQuery 1.4.2
*/

(function (_) {

	var snake = function () {

        var view = 'a.view';

        function getMedia(view) {
        	return _(view).attr('data-url');
        }

        function buildLightbox() {
			_('body').append('<div class="lightbox-admin"><div class="lightbox-media"><img src="' + getMedia(view) + '" height="480" /></div></div>');
        }

        function lightbox() {
            buildLightbox();
        }

        return {
            initLightbox: lightbox
        };

    }();

    // View link
    _('a.view').live('click', function(e) {
		e.preventDefault();
		snake.initLightbox();
	});

    // Close view
    _('div.lightbox-admin').live('click', function(e) {
        _(this).remove();
    });

})(django.jQuery);