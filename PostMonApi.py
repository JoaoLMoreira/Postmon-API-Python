import requests
import json as js
import classAPI
import time as t


def SolicitaCEP():
    CEP = input('Digite o CEP para consulta  : ');
    return trataCEP(CEP)


def printa_linha():
    print('#--------------------------------------------#')

def mostramenu():
    printa_linha() 
    print('Info Cidadades:')
    printa_linha() 
    print('1 - Realizar busca')
    print('2 - Sair')
    printa_linha() 


def trataCEP(CEP):
    aux = CEP.replace('-', '')
    aux = aux.replace('.', '')
    tamanho = len(aux)
    while (tamanho != 8):
       SolicitaCEP()
    return aux 
            
def RealizaRequisicao(CEPR):
    urlPadrao = 'https://api.postmon.com.br/v1/cep/'
    urlrequest = urlPadrao + CEPR
    requisicao = requests.get(urlrequest)
    printacidade(js.loads(requisicao.content)) 
    
def printacidade(response):
    ObjJson =  classAPI.jsonclass(response)
    printa_linha()
    print('Estado: ' + ObjJson.Estado)
    print('Cidade: ' + ObjJson.Cidade)
    print('Bairro: ' + ObjJson.Bairro)
    print('logradouro: ' + ObjJson.Logradouro)
    print('Area do estado: ' + ObjJson.Estado_area_km2)
    print('Area da cidade: ' + ObjJson.Cidade_area_km2)
    print('Codigo do IBGE da cidade: ' + ObjJson.Cidade_codigo_ibge)
    printa_linha()
    

    
def iniciaAplicacao(): 
    
    while True:
        try:
            mostramenu()
            menu  = int(input('Digite: '))
            if(menu == 1):
                printa_linha()
                RealizaRequisicao(SolicitaCEP()) 
                
            elif (menu == 2):
                printa_linha() 
                print('Obrigado por usar o programa ! ') 
                printa_linha()
                t.sleep(5)
                exit()
            else:
                print('Digite ou 1 ou 2 !')
        except ValueError:
            printa_linha()
            print('Escolha entre 1 ou 2 !')
            printa_linha() 


iniciaAplicacao() 
input()
    
    