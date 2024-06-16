import inputs
import time

def main():
    time.sleep(2)
    state_dict = {
        "ABS_X": 0,
        "ABS_Y": 0,
    }
    while True:

        events = inputs.get_gamepad()
        for event in events:
            if event.ev_type == 'Absolute':
                # only show if diff is more than 5
                # if abs(state_dict[event.code] - event.state) > 5:
                #     state_dict[event.code] = event.state
                #     print(f'Axis {event.code} moved to {event.state}')
                print(f'Axis {event.code} moved to {event.state}')
            elif event.ev_type == 'Key':
                if event.state == 1:
                    print(f'Button {event.code} pressed')
                elif event.state == 0:
                    print(f'Button {event.code} released')

if __name__ == "__main__":\
    main()
