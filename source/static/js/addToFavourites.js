$(document).ready(function() {
    $('.add-to-favourites').click(function() {
        let photo = $(this).data('photo-id');

        $.ajax({
            url: '/api/favourite/add/',
            type: 'POST',
            data: {photo: photo},
            success: function(data) {
                $('.add-to-favourites[data-photo-id=' + photo + ']').hide();
                $('.delete-from-favourites[data-photo-id=' + photo + ']').show();
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.error(errorThrown);
            }
        });
    });
});