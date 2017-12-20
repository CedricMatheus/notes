/*****************************************************
SCRIPT DE CONTROLE DA REGRA DE NEGÓCIO GERAL
*****************************************************/
// função para obter dados da sessão em parametro url
function obter_sessao() {
    // criando variavel e obtendo sessão em string json
    var dados = JSON.stringify(sessionStorage);
    // convertendo string json em objeto json
    dados = JSON.parse(dados);
    // convertendo objeto json em parametro url
    dados = $.param(dados);
    // retornando dados da sessão
    return dados;
}


// função para efetuar logout
function logout(mensagem) {
    // removendo todos os dados da sessão
    sessionStorage.clear();
    // exibe mensagem de erro
    alert(mensagem);
    // carregando página de login
    window.open('login.html', '_self');
}


// função para obter id da nota
function obter_id(botao) {
    // retorna id referente a nota do botão clicado
    return botao.parent().siblings('.id_nota').html().trim();
}


// ao carregar documento
$(document).ready(function() {

    // REGRA DE REDIRECIONAMENTO
    // cria variavel e atribui nome do arquivo
    var arquivo = location.pathname.split('/').slice(-1)[0].split('.')[0];
    //se arquivo for diferente de login ou cadastro
    if (arquivo !== 'login' && arquivo !== 'cadastro') {
        // se não existe usuário salvo na sessão
        if (!sessionStorage.nome) {
            // carregando página de login
            window.open('login.html', '_self');
        }
    }


    // REGRA PARA ATRIBUIÇÃO DE NOME AO CAMPO LOGOUT
    // atribuindo nome ao campo logout
    $('#nome').append(sessionStorage.nome);
});

