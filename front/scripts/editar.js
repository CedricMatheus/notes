/*****************************************************
SCRIPT DE CONTROLE DA REGRA DE NEGÓCIO EDITAR
*****************************************************/
//ao carregar documento
$(document).ready(function() {
    // verifica se existe id de nota na sessão
    if (sessionStorage.id_nota) {
        // efetuando requisição ajax
        $.ajax({
            // obtendo dados da sessão
            data: obter_sessao(),
            //definindo o tipo de requisição como post
            type: 'POST',
            //url da api do servidor
            url: 'http://127.0.0.1:8000/notas/carregar/',
            //requisição efetuada com sucesso
            success: function(resposta) {
                // transforma response em um objeto json
                resposta = JSON.parse(resposta);
                // se o estado da requisição for de sucesso
                if (resposta.estado === 'sucesso') {
                    // obtendo json da nota
                    var nota = JSON.parse(resposta.mensagem);
                    // obtendo dados da nota
                    nota = nota[0].fields;
                    console.log(nota)
                    // atribuindo titulo ao formulário editar
                    $('#titulo').val(nota.titulo)
                    // atribuindo corpo da nota ao formulário editar
                    $('#nota').val(nota.nota)
                // se não for sucesso
                } else {
                    // exibe mensagem de erro
                    alert(resposta.mensagem);
                    // carregando página de notas
                    window.open('notas.html', '_self');
                }
            },
        });
    } else {
        // exibe mensagem de erro
        alert('Ocorreu um erro inesperdao!');
        // carregando página de notas
        window.open('notas.html', '_self');
    }
});