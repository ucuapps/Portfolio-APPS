/**
 * Created by StasMaster on 06.08.18.
 */

Date.prototype.addDays = function(days) {
    var date = new Date(this.valueOf());
    date.setDate(date.getDate() + days);
    return date;
}

function dateString(date) {

    return date.getFullYear()+'-'+date.getMonth()+'-'+date.getDate()+'T00:00:00+03:00';
}




function minutes(mins) {
    if(mins == 0) {
        return '00';
    } else if (mins < 10) {
        return '0'+mins;
    }
    return mins;
}

function beautifySchedule() {
        $(".row-cell").each(function() {
                if($(this).find(".day-name").text() === $(this).next().find(".day-name").text() ) {
                    // $(this).find(".day-name").hide();
                    $(this).css({'border':'none', 'padding-bottom':'0px'});

                    // $('#grid .'+ day_id+'_day:first-child h2').css({'display':'block'});
                }
                    var day_id = $(this).find(".day-num").text().split(" ")[0],
                        month_id = $(this).find(".day-num").attr("data-month");

                    $(this).addClass(day_id+'_day_'+month_id);
                    $(this).attr("day", day_id+'_day_'+month_id);
        });

        $(".row-cell").each(function() {
           var atr = $(this).attr("day");
           // $("."+atr+" h2").hide();
           $("."+atr+" h2").first().show();
        });
}


function groupByDays() {
            $(".row-cell").each(function() {
                var data = $(this).find('h2').attr("data-day");



                if($(this).find(".day-name").text() === $(this).next().find(".day-name").text() ) {
                    // $(this).find(".day-name").hide();
                    $(this).css({'border':'none', 'padding-bottom':'0px'});

                }
        });
}

function loadMore() {
// var button = $('.after'),
//     spinner = '<span class="spinner"></span>';
//
// 	if (!button.hasClass('loading')) {
// 		button.toggleClass('loading').html(spinner);
// 	}

     var button = $('.chev-after');
	button.find('i').hide();
	button.find('button').show();

    console.log($(".row-cell:last-child .day").attr("data-day"));
    console.log($("#grid").attr("data-room"));
    console.log($("#grid").attr("data-building"));
    $.ajax(
        {
            url: "http://"+window.location.host+"/calendar/json/",
            data: {
                date: $(".row-cell:last-child .day").attr("data-day"),
                loadBefore: false,
                roomId: $("#grid").attr("data-room"),
                buildingId: $("#grid").attr("data-building"),
            },
           type: 'POST',
            async: true,
            success: function(result){
                console.log(result)
                button.find('button').hide();
                button.find('i').show();
                $("body").scrollTop(button.offset().top);
                var obj = JSON.parse(result);
                console.log(obj.events);
                if(obj.events.length <2) {
                    var cur_date = new Date($(".row-cell:last-child .day").attr("data-day"));
                    $(".row-cell:last-child .day").attr("data-day", dateString(cur_date.addDays(7)));
                    alert("date changed");

                }
                $("body").css({'overflow':'auto'});
                $("#grid").css({'overflow':'auto'});
                // renderEvents(result.events)
                addEvents(obj.events, false)
            }
        });

    return true;
}

function loadBefore() {
    // var button = $('.before'),
    // spinner = '<span class="spinner"></span>';
    //
	// if (!button.hasClass('loading')) {
	// 	button.toggleClass('loading').html(spinner);
	// }
    var button = $('.chev-before');
	button.find('i').hide();
	button.find('button').show();

    console.log($(".row-cell:first-child .day").attr("data-day"));

    $.ajax(
        {
            url: "http://"+window.location.host+"/calendar/json/",
            data: {
                date: $(".row-cell:first-child .day").attr("data-day"),
                loadBefore: true,
                roomId: $("#grid").attr("data-room"),
                buildingId: $("#grid").attr("data-building"),
            },
           type: 'POST',
            async: true,
            success: function(result){
	            button.find('button').hide();
                button.find('i').show();
                $("body").scrollTop(button.offset().top);
                var obj = JSON.parse(result);
                console.log(obj.events);
                // renderEvents(result.events)


                addEvents(obj.events, true);

                $("body").css({'overflow':'auto'});
                $("#grid").css({'overflow':'auto'});
            }
        });
}


