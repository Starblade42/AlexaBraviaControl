#!/usr/bin/env python
""" fauxmo_minimal.py - Fabricate.IO

    This is a demo python file showing what can be done with the debounce_handler.
    The handler prints True when you say "Alexa, device on" and False when you say
    "Alexa, device off".

    If you have two or more Echos, it only handles the one that hears you more clearly.
    You can have an Echo per room and not worry about your handlers triggering for
    those other rooms.

    The IP of the triggering Echo is also passed into the act() function, so you can
    do different things based on which Echo triggered the handler.
"""

import fauxmo
import logging
import time

from debounce_handler import debounce_handler

sony_bravia_address = "10.0.2.10"
sony_bravia_mac_address = "B0:10:41:BD:B3:91"

volume_step_size = 10
volume_increment_delay = .3

SONY_BRAVIA_URL = "http://{}/sony/IRCC".format(sony_bravia_address)

logging.basicConfig(level=logging.DEBUG)

def hdmi1():
    import requests

    url = SONY_BRAVIA_URL

    payload = "<?xml version=\"1.0\"?>\n<s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\">\n    <s:Body>\n        <u:X_SendIRCC xmlns:u=\"urn:schemas-sony-com:service:IRCC:1\">\n            <IRCCCode>AAAAAgAAABoAAABaAw==</IRCCCode>\n        </u:X_SendIRCC>\n    </s:Body>\n</s:Envelope>"
    headers = {
        'content-type': "text/xml; charset=UTF-8",
        'x-auth-psk': "4169",
        'soapaction': "\"urn:schemas-sony-com:service:IRCC:1#X_SendIRCC\"",
        'cache-control': "no-cache",
        'postman-token': "289aa016-d426-b5d4-3a80-75d271eac88f"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

def hdmi2():
    import requests

    url = SONY_BRAVIA_URL

    payload = "<?xml version=\"1.0\"?>\n<s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\">\n    <s:Body>\n        <u:X_SendIRCC xmlns:u=\"urn:schemas-sony-com:service:IRCC:1\">\n            <IRCCCode>AAAAAgAAABoAAABbAw==</IRCCCode>\n        </u:X_SendIRCC>\n    </s:Body>\n</s:Envelope>"
    headers = {
        'content-type': "text/xml; charset=UTF-8",
        'x-auth-psk': "4169",
        'soapaction': "\"urn:schemas-sony-com:service:IRCC:1#X_SendIRCC\"",
        'cache-control': "no-cache",
        'postman-token': "69447f6b-4035-1f89-0cfb-6e8a45569966"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

def hdmi3():
    import requests

    url = SONY_BRAVIA_URL

    payload = "<?xml version=\"1.0\"?>\n<s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\">\n    <s:Body>\n        <u:X_SendIRCC xmlns:u=\"urn:schemas-sony-com:service:IRCC:1\">\n            <IRCCCode>AAAAAgAAABoAAABcAw==</IRCCCode>\n        </u:X_SendIRCC>\n    </s:Body>\n</s:Envelope>"
    headers = {
        'content-type': "text/xml; charset=UTF-8",
        'x-auth-psk': "4169",
        'soapaction': "\"urn:schemas-sony-com:service:IRCC:1#X_SendIRCC\"",
        'cache-control': "no-cache",
        'postman-token': "bf68721b-1139-f2b0-3ecd-c0d09436eef1"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

def hdmi4():
    import requests

    url = SONY_BRAVIA_URL

    payload = "<?xml version=\"1.0\"?>\n<s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\">\n    <s:Body>\n        <u:X_SendIRCC xmlns:u=\"urn:schemas-sony-com:service:IRCC:1\">\n            <IRCCCode>AAAAAgAAABoAAABdAw==</IRCCCode>\n        </u:X_SendIRCC>\n    </s:Body>\n</s:Envelope>"
    headers = {
        'content-type': "text/xml; charset=UTF-8",
        'x-auth-psk': "4169",
        'soapaction': "\"urn:schemas-sony-com:service:IRCC:1#X_SendIRCC\"",
        'cache-control': "no-cache",
        'postman-token': "8582abc4-81bd-16e2-fee1-d58f7b997041"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

def tv_power(state):
    if state == False:
        from wakeonlan import wol
        wol.send_magic_packet(sony_bravia_mac_address)
    else:
        import requests

        url = "http://10.0.2.10/sony/IRCC"

        payload = "<?xml version=\"1.0\"?>\n<s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\">\n    <s:Body>\n        <u:X_SendIRCC xmlns:u=\"urn:schemas-sony-com:service:IRCC:1\">\n            <IRCCCode>AAAAAQAAAAEAAAAvAw==</IRCCCode>\n        </u:X_SendIRCC>\n    </s:Body>\n</s:Envelope>"
        headers = {
            'content-type': "text/xml; charset=UTF-8",
            'x-auth-psk': "4169",
            'soapaction': "\"urn:schemas-sony-com:service:IRCC:1#X_SendIRCC\"",
            'cache-control': "no-cache",
            'postman-token': "dda8bb69-1826-8e57-8091-5e777938557b"
            }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)

def volume_down():
    import requests

    url = "http://10.0.2.10/sony/IRCC"

    payload = "<?xml version=\"1.0\"?>\n<s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\">\n    <s:Body>\n        <u:X_SendIRCC xmlns:u=\"urn:schemas-sony-com:service:IRCC:1\">\n            <IRCCCode>AAAAAQAAAAEAAAATAw==</IRCCCode>\n        </u:X_SendIRCC>\n    </s:Body>\n</s:Envelope>"
    headers = {
        'content-type': "text/xml; charset=UTF-8",
        'x-auth-psk': "4169",
        'soapaction': "\"urn:schemas-sony-com:service:IRCC:1#X_SendIRCC\"",
        'cache-control': "no-cache",
        'postman-token': "bab0b093-5a85-8648-328a-edc6bee63213"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)


def volume_up():
    import requests

    url = "http://10.0.2.10/sony/IRCC"

    payload = "<?xml version=\"1.0\"?>\n<s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\">\n    <s:Body>\n        <u:X_SendIRCC xmlns:u=\"urn:schemas-sony-com:service:IRCC:1\">\n            <IRCCCode>AAAAAQAAAAEAAAASAw==</IRCCCode>\n        </u:X_SendIRCC>\n    </s:Body>\n</s:Envelope>"
    headers = {
        'content-type': "text/xml; charset=UTF-8",
        'x-auth-psk': "4169",
        'soapaction': "\"urn:schemas-sony-com:service:IRCC:1#X_SendIRCC\"",
        'cache-control': "no-cache",
        'postman-token': "a5257972-2447-4aea-e6f6-4bde538bd8dc"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
    

def volume(state):
    if state == False:
        for i in xrange(0,volume_step_size):
            volume_down()
            time.sleep(volume_increment_delay)
    else:
        for i in xrange(0,volume_step_size):
            volume_up()
            time.sleep(volume_increment_delay)

def mute():
    import requests

    url = "http://10.0.2.10/sony/IRCC"

    payload = "<?xml version=\"1.0\"?>\n<s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\">\n    <s:Body>\n        <u:X_SendIRCC xmlns:u=\"urn:schemas-sony-com:service:IRCC:1\">\n            <IRCCCode>AAAAAQAAAAEAAAAUAw==</IRCCCode>\n        </u:X_SendIRCC>\n    </s:Body>\n</s:Envelope>"
    headers = {
        'content-type': "text/xml; charset=UTF-8",
        'x-auth-psk': "4169",
        'soapaction': "\"urn:schemas-sony-com:service:IRCC:1#X_SendIRCC\"",
        'cache-control': "no-cache",
        'postman-token': "25b98e5a-cfa9-7e3f-a367-f8ac118f2681"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)


class device_handler(debounce_handler):
    """Publishes the on/off state requested,
       and the IP address of the Echo making the request.
    """
    def __init__(self, name, port, act_function):
        self.lastEcho = time.time()
        self.name = name
        self.port = port
        if act_function:
            self.act_function = act_function
        else:
            def noop():
                pass
            self.act_function = noop

    def act(self, client_address, state):
        print "State", state, "from client @", client_address
        logging.debug("Executing function - {}".format(act_function.__name__))
        self.act_function(state)
        return True


TRIGGERS = [("HDMI1", 52000, hdmi1),
            ("HDMI2", 52001, hdmi2),
            ("HDMI3", 52002, hdmi3),
            ("HDMI4", 52003, hdmi4),
            ("TV", 52004, tv_power),
            ("VOLUME",52005, volume),
            ("MUTE",53006, mute)
            ]

device_list = []
for trigger in TRIGGERS:
    device_list.append(device_handler(trigger[0],trigger[1],trigger[2]))

if __name__ == "__main__":
    import filelock

    lock = filelock.FileLock("/tmp/AlexaDeviceControl.lock")

    try:
        logging.debug("Attempting to acquire lock")
        with lock.acquire(timeout = 10):
            # Startup the fauxmo server
            logging.info("Success! - Acquired lock")
            fauxmo.DEBUG = True
            p = fauxmo.poller()
            u = fauxmo.upnp_broadcast_responder()
            u.init_socket()
            p.add(u)

            # Register the device callback as a fauxmo handler
            #d = device_handler()
            #for trig, info in d.TRIGGERS.items():
            #    fauxmo.fauxmo(trig, u, p, None, info['port'], d)

            # Register device handlers
            for device in device_list:
                fauxmo.fauxmo(device.name, u, p, None, device.port, device)

            # Loop and poll for incoming Echo requests
            logging.debug("Entering fauxmo polling loop")
            while True:
                try:
                    # Allow time for a ctrl-c to stop the process
                    p.poll(100)
                    time.sleep(0.1)
                except Exception, e:
                    logging.critical("Critical exception: " + str(e))
                    import traceback
                    logging.critical(traceback.format_exc())
                    break
    except filelock.Timeout:
        logging.debug("Lock acquisition timeout. Unable to acquire lock. Exiting")
