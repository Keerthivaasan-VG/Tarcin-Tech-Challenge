import cv2

cap = cv2.VideoCapture(0)
w = int(cap.get(3)); h = int(cap.get(4)); fps = int(cap.get(5)) or 30
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (w,h))

for _ in range(500):  # capture 500 frames
    ret, frame = cap.read()
    if not ret: break
    edges = cv2.Canny(frame,100,200)
    overlay = cv2.addWeighted(frame,0.8,cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR),0.2,0)
    out.write(overlay)

cap.release(); out.release()
