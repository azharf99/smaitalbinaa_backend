from django.utils.translation import gettext_lazy as _



EXTRACURRICULAR_SCORE_CHOICES = (
    (None, "----Pilih Nilai----"),
    ("A", _("A")),
    ("B", _("B")),
    ("C", _("C")),
)

GENDER_CHOICES = (
    (None, "----Pilih Kategori Gender----"),
    ("Putra", _("Putra")),
    ("Putri", _("Putri")),
)

GENDER_AREA_TYPE_CHOICES = (
    (None, "----Pilih Kategori Kelas----"),
    ("Putra", _("Putra")),
    ("Putra", _("Putri")),
    ("Putra-Putri", _("Putra & Putri")),
)

COURSE_CATEGORY_CHOICES = (
    (None, "----Pilih Kategori----"),
    ("Syar'i", _("Syar'i")),
    ("Ashri", _("Ashri")),
    ("Netral", _("Netral")),
)

SCHEDULE_WEEKDAYS = (
    ("Senin", _("Senin")),
    ("Selasa", _("Selasa")),
    ("Rabu", _("Rabu")),
    ("Kamis", _("Kamis")),
    ("Sabtu", _("Sabtu")),
    ("Ahad", _("Ahad")),
)

SCHEDULE_TIME = (
    ("1", _("Jam ke-1")),
    ("2", _("Jam ke-2")),
    ("3", _("Jam ke-3")),
    ("4", _("Jam ke-4")),
    ("5", _("Jam ke-5")),
    ("6", _("Jam ke-6")),
    ("7", _("Jam ke-7")),
    ("8", _("Jam ke-8")),
    ("9", _("Jam ke-9")),
)

SCHEDULE_TIME_DICT = {
    "1": _("Jam ke-1"),
    "2": _("Jam ke-2"),
    "3": _("Jam ke-3"),
    "4": _("Jam ke-4"),
    "5": _("Jam ke-5"),
    "6": _("Jam ke-6"),
    "7": _("Jam ke-7"),
    "8": _("Jam ke-8"),
    "9": _("Jam ke-9"),
}

WEEKDAYS = {
    0: _("Senin"),
    1: _("Selasa"),
    2: _("Rabu"),
    3: _("Kamis"),
    4: _("Jumat"),
    5: _("Sabtu"),
    6: _("Ahad"),
}

INDONESIAN_DAYS_OPTIONS = (
    (None, _("Choose training Day")),
    ('Senin', _('Monday')),
    ('Selasa', _('Tuesday')),
    ('Rabu', _('Wednesday')),
    ('Kamis', _('Thursday')),
    ('Jumat', _('Friday')),
    ('Sabtu', _('Saturday')),
    ('Ahad', _('Sunday'))
)

INDONESIAN_TIME_OPTIONS = (
    (None, _("Choose training time")),
    ("Pagi", _("Morning")),
    ("Siang", _("Noon")),
    ("Sore", _("Evening")),
    ("Malam", _("Night")),
)

EXTRACURRICULAR_TYPES = (
    (None, _("Select Type")),
    ("Ekskul", _("Ekstrakurikuler")),
    ("SC", _("Study Club"))
)

STATUS_CHOICES = (
    (None, "----Pilih Status----"),
    ("Hadir", _("Hadir")),
    ("Izin", _("Izin")),
    ("Sakit", _("Sakit")),
    ("Tanpa Keterangan", _("Tanpa Keterangan")),
    ("Off", _("Off")),
)


TAHSIN_STATUS_CHOICES = (
    (None, "----Pilih Nilai Tahsin----"),
    ("Mumtaz", _("Mumtaz")),
    ("Jayyid Jiddan", _("Jayyid Jiddan")),
    ("Jayyid", _("Jayyid")),
    ("Maqbul", _("Maqbul")),
    ("Da'if", _("Da'if")),
)


TAHSIN_STATUS_LIST = ["Mumtaz", "Jayyid Jiddan", "Jayyid", "Maqbul", "Da'if"]


