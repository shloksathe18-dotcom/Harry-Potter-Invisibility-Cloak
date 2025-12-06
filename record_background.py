import cv2

print("""
╔═══════════════════════════════════════════════════════════╗
║  📹  BACKGROUND VIDEO RECORDER  📹                        ║
║                                                           ║
║  This will record 5 seconds of background video          ║
║  Move away from the camera!                              ║
╚═══════════════════════════════════════════════════════════╝
""")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Cannot access webcam!")
    exit()

# Get video properties
fps = 20
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(f"📊 Video: {width}x{height} @ {fps} FPS")
print("⚠️  MOVE AWAY FROM THE CAMERA NOW!")
print("📹 Recording in 3... 2... 1...")

# Create video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('video.mp4', fourcc, fps, (width, height))

frame_count = 0
max_frames = fps * 5  # 5 seconds

while frame_count < max_frames:
    ret, frame = cap.read()
    
    if not ret:
        print("❌ Error reading from webcam!")
        break
    
    out.write(frame)
    
    # Show recording progress
    remaining = (max_frames - frame_count) / fps
    cv2.putText(frame, f"Recording: {remaining:.1f}s", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Recording Background - Stay Away!", frame)
    
    frame_count += 1
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("✅ Background video saved as 'video.mp4'")
print("🧙‍♂️ Now run: python invisibility_cloak_video.py")
