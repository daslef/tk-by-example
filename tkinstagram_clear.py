# ----------------------------------- Необходимые модули ------------------------------------- #

import tkinter as  tk
import tkinter.simpledialog
import tkinter.filedialog
import tkinter.messagebox
from PIL import Image, ImageTk # хоть мы и пишем PIL, на самом деле используется форк Pillow, поэтому при отсутствии пакета ставим через pip install Pillow

# ----------------------- Функции Open, Save As, Share, Undo, Redo, Reset -------------------- #

def open_file():
    '''
    Open image
    '''
    filetypes = [('All Image Formats', '.jpeg .jpg .png .tiff .bmp .gif'), ('All Files', '.*')]
    filename = tkinter.filedialog.askopenfilename(title='Select Image', filetypes=filetypes)
    if not filename:
        return
    print(filename)


def save_file():
    '''
    Save image
    '''
    filename = tkinter.filedialog.asksaveasfilename()
    if not filename:
        return
    print(filename)

def share():
    '''
    Share image
    '''

    def share_email():
        nonlocal popup
        popup.withdraw() # окей, окно пропадает. но что если мы захотим его вернуть? обратный метод - deiconify
        email = tkinter.simpledialog.askstring('Wanna share by email?', 'Enter correct target email')
        print(email)
        popup.deiconify() # окно возвращается. вторым микрозаданием будет поднять его на передний план, пока же оно скрывается за родителем


    def share_vk():
        pass


    def share_fb():
        pass


    # метод share будет открывать всплывающее окно с тремя кнопками - VK, FB и EMAIL. Для этого нам понадобится виджет Toplevel
    # для установки координаты появления всплывающего окна в случае с Toplevel применяется метод geometry
    popup = tk.Toplevel(root)
    popup.title('Wanna share?')
    # мы отцентрировали левый верхний угол всплывающего окна
    # для абсолютного центрирования необходимо будет сделать поправку на геометрию виджета popup (размеры winfo_height и winfo_width)
    popup.geometry(f'+{root.winfo_x() + root.winfo_width() // 2}+{root.winfo_y() + root.winfo_height() // 2}')
    tk.Button(popup, text='VK', width=20, command=share_vk).pack(side=tk.LEFT, padx=15, pady=10)
    tk.Button(popup, text='FB', width=20, command=share_fb).pack(side=tk.LEFT, padx=15, pady=10)
    tk.Button(popup, text='EMAIL', width=20, command=share_email).pack(side=tk.LEFT, padx=15, pady=10)
    popup.focus_set()


def undo(event=None):
    '''
    Undo last change
    '''
    global current_state
    current_state -= 1
    print(STATES, current_state,sep='\n', end='\n\n')


def redo(event=None):
    '''
    Redo last change
    '''
    global current_state
    current_state += 1
    print(STATES, current_state,sep='\n', end='\n\n')


def reset():
    '''
    Return an image to initial state
    '''
    global current_state, STATES
    confirmed = tkinter.messagebox.askyesno('Confirm', 'All changes will be lost. Are you sure?')
    print(confirmed)
    if confirmed:
        current_state = 0 # у нас будет начальное состояние после загрузки файла в программу (исходное, без изменений)
        STATES = STATES[:1] # оставляем только исходное состояние 
    print(STATES, current_state,sep='\n', end='\n\n')


def filter_1():
    global current_state
    STATES.insert(current_state+1, 'filter1')
    current_state += 1


def filter_2():
    global current_state
    STATES.insert(current_state+1, 'filter2')
    current_state += 1


def filter_3():
    global current_state
    STATES.insert(current_state+1, 'filter3')
    current_state += 1


def filter_4():
    global current_state
    STATES.insert(current_state+1, 'filter4')
    current_state += 1


def filter_5():
    global current_state
    STATES.insert(current_state+1, 'filter5')
    current_state += 1


# ------------------------------- Создание корневого окна -------------------------------------#
# для отмены и возврата действий создадим список состояний - states, и индекс, который будет указывать на рабочее состояние

STATES = ['Initial']
current_state = 0

root = tk.Tk()

root.title('TkFilters')
root.configure(bg='white')

# --------------------------------- Стиль оформления кнопок ----------------------------------- #

button_style = {'fg': 'white', 'bg': 'black', 'font': ('Helvetica', 18)}
grid_style = {'padx': 5, 'pady': 5, 'sticky': 'nwes'}

# ------------- Начнем с создания и размещения кнопок OPEN, SAVE AS и SHARE-------------------- #
# ------------------------------  Строка - 0, Столбцы - 1, 2, 3 ------------------------------- #

open_button = tk.Button(root, **button_style, text='Open', command=open_file)
save_button = tk.Button(root, text='Save As', command=save_file,  **button_style)
share_button = tk.Button(root, text='Share', command=share,  **button_style)

open_button.grid(column=1, row=0, **grid_style)
save_button.grid(column=2, row=0, **grid_style)
share_button.grid(column=3, row=0, **grid_style)

# ------------- Теперь создадим и разместим кнопки UNDO, REDO и RESET------------------------ #
# ------------------------------  Строка - 6, Столбцы - 1, 2, 3 ------------------------------- #

undo_button = tk.Button(root, text='Undo', command=undo, **button_style)
redo_button = tk.Button(root, text='Redo', command=redo, **button_style)
reset_button = tk.Button(root, text='Reset', command=reset, **button_style)

undo_button.grid(column=1, row=6, **grid_style)
redo_button.grid(column=2, row=6, **grid_style)
reset_button.grid(column=3, row=6, **grid_style)

# ------------- Наконец, создадим и разместим кнопки бокового меню ---------------------------- #
# ------------------------------  Строки - 1, 2, 3, 4, 5, Столбец - 0 ------------------------- #

filter1_button = tk.Button(root, text='Filter1', command=filter_1, **button_style)
filter2_button = tk.Button(root, text='Filter2',command=filter_2, **button_style)
filter3_button = tk.Button(root, text='Filter3', command=filter_3, **button_style)
filter4_button = tk.Button(root, text='Filter4', command=filter_4, **button_style)
filter5_button = tk.Button(root, text='Filter5', command=filter_5, **button_style)

filter1_button.grid(column=0, row=1, **grid_style)
filter2_button.grid(column=0, row=2, **grid_style)
filter3_button.grid(column=0, row=3, **grid_style)
filter4_button.grid(column=0, row=4, **grid_style)
filter5_button.grid(column=0, row=5, **grid_style)

# ------------- Добавим последний элемент - label, хранящий изображение ----------------------- #
# ------------------------------  Строки - 1-5, Столбцы - 1-3 ------------------------- #

image_label = tk.Label(root)
image_label.grid(row=1, column=1, rowspan=5, columnspan=3, sticky='nwes') # rowspan и columnspan показывают, на сколько ячеек мы растягиваем виджет

image_src = Image.open(r'C:\Users\Dell\Pictures\yoda-e1481463137279.png')
image_tk = ImageTk.PhotoImage(image_src)

image_label.configure(image=image_tk) # тем самым я задал стартовое изображение. вряд ли это хорошая идея. поэтому четвертое микрозадание - добавить более подходящую исходную картинку

# ------------- Main Loop ---------------------------- #

# теперь забиндим undo и redo на комбинации клавиш
# как мы помним, при возникновении событий передается объект event, перепишем функции для его принятия

root.bind('<Control-z>', undo) # работает, но наверняка вы заметили странное поведение указателя current_state. это третье микрозадание
root.bind('<Control-y>', redo)
root.mainloop()
