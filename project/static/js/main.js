$(document).ready(function() {
    $(document).on('submit', 'form.pjax-form', function(event) {
        $.pjax.submit(event, '#pjax-container');
    });
});