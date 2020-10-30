/* sumple

$("user").submit(function(event){
// stop form from submitting normally
    event.preventDefault();
//get some values from elements on the pages
    var $form=$(this),
    term=$form.find("input[name='s]").val,
    url=$form.attr("action");
//send the data using post
    var posting=$.post(url,{s:term});
//put the data using post
    posting.done(function(data){
        var content=$(data).find("#content");
        $("#result").empty().append(content);
    });
});

*/  

$("user").submit(function(event){
    event.preventDefault();
    
    $.post('https://httpbin.org/post',$('form').serialize())

    .done(function(data){
        console.log(data.form);
    })
})