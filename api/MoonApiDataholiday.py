# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = moon_api_dataholiday_from_dict(json.loads(json_string))

from datetime import datetime
from typing import Any, TypeVar, Type, cast
import dateutil.parser


T = TypeVar("T")


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_str(x: Any) -> str:
    #assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    #assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    #assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    #assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Info:
    date: datetime
    descr: str
    week: int
    offwork: bool
    name: str
    type: int
    weekname: str
    wage: int

    def __init__(self, date: datetime, descr: str, week: int, offwork: bool, name: str, type: int, weekname: str, wage: int) -> None:
        self.date = date
        self.descr = descr
        self.week = week
        self.offwork = offwork
        self.name = name
        self.type = type
        self.weekname = weekname
        self.wage = wage

    @staticmethod
    def from_dict(obj: Any) -> 'Info':
        #assert isinstance(obj, dict)
        date = from_datetime(obj.get("date"))
        descr = from_str(obj.get("descr"))
        week = from_int(obj.get("week"))
        offwork = from_bool(obj.get("offwork"))
        name = from_str(obj.get("name"))
        type = from_int(obj.get("type"))
        weekname = from_str(obj.get("weekname"))
        wage = from_int(obj.get("wage"))
        return Info(date, descr, week, offwork, name, type, weekname, wage)

    def to_dict(self) -> dict:
        result: dict = {}
        result["date"] = self.date.isoformat()
        result["descr"] = from_str(self.descr)
        result["week"] = from_int(self.week)
        result["offwork"] = from_bool(self.offwork)
        result["name"] = from_str(self.name)
        result["type"] = from_int(self.type)
        result["weekname"] = from_str(self.weekname)
        result["wage"] = from_int(self.wage)
        return result


class Data:
    chat: str
    info: Info

    def __init__(self, chat: str, info: Info) -> None:
        self.chat = chat
        self.info = info

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        #assert isinstance(obj, dict)
        chat = from_str(obj.get("chat"))
        info = Info.from_dict(obj.get("info"))
        return Data(chat, info)

    def to_dict(self) -> dict:
        result: dict = {}
        result["chat"] = from_str(self.chat)
        result["info"] = to_class(Info, self.info)
        return result


class MoonAPIDataholiday:
    status: str
    data: Data
    time: int
    code: str
    message: str

    def __init__(self, status: str, data: Data, time: int, code: str, message: str) -> None:
        self.status = status
        self.data = data
        self.time = time
        self.code = code
        self.message = message

    @staticmethod
    def from_dict(obj: Any) -> 'MoonAPIDataholiday':
        #assert isinstance(obj, dict)
        status = from_str(obj.get("status"))
        data = Data.from_dict(obj.get("data"))
        time = from_int(obj.get("time"))
        code = from_str(obj.get("code"))
        message = from_str(obj.get("message"))
        return MoonAPIDataholiday(status, data, time, code, message)

    def to_dict(self) -> dict:
        result: dict = {}
        result["status"] = from_str(self.status)
        result["data"] = to_class(Data, self.data)
        result["time"] = from_int(self.time)
        result["code"] = from_str(self.code)
        result["message"] = from_str(self.message)
        return result


def moon_api_dataholiday_from_dict(s: Any) -> MoonAPIDataholiday:
    return MoonAPIDataholiday.from_dict(s)


def moon_api_dataholiday_to_dict(x: MoonAPIDataholiday) -> Any:
    return to_class(MoonAPIDataholiday, x)
