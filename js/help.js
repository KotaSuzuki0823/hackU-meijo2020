/* テスト用にプロフィールオブジェクトを生成する */
var data=[
    {
        "name":"江間結斗",
        "age":"20",
        "jender":"男",
        "adress": "愛知県"
    },
    {
        "name":"荻野あきょみち",
        "age":"21",
        "jender":"男",
        "adress":"愛知県"
    },
    {
        "name":"女の子A",
        "age":"18",
        "jender":"女",
        "adress":"岐阜県"
    }
];

var flag;    
var url = "http://localhost:5000/user/registration";


/* 人を選択した時の操作 */
$('a').on('click',function(){
    //押されたボタンのclassを取得
    var class_name=$(this).attr('class')
    if(class_name=='pe1'){
        flag=1;
    }else if(class_name=='pe2'){
        flag=2;
    }else if(class_name=='pe3'){
        flag=3;
    }else if(class_name=='pe4'){
        flag=4;
    }else if(class_name=='pe5'){
        flag=5;
    }else if(class_name=='pe6'){
        flag=6;
    }else if(class_name=='pe7'){
        flag=7;
    }else if(class_name=='pe8'){
        flag=8;
    }
    $('.popup').addClass('show').fadeIn();

});
/* popupの非表示 */
$('#close').on('click',function(){
    $('.popup').fadeOut();
})
/* 決定した後*/
$('#decide').on('click',function(){
    alert(data[flag-1].name+'にお願いをします');
    location.href="./index.html";
    /* postで色々と通信を行う
        ・お助けで入力した詳細
        ・お願いする人
        ・あと何かあるかな
    */

})

/* 若者のデータをもとに処理を行う */
$("div[class!='renew']").each(function(index,element){
    var h='<dl><dt>名前</dt><dd>'+data[index].name
        +'</dd><dt>年齢</dt><dd>'+data[index].age
        +'</dd><dt>性別</dt><dd>'+data[index].jender
        +'</dd><dt>住み</dt><dd>'+data[index].adress
        +'</dd></dl>';
        
    $(this).append(h);
    /* 性別に応じて色付け */
    if(data[index].jender=="男"){
        $(this).css('background-color','rgba(21, 190, 241, 0.849)');
    }else if(data[index].jender=="女"){
        $(this).css('background-color','rgb(247, 9, 227)')
    };
});

