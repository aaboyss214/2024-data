import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os
from datetime import datetime, timedelta

USER_FILE = 'users.txt'

def user_exists(username):
    if not os.path.exists(USER_FILE):
        return False
    with open(USER_FILE, 'r', encoding='utf-8') as file:
        for line in file:
            stored_username, _, _ = line.strip().split(',')
            if stored_username == username:
                return True
    return False

def register_user(username, password, phone):
    if user_exists(username):
        return False, "Username already exists."
    with open(USER_FILE, 'a', encoding='utf-8') as file:
        file.write(f"{username},{password},{phone}\n")
    return True, "User registered successfully."

def authenticate_user(username, password):
    if not os.path.exists(USER_FILE):
        return False, "No users registered yet."
    with open(USER_FILE, 'r', encoding='utf-8') as file:
        for line in file:
            stored_username, stored_password, _ = line.strip().split(',')
            if stored_username == username:
                if stored_password == password:
                    return True, "Login successful."
                else:
                    return False, "Incorrect password."
    return False, "Username does not exist."

department_symptoms = {
    "정형외과": ["골절", "관절통", "허리통증", "목통증", "손목통증", "발목통증", "무릎통증"],
    "성형외과": ["성형수술", "화상", "흉터", "미용", "눈성형", "코성형", "주름제거"],
    "피부과": ["피부발진", "여드름", "두드러기", "건선", "습진", "탈모", "사마귀"],
    "내과": ["복통", "감기", "두통", "피로", "어지러움", "속쓰림", "변비", "설사", "고혈압", "당뇨"],
    "정신건강의학과": ["우울", "불안", "불면증", "스트레스", "공황장애", "강박증", "조울증"],
    "외과": ["수술", "외상", "종양", "복부통증", "탈장", "맹장염", "치핵"],
    "산부인과": ["임신", "생리통", "불임", "산후관리", "질염", "유방통", "폐경"],
    "마취통증의학과": ["수술마취", "통증관리", "신경차단", "만성통증", "관절염", "요통"],
    "신경외과": ["뇌출혈", "척수손상", "뇌졸중", "디스크", "뇌진탕", "경련", "편두통"],
    "재활의학과": ["재활치료", "물리치료", "운동치료", "근육통", "관절운동", "재활훈련"],
    "가정의학과": ["건강검진", "예방접종", "만성질환관리", "생활습관병", "다이어트", "금연상담"],
    "비뇨의학과": ["소변통증", "신장결석", "요로감염", "전립선질환", "발기부전", "성병"],
    "소아청소년과": ["소아발진", "소아감기", "소아열", "소아천식", "소아알레르기", "성장발달"],
    "이비인후과": ["코막힘", "목통증", "귀통증", "알레르기", "중이염", "축농증", "편도염"],
    "안과": ["눈통증", "시력저하", "눈부심", "안구건조증", "결막염", "백내장", "녹내장"],
    "영상의학과": ["X-ray", "CT", "MRI", "초음파검사", "뇌파검사", "골밀도검사"],
    "비뇨기과": ["신장결석", "방광염", "전립선염", "요도염", "요실금", "신우신염"],
    "신경과": ["두통", "어지러움", "경련", "치매", "신경통", "수전증", "근육마비"],
    "사상체질과": ["체질검사", "체질상담", "한방치료", "사상체질진단", "사상체질요법"],
    "침구과": ["침치료", "뜸치료", "한방물리치료", "부항치료", "추나요법"],
    "한방내과": ["한방진료", "한약처방", "한방치료", "체질치료", "한방다이어트"],
    "한방신경정신과": ["한방정신과진료", "한방우울증치료", "한방불면증치료"],
    "한방재활의학과": ["한방재활치료", "한방물리치료", "한방추나요법"],
    "보훈병원": ["보훈진료", "상해치료", "재활치료", "보훈의료"],
    "진단검사의학과": ["혈액검사", "소변검사", "조직검사", "유전자검사"],
    "구강악안면외과": ["구강수술", "턱교정수술", "악안면외상", "임플란트수술"],
    "예방치과": ["치아예방", "스케일링", "치아미백", "치아홈메우기"],
    "치과보존과": ["충치치료", "치아복원", "신경치료", "치아크라운"],
    "치과보철과": ["틀니", "임플란트", "브릿지", "의치"],
    "치주과": ["잇몸질환", "치주염", "잇몸출혈", "치아흔들림"],
    "예방의학과": ["예방접종", "건강검진", "건강상담", "건강교육"]
}

