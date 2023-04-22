$(document).ready(function() {
    $('.delete-from-favourites').click(function() {
        let photo = $(this).data('photo-id');

        $.ajax({
            url: '/api/favourite/delete/',
            type: 'DELETE',
            data: {photo: photo},
            success: function(data) {
                $('.delete-from-favourites[data-photo-id=' + photo + ']').hide();
                $('.add-to-favourites[data-photo-id=' + photo + ']').show();
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.error(errorThrown);
            }
        });
    });
});