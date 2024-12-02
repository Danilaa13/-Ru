from tkinter import *
import requests

window = Tk()

def btn_click():
    city = cityField.get()

    key = 'ffa785ba15c3d3af0c1092c47b754449'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params)
    weather = result.json()

    try:
        city_name = weather["name"]
        temp = weather["main"]["temp"]
        wind_speed = weather["wind"]["speed"]
        cloudiness = weather["clouds"]["all"]

        info['text'] = (f'{city_name}:\n'
                        f'Температура: {temp}°C\n'
                        f'Ветер: {wind_speed} м/с\n'
                        f'Облачность: {cloudiness}%')
    except KeyError:
        info['text'] = "Ошибка: Проверьте название города"

window['bg'] = '#fafafa'
window.title('Погода')
window.geometry('600x600')
window.wm_attributes('-topmost', 0.7)

window.resizable(False, False)

canvas = Canvas(window, width=600, height=600)
canvas.pack()

frame_top = Frame(window, bg='orange', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.3)

frame_bottom = Frame(window, bg='orange', bd=5)
frame_bottom.place(relx=0.30, rely=0.55, relwidth=0.40, relheight=0.2)

title = Label(window, text='Введите город', bg='brown', font=40)
title.place(relx=0.36, rely=0.15, width=150, height=30)
btn = Button(window, text='Посмотреть погоду', bg='white', command=btn_click)
btn.place(relx=0.29, rely=0.31, width=250, height=30)

cityField = Entry(frame_top, bg='white')
cityField.place(relx=0.05, rely=0.35, width=375, height=30)

info = Label(frame_bottom, text='Погодная информация', bg='orange', font=40, justify='left')
info.pack()

window.mainloop()
