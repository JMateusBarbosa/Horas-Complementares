document.querySelector('form').addEventListener('submit', function(event) {
    var nome = document.getElementById('nome').value;
    var email = document.getElementById('email').value;
    var senha = document.getElementById('senha').value;

    var errorMessage = '';

    if (nome === '') {
        errorMessage += 'O campo Nome é obrigatório.\n';
    }

    if (email === '') {
        errorMessage += 'O campo E-mail é obrigatório.\n';
    }

    if (senha === '') {
        errorMessage += 'O campo Senha é obrigatório.\n';
    }

    if (errorMessage !== '') {
        alert(errorMessage);
        event.preventDefault();
    }
});

document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        var formData = new FormData(form);

        fetch('/register', {
            method: 'POST',
            body: formData
        })
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            alert(data.message);
            form.reset();
        })
        .catch(function(error) {
            console.error(error);
            alert('Erro ao enviar o formulário');
        });
    });
});
