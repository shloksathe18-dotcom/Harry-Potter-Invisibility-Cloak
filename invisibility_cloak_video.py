import cv2
import numpy as np

print("""
╔═══════════════════════════════════════════════════════════╗
║  🧙‍♂️  INVISIBILITY CLOAK (Video Background Version)  🧙‍♂️  ║
║                                                           ║
║  This version uses a looping background video            ║
║  Press 'q' to quit                                       ║
╚═══════════════════════════════════════════════════════════╝
""")

# Open webcam
cap = cv2.VideoCapture(0)

# Load background video
bg_video = cv2.VideoCapture('video.mp4')

if not cap.isOpened():
    print("❌ Error: Cannot access webcam!")
    exit()

if not bg_video.isOpened():
    print("❌ Error: Cannot load background video!")
    print("💡 Run 'python record_background.py' first to create video.mp4")
    exit()

print("✅ Webcam and background video loaded!")
print("🎭 Wear something RED and watch the magic!")

# Main loop
while cap.isOpened():
    ret, frame = cap.read()
    ret_bg, background = bg_video.read()
    
    # Loop the background video when it ends
    if not ret_bg:
        bg_video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret_bg, background = bg_video.read()
    
    if not ret or not ret_bg:
        break
    
    # Resize background to match webcam frame size
    background = cv2.resize(background, (frame.shape[1], frame.shape[0]))
    
    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define range for red color in HSV
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    
    # Combine both red masks
    mask = mask1 + mask2
    
    # Morphological operations to clean up the mask
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel, iterations=1)
    
    # Create inverse mask
    mask_inv = cv2.bitwise_not(mask)
    
    # Extract cloak region from background
    cloak_area = cv2.bitwise_and(background, background, mask=mask)
    
    # Extract non-cloak region from current frame
    non_cloak_area = cv2.bitwise_and(frame, frame, mask=mask_inv)
    
    # Combine both parts
    final_output = cv2.addWeighted(cloak_area, 1, non_cloak_area, 1, 0)
    
    # Display the result
    cv2.imshow("🧙‍♂️ Invisibility Cloak - Press 'q' to quit", final_output)
    
    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
bg_video.release()
cv2.destroyAllWindows()

print("\n✨ Magic ended! Thanks for trying the invisibility cloak!")
