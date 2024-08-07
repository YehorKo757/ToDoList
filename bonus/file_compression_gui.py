import FreeSimpleGUI

label1 = FreeSimpleGUI.Text("Select files to compress:")
input1 = FreeSimpleGUI.Input()
choose_button1 = FreeSimpleGUI.FilesBrowse("Choose")

label2 = FreeSimpleGUI.Text("Select destination folder:")
input2 = FreeSimpleGUI.Input()
choose_button2 = FreeSimpleGUI.FolderBrowse("Choose")

compress_button = FreeSimpleGUI.Button("Compress")

window = FreeSimpleGUI.Window("File Compressor",
                              layout=[[label1, input1, choose_button1],
                                      [label2, input2, choose_button2],
                                      [compress_button]])

window.read()
window.close()