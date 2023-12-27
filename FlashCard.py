from PyQt5 import QtCore, QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow,QInputDialog,QLineEdit,QMessageBox,QColorDialog,QFileDialog, QGraphicsScene, QGraphicsView, QGraphicsItem, QGraphicsEllipseItem, QGraphicsRectItem,QGraphicsItem, QAction, QFileDialog, QColorDialog,QGraphicsTextItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem, QGraphicsItemGroup, QVBoxLayout, QPushButton, QWidget,QGraphicsPixmapItem,QGraphicsRectItem,QGraphicsEllipseItem,QGraphicsPolygonItem
from PyQt5.QtCore import Qt ,QPoint,QPointF
from PyQt5.QtGui import QTextCursor, QTextCharFormat,QFont,QTextListFormat,QTextBlockFormat,QTextImageFormat,QPixmap,QPainter,QColor, QPen,QBrush,QPolygonF
import sys
import json
import time
import os
import io
from PIL import Image
from Main_Window import Ui_MainWindow
from Add_basic_window import Ui_AddFlashCard
from select_image_window import Ui_ImgSelectWindow
from image_editing_window import Ui_ImgEditWindow
from show_answer_window import Ui_show_question_window
from category_window import Ui_show_answer_window
from show_card_window import Ui_show_card_window
from finish_cards_window import Ui_finish_window
class FlashCardApp(QMainWindow):
    #constructor of FlashCardApp Class
    def __init__(self):
        super(FlashCardApp, self).__init__()

        #creat object of ui class that we create import from Main_Window file  
        self.ui=Ui_MainWindow() 
        self.ui.setupUi(self)
        self.ui.deck_name_list_widget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.deck_name_list_widget.customContextMenuRequested.connect(self.ui.showContextMenu)

        self.add_window=QtWidgets.QMainWindow()
        self.add_card_ui =Ui_AddFlashCard()
        self.add_card_ui.setupUi(self.add_window) 

        self.image_edit_window =QtWidgets.QMainWindow()
        self.imgEdit_ui=Ui_ImgEditWindow()
        self.imgEdit_ui.setupUi(self.image_edit_window)

        self.image_select_window =QtWidgets.QMainWindow()
        self.imgSelect_ui=Ui_ImgSelectWindow()
        self.imgSelect_ui.setupUi(self.image_select_window)

        self.show_card_widow=QtWidgets.QMainWindow()
        self.show_card_ui=Ui_show_card_window()
        self.show_card_ui.setupUi(self.show_card_widow)

        self.show_question_window=QtWidgets.QMainWindow()
        self.show_question_ui=Ui_show_question_window()
        self.show_question_ui.setupUi(self.show_question_window)

        self.show_answer_window=QtWidgets.QMainWindow()
        self.show_answer_ui=Ui_show_answer_window()
        self.show_answer_ui.setupUi(self.show_answer_window)
        #self.image_select_window.show()

        self.finish_window=QtWidgets.QMainWindow()
        self.finish_ui=Ui_finish_window()
        self.finish_ui.setupUi(self.finish_window)

        #List Of Deck Name
        self.deck_list=[]

        #Dictionary of Key:deck with value:list of new,learn,due count and cards name of deck
        self.dic={}
        
        self.currFront_ImgDic={}
        self.currBack_ImgDic={}
        #load all previous decks
        self.dic['Time']=[0,0,0]
        self.Load_Decks()
        self.update_speed_label()

        #print(self.dic)

        self.current_index=self.ui.deck_name_list_widget.currentRow()
        self.ui.new_list_widget.setCurrentRow(self.current_index)
        self.ui.learn_list_widget.setCurrentRow(self.current_index)
        self.ui.due_list_widget.setCurrentRow(self.current_index)

        # Connect Buttons (deck,add card,stat,dark_mode) On top to every window
        self.ui.add_button.clicked.connect(self.Add_FlashCard)
        self.ui.dark_mode_radio_button.clicked.connect(self.Toggle_dark_mode)
        #self.ui.deck_button.clicked.connect(lambda :self.Decks())
        self.ui.stat_button.clicked.connect(self.Stats)

        self.show_card_ui.add_button.clicked.connect(self.Add_FlashCard)
        self.show_card_ui.dark_mode_radio_button.clicked.connect(self.Toggle_dark_mode)
        self.show_card_ui.deck_button.clicked.connect(lambda:self.Decks(self.show_card_widow))
        self.show_answer_ui.stat_button.clicked.connect(self.Stats)

        self.show_question_ui.add_button.clicked.connect(self.Add_FlashCard)
        self.show_question_ui.dark_mode_radio_button.clicked.connect(self.Toggle_dark_mode)
        self.show_question_ui.deck_button.clicked.connect(lambda:self.Decks(self.show_question_window))
        self.show_question_ui.stat_button.clicked.connect(self.Stats)

        self.show_answer_ui.add_button.clicked.connect(self.Add_FlashCard)
        self.show_answer_ui.dark_mode_radio_button.clicked.connect(self.Toggle_dark_mode)
        self.show_answer_ui.deck_button.clicked.connect(lambda:self.Decks(self.show_answer_window))
        self.show_answer_ui.stat_button.clicked.connect(self.Stats)

        self.finish_ui.add_button.clicked.connect(self.Add_FlashCard)
        self.finish_ui.dark_mode_radio_button.clicked.connect(self.Toggle_dark_mode)
        self.finish_ui.deck_button.clicked.connect(lambda:self.Decks(self.finish_window))
        self.finish_ui.stat_button.clicked.connect(self.Stats)

        self.ui.create_deck_button.clicked.connect(self.Add_deck) 
        self.ui.actionExit.triggered.connect(self.exit)


        self.ui.rename_action.triggered.connect(self.Rename_deck)
        self.ui.remove_action.triggered.connect(self.Remove_deck)
        self.ui.add_deck.triggered.connect(self.Add_deck)
        self.ui.movedown_action.triggered.connect(self.Move_down_deck)
        self.ui.moveup_action.triggered.connect(self.Move_up_deck)
        #create tool boxobject

        # connect with front text widget 
        self.add_card_ui.bold_button.clicked.connect(lambda:self.format_text_bold(self.add_card_ui.front_text))
        self.add_card_ui.italic_button.clicked.connect(lambda :self.format_text_italic(self.add_card_ui.front_text))
        self.add_card_ui.underline_button.clicked.connect(lambda:self.format_text_underline(self.add_card_ui.front_text))
        self.add_card_ui.font_color_button.clicked.connect(lambda:self.set_font_color(self.add_card_ui.front_text))
        self.add_card_ui.highlight_button.clicked.connect(lambda:self.set_text_highlight(self.add_card_ui.front_text))
        self.add_card_ui.bullete_button.clicked.connect(lambda:self.insert_bullet_point(self.add_card_ui.front_text))
        self.add_card_ui.numbered_buttton.clicked.connect(lambda:self.insert_numbered_bullet_point(self.add_card_ui.front_text))
        self.add_card_ui.left_align_button.clicked.connect(lambda: self.set_text_alignment(Qt.AlignLeft,self.add_card_ui.front_text))
        self.add_card_ui.right_align_button.clicked.connect(lambda: self.set_text_alignment(Qt.AlignRight,self.add_card_ui.front_text))
        self.add_card_ui.center_align_button.clicked.connect(lambda: self.set_text_alignment(Qt.AlignCenter,self.add_card_ui.front_text))
        self.add_card_ui.image_insert_button.clicked.connect(lambda: self.insert_image(self.add_card_ui.front_text))
        #self.add_card_ui.font_size_spin.valueChanged.connect(self.set_font_size)
        self.add_card_ui.font_size_spin.setRange(1, 44)# Set a reasonable range for font size
        self.add_card_ui.font_size_spin.setValue(10)# Set default font size
        self.add_card_ui.font_size_spin.valueChanged.connect(lambda size:self.set_font_size(size,self.add_card_ui.front_text))
        self.add_card_ui.font_style_combobox.currentFontChanged.connect(lambda style:self.set_font_style(style,self.add_card_ui.front_text))
        
        #connet with back text widget 
        self.add_card_ui.bold_button.clicked.connect(lambda:self.format_text_bold(self.add_card_ui.back_text))
        self.add_card_ui.italic_button.clicked.connect(lambda :self.format_text_italic(self.add_card_ui.back_text))
        self.add_card_ui.underline_button.clicked.connect(lambda:self.format_text_underline(self.add_card_ui.back_text))
        self.add_card_ui.font_color_button.clicked.connect(lambda:self.set_font_color(self.add_card_ui.back_text))
        self.add_card_ui.highlight_button.clicked.connect(lambda:self.set_text_highlight(self.add_card_ui.back_text))
        self.add_card_ui.bullete_button.clicked.connect(lambda:self.insert_bullet_point(self.add_card_ui.back_text))
        self.add_card_ui.numbered_buttton.clicked.connect(lambda:self.insert_numbered_bullet_point(self.add_card_ui.back_text))
        self.add_card_ui.left_align_button.clicked.connect(lambda: self.set_text_alignment(Qt.AlignLeft,self.add_card_ui.back_text))
        self.add_card_ui.right_align_button.clicked.connect(lambda: self.set_text_alignment(Qt.AlignRight,self.add_card_ui.back_text))
        self.add_card_ui.center_align_button.clicked.connect(lambda: self.set_text_alignment(Qt.AlignCenter,self.add_card_ui.back_text))
        self.add_card_ui.image_insert_button.clicked.connect(lambda:self.insert_image(self.add_card_ui.back_text))
        #self.add_card_ui.font_size_spin.valueChanged.connect(self.set_font_size)
        self.add_card_ui.font_size_spin.setRange(1, 44)# Set a reasonable range for font size
        self.add_card_ui.font_size_spin.setValue(10)# Set default font size
        self.add_card_ui.font_size_spin.valueChanged.connect(lambda size:self.set_font_size(size,self.add_card_ui.back_text))
        self.add_card_ui.font_style_combobox.currentFontChanged.connect(lambda style:self.set_font_style(style,self.add_card_ui.back_text))

        #connect flash card options combobox
        self.add_card_ui.flash_card_options.activated.connect(lambda:self.change_window(self.add_card_ui.flash_card_options))
        self.imgSelect_ui.flash_card_options.activated.connect(lambda:self.change_window(self.imgSelect_ui.flash_card_options))
        #self.imgEdit_ui.flash_card_options.activated.connect(self.change_window_edit_img)

        self.imgSelect_ui.select_image_button.clicked.connect(self.Insert_image_in_Label)

        self.imgEdit_ui.pushButton.clicked.connect(self.save_scene) #############
        self.imgEdit_ui.pushButton_2.clicked.connect(lambda:self.close_window(self.image_edit_window))

        # image edition variables
        self.imgEdit_ui.zoomIn_button.clicked.connect(self.zoom_in)
        self.imgEdit_ui.zoomOut_button.clicked.connect(self.zoom_out)
        self.imgEdit_ui.image_fit_button.clicked.connect(self.zoom_fit)
        self.imgEdit_ui.rec_shape_button.clicked.connect(self.draw_rectangle)
        self.imgEdit_ui.circle_shape_button.clicked.connect(self.draw_oval)
        self.imgEdit_ui.toolButton_4.clicked.connect(self.draw_polygon)
        self.imgEdit_ui.undo_button.clicked.connect(self.undo)
        self.imgEdit_ui.redo_button.clicked.connect(self.redo)
        self.imgEdit_ui.delete_button.clicked.connect(self.delete_item)
        self.imgEdit_ui.copy_button.clicked.connect(self.copy_item)
        self.imgEdit_ui.text_widget_button.clicked.connect(self.add_text)
        self.imgEdit_ui.see_button.clicked.connect(self.deselect_all_items)
        self.imgEdit_ui.image_insert_button.clicked.connect(self.Insert_image_in_Label)

        # self.imgEdit_ui.toolButton_28.clicked.connect(self.group_selected_items)
        # self.imgEdit_ui.toolButton_29.clicked.connect(self.ungroup_selected_item)
        
        self.imgEdit_ui.left_align_image_button.clicked.connect(lambda: self.set_align_image(Qt.AlignLeft))
        self.imgEdit_ui.right_align_image_button.clicked.connect(lambda: self.set_align_image(Qt.AlignRight))
        self.imgEdit_ui.center_align_image_button.clicked.connect(lambda: self.set_align_image(Qt.AlignCenter))

        self.draw_button_clicked = False
        self.rect_color = Qt.red
        self.begin, self.destination = QPoint(), QPoint()
        #self.imgEdit_ui.rec_shape_button.clicked.connect(self.toggle_draw_rec_button)

        self.sceneItems =[]
        self.deletedItems=[]
        self.reversed_flag=False

        # connect List Entry with function
        self.ui.deck_name_list_widget.itemClicked.connect(self.do_something)
        # connect for store flash card 
        self.add_card_ui.add_button.clicked.connect(lambda:self.save_text(self.add_card_ui.front_text))
        self.add_card_ui.add_button.clicked.connect(lambda:self.save_text(self.add_card_ui.back_text))
        self.add_card_ui.close_button.clicked.connect(lambda:self.close_window(self.add_window))
        self.add_card_ui.front_text.cursorPositionChanged.connect(self.cursor_position_changed)
        self.add_card_ui.back_text.cursorPositionChanged.connect(self.cursor_position_changed)

        self.show_card_ui.pushButton.clicked.connect(self.Show_cards)

        self.show_question_ui.show_answer_button.clicked.connect(self.Show_answer)
        self.show_question_ui.save_changes_button.clicked.connect(self.save_changes_que)

        self.show_answer_ui.save_changes_button.clicked.connect(self.save_changes_ans)
        self.show_answer_ui.again_button.clicked.connect(self.Next_card)
        self.show_answer_ui.hard_button.clicked.connect(self.Next_card)
        self.show_answer_ui.good_button.clicked.connect(self.Next_card)
        self.show_answer_ui.easy_button.clicked.connect(self.Next_card)


    ################# Flash Card Viewing Functionalities #####################
    
    #open Flashh Card For Preticular deck
    def Show_cards(self):
        self.show_card_widow.close()
        self.deck_name=self.show_card_ui.deck_name_label.text()
        # totalCrads_in_deck=self.dic[self.deck_name][3]
        # itr=self.dic[self.deck_name][4]
        self.count=0

        #while(self.count<totalCrads_in_deck):
        # file_directory = f".\\data\\{self.deck_name}\\card_{self.dic[self.deck_name][4]}" 
        # self.front_file_path = f"{file_directory}\\front_{self.dic[self.deck_name][4]}.html"
        # self.load_text(self.front_file_path,self.show_question_ui.front_text)
        self.Show_question()
        # After user Clicked show answer Button Then close que window show answer window with both que. ned answer
    
    # Show card's front(Question) text
    def Show_question(self):
        if(self.count>=self.dic[self.deck_name][3]):
            self.finish_window.show()
            return 
        
        if(self.dic[self.deck_name][4] < self.dic[self.deck_name][5]):
            self.dic[self.deck_name][8]=0
        elif(self.dic[self.deck_name][4]>=self.dic[self.deck_name][5] and self.dic[self.deck_name][4]<(self.dic[self.deck_name][5]+self.dic[self.deck_name][6])):
            self.dic[self.deck_name][8]=1
        else:
            self.dic[self.deck_name][8]=2

        flag=self.dic[self.deck_name][8]


        if flag ==0 :
            file_directory = f".\\data\\{self.deck_name}\\Basic\\card_{self.dic[self.deck_name][4]}" 
            self.front_file_path = f"{file_directory}\\front_{self.dic[self.deck_name][4]}.html"
            self.load_text(self.front_file_path,self.show_question_ui.front_text)
        elif flag==1:
            file_directory = f".\\data\\{self.deck_name}\\Basic (and Reversed card)\\card_{self.dic[self.deck_name][4]}" 
            self.front_file_path = f"{file_directory}\\front_{self.dic[self.deck_name][4]}.html"
            self.load_text(self.front_file_path,self.show_question_ui.front_text)

        elif flag==2:
            file_directory = f".\\data\\{self.deck_name}\\Image Occlusion\\card_{self.dic[self.deck_name][4]}" 
            # jpg ,png ,...
            self.front_file_path = f"{file_directory}\\front_{self.dic[self.deck_name][4]}.jpg"
            #self.load_text(self.front_file_path,self.show_question_ui.front_text)
            #inser image here 
            self.load_card_as_image(self.front_file_path,self.show_question_ui.front_text)
            
        self.start_time=time.time()
        self.show_question_window.show()
  
    #Show card's back(answer) text 
    def Show_answer(self):
        flag=self.dic[self.deck_name][8]
        if flag ==0 :
            file_directory = f".\\data\\{self.deck_name}\\Basic\\card_{self.dic[self.deck_name][4]}" 
            self.front_file_path = f"{file_directory}\\front_{self.dic[self.deck_name][4]}.html"
            self.back_file_path = f"{file_directory}\\back_{self.dic[self.deck_name][4]}.html"
            self.load_text(self.front_file_path,self.show_answer_ui.front_text)
            self.load_text(self.back_file_path,self.show_answer_ui.back_text)


        elif flag==1:
            file_directory = f".\\data\\{self.deck_name}\\Basic (and Reversed card)\\card_{self.dic[self.deck_name][4]}" 
            self.front_file_path = f"{file_directory}\\front_{self.dic[self.deck_name][4]}.html"
            self.back_file_path = f"{file_directory}\\back_{self.dic[self.deck_name][4]}.html"
            self.load_text(self.front_file_path,self.show_answer_ui.front_text)
            self.load_text(self.back_file_path,self.show_answer_ui.back_text)            

        elif flag==2:
            file_directory = f".\\data\\{self.deck_name}\\Image Occlusion\\card_{self.dic[self.deck_name][4]}"
            # jpg ,png ,...
            self.front_file_path = f"{file_directory}\\front_{self.dic[self.deck_name][4]}.jpg"
            self.back_file_path = f"{file_directory}\\back_{self.dic[self.deck_name][4]}.jpg"
            self.load_card_as_image(self.front_file_path,self.show_answer_ui.front_text)
            self.load_card_as_image(self.back_file_path,self.show_answer_ui.back_text)
            

        self.show_question_ui.front_text.clear()
        self.show_question_window.close()
        self.show_answer_window.show()

    #Move To Next Card Of current deck
    def Next_card(self): 
        if self.dic[self.deck_name][8]==1:
            self.swap_file_content(self.front_file_path, self.back_file_path)
        self.show_answer_ui.front_text.clear()
        self.show_answer_ui.back_text.clear()
        self.show_answer_window.close()

        self.count+=1
        self.dic[self.deck_name][4]=(self.dic[self.deck_name][4]+1)%(self.dic[self.deck_name][3])
    
        if self.dic[self.deck_name][2]<self.dic[self.deck_name][3]:
            self.dic[self.deck_name][2]+=1

        if self.dic[self.deck_name][0]>=1:
            self.dic[self.deck_name][0]-=1
        self.end_time=time.time()

        take_time = round(self.end_time - self.start_time, 2)

        self.dic['Time'][1]+=take_time
        self.dic['Time'][0]+=1
        self.dic['Time'][2]=self.dic['Time'][1] / self.dic['Time'][0]
        self.dic['Time'][2] = round(self.dic['Time'][2], 2)

        self.save_decks()
        self.Load_Decks()
        self.update_speed_label()
        self.Show_question()

    # swap file content 
    def swap_file_content(self,file_path1, file_path2):
        # Read data from File 1
        with open(file_path1, 'r',errors='ignore') as file1:
            data1 = file1.read()

        # Read data from File 2
        with open(file_path2, 'r',errors='ignore') as file2:
            data2 = file2.read()

        # Write data from File 2 to File 1
        with open(file_path1, 'w',errors='ignore') as file1:
            file1.write(data2)

        # Write data from File 1 to File 2
        with open(file_path2, 'w',errors='ignore') as file2:
            file2.write(data1)
 
    #Update Speed Label That is on main_window
    def update_speed_label(self):
        s=f"Studied {self.dic['Time'][0]} cards in {self.dic['Time'][1]} seconds today {self.dic['Time'][2]} s/card"
        self.ui.card_count_Label.setText(s)
    
    #Save Changes when viewing flashCard 
    def save_changes_que(self):
        rich_text_content = self.show_question_ui.front_text.toHtml()

        with open(self.front_file_path, 'w',errors='ignore') as file:
            file.write(rich_text_content)

    def save_changes_ans(self):
        rich_text_content = self.show_answer_ui.front_text.toHtml()

        with open(self.front_file_path, 'w',errors='ignore') as file:
            file.write(rich_text_content)
        
        rich_text_content = self.show_answer_ui.back_text.toHtml()

        with open(self.back_file_path, 'w',errors='ignore') as file:
            file.write(rich_text_content)   
    
   #Load saved card text in Widget 
    def load_text(self, file_path,text_edit):
        try:
            with open(file_path, 'r',errors='ignore') as file:
                # Read the HTML content from the file
                rich_text_content = file.read()

                # Set the HTML content in the QTextEdit
                text_edit.setHtml(rich_text_content)
        except Exception as e:
            print(f"Error: {e}")
    
    # When Click on any deck entry from List Widget Show Window For Show Their Cards
    def do_something(self,item):
        deck_name =item.text()
        self.show_card_ui.deck_name_label.setText(f"{item.text()}")
        self.show_card_ui.new_entry_label.setText(f"{self.dic[deck_name][0]}")
        self.show_card_ui.learnig_entry_label_2.setText(f"{self.dic[deck_name][1]}")
        self.show_card_ui.to_review_entry_label.setText(f"{self.dic[deck_name][2]}")
        self.close()
        self.show_card_widow.show()
        print(f"{item.text()} clicked at row {self.ui.deck_name_list_widget.row(item)}")

    def insert_image_At_position(self,text_edit):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Open Image', '', 'Images (*.png *.xpm *.jpg *.bmp);;All Files (*)')

        if file_path:
            image_format = QTextImageFormat()
            image_format.setName(file_path)

            image_format.setWidth(100)
            image_format.setHeight(100)
            
            # Get the text cursor
            cursor = text_edit.textCursor()

            # Set the cursor position to the second position (index 1)
            cursor.setPosition(1)

            # # Set the modified cursor back to the QTextEdit widget
            #text_edit.setTextCursor(cursor)
            # cursor = text_edit.textCursor()
            
            if cursor:
                cursor.insertImage(image_format)

    # Get every time cursor position form text widgets 
    def cursor_position_changed(self):
        #cursor = self.add_card_ui.front_text.textCursor()
        self.front_position = self.add_card_ui.front_text.textCursor().position()
        print("front Position:", self.front_position)

        self.back_position = self.add_card_ui.back_text.textCursor().position()
        print("front Position:", self.back_position)

    # save text in file from text Widget
    def save_text(self,text_edit):
        deck_name= self.add_card_ui.Deck_Options.currentText()
        card_type=self.add_card_ui.flash_card_options.currentText()

        if deck_name:
            
            if text_edit is self.add_card_ui.front_text :
                file_directory = f".\\data\\{deck_name}\\{card_type}\\card_{self.dic[deck_name][3]}" 
                file_path = f"{file_directory}\\front_{self.dic[deck_name][3]}.html"
            elif text_edit is self.add_card_ui.back_text:
                file_directory = f".\\data\\{deck_name}\\{card_type}\\card_{self.dic[deck_name][3]}"
                file_path = f"{file_directory}\\back_{self.dic[deck_name][3]}.html"
                
                
            #if file_path:
            rich_text_content = text_edit.toHtml()
            try:
                # Create the directory if it doesn't exist
                os.makedirs(file_directory, exist_ok=True)

                with open(file_path, 'w',errors='ignore') as file:
                    file.write(rich_text_content)
            except Exception as e:
                print(f"Error: {e}")
            
            # curr_cardNo= self.dic[deck_name][3]+5
            # if len(self.dic[deck_name]) <= curr_cardNo:
            #     pass
            #     #self.dic[deck_name].append([self.currFront_ImgDic,self.currBack_ImgDic])
            
            if text_edit is self.add_card_ui.back_text:
                self.dic[deck_name][3]+=1
                #self.dic[deck_name][4]+=1
                self.dic[deck_name][0]+=1
                
                if card_type=="Basic":
                    self.dic[deck_name][5]+=1
                elif card_type=="Basic (and Reversed card)":
                    self.dic[deck_name][6]+=1
            
            self.save_decks()
            self.Load_Decks()
            self.currBack_ImgDic.clear()
            self.currFront_ImgDic.clear()
            text_edit.clear()
        else:
            QMessageBox.critical(self.add_window, "Error", "Deck Required")

    def load_card_as_image(self,file_path,text_edit):
        if file_path:
                image_format = QTextImageFormat()
                image_format.setName(file_path)

                cursor = text_edit.textCursor()
                if cursor:
                    cursor.insertImage(image_format)

    def close_window(self,w):
        w.close()

    ######################### Image Editing functionalities #################################
        
    #insert image in label
    def Insert_image_in_Label(self):
        self.file_name,_= QFileDialog.getOpenFileName(self.image_select_window,"Select Image","C:\\Users\\Swayam\\OneDrive\\Pictures","All Files (*);; PNG Files(*.png);;JPG Files (*.jpg)")
        self.image_select_window.close()
        if self.file_name:
            pixmap = QPixmap(self.file_name)
            item = QGraphicsPixmapItem(pixmap)
            
            self.imgEdit_ui.scene.clear()
            self.imgEdit_ui.scene.addItem(item)
            # self.imgEdit_ui.view = QGraphicsView(self.imgEdit_ui.scene)
            self.imgEdit_ui.view.setRenderHint(QPainter.Antialiasing, True)
            self.imgEdit_ui.view.setRenderHint(QPainter.SmoothPixmapTransform, True)
            self.imgEdit_ui.view.setInteractive(True)
            self.image_edit_window.show()

    #save image 
    def save_scene(self):

        deck_name = self.imgEdit_ui.Deck_Options.currentText()

        if deck_name:
            # Get the bounding rectangle of all items in the scene
            scene_rect = self.imgEdit_ui.scene.itemsBoundingRect()

            # Create an image with a white background
            image = QPixmap(scene_rect.size().toSize())
            image.fill(Qt.white)

            # Create a painter to render the scene onto the image
            painter = QPainter(image)
            self.imgEdit_ui.scene.render(painter, target=QtCore.QRectF(image.rect()), source=scene_rect)
            painter.end()
            # Save the image to a file (you can adjust the file format as needed)

            self.save_image(deck_name)
            # Check if the directory exists, and create it if not
            file_directory = f".\\data\\{deck_name}\\Image Occlusion\\card_{self.dic[deck_name][3]}"
            if not os.path.exists(file_directory):
                try:
                    os.makedirs(file_directory)
                except OSError as e:
                    print(f"Error creating directory {file_directory}: {e}")
            # jpg ,png ,...
            _, file_extension = os.path.splitext(self.file_name)
            save_path = f"{file_directory}\\front_{self.dic[deck_name][3]}{file_extension}"
            image.save(save_path)
            self.dic[deck_name][3]+=1
            self.dic[deck_name][7]+=1
            self.dic[deck_name][0]+=1

            self.save_decks()
            self.Load_Decks()
            self.imgEdit_ui.scene.clear()

    def save_image(self,deck_name):
        # Open the image file
        with open(self.file_name, 'rb') as file:
            image_data = file.read()

        # Create a PIL Image object
        image = Image.open(io.BytesIO(image_data))

        # Specify the output path and filename in the output folder
        file_directory = f".\\data\\{deck_name}\\Image Occlusion\\card_{self.dic[deck_name][3]}"
        # Check if the directory exists, and create it if not
        if not os.path.exists(file_directory):
            try:
                os.makedirs(file_directory)
            except OSError as e:
                print(f"Error creating directory {file_directory}: {e}")
        # jpg ,png ,...
        _, file_extension = os.path.splitext(self.file_name)
        save_path = f"{file_directory}\\back_{self.dic[deck_name][3]}{file_extension}"

        # Save the image to the specified path
        image.save(save_path)

    #set alignment     
    def set_align_image(self, alignment):
        # Set alignment for image_label
        self.imgEdit_ui.image_label.setAlignment(alignment)

        # Set alignment for the view (assuming self.view is your QGraphicsView)
        self.imgEdit_ui.view.setAlignment(alignment)

        # # Update the scene rectangle to ensure correct display
        # self.imgEdit_ui.scene.setSceneRect(self.imgEdit_ui.view.rect())

        # # Update the QGraphicsView
        # self.imgEdit_ui.view.setScene(self.imgEdit_ui.scene)
    
    # Zoom In-Out functionalities
    def zoom_in(self):
        self.imgEdit_ui.view.scale(1.2,1.2)

    def zoom_out(self):
        self.imgEdit_ui.view.scale(1/1.2, 1/1.2)

    def zoom_fit(self):
        bounding_rect = self.imgEdit_ui.scene.itemsBoundingRect()

        if not bounding_rect.isNull():
            self.imgEdit_ui.view.setSceneRect(bounding_rect)
            self.imgEdit_ui.view.fitInView(bounding_rect, Qt.KeepAspectRatio) 
            
    def set_item_properties(self, item):
        if isinstance(item, QGraphicsTextItem):
            item.setTextInteractionFlags(Qt.TextEditorInteraction | Qt.TextSelectableByMouse)
            item.setFont(QFont("Arial", 12))
            item.setDefaultTextColor(Qt.black)
        else:
            pen = QPen()
            pen.setColor(Qt.black)
            item.setPen(pen)
            brush = QBrush(QColor(0, 0, 250))  # Semi-transparent red
            item.setBrush(brush)
        item.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)

    # Draw shapes
    def draw_rectangle(self):
        rect_item = QGraphicsRectItem(50, 50,200, 40)
        self.set_item_properties(rect_item)

        self.sceneItems.append(rect_item)

        self.imgEdit_ui.scene.addItem(rect_item)

    def draw_oval(self):
        oval_item = QGraphicsEllipseItem(50, 50, 150, 100)
        self.set_item_properties(oval_item)
        self.sceneItems.append(oval_item)
        self.imgEdit_ui.scene.addItem(oval_item)

    def draw_polygon(self):
        polygon_item = QGraphicsPolygonItem(QPolygonF([QPointF(50, 50), QPointF(150, 50), QPointF(100, 150)]))
        self.set_item_properties(polygon_item)
        self.sceneItems.append(polygon_item)
        self.imgEdit_ui.scene.addItem(polygon_item)

    #Add TextBox on image 
    def add_text(self):
        text, ok = QInputDialog.getText(self, 'Add Text', 'Enter your text:')
        if ok:
            text_item = QGraphicsTextItem(text)
            self.set_item_properties(text_item)
            text_item.setPos(50, 50)  # Adjust the position based on the scene coordinates
            self.sceneItems.append(text_item)
            self.imgEdit_ui.scene.addItem(text_item)
            text_item.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)

    #Undo and Redo
    def undo(self):
        item=self.sceneItems.pop()
        self.deletedItems.append(item)
        self.imgEdit_ui.scene.removeItem(item)

    def redo(self):
        item = self.deletedItems.pop()
        self.sceneItems.append(item)
        self.imgEdit_ui.scene.addItem(item)

    #Deselect All Item of scene widget 
    def deselect_all_items(self):
        self.imgEdit_ui.scene.clearSelection()

    # delete selected item from scene
    def delete_item(self):
        selected_items = self.imgEdit_ui.scene.selectedItems()
        for item in selected_items:
            self.sceneItems.append(item)
            self.imgEdit_ui.scene.removeItem(item)

    #copy selected item from scene
    def copy_item(self):
        selected_items = self.imgEdit_ui.scene.selectedItems()
        for item in selected_items:
            if isinstance(item, QGraphicsPixmapItem):
                # Handle copying of QGraphicsPixmapItem
                pixmap = item.pixmap()
                copy_item = QGraphicsPixmapItem(pixmap)
            elif isinstance(item, QGraphicsTextItem):
                # Handle copying of QGraphicsTextItem
                copy_item = QGraphicsTextItem(item.toPlainText())
                copy_item.setFont(item.font())
                copy_item.setDefaultTextColor(item.defaultTextColor())
            elif isinstance(item, QGraphicsRectItem):
                # Handle copying of QGraphicsRectItem
                copy_item = QGraphicsRectItem(item.rect())
            elif isinstance(item, QGraphicsEllipseItem):
                # Handle copying of QGraphicsEllipseItem
                copy_item = QGraphicsEllipseItem(item.rect())
            elif isinstance(item, QGraphicsPolygonItem):
                # Handle copying of QGraphicsPolygonItem
                copy_item = QGraphicsPolygonItem(item.polygon())

            self.set_item_properties(copy_item)
            copy_item.setPos(item.pos() + QPointF(20, 20))  # Adjust the position for the copy
            self.sceneItems.append(copy_item)
            self.imgEdit_ui.scene.addItem(copy_item)


    # Function For Change window when change Falsh Card Option
    def change_window(self,combo):
        if combo.currentText() == "Basic" or self.add_card_ui.flash_card_options.currentText() == "Basic (and Reversed card)":
            self.image_select_window.close()
            self.load_deck_in_combo(self.add_card_ui.Deck_Options)
            self.add_window.show()              
        else:
            self.add_window.close()
            self.load_deck_in_combo(self.imgSelect_ui.Deck_Options)
            self.load_deck_in_combo(self.imgEdit_ui.Deck_Options)
            self.image_select_window.show()

    # Load deck list in combobox 
    def load_deck_in_combo(self,combo):
        combo.clear()
        for i in range(len(self.deck_list)):
            combo.addItem(self.deck_list[i])

    ###################### Main window changes #########
            
    # Return To Deck List from any screen
    def Decks(self,win):
        win.close()
        self.Load_Decks()
        self.update()
        self.show()   

    #Open New Add Flash card window 
    def Add_FlashCard(self):
        #self.Toggle_dark_mode(self)
        # self.add_card_ui =Ui_AddFlashCard()
        # self.add_card_ui.setupUi(self.add_window)
        #self.add_card_ui.flash_card_options.activated(lambda: self.change_window(self.add_card_ui))
        # if self.add_card_ui.flash_card_options.currentText() == "Basic" or self.add_card_ui.flash_card_options.currentText() == "Basic (and Reversed card)":
        #     self.add_window.show()             
        # else :
        #     pass
        self.load_deck_in_combo(self.add_card_ui.Deck_Options)
        self.add_window.show()

    #Open Stat window
    def Stats(self):
        pass

    ######################## Deck Handeling Functions ########################

    # toggle mode
    def Toggle_dark_mode(self,dark_mode):
        if dark_mode:
            self.setStyleSheet("QMainWindow { background-color: #222; color: #FFF; }"
                                "QLabel { color: #FFF; }"
                                "QRadioButton { color: #FFF; }"
                                "QPushButton {  background-color: #333; color: #FFF; }"
                                "QFrame {  background-color: #333; color: #FFF; }"
                                "QListWidget{  background-color: #333; color: #FFF;border: 1px solid #222; }"
                                "QMenuBar{ background-color: #333; color: #FFF;}"
                                "QInputDialog{ background-color: #333; color: #FFF;}"
                                "QLineEdit{ background-color: #333; color: #FFF;}"
                                "QMessageBox{ background-color: #333; color: #FFF;}"
                                "QStatusBar{ background-color: #333; color: #FFF;}"
                                "QAction{ background-color: #333; color: #FFF;}"
                                "QGroupBox{ background-color: #333; color: #FFF;}"

                                ''' QMenuBar::item { background-color: #333; color: #FFF; }
                                    QMenuBar::item::selected { background-color: #555; color: #FFF; }
                                    QMenuBar::item::!active { background-color: #333; color: #FFF; }
                                    QMenu { background-color: #333; color: #FFF; }
                                    QMenu::item { background-color: #333; color: #FFF; }
                                    QMenu::item::selected { background-color: #555; color: #FFF; }
                                    QMenu::item::!active { background-color: #333; color: #FFF; } 
                                        '''
                                )
            self.add_window.setStyleSheet("QMainWindow { background-color: #222; color: #FFF; }"
                                "QLabel { color: #FFF; }"
                                "QRadioButton { color: #FFF; }"
                                "QPushButton {  background-color: #333; color: #FFF; }"
                                "QFrame {  background-color: #333; color: #FFF; }"
                                "QListWidget{  background-color: #333; color: #FFF;border: 1px solid #222; }"
                                "QMenuBar{ background-color: #333; color: #FFF;}"
                                "QInputDialog{ background-color: #333; color: #FFF;}"
                                "QLineEdit{ background-color: #333; color: #FFF;}"
                                "QMessageBox{ background-color: #333; color: #FFF;}"
                                "QStatusBar{ background-color: #333; color: #FFF;}"
                                "QAction{ background-color: #333; color: #FFF;}"
                                "QGroupBox{ background-color: #333; color: #FFF;border: 1px solid #222;}"

                                ''' QMenuBar::item { background-color: #333; color: #FFF; }
                                    QMenuBar::item::selected { background-color: #555; color: #FFF; }
                                    QMenuBar::item::!active { background-color: #333; color: #FFF; }
                                    QMenu { background-color: #333; color: #FFF; }
                                    QMenu::item { background-color: #333; color: #FFF; }
                                    QMenu::item::selected { background-color: #555; color: #FFF; }
                                    QMenu::item::!active { background-color: #333; color: #FFF; }
                                    
                                        ''')
            self.image_select_window.setStyleSheet("QMainWindow { background-color: #222; color: #FFF; }"
                                "QLabel { color: #FFF; }"
                                "QRadioButton { color: #FFF; }"
                                "QPushButton {  background-color: #333; color: #FFF; }"
                                "QFrame {  background-color: #333; color: #FFF; }"
                                "QListWidget{  background-color: #333; color: #FFF;border: 1px solid #222; }"
                                "QMenuBar{ background-color: #333; color: #FFF;}"
                                "QInputDialog{ background-color: #333; color: #FFF;}"
                                "QLineEdit{ background-color: #333; color: #FFF;}"
                                "QMessageBox{ background-color: #333; color: #FFF;}"
                                "QStatusBar{ background-color: #333; color: #FFF;}"
                                "QAction{ background-color: #333; color: #FFF;}"
                                "QGroupBox{ background-color: #333; color: #FFF;border: 1px solid #222;}"

                                ''' QMenuBar::item { background-color: #333; color: #FFF; }
                                    QMenuBar::item::selected { background-color: #555; color: #FFF; }
                                    QMenuBar::item::!active { background-color: #333; color: #FFF; }
                                    QMenu { background-color: #333; color: #FFF; }
                                    QMenu::item { background-color: #333; color: #FFF; }
                                    QMenu::item::selected { background-color: #555; color: #FFF; }
                                    QMenu::item::!active { background-color: #333; color: #FFF; }
                                    
                                        '''
                                )
            self.image_edit_window.setStyleSheet("QMainWindow { background-color: #222; color: #FFF; }"
                                "QLabel { color: #FFF; }"
                                "QRadioButton { color: #FFF; }"
                                "QPushButton {  background-color: #333; color: #FFF; }"
                                "QFrame {  background-color: #333; color: #FFF; }"
                                "QListWidget{  background-color: #333; color: #FFF;border: 1px solid #222; }"
                                "QMenuBar{ background-color: #333; color: #FFF;}"
                                "QInputDialog{ background-color: #333; color: #FFF;}"
                                "QLineEdit{ background-color: #333; color: #FFF;}"
                                "QMessageBox{ background-color: #333; color: #FFF;}"
                                "QStatusBar{ background-color: #333; color: #FFF;}"
                                "QAction{ background-color: #333; color: #FFF;}"
                                "QGroupBox{ background-color: #333; color: #FFF;border: 1px solid #222;}"

                                ''' QMenuBar::item { background-color: #333; color: #FFF; }
                                    QMenuBar::item::selected { background-color: #555; color: #FFF; }
                                    QMenuBar::item::!active { background-color: #333; color: #FFF; }
                                    QMenu { background-color: #333; color: #FFF; }
                                    QMenu::item { background-color: #333; color: #FFF; }
                                    QMenu::item::selected { background-color: #555; color: #FFF; }
                                    QMenu::item::!active { background-color: #333; color: #FFF; }
                                    
                                        '''
                                )
        
            self.show_card_widow.setStyleSheet("QMainWindow { background-color: #222; color: #FFF; }"
                                "QLabel { color: #FFF; }"
                                "QRadioButton { color: #FFF; }"
                                "QPushButton {  background-color: #333; color: #FFF; }"
                                "QFrame {  background-color: #333; color: #FFF; }"
                                "QListWidget{  background-color: #333; color: #FFF;border: 1px solid #222; }"
                                "QMenuBar{ background-color: #333; color: #FFF;}"
                                "QInputDialog{ background-color: #333; color: #FFF;}"
                                "QLineEdit{ background-color: #333; color: #FFF;}"
                                "QMessageBox{ background-color: #333; color: #FFF;}"
                                "QStatusBar{ background-color: #333; color: #FFF;}"
                                "QAction{ background-color: #333; color: #FFF;}"
                                "QGroupBox{ background-color: #333; color: #FFF;border: 1px solid #222;}"

                                ''' QMenuBar::item { background-color: #333; color: #FFF; }
                                    QMenuBar::item::selected { background-color: #555; color: #FFF; }
                                    QMenuBar::item::!active { background-color: #333; color: #FFF; }
                                    QMenu { background-color: #333; color: #FFF; }
                                    QMenu::item { background-color: #333; color: #FFF; }
                                    QMenu::item::selected { background-color: #555; color: #FFF; }
                                    QMenu::item::!active { background-color: #333; color: #FFF; }
                                    
                                        '''
                                )
            self.show_question_window.setStyleSheet("QMainWindow { background-color: #222; color: #FFF; }"
                                "QLabel { color: #FFF; }"
                                "QRadioButton { color: #FFF; }"
                                "QPushButton {  background-color: #333; color: #FFF; }"
                                "QFrame {  background-color: #333; color: #FFF; }"
                                "QListWidget{  background-color: #333; color: #FFF;border: 1px solid #222; }"
                                "QMenuBar{ background-color: #333; color: #FFF;}"
                                "QInputDialog{ background-color: #333; color: #FFF;}"
                                "QLineEdit{ background-color: #333; color: #FFF;}"
                                "QMessageBox{ background-color: #333; color: #FFF;}"
                                "QStatusBar{ background-color: #333; color: #FFF;}"
                                "QAction{ background-color: #333; color: #FFF;}"
                                "QGroupBox{ background-color: #333; color: #FFF;border: 1px solid #222;}"

                                ''' QMenuBar::item { background-color: #333; color: #FFF; }
                                    QMenuBar::item::selected { background-color: #555; color: #FFF; }
                                    QMenuBar::item::!active { background-color: #333; color: #FFF; }
                                    QMenu { background-color: #333; color: #FFF; }
                                    QMenu::item { background-color: #333; color: #FFF; }
                                    QMenu::item::selected { background-color: #555; color: #FFF; }
                                    QMenu::item::!active { background-color: #333; color: #FFF; }
                                    
                                        '''
                                )
            self.show_answer_window.setStyleSheet("QMainWindow { background-color: #222; color: #FFF; }"
                                "QLabel { color: #FFF; }"
                                "QRadioButton { color: #FFF; }"
                                "QPushButton {  background-color: #333; color: #FFF; }"
                                "QFrame {  background-color: #333; color: #FFF; }"
                                "QListWidget{  background-color: #333; color: #FFF;border: 1px solid #222; }"
                                "QMenuBar{ background-color: #333; color: #FFF;}"
                                "QInputDialog{ background-color: #333; color: #FFF;}"
                                "QLineEdit{ background-color: #333; color: #FFF;}"
                                "QMessageBox{ background-color: #333; color: #FFF;}"
                                "QStatusBar{ background-color: #333; color: #FFF;}"
                                "QAction{ background-color: #333; color: #FFF;}"
                                "QGroupBox{ background-color: #333; color: #FFF;border: 1px solid #222;}"

                                ''' QMenuBar::item { background-color: #333; color: #FFF; }
                                    QMenuBar::item::selected { background-color: #555; color: #FFF; }
                                    QMenuBar::item::!active { background-color: #333; color: #FFF; }
                                    QMenu { background-color: #333; color: #FFF; }
                                    QMenu::item { background-color: #333; color: #FFF; }
                                    QMenu::item::selected { background-color: #555; color: #FFF; }
                                    QMenu::item::!active { background-color: #333; color: #FFF; }
                                    
                                        '''
                                )

            self.finish_window.setStyleSheet("QMainWindow { background-color: #222; color: #FFF; }"
                                "QLabel { color: #FFF; }"
                                "QRadioButton { color: #FFF; }"
                                "QPushButton {  background-color: #333; color: #FFF; }"
                                "QFrame {  background-color: #333; color: #FFF; }"
                                "QListWidget{  background-color: #333; color: #FFF;border: 1px solid #222; }"
                                "QMenuBar{ background-color: #333; color: #FFF;}"
                                "QInputDialog{ background-color: #333; color: #FFF;}"
                                "QLineEdit{ background-color: #333; color: #FFF;}"
                                "QMessageBox{ background-color: #333; color: #FFF;}"
                                "QStatusBar{ background-color: #333; color: #FFF;}"
                                "QAction{ background-color: #333; color: #FFF;}"
                                "QGroupBox{ background-color: #333; color: #FFF;border: 1px solid #222;}"

                                ''' QMenuBar::item { background-color: #333; color: #FFF; }
                                    QMenuBar::item::selected { background-color: #555; color: #FFF; }
                                    QMenuBar::item::!active { background-color: #333; color: #FFF; }
                                    QMenu { background-color: #333; color: #FFF; }
                                    QMenu::item { background-color: #333; color: #FFF; }
                                    QMenu::item::selected { background-color: #555; color: #FFF; }
                                    QMenu::item::!active { background-color: #333; color: #FFF; }
                                    
                                        '''
                                )

        else:
            self.setStyleSheet("")
            self.add_window.setStyleSheet("")
            self.image_select_window.setStyleSheet("")
            self.image_edit_window.setStyleSheet("")
            self.show_card_widow.setStyleSheet("")
            self.show_question_window.setStyleSheet("")
            self.show_answer_window.setStyleSheet("")
            self.finish_window.setStyleSheet("")

    # Load All deck list in list widget from json file
    def Load_Decks(self):
        try:
            with open('data.json','r') as file:
                stored_decks=json.load(file)
                self.deck_list=stored_decks['list_data']
                self.dic=stored_decks['dict_data']
        except FileNotFoundError:
            pass
        self.ui.deck_name_list_widget.clear()
        self.ui.new_list_widget.clear()
        self.ui.learn_list_widget.clear()
        self.ui.due_list_widget.clear()

        self.ui.deck_name_list_widget.addItems(self.deck_list)
        new_list=[]
        learn_list=[]
        due_list=[]
        for name in self.deck_list:
            new_list.append(str(self.dic[name][0]))
            learn_list.append(str(self.dic[name][1]))
            due_list.append(str(self.dic[name][2]))

        print(self.deck_list)
        print(self.dic)
            
        self.ui.new_list_widget.addItems(new_list)
        self.ui.learn_list_widget.addItems(learn_list)
        self.ui.due_list_widget.addItems(due_list)
            

        self.ui.deck_name_list_widget.setCurrentRow(0)
        self.ui.new_list_widget.setCurrentRow(0)
        self.ui.learn_list_widget.setCurrentRow(0)
        self.ui.due_list_widget.setCurrentRow(0)

    # Save Decks in json file
    def save_decks(self):
        with open('data.json', 'w') as file:
            json.dump({'list_data': self.deck_list, 'dict_data': self.dic}, file)
    
    # Create new Deck
    def Add_deck(self):
        curr_index= self.ui.deck_name_list_widget.currentRow()
        text , ok = QInputDialog.getText(self,"Creat Deck","New deck name:")
        if ok and len(text)>0:
            # add decks in text widget also in List and dictionary
            self.ui.deck_name_list_widget.insertItem(curr_index,text) 
            self.deck_list.insert(curr_index,text)
            self.dic[text]=[]

           
            self.ui.new_list_widget.insertItem(curr_index,"0")
            self.dic[text].append(0)
            self.ui.learn_list_widget.insertItem(curr_index,"0") 
            self.dic[text].append(0)
            self.ui.due_list_widget.insertItem(curr_index,"0") 
            self.dic[text].append(0)    

            # Number of flash Cards
            self.dic[text].append(0)
            # current flash_card
            self.dic[text].append(0)
            # Basic Flash_Card 
            self.dic[text].append(0)
            #Reverser_card 
            self.dic[text].append(0)
            #Image Card 
            self.dic[text].append(0)
            # Card Identity Flag
            self.dic[text].append(0)

            print(self.dic)
            print(self.deck_list)
            self.save_decks()
    
    #Rename Deck
    def Rename_deck(self):
        curr_index=self.ui.deck_name_list_widget.currentRow()
        deck=self.ui.deck_name_list_widget.item(curr_index) # gives entry at index not text 

        if deck is not None:
            text , ok = QInputDialog.getText(self,"Rename Deck","Edit deck name:",QLineEdit.Normal,deck.text())
            if ok and text is not None:
                #change in list and dic
                oldText=deck.text()
                index=self.deck_list.index(oldText)
                self.dic[text]=self.dic.pop(oldText)
                if index!=ValueError:
                    self.deck_list[index]=text
                #change in list widget 
                deck.setText(text)

        print(self.deck_list)
        print(self.dic)

    #Remove Deck from List and data base
    def Remove_deck(self):
        curr_index=self.ui.deck_name_list_widget.currentRow()
        deck=self.ui.deck_name_list_widget.item(curr_index)

        if deck is not None:
            question=QMessageBox.question(self,"Remove Deck",f"Do you want to delete {deck.text()} Deck?" ,QMessageBox.Yes | QMessageBox.No)
            if question == QMessageBox.Yes:

                #remove from List Widget and from deck list and dic
                text = self.ui.deck_name_list_widget.takeItem(curr_index)
                n=self.ui.new_list_widget.takeItem(curr_index)
                l=self.ui.learn_list_widget.takeItem(curr_index)
                d=self.ui.due_list_widget.takeItem(curr_index)
                del n,l,d
                oldText=deck.text()
                index=self.deck_list.index(oldText)
                del self.dic[oldText]
                if index!=ValueError:
                    del self.deck_list[index]
                del text

        print(self.deck_list)
        print(self.dic)
 
    #Sort List entry acrding to Name
    def Sort_deck(self):
        self.ui.deck_name_list_widget.sortItems()
        self.deck_list.sort()

        count= self.ui.deck_name_list_widget.count()
        for i in range(count):
            deck=self.ui.deck_name_list_widget.item(i).text()
            n=self.ui.new_list_widget.item(i)
            n.setText(str(self.dic[deck][0]))
            l=self.ui.learn_list_widget.item(i)
            l.setText(str(self.dic[deck][0]))
            d=self.ui.due_list_widget.item(i)
            d.setText(str(self.dic[deck][0]))

    #exit programm
    def exit(self):
        question = QMessageBox.question(self,"Quit","Do you want to quit ?",QMessageBox.Yes|QMessageBox.No)
        if question==QMessageBox.Yes:
            quit()
    
    #Move one up any selected deck
    def Move_up_deck(self):
        curr_index=self.ui.deck_name_list_widget.currentRow()

        deck=self.ui.deck_name_list_widget.item(curr_index)
        n=self.ui.new_list_widget.item(curr_index)
        l=self.ui.learn_list_widget.item(curr_index)
        d=self.ui.due_list_widget.item(curr_index)

        if curr_index>=1:
            up_index=curr_index-1
            upDeck=self.ui.deck_name_list_widget.item(up_index)
            un=self.ui.new_list_widget.item(up_index)
            ul=self.ui.learn_list_widget.item(up_index)
            ud=self.ui.due_list_widget.item(up_index)

            curr_text=deck.text()
            nc=n.text()
            lc=l.text()
            dc=d.text()
            up_text=upDeck.text()
            unc=un.text()
            ulc=ul.text()
            udc=ud.text()
            
            deck.setText(up_text)
            n.setText(unc)
            l.setText(ulc)
            d.setText(udc)

            upDeck.setText(curr_text)
            un.setText(nc)
            ul.setText(lc)
            ud.setText(dc)

    #Move one down any selected deck
    def Move_down_deck(self):
        curr_index=self.ui.deck_name_list_widget.currentRow()

        deck=self.ui.deck_name_list_widget.item(curr_index)
        n=self.ui.new_list_widget.item(curr_index)
        l=self.ui.learn_list_widget.item(curr_index)
        d=self.ui.due_list_widget.item(curr_index)

        if curr_index<=self.ui.deck_name_list_widget.count()-2:
            up_index=curr_index+1
            upDeck=self.ui.deck_name_list_widget.item(up_index)
            un=self.ui.new_list_widget.item(up_index)
            ul=self.ui.learn_list_widget.item(up_index)
            ud=self.ui.due_list_widget.item(up_index)

            curr_text=deck.text()
            nc=n.text()
            lc=l.text()
            dc=d.text()
            up_text=upDeck.text()
            unc=un.text()
            ulc=ul.text()
            udc=ud.text()
            
            deck.setText(up_text)
            n.setText(unc)
            l.setText(ulc)
            d.setText(udc)

            upDeck.setText(curr_text)
            un.setText(nc)
            ul.setText(lc)
            ud.setText(dc)

    ######################## ToolBox Functions ########################

    # insertImage in textwidget
    def insert_image(self,text_edit):
        if text_edit is self.add_card_ui.front_text:
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getOpenFileName(self.add_window, f'Open Image', '', 'Images (*.png *.xpm *.jpg *.bmp);;All Files (*)')
            if file_path:
                image_format = QTextImageFormat()
                image_format.setName(file_path)

                image_format.setWidth(300)
                image_format.setHeight(150)

                cursor = text_edit.textCursor()
                if cursor:
                    cursor.insertImage(image_format)

                #self.currFront_ImgDic[file_path]=self.front_position

        elif text_edit is self.add_card_ui.back_text:
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getOpenFileName(self, f'Open Image', '', 'Images (*.png *.xpm *.jpg *.bmp);;All Files (*)')

            if file_path:
                image_format = QTextImageFormat()
                image_format.setName(file_path)

                image_format.setWidth(100)
                image_format.setHeight(100)

                cursor = text_edit.textCursor()
                if cursor:
                    cursor.insertImage(image_format)
            #self.currBack_ImgDic[file_path]=self.back_position

        print(self.currFront_ImgDic)
        print(self.currBack_ImgDic)
    
    # Bold Sleceted Text
    def format_text_bold(self,text_edit):
        cursor = text_edit.textCursor()
        current_format = cursor.charFormat()
        new_format = QTextCharFormat(current_format)

        # Toggle between making text bold and removing bold formatting
        if current_format.fontWeight() == QFont.Bold:
            new_format.setFontWeight(QFont.Normal)
        else:
            new_format.setFontWeight(QFont.Bold)

        # Explicitly set the format to ensure toggling
        self.apply_formatting(new_format,text_edit)

    # Italic Sleceted Text
    def format_text_italic(self,text_edit):
        cursor= text_edit.textCursor()
        current_format = cursor.charFormat()
        new_format = QTextCharFormat(current_format)
        new_format.setFontItalic(not current_format.fontItalic())
        self.apply_formatting(new_format,text_edit)
    
    # UnderLine Sleceted Text
    def format_text_underline(self,text_edit):
        cursor = text_edit.textCursor()
        current_format=cursor.charFormat()
        new_format = QTextCharFormat(current_format)
        new_format.setUnderlineStyle(not current_format.fontUnderline())
        self.apply_formatting(new_format,text_edit)
    
    # set font size that is in spin box
    def set_font_style(self, font,text_edit):
        cursor = text_edit.textCursor()
        current_format=cursor.charFormat()
        new_format = QTextCharFormat(current_format)
        new_format.setFont(font)
        self.apply_formatting(new_format,text_edit)

    # set font style that is in font combobox 
    def set_font_size(self, size,text_edit):
        cursor = text_edit.textCursor()
        current_format=cursor.charFormat()
        new_format = QTextCharFormat(current_format)
        new_format.setFontPointSize(size)
        self.apply_formatting(new_format,text_edit)

    # Change Font color of Sleceted Text
    def set_font_color(self,text_edit):
        color = QColorDialog.getColor()
        if color.isValid():
            cursor= text_edit.textCursor()
            current_format = cursor.charFormat()
            new_format = QTextCharFormat(current_format)
            new_format.setForeground(color)
            self.apply_formatting(new_format,text_edit)
    
    # Change Background Color of Sleceted Text
    def set_text_highlight(self,text_edit):
        color = QColorDialog.getColor()
        if color.isValid():
            cursor= text_edit.textCursor()
            current_format = cursor.charFormat()
            new_format = QTextCharFormat(current_format)
            new_format.setBackground(color)
            self.apply_formatting(new_format,text_edit)

    def apply_formatting(self, text_format,text_edit):
        cursor = text_edit.textCursor()
        if not cursor.hasSelection():
            return
        cursor.mergeCharFormat(text_format)
    
    #Inser Bullet Point in text
    def insert_bullet_point(self,text_edit):
        cursor = text_edit.textCursor()
        cursor.insertList(QTextListFormat.ListDisc)
    
    # Insert Numbered bullet Points Text
    def insert_numbered_bullet_point(self,text_edit):
        cursor = text_edit.textCursor()
        cursor.insertList(QTextListFormat.ListDecimal)

    # set alignment of text in TextWidget
    def set_text_alignment(self, alignment,text_edit):
        cursor = text_edit.textCursor()
        block_format = cursor.blockFormat()
        block_format.setAlignment(alignment)
        cursor.setBlockFormat(block_format)
    
    #save data when close event accource
    def closeEvent(self, event):
        self.save_decks()
        event.accept()
    

def window():
    app = QApplication(sys.argv)
    win = FlashCardApp()
    win.show()
    sys.exit(app.exec_())

window()


