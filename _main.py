from pynput.keyboard import Key, Controller
import time
import can

bus = can.Bus(interface='socketcan',
              channel='can0',
              receive_own_messages=True)
bus.set_filters([{"can_id": 0x5C1, "can_mask": 0xFFF, "extended": False}])

values = []
for i in range(15):
    values.append(i+1)
values = values + values + values
print(values)
clicks = [7,6,5,4,3,2,1]

vol_value = None
ctrl_value = None
keyboard = Controller()

for msg in bus:
    #print(msg)
    if msg.arbitration_id == 1473:
      
        if len(msg.data) > 0:
            if msg.data[0] == 19: #volume
                new = int(msg.data[2])
                print(new)
                if vol_value == None:
                    vol_value = new
                newvalues = values[new+7:new+22]
                print(newvalues)
                valuepos = newvalues.index(vol_value)
                if valuepos > 7:
                    #print(valuepos)
                    for i in range(valuepos - 7):
                        print('-')
                        keyboard.press(Key.f7)
                        keyboard.release(Key.f7)
                if valuepos < 7:
                    for i in range(clicks[valuepos]):
                        print('+')
                        keyboard.press(Key.f8)
                        keyboard.release(Key.f8)
                vol_value = new
                print("")

            if msg.data[0] == 20: #control
                new = int(msg.data[2])
                print(new)
                if ctrl_value == None:
                    ctrl_value = new
                newvalues = values[new+7:new+22]
                print(newvalues)
                valuepos = newvalues.index(ctrl_value)
                if valuepos > 7:
                    #print(valuepos)
                    for i in range(valuepos - 7):
                        print('-')
                        keyboard.press('1')
                        keyboard.release('1')
                if valuepos < 7:
                    for i in range(clicks[valuepos]):
                        print('+')
                        keyboard.press('2')
                        keyboard.release('2')
                ctrl_value = new
                print("")

            if msg.data[0] == 43: # vol click
                keyboard.press('')
                keyboard.release('')

            if msg.data[0] == 40: # ctrl click
                keyboard.press('')
                keyboard.release('')

            if msg.data[0] == 1: # cycle  
                keyboard.press('')
                keyboard.release('')

            if msg.data[0] == 2: # >
                keyboard.press('N')
                keyboard.release('N')

            if msg.data[0] == 3: # <
                keyboard.press('V')
                keyboard.release('V')

            if msg.data[0] == 41: # return
                keyboard.press('key.esc')
                keyboard.release('key.esc')