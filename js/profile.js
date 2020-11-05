/* postの送信の仕方 
$("#user").submit(function(event){
    event.preventDefault();
    
    $.post('https://httpbin.org/post',$('form').serialize())

})

*/

$("#user").submit(function(event){
    /* event.preventDefault(); */
    /* alert($('form').serialize()); */
    var url="";
    var test=$('form').serialize();
    $.post('https://correliv.azurewebsites.net/user/registration',$('form').serialize())
    alert(test);

})
