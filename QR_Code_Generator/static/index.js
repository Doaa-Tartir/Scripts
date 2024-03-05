$(document).ready(function() {
    $('.generate-btn').click(function() {
        var formData = $('#link-form').serialize();
        $.post('/', formData, function(data) {
            $('.generated-div img').attr('src', data);
        });
    });
});

$("#link-btn").on("click",function(){
    $("#link-div").show();
})


