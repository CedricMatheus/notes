/*****************************************************
SCRIPT DE CONTROLE DA REGRA DE NEGÓCIO NOTAS
*****************************************************/
//ao carregar documento
$(document).ready(function() {
        //efetuando requisição ajax
        $.ajax({
            // obtendo dados da sessão
            data: obter_sessao(),
            //definindo o tipo de requisição como post
            type: 'POST',
            //url da api do servidor
            url: 'http://127.0.0.1:8000/notas/listar/',
            //requisição efetuada com sucesso
            success: function(resposta) {
                // transforma response em um objeto json
                resposta = JSON.parse(resposta);
                // se o estado da requisição for de sucesso
                if (resposta.estado === 'sucesso') {
                    // obtendo json das notas
                    var notas = JSON.parse(resposta.mensagem);
                    // carrega o snippet de nota
                    $.get('snippets/nota.html', function (nota_snip) {
                        // percorrendo todas as notas
                        $.each(notas, function(chave, valor) {
                            // criando uma nova nota através do snippet
                            var nota = nota_snip;
                            // obtendo data
                            var data = valor.fields.data;
                            // tratando data
                            data = new Date(Date.parse(data)).toLocaleDateString();
                            // atribuindo id da nota
                            nota = nota.replace('#ID#', valor.pk);
                            // atribuindo o titulo da nota
                            nota = nota.replace('#TITULO#', valor.fields.titulo);
                            // atribuindo a data da nota
                            nota = nota.replace('#DATA#', data);
                            // adicionando nota a lista de notas
                            $('#notas').append(nota);
                        });
                    // definindo snippet como html
                    }, 'html');
                // se for vazio
                } else if (resposta.estado == 'vazia') {
                    // exibe mensagem
                    alert(resposta.mensagem);
                // se for erro
                } else {
                    // efetua logout
                    logout(resposta.mensagem);
                }
            },
        });
});