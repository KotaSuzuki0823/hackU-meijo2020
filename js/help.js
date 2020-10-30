var flag;

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
    alert('押されたのは'+class_name+'でした');
    $('.popup').addClass('show').fadeIn();
});

/* popupの非表示 */
$('#close').on('click',function(){
    $('.popup').fadeOut();
})

/* 決定した後*/
$('#decide').on('click',function(){
    location.href="../index.html";
})

