import PySimpleGUI as pg
import uncompressor

label1 = pg.Text("Select Files to uncompress: ")
input1 = pg.Input(key='file_input')
choose_button1 = pg.FileBrowse("Choose", key='file_choose')

label2 = pg.Text("Select destination folder: ")
input2 = pg.Input(key='dest_input')
choose_button2 = pg.FolderBrowse("Choose", key='dest_choose')

output_label = pg.Text(key='output_label',text_color="green")
uncompress_button = pg.Button("Uncompress", key='compress')

window = pg.Window('File UnZipper', layout=[[label1, input1, choose_button1],
                                          [label2, input2, choose_button2],
                                          [uncompress_button, output_label]])



while True:

    event, values = window.read()
    print(event, values)

    archive_path = values['file_input']
    dest_path = values['dest_input']

    uncompressor.uncompress(archive_path, dest_path)

    window["output_label"].update(value="Uncompression Completed")






window.close()