hospital_dict = {
    "정형외과": [
        "유플러스정형외과의원",
        "인천메트로정형외과의원",
        "연세으뜸의원",
        "학익정형외과의원",
        "박명주정형외과의원",
        "중앙메디칼의원",
        "성모프라임정형외과의원",
        "다나은서울의원",
        "푸른메디칼의원",
        "다사랑메디칼의원",
        "인천재활의원",
        "바로척정형외과의원"
    ],
    "소아청소년과": [
        "나무두리소아청소년과의원",
        "초록소아청소년과의원",
        "박이비인후과의원",
        "연세리더스내과의원",
        "준소아과의원",
        "탑신경외과",
        "코코이비인후과의원",
        "김철내과의원",
        "다사랑메디칼의원",
        "푸른메디칼의원",
        "인천위대한내과의원",
        "김가정의원"
    ],
    "내과": [
        "나무두리소아청소년과의원",
        "김은아의건강한내과의원",
        "초록소아청소년과의원",
        "박이비인후과의원",
        "연세리더스내과의원",
        "인하여성의원",
        "서울중앙의원",
        "탑신경외과",
        "코코이비인후과의원",
        "김철내과의원",
        "삼성수의원",
        "다사랑메디칼의원",
        "인천재활의원",
        "중앙메디칼의원",
        "푸른메디칼의원",
        "주안의원",
        "서울가정의원",
        "모아메디컬의원",
        "양지의원",
        "용현제일의원",
        "다나은서울의원",
        "인천위대한내과의원",
        "김가정의원"
    ],
    "피부과": [
        "나무두리소아청소년과의원",
        "맑고고운의원 인하대역",
        "초록소아청소년과의원",
        "연세리더스내과의원",
        "에이치봄의원",
        "미인도의원",
        "김철내과의원",
        "다사랑메디칼의원",
        "푸른메디칼의원",
        "다나은서울의원",
        "인천위대한내과의원"
    ],
    "성형외과": [
        "맑고고운의원 인하대역",
        "미인도의원"
    ],
    "정신건강의학과": [
        "인천마음벗정신건강의학과의원"
    ],
    "가정의학과": [
        "초록소아청소년과의원",
        "연세리더스내과의원",
        "연세으뜸의원",
        "현대가정의원",
        "인천지방법원부속의원",
        "주안의원",
        "서울가정의원",
        "다나은서울의원",
        "인천위대한내과의원",
        "김가정의원"
    ],
    "이비인후과": [
        "박이비인후과의원",
        "초록소아청소년과의원",
        "정이비인후과의원",
        "코코이비인후과의원",
        "김철내과의원",
        "다사랑메디칼의원",
        "푸른메디칼의원",
        "인천위대한내과의원",
        "김이비인후과의원"
    ],
    "산부인과": [
        "연세리더스내과의원",
        "인하여성의원"
    ],
    "신경과": [
        "연세리더스내과의원",
        "학익정형외과의원",
        "탑신경외과",
        "정항재신경과의원",
        "푸른메디칼의원",
        "모아메디컬의원",
        "인천위대한내과의원",
        "김가정의원"
    ],
    "영상의학과": [
        "연세리더스내과의원",
        "박명주정형외과의원"
    ],
    "예방의학과": [
        "연세리더스내과의원",
        "인천위대한내과의원"
    ],
    "외과": [
        "인천항외과의원",
        "학익정형외과의원",
        "전외과의원",
        "푸른메디칼의원"
    ],
    "마취통증의학과": [
        "인천메트로정형외과의원",
        "연세으뜸의원",
        "박명주정형외과의원",
        "다나은서울의원",
        "성모프라임정형외과의원",
        "바로척정형외과의원"
    ],
    "비뇨의학과": [
        "학익정형외과의원",
        "김철내과의원",
        "삼성수의원",
        "다사랑메디칼의원",
        "푸른메디칼의원",
        "모아메디컬의원"
    ],
    "안과": [
        "우성안과의원",
        "김철내과의원"
    ],
    "재활의학과": [
        "인천메트로정형외과의원",
        "연세으뜸의원",
        "박명주정형외과의원",
        "다사랑메디칼의원",
        "인천재활의원",
        "성모프라임정형외과의원",
        "바로척정형외과의원"
    ],
     "구강내과": [
        "서울바름치과의원",
        "하앤박치과의원",
        "다온미소치과의원",
        "연세꿈꾸는아이치과의원 인천용현점",
        "퍼스트민치과의원",
        "유어플란트치과의원",
        "사계절플러스치과의원",
        "맑은향기치과의원",
        "올플란트치과의원",
        "우성치과의원",
        "현대치과의원",
        "박경빈치과의원",
        "연세채움치과의원 인천",
        "네오연세치과의원",
        "김식만치과"
    ],
    "구강병리과": [
        "서울바름치과의원",
        "하앤박치과의원",
        "다온미소치과의원",
        "연세꿈꾸는아이치과의원 인천용현점",
        "퍼스트민치과의원",
        "유어플란트치과의원",
        "사계절플러스치과의원",
        "맑은향기치과의원",
        "올플란트치과의원",
        "우성치과의원",
        "현대치과의원",
        "박경빈치과의원",
        "연세채움치과의원 인천",
        "네오연세치과의원",
        "김식만치과"
    ],
    "구강악안면외과": [
        "서울바름치과의원",
        "하앤박치과의원",
        "다온미소치과의원",
        "연세꿈꾸는아이치과의원 인천용현점",
        "퍼스트민치과의원",
        "유어플란트치과의원",
        "사계절플러스치과의원",
        "맑은향기치과의원",
        "올플란트치과의원",
        "우성치과의원",
        "현대치과의원",
        "박경빈치과의원",
        "연세채움치과의원 인천",
        "네오연세치과의원",
        "김식만치과"
    ],
    "소아치과": [
        "서울바름치과의원",
        "하앤박치과의원",
        "다온미소치과의원",
        "SNC시카고치과의원",
        "연세꿈꾸는아이치과의원 인천용현점",
        "퍼스트민치과의원",
        "유어플란트치과의원",
        "사계절플러스치과의원",
        "맑은향기치과의원",
        "올플란트치과의원",
        "우성치과의원",
        "현대치과의원",
        "박경빈치과의원",
        "연세채움치과의원 인천",
        "네오연세치과의원",
        "김식만치과"
    ],
    "영상치의학과": [
        "서울바름치과의원",
        "하앤박치과의원",
        "다온미소치과의원",
        "연세꿈꾸는아이치과의원 인천용현점",
        "퍼스트민치과의원",
        "유어플란트치과의원",
        "사계절플러스치과의원",
        "맑은향기치과의원",
        "올플란트치과의원",
        "우성치과의원",
        "현대치과의원",
        "박경빈치과의원",
        "연세채움치과의원 인천",
        "네오연세치과의원",
        "김식만치과"
    ],
    "예방치과": [
        "서울바름치과의원",
        "하앤박치과의원",
        "다온미소치과의원",
        "연세꿈꾸는아이치과의원 인천용현점",
        "퍼스트민치과의원",
        "유어플란트치과의원",
        "사계절플러스치과의원",
        "맑은향기치과의원",
        "올플란트치과의원",
        "우성치과의원",
        "현대치과의원",
        "박경빈치과의원",
        "연세채움치과의원 인천",
        "네오연세치과의원",
        "김식만치과"
    ],
    "치과교정과": [
        "서울바름치과의원",
        "하앤박치과의원",
        "다온미소치과의원",
        "SNC시카고치과의원",
        "연세꿈꾸는아이치과의원 인천용현점",
        "퍼스트민치과의원",
        "유어플란트치과의원",
        "사계절플러스치과의원",
        "맑은향기치과의원",
        "올플란트치과의원",
        "우성치과의원",
        "현대치과의원",
        "박경빈치과의원",
        "연세채움치과의원 인천",
        "네오연세치과의원",
        "김식만치과"
    ],
    "치과보존과": [
        "서울바름치과의원",
        "하앤박치과의원",
        "다온미소치과의원",
        "SNC시카고치과의원",
        "연세꿈꾸는아이치과의원 인천용현점",
        "퍼스트민치과의원",
        "유어플란트치과의원",
        "사계절플러스치과의원",
        "맑은향기치과의원",
        "올플란트치과의원",
        "우성치과의원",
        "현대치과의원",
        "박경빈치과의원",
        "연세채움치과의원 인천",
        "네오연세치과의원",
        "김식만치과"
    ],
    "치과보철과": [
        "서울바름치과의원",
        "하앤박치과의원",
        "다온미소치과의원",
        "SNC시카고치과의원",
        "연세꿈꾸는아이치과의원 인천용현점",
        "퍼스트민치과의원",
        "유어플란트치과의원",
        "사계절플러스치과의원",
        "맑은향기치과의원",
        "올플란트치과의원",
        "우성치과의원",
        "현대치과의원",
        "박경빈치과의원",
        "연세채움치과의원 인천",
        "네오연세치과의원",
        "김식만치과"
    ],
    "치주과": [
        "서울바름치과의원",
        "하앤박치과의원",
        "다온미소치과의원",
        "연세꿈꾸는아이치과의원 인천용현점",
        "퍼스트민치과의원",
        "유어플란트치과의원",
        "사계절플러스치과의원",
        "맑은향기치과의원",
        "올플란트치과의원",
        "우성치과의원",
        "현대치과의원",
        "박경빈치과의원",
        "연세채움치과의원 인천",
        "네오연세치과의원",
        "김식만치과"
    ],
    "치과": [
        "다나치과의원",
        "구제훈치과의원",
        "현치과의원",
        "송원빈치과의원"
    ],
    "(통합치의학과)": [
        "하앤박치과의원",
        "다온미소치과의원",
        "연세꿈꾸는아이치과의원 인천용현점",
        "퍼스트민치과의원",
        "유어플란트치과의원",
        "사계절플러스치과의원",
        "맑은향기치과의원",
        "올플란트치과의원",
        "우성치과의원",
        "현대치과의원",
        "박경빈치과의원",
        "연세채움치과의원 인천",
    ],
    "침구과": [
        "안녕한의원",
        "우리한의원",
        "인천시원한의원",
        "성인천한의원",
        "다솜한의원",
        "경희최한의원",
        "감초한의원",
        "동남한의원",
        "석재홍한의원",
        "365엄지한방병원",
        "성제한의원",
        "동인한의원",
        "경희만석한의원",
        "덕윤한의원",
        "왕소연중국한의원",
        "덕창한의원",
        "박지영한의원",
        "임베문한의원",
        "바른한의원",
        "용현보화한의원"
    ],
    "한방내과": [
        "안녕한의원",
        "우리한의원",
        "인천시원한의원",
        "성인천한의원",
        "다솜한의원",
        "경희최한의원",
        "감초한의원",
        "동남한의원",
        "석재홍한의원",
        "성제한의원",
        "동인한의원",
        "경희만석한의원",
        "덕윤한의원",
        "왕소연중국한의원",
        "덕창한의원",
        "박지영한의원",
        "임베문한의원",
        "바른한의원",
        "용현보화한의원"
    ],
    "한방부인과": [
        "안녕한의원",
        "우리한의원",
        "인천시원한의원",
        "성인천한의원",
        "다솜한의원",
        "경희최한의원",
        "감초한의원",
        "동남한의원",
        "석재홍한의원",
        "성제한의원",
        "동인한의원",
        "경희만석한의원",
        "덕윤한의원",
        "왕소연중국한의원",
        "덕창한의원",
        "박지영한의원",
        "임베문한의원",
        "바른한의원",
        "용현보화한의원"
    ],
    "한방소아과": [
        "안녕한의원",
        "우리한의원",
        "인천시원한의원",
        "성인천한의원",
        "다솜한의원",
        "경희최한의원",
        "감초한의원",
        "동남한의원",
        "석재홍한의원",
        "성제한의원",
        "동인한의원",
        "경희만석한의원",
        "덕윤한의원",
        "왕소연중국한의원",
        "덕창한의원",
        "박지영한의원",
        "임베문한의원",
        "바른한의원",
        "용현보화한의원"
    ],
    "한방신경정신과": [
        "안녕한의원",
        "우리한의원",
        "인천시원한의원",
        "성인천한의원",
        "다솜한의원",
        "경희최한의원",
        "감초한의원",
        "동남한의원",
        "석재홍한의원",
        "성제한의원",
        "동인한의원",
        "경희만석한의원",
        "덕윤한의원",
        "왕소연중국한의원",
        "덕창한의원",
        "박지영한의원",
        "임베문한의원",
        "바른한의원",
        "용현보화한의원"
    ],
    "한방안·이비인후·피부과": [
        "안녕한의원",
        "우리한의원",
        "인천시원한의원",
        "성인천한의원",
        "다솜한의원",
        "경희최한의원",
        "감초한의원",
        "동남한의원",
        "석재홍한의원",
        "성제한의원",
        "동인한의원",
        "경희만석한의원",
        "덕윤한의원",
        "왕소연중국한의원",
        "덕창한의원",
        "박지영한의원",
        "임베문한의원",
        "바른한의원",
        "용현보화한의원"
    ],
    "한방재활의학과": [
        "안녕한의원",
        "우리한의원",
        "인천시원한의원",
        "성인천한의원",
        "다솜한의원",
        "경희최한의원",
        "감초한의원",
        "동남한의원",
        "석재홍한의원",
        "성제한의원",
        "동인한의원",
        "경희만석한의원",
        "덕윤한의원",
        "왕소연중국한의원",
        "덕창한의원",
        "박지영한의원",
        "임베문한의원",
        "바른한의원",
        "용현보화한의원"
    ],
    "사상체질과": [
        "우리한의원",
        "인천시원한의원",
        "성인천한의원",
        "경희최한의원",
        "감초한의원",
        "동남한의원",
        "동인한의원",
        "경희만석한의원",
        "덕윤한의원",
        "왕소연중국한의원",
        "덕창한의원",
        "박지영한의원",
        "바른한의원",
        "용현보화한의원"
    ],
    "한방병원": [
        "365엄지한방병원"
    ],
    "한방응급": [
        "석재홍한의원",
        "성제한의원",
        "동인한의원",
        "덕윤한의원",
        "왕소연중국한의원",
        "덕창한의원",
        "박지영한의원",
        "임베문한의원",
        "바른한의원",
        "용현보화한의원"
    ]

}

