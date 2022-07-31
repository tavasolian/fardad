SSID='Fardad_Azma'
PASSWD='@Faraz2019#'
def connectToWifiAndUpdate():
    import time
#    upd.save(b"update","False")
#    aoff()        
    time.sleep_ms(200)
    from network import WLAN ,AP_IF,STA_IF
    sta_if=WLAN(STA_IF)
    print(sta_if.ifconfig())
    sta_if.active(True)
    ap_if=WLAN(AP_IF)
    ap_if.active(False)
    if sta_if.ifconfig()[0]=='0.0.0.0':            
        print('connectToWifiAndUpdate')
        try:
            sta_if.connect(SSID,PASSWD) 
        except OSError:
            pass
        print('waiting for connection...')
        while sta_if.ifconfig()[0]=='0.0.0.0':
            print(sta_if.ifconfig())
            time.sleep(3)
    from ota_updater import OTAUpdater
    if(sta_if.ifconfig()[0]!='0.0.0.0'):
        print('network config:', sta_if.ifconfig())
        token='git access token'
        git='https://git.msb-co.ir/MSB_Electronics/esp32_ota_example'
        md='app'
        try:
            print(md,'\n',git,'\n')
            # otaUpdater = OTAUpdater(git, main_dir=md,headers={'Authorization': 'token {}'.format(token)})
            otaUpdater = OTAUpdater(git, main_dir=md)
            hasUpdated=None
            try:
                hasUpdated = otaUpdater.install_update_if_available()
            except OSError as e:
                import sys
                from uio import StringIO
                s=StringIO()
                sys.print_exception(e, s)  
                s=s.getvalue()
                print(s)
            if hasUpdated:
                import machine
                machine.reset()
            else:
                del(otaUpdater)
        except TypeError:
            pass
    print('DONE')
    import gc
    gc.collect()
connectToWifiAndUpdate()

