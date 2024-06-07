# AWS Lambda Function para Enviar Email usando Amazon SES

**Explicação: Professor, não tenho cartão de crédito e não consigo criar uma conta por isso, fiz o trabalho utilizando o e-mail de um colega e deu certo, mas no trabalho coloquei meu próprio e-mail no qual não tenho conta na AWS**

## Descrição
Esta função AWS Lambda permite o envio de e-mails utilizando o Amazon Simple Email Service (SES). A função é implementada em Python e usa a biblioteca boto3 para comunicação com o SES.

## Entrada Esperada
A função está configurada para enviar um e-mail fixo sem necessitar de entrada específica. Para enviar e-mails com conteúdo dinâmico, o código pode ser modificado para aceitar parâmetros via um evento JSON.

## Saída Esperada
A função retorna um código de status 200 se o e-mail for enviado com sucesso. Em caso de erro, retorna um código de status 500.

## Dependências Externas
*boto3*: Biblioteca oficial da AWS para Python.

## Instruções:
  *Verificação de Endereços de E-mail no SES*:
  Verifique os endereços de e-mail do remetente e do destinatário no Amazon SES.

  *Criação da Função Lambda*:
  Crie uma nova função Lambda no console AWS.
  Insira o código fonte do arquivo lambda.py.
  Configure as permissões da função para permitir o envio de e-mails através do SES.

  *Teste da Função Lambda*:
  Utilize o console do AWS Lambda para configurar um evento de teste com um payload JSON simples {}.

## Teste e Depuração
  *Logs do CloudWatch*:
  A função Lambda gera logs no Amazon CloudWatch. Consulte esses logs para resolver possíveis problemas.

  *Eventos de Teste*:
  Configure eventos de teste no console do Lambda para simular diferentes entradas e verificar o comportamento da função.

## Exemplo de Evento de Teste:
Para enviar um e-mail com conteúdo dinâmico, você pode utilizar o seguinte evento de teste:

```json
{
  "recipient_email": "gabrielstocch@gmail.com",
  "subject": "Test Email AWS Lambda",
  "body_text": "This is a test email sent from an AWS Lambda.",
  "body_html": "<html><head></head><body><h1>Test Email AWS Lambda</h1><p>This is a test email sent from an AWS Lambda.</p></body></html>"
}