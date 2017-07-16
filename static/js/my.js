$('#exampleModalLong').on('show.bs.modal', function (e) {
    var button = $(e.relatedTarget)
    var detail = button.data('whatever')
    var modal = $(this)
    modal.find('.modal-body textarea').val(detail)
})