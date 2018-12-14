$(document).ready(function() {
    $('#searchForm').submit(function() {
        $("#container").hide();
        $("#loadDiv").show()

        return true;
    });
});
