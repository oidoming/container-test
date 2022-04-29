import os 
import sys
import time

VALUE = os.environ['VALUE_KEY']

def main():
    try:        
        while True:
            print(VALUE)
            time.sleep(5)
    except KeyboardInterrupt:
        sys.exit(1)

if __name__ == '__main__':
    main()
