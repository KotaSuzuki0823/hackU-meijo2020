/* postの送信の仕方 
$("user").submit(function(event){
    event.preventDefault();
    
    $.post('https://httpbin.org/post',$('form').serialize())

})

*/

$("#user").submit(function(event){
    /* event.preventDefault(); */
    /* alert($('form').serialize()); */
    var test=$('form').serialize();
    alert(test);

})
