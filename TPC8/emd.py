import PySimpleGUI as sg
import emdDataset as data

parametros =[]

funcionalidades = [
    [sg.Button("Carregar")],
    [sg.Button("Listar")],
    [sg.Button("Modalidades")],
    [sg.Button("Por ano")],
    [sg.Button("Por clube")]
]

representacao = [
    [sg.Text(size=(60,1), key="_carregar_")],
    [sg.Listbox(values=parametros, size=(50,10), key="_representar_")]]


interface = [
    [
        sg.Column(funcionalidades),
        sg.VSeperator(),
        sg.Column(representacao),
    ]
]


window = sg.Window("Exames médicos",font="Helvetiva 24", 
                    default_element_size=(20,1)).Layout(interface)

stop = False
while not stop:
    event, values = window.read()  
    if event == sg.WIN_CLOSED:
        stop = True
    
    elif event=="Carregar":
        parametros.clear()
        window.find_element("_representar_").Update(values=parametros)
        window["_carregar_"].update("Estamos a carregar os EMDs disponíveis") 
        
    elif event=="Listar":
         window["_carregar_"].update("Aqui tem a lista por ordem cronológica decrescente dos nossos EMDs")
         parametros= data.listarDataset(data.BD)
         window.find_element("_representar_").Update(values=parametros)
    elif event == "Modalidades":
        window["_carregar_"].update("Até ao dia de hoje, testamos atletas das seguintes modalidades")
        parametros = data.modalidades(data.BD)
        window.find_element("_representar_").Update(values=parametros)
    elif event == "Por ano":
        window["_carregar_"].update("Uma janela nova está aberta com o gráfico que deseja")
        parametros.clear()
        window.find_element("_representar_").Update(values=parametros)
        data.plotDistrib(data.distrib(data.BD,1))
    elif event == "Por clube":
        window["_carregar_"].update("Uma janela nova está aberta com o gráfico que deseja")
        parametros.clear()
        window.find_element("_representar_").Update(values=parametros)
        data.plotDistrib(data.distrib(data.BD,8))

        
       

        
         
        
       

window.close()
