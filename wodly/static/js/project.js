/* Project specific Javascript goes here. */
$(document).ready(function() {
    $('.add-item').click(function(ev) {
        ev.preventDefault();
        var count = $('.items-form-container').children().length;
        var tmplMarkup = $('#item-template').html();
        var compiledTmpl = tmplMarkup.replace(/exercise/g, count);
        $('div.items-form-container').append(compiledTmpl);

        // update form count
        $('#id_item_items-TOTAL_FORMS').attr('value', count + 1);

        // some animate to scroll to view our new form
        $('html, body').animate({
            scrollTop: $("#add-item-button").position().top - 200
        }, 800);
    });
});
