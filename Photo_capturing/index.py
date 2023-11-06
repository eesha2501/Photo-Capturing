import cv2
from PIL import Image

# Function to capture an image from the camera and save it
def capture_and_save_image(image_count):
    cap = cv2.VideoCapture(0)  # 0 represents the default camera (usually the built-in webcam)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    ret, frame = cap.read()
    if not ret:
        print("Error: Could not capture an image.")
        return

    cap.release()  # Release the camera

    # Save the captured image with the specified name
    file_name = f"pic{image_count}.jpg"
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert image from BGR to RGB
    pil_image = Image.fromarray(image)  # Convert to PIL image
    pil_image.save(file_name)
    print(f"Image saved as {file_name}")

if __name__ == "__main__":
    image_count = 1

    while True:
        user_input = input("Do you want to capture an image? (yes/no): ").lower()

        if user_input != "yes":
            break

        capture_and_save_image(image_count)
        image_count += 1
