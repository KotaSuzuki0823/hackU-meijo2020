/* テスト用のオブジェクト */

var help_data = [
    {
        /* お助けの項目から入力されたオブジェクト */
        "date": "2020/11/06",
        "when": "朝",
        "time": "3時間",
        "content": "買い物",
        "detail": "荻野の家に行く"

    },
    {
        "date": "2020/11/08",
        "when": "昼",
        "time": "6時間",
        "content": "その他",
        "detail": "Hack U本番!"
    }
]

var young_data = [
    {
        "name": "江間結斗",
        "age": "20",
        "jender": "男",
        "adress": "愛知県",
        "phone": "080-6953-5078"
    },
    {
        "name": "荻野あきょみち",
        "age": "21",
        "jender": "男",
        "adress": "愛知県",
        "phone": "xxx-xxxx-xxxx"
    }
]

var old_data = [
    {
        "name": "江間結斗",
        "age": "80",
        "jender": "男",
        "adress": "愛知県"
    },
    {
        "name": "荻野あきょみち",
        "age": "72",
        "jender": "男",
        "adress": "岐阜県"
    },
]

/* 適切な値を使うためにオブジェクトを整理 */

$.each(help_data, function (index, value) {
    /* 1.得られたオブジェクトについてタグを生成 */
    var tagDt = "<dt>" + help_data[index].date + "</dt>";
    var whenDiv = "<dd><div class='title'>時間帯</div>"
        + "<div class='main'>" + help_data[index].when + "</div>";
    var timeDiv = "<div class='title'>所要時間</div>"
        + "<div class='main'>" + help_data[index].time + "</div>";
    var contentDiv = "<div class='title'>内容</div>"
        + "<div class='main'>" + help_data[index].content + "</div>";
    var detailDiv = "<div class='title'>詳細</div>"
        + "<div class='main'>" + help_data[index].detail + "</div></dd>";

    /* 2.実際に組込み */
    $("#up").append(tagDt + whenDiv + timeDiv + contentDiv + detailDiv);
});


$.each(young_data, function (index, value) {
    var nametag = "<dt>" + young_data[index].name + "</dt>";
    var ageDiv = "<dd><div class='title'>年齢</div>"
        + "<div class='main'>" + young_data[index].age + "</div>";
    var jenderDiv = "<div class='title'>性別</div>"
        + "<div class='main'>" + young_data[index].jender + "</div>";
    var adressDiv = "<div class='title'>住所</div>"
        + "<div class='main'>" + young_data[index].adress + "</div>";
    var phoneDiv = "<div class='title'>電話番号</div>"
        + "<div class='main'>" + young_data[index].phone + "</div></dd>";

    $("#down").append(nametag + ageDiv + jenderDiv + adressDiv + phoneDiv);
});

$(function () {
    var class_closed = 'closed';
    $('.accordion').each(function () {
        var dl = $(this);
        var allDt = dl.find('dt');
        var allDd = dl.find('dd');

        function closeAll() {
            allDt.addClass(class_closed);
            allDd.addClass(class_closed);
        }
        function open(dt, dd) {
            dt.removeClass(class_closed);
            dd.removeClass(class_closed);
        }
        closeAll();


        allDt.click(function () {
            var dt = $(this);
            var dd = dt.next();
            closeAll();
            open(dt, dd);
        });
    });
});