class DatePicker(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Select Date")
        self.geometry("300x400")
        
        self.selected_date = None
        self.calendar = Calendar(self, self.date_selected)
        self.calendar.pack(pady=10)

    def date_selected(self, date):
        self.selected_date = date
        self.destroy()

class Calendar(tk.Frame):
    def __init__(self, parent, date_selected_callback):
        super().__init__(parent)
        self.date_selected_callback = date_selected_callback
        self.current_date = datetime.now()
        self.month_names = ["1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월"]
        self.create_widgets()

    def create_widgets(self):
        self.header_frame = tk.Frame(self)
        self.header_frame.pack(pady=5)

        self.prev_month_button = tk.Button(self.header_frame, text="<", command=self.prev_month)
        self.prev_month_button.grid(row=0, column=0)

        month_year = f"{self.month_names[self.current_date.month - 1]} {self.current_date.year}"
        self.month_label = tk.Label(self.header_frame, text=month_year, font=("Arial", 14))
        self.month_label.grid(row=0, column=1, padx=10)

        self.next_month_button = tk.Button(self.header_frame, text=">", command=self.next_month)
        self.next_month_button.grid(row=0, column=2)

        self.header_frame.grid_columnconfigure(1, weight=1)  # This line ensures the label is centered between the buttons

        days_frame = tk.Frame(self)
        days_frame.pack()

        days = ["월", "화", "수", "목", "금", "토", "일"]
        for day in days:
            tk.Label(days_frame, text=day).grid(row=0, column=days.index(day), padx=10)

        self.days_frame = days_frame
        self.populate_days()

    def populate_days(self):
        for widget in self.days_frame.winfo_children()[7:]:
            widget.destroy()

        month_start = self.current_date.replace(day=1)
        month_end = (self.current_date.replace(month=self.current_date.month % 12 + 1, day=1) - timedelta(days=1))
        days_in_month = [day for day in range(1, month_end.day + 1)]

        row, col = 1, (month_start.weekday() + 1) % 7
        if (month_start.weekday() + 1) % 7 == 6:  # If the first day is Sunday
            row += 1
            col = 0

        for day in days_in_month:
            button = tk.Button(self.days_frame, text=str(day), command=lambda d=day: self.date_selected(d))
            button.grid(row=row, column=col, padx=10, pady=5)
            col += 1
            if col > 6:
                col = 0
                row += 1

    def date_selected(self, day):
        selected_date = self.current_date.replace(day=day)
        self.date_selected_callback(selected_date.strftime('%Y-%m-%d'))

    def prev_month(self):
        self.current_date = (self.current_date.replace(day=1) - timedelta(days=1)).replace(day=1)
        month_year = f"{self.month_names[self.current_date.month - 1]} {self.current_date.year}"
        self.month_label.config(text=month_year)
        self.populate_days()

    def next_month(self):
        next_month = self.current_date.replace(month=self.current_date.month % 12 + 1, day=1)
        self.current_date = next_month
        month_year = f"{self.month_names[self.current_date.month - 1]} {self.current_date.year}"
        self.month_label.config(text=month_year)
        self.populate_days()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("User System")
        self.geometry("1000x500")
        
        self.create_widgets()

    def create_widgets(self):
        self.clear_widgets()
        self.lbl_title = tk.Label(self, text="Login")
        self.lbl_title.pack(pady=10)

        self.lbl_username = tk.Label(self, text="ID")
        self.lbl_username.pack()
        self.ent_username = tk.Entry(self)
        self.ent_username.pack()

        self.lbl_password = tk.Label(self, text="Password")
        self.lbl_password.pack()
        self.ent_password = tk.Entry(self, show="*")
        self.ent_password.pack()

        self.btn_submit = tk.Button(self, text="로그인", command=self.login)
        self.btn_submit.pack(pady=10)

        self.btn_register = tk.Button(self, text="회원가입", command=self.show_register)
        self.btn_register.pack(pady=5)

    def show_register(self):
        self.clear_widgets()
        self.lbl_title = tk.Label(self, text="회원가입")
        self.lbl_title.pack(pady=10)

        self.lbl_username = tk.Label(self, text="ID")
        self.lbl_username.pack()
        self.ent_username = tk.Entry(self)
        self.ent_username.pack()

        self.lbl_password = tk.Label(self, text="Password")
        self.lbl_password.pack()
        self.ent_password = tk.Entry(self, show="*")
        self.ent_password.pack()

        self.lbl_phone = tk.Label(self, text="전화번호(숫자만)")
        self.lbl_phone.pack()
        self.ent_phone = tk.Entry(self)
        self.ent_phone.pack()

        self.btn_submit = tk.Button(self, text="완료", command=self.register)
        self.btn_submit.pack(pady=10)

        self.btn_back = tk.Button(self, text="뒤로가기", command=self.back_to_main)
        self.btn_back.pack(pady=5)

    def register(self):
        username = self.ent_username.get()
        password = self.ent_password.get()
        phone = self.ent_phone.get()
        success, message = register_user(username, password, phone)
        messagebox.showinfo("Register", message)
        if success:
            self.back_to_main()

    def login(self):
        username = self.ent_username.get()
        password = self.ent_password.get()
        success, message = authenticate_user(username, password)
        if success:
            messagebox.showinfo("Login", message)
            self.show_symptom_selection_form()
        else:
            messagebox.showerror("Login Error", message)

    def show_symptom_selection_form(self):
        self.clear_widgets()
        self.lbl_title = tk.Label(self, text="진단 예약")
        self.lbl_title.pack(pady=10)

        self.lbl_department = tk.Label(self, text="희망진료과")
        self.lbl_department.pack()
        
        # Combobox for selecting department
        self.cmb_department = ttk.Combobox(self, values=self.get_sorted_departments(), state="readonly")
        self.cmb_department.pack()
        self.cmb_department.bind("<<ComboboxSelected>>", self.update_symptoms_combobox)

        self.lbl_symptoms = tk.Label(self, text="증상")
        self.lbl_symptoms.pack()
        self.cmb_symptoms = ttk.Combobox(self, state="readonly")
        self.cmb_symptoms.pack()
        self.cmb_symptoms.bind("<1>", self.check_department_selected)

        self.btn_next = tk.Button(self, text="병원 검색", command=self.show_appointment_form)
        self.btn_next.pack(pady=10)

        self.btn_back = tk.Button(self, text="뒤로가기", command=self.back_to_main)
        self.btn_back.pack(pady=5)

    def get_sorted_departments(self):
        return sorted(department_symptoms.keys())

    def update_symptoms_combobox(self, event):
        selected_department = self.cmb_department.get()
        if selected_department in department_symptoms:
            symptoms = department_symptoms[selected_department]
            self.cmb_symptoms.config(values=symptoms)
            self.cmb_symptoms.set('')

    def check_department_selected(self, event):
        if not self.cmb_department.get():
            messagebox.showwarning("Warning", "희망진료과를 먼저 선택해주세요.")

    def show_appointment_form(self):
        department = self.cmb_department.get()
        symptom = self.cmb_symptoms.get()
        if not department or not symptom:
            messagebox.showerror("Error", "진료과와 증상을 모두 선택해주세요.")
            return

        self.clear_widgets()
        self.lbl_title = tk.Label(self, text="진단 예약")
        self.lbl_title.pack(pady=10)

        self.lbl_appointment_date = tk.Label(self, text="진단희망날짜")
        self.lbl_appointment_date.pack()
        self.ent_appointment_date = tk.Entry(self)
        self.ent_appointment_date.pack()
        self.ent_appointment_date.bind("<1>", self.show_date_picker)

        self.lbl_appointment_time = tk.Label(self, text="진단희망시간")
        self.lbl_appointment_time.pack()
        self.ent_appointment_time = tk.Entry(self)
        self.ent_appointment_time.pack()

        self.btn_submit_appointment = tk.Button(self, text="예약 완료", command=lambda: self.submit_appointment(department, symptom))
        self.btn_submit_appointment.pack(pady=10)

        self.btn_back = tk.Button(self, text="뒤로가기", command=self.show_symptom_selection_form)
        self.btn_back.pack(pady=5)

    def show_date_picker(self, event):
        date_picker = DatePicker(self)
        self.wait_window(date_picker)
        if date_picker.selected_date:
            self.ent_appointment_date.delete(0, tk.END)
            self.ent_appointment_date.insert(0, date_picker.selected_date)

    def submit_appointment(self, department, symptom):
        appointment_date = self.ent_appointment_date.get()
        appointment_time = self.ent_appointment_time.get()
        if not appointment_date or not appointment_time:
            messagebox.showerror("Error", "날짜와 시간을 모두 선택해주세요.")
            return
        messagebox.showinfo("Appointment", f"진료과: {department}\n증상: {symptom}\n진단희망날짜: {appointment_date}\n진단희망시간: {appointment_time}")
        self.back_to_main()

    def back_to_main(self):
        self.clear_widgets()
        self.create_widgets()

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
