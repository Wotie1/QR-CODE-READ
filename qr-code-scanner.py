
import cv2

# Kamerayi baslat
cap = cv2.VideoCapture(0)

# Kamera kontrolu
if not cap.isOpened():
    print("ERROR: Camera could not be opened!")
    exit()

# QR kod algilayicisini olustur
detector = cv2.QRCodeDetector()

print("Show a QR code to the camera.")
print("Press 'q' to quit.")

last_data = None

try:
    while True:

        # Kameradan goruntu al
        ret, img = cap.read()

        if not ret or img is None:
            print("ERROR: Could not read camera frame!")
            break

        # QR kodu algila ve icerigini coz
        data, bbox, _ = detector.detectAndDecode(img)

        if data:
            if data != last_data:
                print("QR CODE DETECTED:", data)
                last_data = data

            # QR kodun etrafina dikdortgen ciz
            if bbox is not None:
                points = bbox.astype(int)

                for i in range(len(points[0])):
                    pt1 = tuple(points[0][i])
                    pt2 = tuple(points[0][(i + 1) % len(points[0])])

                    cv2.line(img, pt1, pt2, (0, 255, 0), 2)

        else:
            last_data = None

        # Goruntuyu ekranda goster
        cv2.imshow("QR Reader", img)

        # Q tusuyla cikis
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

except cv2.error as e:
    print("OpenCV Error:", e)

except Exception as e:
    print("Unexpected Error:", e)

finally:
    cap.release()
    cv2.destroyAllWindows()
    print("QR Reader closed.")
