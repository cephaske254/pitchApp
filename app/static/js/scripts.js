$(document).ready(function(){
    $('button.image-button').click(function(){
        $('form.image-form').slideToggle()
    })
    $('form.image-form').submit(function(){
        $(this).slideToggle()
    })
})