QURAN_SURAH_DICT = {
    "1": "Al-Fatihah",
    "2": "Al-Baqarah",
    "3": "Ali 'Imran",
    "4": "An-Nisa'",
    "5": "Al-Ma'idah",
    "6": "Al-An'am",
    "7": "Al-A'raf",
    "8": "Al-Anfal",
    "9": "At-Tawbah",
    "10": "Yunus",
    "11": "Hud",
    "12": "Yusuf",
    "13": "Ar-Ra'd",
    "14": "Ibrahim",
    "15": "Al-Hijr",
    "16": "An-Nahl",
    "17": "Al-Isra'",
    "18": "Al-Kahf",
    "19": "Maryam",
    "20": "Ta Ha",
    "21": "Al-Anbiya'",
    "22": "Al-Hajj",
    "23": "Al-Mu'minun",
    "24": "An-Nur",
    "25": "Al-Furqan",
    "26": "Ash-Shu'ara'",
    "27": "An-Naml",
    "28": "Al-Qasas",
    "29": "Al-Ankabut",
    "30": "Ar-Rum",
    "31": "Luqman",
    "32": "As-Sajdah",
    "33": "Al-Ahzab",
    "34": "Saba'",
    "35": "Fatir",
    "36": "Ya Sin",
    "37": "As-Saffat",
    "38": "Sad",
    "39": "Az-Zumar",
    "40": "Ghafir",
    "41": "Fussilat",
    "42": "Ash-Shura",
    "43": "Az-Zukhruf",
    "44": "Ad-Dukhan",
    "45": "Al-Jathiyah",
    "46": "Al-Ahqaf",
    "47": "Muhammad",
    "48": "Al-Fath",
    "49": "Al-Hujurat",
    "50": "Qaf",
    "51": "Adh-Dhariyat",
    "52": "At-Tur",
    "53": "An-Najm",
    "54": "Al-Qamar",
    "55": "Ar-Rahman",
    "56": "Al-Waqi'ah",
    "57": "Al-Hadid",
    "58": "Al-Mujadila",
    "59": "Al-Hashr",
    "60": "Al-Mumtahanah",
    "61": "As-Saff",
    "62": "Al-Jumu'ah",
    "63": "Al-Munafiqun",
    "64": "At-Taghabun",
    "65": "At-Talaq",
    "66": "At-Tahrim",
    "67": "Al-Mulk",
    "68": "Al-Qalam",
    "69": "Al-Haqqah",
    "70": "Al-Ma'arij",
    "71": "Nuh",
    "72": "Al-Jinn",
    "73": "Al-Muzzammil",
    "74": "Al-Muddaththir",
    "75": "Al-Qiyamah",
    "76": "Al-Insan",
    "77": "Al-Mursalat",
    "78": "An-Naba'",
    "79": "An-Nazi'at",
    "80": "Abasa",
    "81": "At-Takwir",
    "82": "Al-Infitar",
    "83": "Al-Mutaffifin",
    "84": "Al-Inshiqaq",
    "85": "Al-Buruj",
    "86": "At-Tariq",
    "87": "Al-A'la",
    "88": "Al-Ghashiyah",
    "89": "Al-Fajr",
    "90": "Al-Balad",
    "91": "Ash-Shams",
    "92": "Al-Lail",
    "93": "Ad-Duhaa",
    "94": "Ash-Sharh",
    "95": "At-Tin",
    "96": "Al-'Alaq",
    "97": "Al-Qadr",
    "98": "Al-Bayyinah",
    "99": "Az-Zalzalah",
    "100": "Al-'Adiyat",
    "101": "Al-Qari'ah",
    "102": "At-Takathur",
    "103": "Al-Asr",
    "104": "Al-Humazah",
    "105": "Al-Fil",
    "106": "Quraysh",
    "107": "Al-Ma'un",
    "108": "Al-Kawthar",
    "109": "Al-Kafirun",
    "110": "An-Nasr",
    "111": "Al-Masad",
    "112": "Al-Ikhlas",
    "113": "Al-Falaq",
    "114": "An-Nas"
  }
