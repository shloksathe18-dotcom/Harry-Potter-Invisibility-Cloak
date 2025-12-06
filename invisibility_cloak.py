import cv2
import numpy as np
import time

print("""
╔═══════════════════════════════════════════════════════════╗
║  🧙‍♂️  HARRY POTTER'S INVISIBILITY CLOAK  🧙‍♂️              ║
║                                                           ║
║  Instructions:                                            ║
║  1. Move away from the camera for 3 seconds              ║
║  2. Wear something RED (cloak, cloth, shirt)             ║
║  3. The red area will become invisible!                  ║
║  4. Press 'q' to quit                                    ║
╚═══════════════════════════════════════════════════════════╝
""")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Cannot access webcam!")
    exit()

# Give time to read instructions
time.sleep(2)

print("📸 Capturing background in 3 seconds...")
print("⚠️  MOVE AWAY FROM THE CAMERA NOW!")
time.sleep(3)

# Capture background (take multiple frames and average for stability)
background = None
for i in range(30):
    ret, background = cap.read()
    if not ret:
        print("❌ Error: Cannot read from webcam!")
        exit()

background = np.flip(background, axis=1)  # Mirror the background

print("✅ Background captured!")
print("🎭 Now wear something RED and watch the magic!")
time.sleep(1)

# Main loop
while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Mirror the frame for natural interaction
    frame = np.flip(frame, axis=1)
    
    # Convert frame to HSV color space (better for color detection)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define range for red color in HSV
    # Red color wraps around in HSV, so we need two ranges
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    
    # Combine both red masks
    mask = mask1 + mask2
    
    # Morphological operations to remove noise and smooth the mask
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel, iterations=1)
    
    # Create inverse mask
    mask_inv = cv2.bitwise_not(mask)
    
    # Extract the cloak region from background
    cloak_area = cv2.bitwise_and(background, background, mask=mask)
    
    # Extract the non-cloak region from current frame
    non_cloak_area = cv2.bitwise_and(frame, frame, mask=mask_inv)
    
    # Combine both parts to create the final output
    final_output = cv2.addWeighted(cloak_area, 1, non_cloak_area, 1, 0)
    
    # Display the result
    cv2.imshow("🧙‍♂️ Invisibility Cloak - Press 'q' to quit", final_output)
    
    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

print("\n✨ Magic ended! Thanks for trying the invisibility cloak!")
