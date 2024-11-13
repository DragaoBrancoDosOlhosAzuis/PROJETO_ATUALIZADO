@echo off
REM Script para iniciar a API Ollama com o modelo Llama 3.2

REM Navega até a pasta ollama-api
echo Acessando a pasta do projeto ollama-api...
cd /d "C:\caminho\para\ollama-api"  REM Substitua pelo caminho correto da pasta

REM Baixa o modelo Llama 3.2
echo Baixando o modelo Llama versão 3.2...
ollama pull llama3.2

REM Inicia o VS Code na pasta atual (ollama-api)
echo Iniciando o Visual Studio Code...
code .

REM Aguardando para iniciar o servidor
timeout /t 2 >nul

REM Inicia o servidor da API
echo Iniciando o servidor da API...
start cmd /k "cd /d C:\caminho\para\ollama-api && node index.js"

echo API Ollama pronta para uso.
pause