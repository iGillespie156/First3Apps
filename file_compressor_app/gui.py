import shutil as su

import PySimpleGUI as pg

label1 = pg.Text("Select Files to compress: ")
input1 = pg.Input()
choose_button1 = pg.FilesBrowse("Choose")

label2 = pg.Text("Select destination folder: ")
input2 = pg.Input()
choose_button2 = pg.FolderBrowse("Choose")

compress_button = pg.Button("Compress")

window = pg.Window('File Zipper', layout=[[label1, input1, choose_button1],
                                          [label2, input2, choose_button2],
                                          [compress_button]])

window.read()
window.close()