import FreeSimpleGUI
from zip_creator import make_archive

label1 = FreeSimpleGUI.Text("Select files to compress:")
input1 = FreeSimpleGUI.Input(key="input_files")
choose_button1 = FreeSimpleGUI.FilesBrowse("Choose",
                                           key="Choose_files")

label2 = FreeSimpleGUI.Text("Select destination folder:")
input2 = FreeSimpleGUI.Input(key="input_folder")
choose_button2 = FreeSimpleGUI.FolderBrowse("Choose",
                                            key="Choose_folder")

compress_button = FreeSimpleGUI.Button("Compress")
output = FreeSimpleGUI.Text(key="output",
                            text_color="red")

window = FreeSimpleGUI.Window("File Compressor",
                              layout=[[label1, input1, choose_button1],
                                      [label2, input2, choose_button2],
                                      [compress_button, output]])
while True:
    event, values = window.read()
    print(event, values)
    try:
        filepaths = values["input_files"].split(";")
        folder = values["input_folder"]
    except:
        break
    match event:
        case "Compress":
            make_archive(filepaths, folder)
            window["output"].update(value="Compression completed!")
        case FreeSimpleGUI.WIN_CLOSED:
            break

window.close()
