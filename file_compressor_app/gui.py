import file_creator

import PySimpleGUI as pg

label1 = pg.Text("Select Files to compress: ")
input1 = pg.Input(key='file_input')
choose_button1 = pg.FilesBrowse("Choose", key='file_choose')

label2 = pg.Text("Select destination folder: ")
input2 = pg.Input(key='dest_input')
choose_button2 = pg.FolderBrowse("Choose", key='dest_choose')
output_label = sg.text(key='output_label')

compress_button = pg.Button("Compress", key='compress', text_color = 'green')

window = pg.Window('File Zipper', layout=[[label1, input1, choose_button1],
                                          [label2, input2, choose_button2],
                                          [compress_button, output_label],)



while True:

    event, values = window.read()
    print(event, values)

    file_paths = values['file_input'].split(';')
    dest_path = values['dest_input']

    file_creator.make_archive(file_paths, dest_path)
    window["output"].update(value="Compression Completed")






window.close()