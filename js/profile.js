/*
$("form").submit(function(event){
    event.preventDefault();

    var url="https://localhost:5000/user/registration";
    $.post(url,$('form').serialize())

});
*/

/*
$("form").submit(function (event) {

    var url = "https://localhost:5000/user/registration";
    var test = 'これはテストデータです';

    const res = await axios.post('http://localhost:5000/user/registration', {
        id: 123,
        name: 'Yamada Tarou'
    }
    )
    alert('完了');
});
*/
var url = "http://localhost:5000/user/registration";


$("form").submit(function getdataFetch() {
    var response=$('form').serialize();
    fetch(url, {
        mode: 'cors'
    })
        .then(function (response) {
            return response.json();
        })
        .then(function (body) {
            console.log(body.fetch)
            document.getElementById("resultFetch").innerText += body.fetch;
        })
        .catch(function (error) {
            console.log(error)
            document.getElementById("resultFetch").innerText = 'ERR';
        });
});