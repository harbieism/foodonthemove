$(document).ready(function () {

    function refreshData(){
        $.ajax({
            url: 'list_ticket/',
            type: 'get',
            success: function(data) {
                $(".searchable").empty();
                $.each(data, function(index, value){
                    name_col = "<td class='col-xs-5'>" + value.first_name + " " + value.last_name + "</td>"
                    username_col = "<td class='col-xs-5'>" + value.username + "</td>"
                    if (value.is_paying == true){
                        paying_col = "<td class='col-xs-2'> $" + value.payment_amount + "</td>"
                    } else {
                        paying_col = "<td class='col-xs-2'><span class='glyphicon glyphicon-remove'></span></td>"
                    }

                    $(".searchable").append("<tr>" + name_col + username_col + paying_col + "</tr>");
                });
            },
            failure: function(data) { 
                alert('Got an error dude');
            }
        }); 
    };

    refreshData();

    $('#filter').keyup(function () {
        var rex = new RegExp($(this).val(), 'i');
        $('.searchable tr').hide();
        $('.searchable tr').filter(function () {
            return rex.test($(this).text());
        }).show();

    })


    $('#filter').click(function() {
        refreshData();
    })



});