function addEvents(events, prepend) {
    if (events.length > 0) {

        if(prepend) {
        for (i = events.length; i > 0 ; i--) {

            var event = events[i-1];
            // appendPre(event.summary + ' (' + when + ')')
            // console.log(event);
            apppendEvent(event, prepend);
        }

        }else {
            for (i = 1; i < events.length; i++) {
            var event = events[i];

            // appendPre(event.summary + ' (' + when + ')')
            // console.log(event);
            apppendEvent(event, prepend);
        }
        }

    }
    beautifySchedule();
}

function apppendEvent(event, prepend) {
        var weekday = new Array(7);
        weekday[0] =  "Нд";
        weekday[1] = "Пн";
        weekday[2] = "Вт";
        weekday[3] = "Ср";
        weekday[4] = "Чт";
        weekday[5] = "Пт";
        weekday[6] = "Сб";
        var month = new Array(12);
            month[0] = "січ";
            month[1] = "лют";
            month[2] = "бер";
            month[3] = "кві";
            month[4] = "тра";
            month[5] = "чер";
            month[6] = "лип";
            month[7] = "сер";
            month[8] = "вер";
            month[9] = "жов";
            month[10] = "лис";
            month[11] = "гру";


        var date = new Date(event.start.dateTime),
            date_end = new Date(event.end.dateTime)

        var grid = $("#grid");
            calend_event = $('<div class="row-cell" ></div>'),
            row_el = $("<div class='row-el'></div>"),
            grid_cell = $("<div class='grid-cell'></div>"),
            day = $("<h2 class='day today' data-day='"+event.start.dateTime+"' style='display:none;'></h2>"),
            day_name = $("<div class='day-name'></div>").text(weekday[date.getDay()]),
            day_num = $("<div class='day-num' data-month="+date.getMonth()+"></div>").text( date.getDate() +' '+ month[date.getMonth()] +'.');

        //appending

        grid_cell.append(day.append(day_name).append(day_num))

        var presentation =  $('<div class="presentation item first"></div>'),
            block_time = $('<div class="right-block block-time" ></div> ').text(minutes(date.getHours()) +':'+minutes(date.getMinutes())+' – '+minutes(date_end.getHours()) +':'+ minutes(date_end.getMinutes()) ),
            blob_block = $('<div class="right-block blob-block resource " ></div> '),
            blob_text = $('<div class="blob-text blob-resource " ></div> ').append(" <html-blob>"+event.summary+' ('+ event.organizer.email+') <span> '+ event.location+ "</span> </html-blob>"),
            circle = $('<div role="gridcell" class="right-block circle">'),
            circle_box = $('<div class="circle-box"></div>'),
            circle_inner = $('<div class="circle-inner " style="border-color: #E4C441;"></div>'),
            circle_text = $('<span class="circle-text"></span>').text(event.summary);
        //appending
          presentation.append(block_time)
                      .append(blob_block.append(blob_text))
                      .append(circle.append(circle_inner.append(circle_text)));
          if(prepend) {
              grid.prepend(calend_event.append(row_el.append(grid_cell).append(presentation)));
          }else {
            grid.append(calend_event.append(row_el.append(grid_cell).append(presentation)));
          }

      }

      $("document").ready(function () {
            beautifySchedule();

      });

var scroll_active = true;

function to_wait(_callback) {
    $("#grid").css({'overflow':'hidden'});
    $("body").css({'overflow':'hidden'});
    loadMore();
    _callback();
}


function to_wait_top(_callback) {
    $("#grid").css({'overflow':'hidden'});
    $("body").css({'overflow':'hidden'});
    loadBefore();
    _callback();
}



$(window).scroll(function() {
    if($(window).scrollTop() == $(document).height() - $(window).height()) {
        console.log("scrolled")
        if(scroll_active) {
            scroll_active = false;
            to_wait(function() {
                scroll_active=true;
            })
        }
    }else if($(window).scrollTop() == 0) {
        if (scroll_active) {
            scroll_active = false;
            to_wait_top(function () {
                scroll_active = true;
            })
        }
    }
});



