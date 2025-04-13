from picamera2 import Picamera2
import time

def main():
    #Initializes the camera and configures it
    picam2 = Picamera2()
    picam2.configure(picam2.create_preview_configuration())

    #Starts the camera and captures the photo
    picam2.start()
    print("Camera started, waiting 2 seconds...")
    time.sleep(2)
    print("Capturing photo...")
    picam2.capture_file("test_simple.png")
    print("Photo saved as test_simple.png")
    picam2.close()
     
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print (f"Error: {e}")