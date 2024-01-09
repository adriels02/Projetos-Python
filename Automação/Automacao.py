import openpyxl
import pyperclip
import pyautogui

workbook = openpyxl.load_workbook('C:\workspace\Python\Automação\produtos_ficticios.xlsx')
sheet_produtos = workbook['Produtos']

pyautogui.click(649,750,duration = 1)
pyautogui.click(99,9,duration = 1)

for linha in sheet_produtos.iter_rows(min_row = 2):

    nome_produto = linha[0].value
    pyautogui.hotkey('tab')
    pyperclip.copy(nome_produto)
    pyautogui.hotkey('ctrl', 'v') 
    pyautogui.hotkey('tab')

    descricao = linha[1].value
    pyperclip.copy(descricao)   
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('tab')

    categoria = linha[2].value
    pyperclip.copy(categoria)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('tab')

    codigo_produto = linha[3].value
    pyperclip.copy(codigo_produto)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('tab')

    peso = linha[4].value
    pyperclip.copy(peso)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('tab')

    dimensoes = linha[5].value
    pyperclip.copy(dimensoes)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    pyautogui.sleep(3)
    pyautogui.hotkey('tab')

    preco = linha[6].value
    pyperclip.copy(preco)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('tab')
    
    quantidade_estoque = linha[7].value
    pyperclip.copy(quantidade_estoque)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('tab')

    data_validade = linha[8].value
    pyperclip.copy(data_validade)
    pyautogui.hotkey('ctrl' , 'v')
    pyautogui.hotkey('tab')

    cor = linha[9].value
    pyperclip.copy(cor)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')

    tamanho = linha[10].value
    pyperclip.copy(tamanho)
    if (tamanho == 'Pequeno'):
     pyautogui.hotkey('enter')
    elif tamanho == 'Médio':
       pyautogui.keyDown('down')
       pyautogui.hotkey('enter')
    else:
       pyautogui.keyDown('down')
       pyautogui.keyDown('down')
       pyautogui.hotkey('enter')
    pyautogui.hotkey('tab')

    material = linha[11].value
    pyperclip.copy(material)
    pyautogui.hotkey('ctrl' , 'v')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')

    pyautogui.sleep(3)
    pyautogui.hotkey('tab')

    fabricante = linha[12].value
    pyperclip.copy(fabricante)
    pyautogui.hotkey('ctrl' , 'v')
    pyautogui.hotkey('tab')

    pais_origem = linha[13].value
    pyperclip.copy(pais_origem)
    pyautogui.hotkey('ctrl' , 'v')
    pyautogui.hotkey('tab')

    observacoes = linha[14].value
    pyperclip.copy(observacoes)
    pyautogui.hotkey('ctrl' , 'v')
    pyautogui.hotkey('tab')

    codigo_barras = linha[15].value
    pyperclip.copy(codigo_barras)
    pyautogui.hotkey('ctrl' , 'v')
    pyautogui.hotkey('tab')

    localizacao = linha[16].value
    pyperclip.copy(localizacao)
    pyautogui.hotkey('ctrl' , 'v')
    pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    pyautogui.sleep(1)
    pyautogui.hotkey('enter')
    pyautogui.sleep(3)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    pyautogui.sleep(3)