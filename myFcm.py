# Send to single device.
from pyfcm import FCMNotification

# OR initialize with proxies

# proxy_dict = {
#          "http"  : "http://127.0.0.1",
#          "https" : "http://127.0.0.1",
#        }
# push_service = FCMNotification(api_key="<api-key>", proxy_dict=proxy_dict)

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging


# Send to multiple devices by passing a list of ids.
# registration_ids = ["<device registration_id 1>", "<device registration_id 2>", ...]
# message_title = "Uber update"
# message_body = "Hope you're having fun this weekend, don't forget to check today's news"
# result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)
from MySQL import MySQLFcm


def sendSingle(device, title, body):
    push_service = FCMNotification(
        api_key="AAAAQn5_iJg:APA91bFdiwm0w09hLXEl0mBQ_kuT6KHaSZDiaAltep-3KaUV2AlhmFL5WRQwMgS1juLjDoleWxXAcOgKicvJZXJwm32UXWrPFbYKdJ1384w8vIVgBtgTFMGv4GBvDKl35tBhsqR-Bpb7")
    result = push_service.notify_single_device(registration_id=device, message_title=title,
                                               message_body=body)
    print(result)


def sendMultiple(devices, title, body):
    push_service = FCMNotification(
        api_key="AAAAQn5_iJg:APA91bFdiwm0w09hLXEl0mBQ_kuT6KHaSZDiaAltep-3KaUV2AlhmFL5WRQwMgS1juLjDoleWxXAcOgKicvJZXJwm32UXWrPFbYKdJ1384w8vIVgBtgTFMGv4GBvDKl35tBhsqR-Bpb7")
    result = push_service.notify_multiple_devices(registration_ids=devices, message_title=title, message_body=body)
    print(result)


def sendDeviceRegister(pns):
    FcmMySQL = MySQLFcm()
    # cek data existing
    FcmMySQL.getDevice(pns)
    # Fetch Result
    row = FcmMySQL.row()
    num = FcmMySQL.num_rows()
    device_register = None
    first_name = None
    last_name = None

    if num > 0:
        device_register = row[0]
        first_name = row[1]
        last_name = row[2]

    FcmMySQL.commit()
    FcmMySQL.close()

    if device_register is not None:
        message_title = "Smart Presensi REMINDER"
        message_body = "Hi " + first_name + last_name + ", your customized news for today is ready Multiple"
        sendSingle(device_register, message_title, message_body)


def sendAllDeviceRegister():
    FcmMySQL = MySQLFcm()
    # cek data existing
    FcmMySQL.getAllDevice()
    # Fetch Result
    result = FcmMySQL.result()
    for val in result:
        device_register = val[0]
        first_name = val[1]
        last_name = val[2]
        pagi = val[3]
        siang = val[4]
        sore = val[5]
        malam = val[6]
        absen = val[7]
        message_body = None

        if pagi == 1:
            message_body = "Hi " + first_name + last_name + ", Batas Absen Pagi Jam 08:00 WITA"

        if siang == 1:
            message_body = "Hi " + first_name + last_name + ", Batas Absen Siang Jam 13:00 WITA"

        if sore == 1:
            message_body = "Hi " + first_name + last_name + ", Batas Absen Sore Jam 18:00 WITA"

        if malam == 1:
            message_body = "Hi " + first_name + last_name + ", Batas Absen Malam Jam 24:00 WITA"

        if absen == 1:
            message_body = "Hi " + first_name + last_name + ", Waktu absen mulai jam 7 Pagi"

        print(device_register)

        if device_register is not None:
            message_title = "Smart Presensi"
            sendSingle(device_register, message_title, message_body)

    FcmMySQL.commit()
    FcmMySQL.close()


registration_id = [
    "e1KL7nOhTUqrhFD3c22B53:APA91bGBFmT7csHyhXqFLCCFlqWedFkWqZvjea4Sl3SWTMZlpPbzuq0FHYMSM2t6x4LJFcwNJLDkREHCA7985dGWWQOqce3Wcd1QW8pSXXzvA878SdBA43wfGic7MKm57yV5eEwF2Gfq",
    "dw5kDVUBS7mJhnxbFalTCZ:APA91bECsyIABroj50xReSSa5OsfZYzkPykRn4TGssSVrXb9uhqVXJoMzJX8-N74URxmqIzCowNwDPkjlpuOd-iB4TQRZaBG816Bi4erZNtZt8puD5f576AYzu0A8Mbg6qYbGbzRIJQ0"]

#sendDeviceRegister("0E2621E17314440FE050640A15023D38")
sendAllDeviceRegister()
