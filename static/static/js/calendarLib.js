/**
 * Created by StasMaster on 06.08.18.
 */

function loadMore() {
var button = $('.after'),
    spinner = '<span class="spinner"></span>';

	if (!button.hasClass('loading')) {
		button.toggleClass('loading').html(spinner);
	}



    $.ajax(
        {
            url: "http://127.0.0.1:8000/calendar/json/",
            data: {
                date: $(".row-cell:last-child .day").attr("data-day"),
                loadBefore: false,
            },
           type: 'POST',
            async: true,
            success: function(result){
                button.toggleClass('loading').html("Завантажити");
                $("body").scrollTop($(".button").offset().top);
                var obj = JSON.parse(result);
                console.log(obj.events);
                // renderEvents(result.events)
                addEvents(obj.events, false)
            }
        });
}

function loadBefore() {
    var button = $('.before'),
    spinner = '<span class="spinner"></span>';

	if (!button.hasClass('loading')) {
		button.toggleClass('loading').html(spinner);
	}

    console.log($(".row-cell:first-child .day").attr("data-day"));

    $.ajax(
        {
            url: "http://127.0.0.1:8000/calendar/json/",
            data: {
                date: $(".row-cell:first-child .day").attr("data-day"),
                loadBefore: true,
            },
           type: 'POST',
            async: true,
            success: function(result){
                button.toggleClass('loading').html("Завантажити");
                $("body").scrollTop($(".button").offset().top);
                var obj = JSON.parse(result);
                console.log(obj.events);
                // renderEvents(result.events)
                addEvents(obj.events, true)
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
            day = $("<h2 class='day today' data-day='"+event.start.dateTime+"'></h2>"),
            day_name = $("<div class='day-name'></div>").text(weekday[date.getDay()]),
            day_num = $("<div class='day-num'></div>").text( date.getDate() +' '+ month[date.getMonth()] +'.');

        //appending

        grid_cell.append(day.append(day_name).append(day_num))

        var presentation =  $('<div class="presentation item first"></div>'),
            block_time = $('<div class="right-block block-time" ></div> ').text(date.getHours()+':'+date.getMinutes() +' – '+date_end.getHours()+':'+date.getMinutes()),
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

