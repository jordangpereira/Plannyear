$(document).ready(function () { 
    $('#task-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget)
        const taskID = button.data('source')
        const content = button.data('content')

        const modal = $(this)
        if (taskID === 'Nova Tarefa') {
            modal.find('.modal-title').text(taskID)
            $('#task-form-display').removeAttr('taskID')
        } else {
            modal.find('.modal-title').text('Alterar Tarefa ' + taskID)
            $('#task-form-display').attr('taskID', taskID)
        }

        if (content) {
            modal.find('.form-control').val(content);
        } else {
            modal.find('.form-control').val('');
        }
    })


    $('#submit-task').click(function () {
        const tID = $('#task-form-display').attr('taskID');
        console.log($('#task-modal').find('.form-control').val())
        $.ajax({
            type: 'POST',
            url: tID ? '/todoThings/update/' + tID : '/todoThings/create',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#task-modal').find('.form-control').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.remove').click(function () {
        const remove = $(this)
        $.ajax({
            type: 'POST',
            url: '/todoThings/delete/' + remove.data('source'),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.state').click(function () {
        const state = $(this)
        const tID = state.data('source')
        var new_state = "A Fazer"

        if (state.text() === "Em Curso") {
            new_state = "Concluída"
        } else if (state.text() === "Concluída") {
            new_state = "A Fazer"
        } else if (state.text() === "A Fazer") {
            new_state = "Em Curso"
        }

        $.ajax({
            type: 'POST',
            url: '/todoThings/update/' + tID,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'status': new_state
            }),
            success: function (res) {
                console.log(res)
                location.reload();
            },
            error: function () { 
                console.log('Error');
            }
        });
    });

});