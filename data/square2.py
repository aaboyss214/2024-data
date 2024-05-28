import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

# 예약 데이터를 저장하기 위한 딕셔너리
reservations = {}

# 기본 시설 목록
facilities = ["5호관", "서호관"]

class ReservationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Facility Reservation System")
        
        # 날짜 선택
        self.date_label = tk.Label(root, text="Select Date (YYYY-MM-DD):")
        self.date_label.grid(row=0, column=0)
        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=0, column=1)
        
        # 시설 선택
        self.facility_label = tk.Label(root, text="Select Facility:")
        self.facility_label.grid(row=1, column=0)
        self.facility_var = tk.StringVar(root)
        self.facility_var.set(facilities[0])
        self.facility_menu = tk.OptionMenu(root, self.facility_var, *facilities, command=self.show_available_times)
        self.facility_menu.grid(row=1, column=1)
        
        # 시간 선택 캔버스
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.grid(row=2, column=0, columnspan=2)
        self.canvas.bind("<Button-1>", self.select_time)

        # 예약 버튼
        self.reserve_button = tk.Button(root, text="Reserve", command=self.reserve)
        self.reserve_button.grid(row=3, column=0, columnspan=2)

        self.selected_time = None
        self.selected_facility = None

    def draw_times(self):
        self.canvas.delete("all")
        for i in range(24):
            x = i * 25
            color = "white"
            if 20 <= i < 22:
                color = "gray"
            self.canvas.create_rectangle(x, 50, x + 25, 150, fill=color, tags="time_slot")
            self.canvas.create_text(x + 12, 30, text=f"{i:02}:00", tags="time_text")
            self.canvas.create_text(x + 12, 170, text=f"{i + 1:02}:00", tags="time_text")

    def select_time(self, event):
        if event.y < 50 or event.y > 150:
            return
        hour = event.x // 25
        if 20 <= hour < 22:
            messagebox.showerror("Invalid Time", "20:00 to 22:00 is not available for reservation.")
            return
        
        self.selected_time = hour
        self.draw_times()
        self.canvas.create_rectangle(hour * 25, 50, hour * 25 + 25, 150, fill="blue", tags="selected_time")

    def reserve(self):
        date = self.date_entry.get()
        facility = self.facility_var.get()
        
        if self.selected_time is None:
            messagebox.showerror("Invalid Selection", "Please select a time by clicking on the canvas.")
            return

        try:
            reservation_time = datetime.strptime(f"{date} {self.selected_time:02}:00", "%Y-%m-%d %H:%M")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid date in the format YYYY-MM-DD.")
            return
        
        end_time = reservation_time + timedelta(hours=1)
        
        if facility not in reservations:
            reservations[facility] = []
        
        for start, end in reservations[facility]:
            if reservation_time < end and end_time > start:
                messagebox.showerror("Reservation Error", "This time slot is already reserved.")
                return
        
        reservations[facility].append((reservation_time, end_time))
        messagebox.showinfo("Reservation Success", f"Reserved {facility} from {reservation_time} to {end_time}")
        self.date_entry.delete(0, tk.END)
        self.canvas.delete("selected_time")
        self.selected_time = None

    def show_available_times(self, selected_facility):
        self.selected_facility = selected_facility
        self.draw_times()

if __name__ == "__main__":
    root = tk.Tk()
    app = ReservationSystem(root)
    root.mainloop()

