###1.单继承


class Phone(object):
    IMEI = None
    producer = "ITdark"

    def call_by_4g(self):
        print("4g通话")


class Phone2022(Phone):
    face_id = "10001"

    def call_by_5g(self):
        print("2022年新功能：5g通话")


# phone = Phone2022()
#
# print(phone.producer)
# phone.call_by_4g()
# phone.call_by_5g()


####2.多继承

class NFC_Reader(object):
    nfc_typer = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")


class RemoteControl(object):
    rc_type = "红外遥控"
    def control(self):
        print("红外遥控已开启")



class MyPhone(Phone,NFC_Reader,RemoteControl):
    pass


phone=MyPhone()
print(phone.producer)   #谁先继承，谁的优先级高（从左向右）
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()