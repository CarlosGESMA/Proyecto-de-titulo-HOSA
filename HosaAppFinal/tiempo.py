
    
from datetime import datetime
import flet as ft

def main(page: ft.Page):

    time = datetime.now()

    def change_time(e):
        print(f"Time picker changed, value (minute) is {time_picker.value.hour} : {time_picker.value.minute}")
        horaActual1 =  f"{time_picker.value.hour}:{time_picker.value.minute}"
        horaActual2 =  f"{time.hour}:{time.minute}"
        print(f"hora1: {horaActual1}")
        print(f"hora2: {horaActual2}")

        if horaActual1 == horaActual2:
            print("PRENDER LUZ")

    def dismissed(e):
        print(f"Time picker dismissed, value is {time_picker.value}")

    time_picker = ft.TimePicker(
        confirm_text="Confirm",
        error_invalid_text="Time out of range",
        help_text="Pick your time slot",
        on_change=change_time,
        on_dismiss=dismissed,
    )

    page.overlay.append(time_picker)

    date_button = ft.ElevatedButton(
        "Pick time",
        icon=ft.icons.TIME_TO_LEAVE,
        on_click=lambda _: time_picker.pick_time(),
    )

    page.add(date_button)


ft.app(target=main)
