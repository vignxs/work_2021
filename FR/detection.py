import cv2
import numpy as np

weights = "C:\\Users\\ELCOT\\Downloads\\yolov3.weights"
config = "C:\\Users\\ELCOT\\Documents\\darknet\\darknet\\cfg\\yolov3.cfg"
coco = "C:\\Users\\ELCOT\\Documents\\darknet\\darknet\\data\\coco.names"

net = cv2.dnn.readNet(weights,config)

classes = []
with open(coco, 'r') as f:
    classes = f.read().splitlines()

cam = cv2.VideoCapture(0)
# img = cv2.imread("image.jpg")

while True:
    _, img = cam.read()

    height, width , _ = img.shape

    blob = cv2.dnn.blobFromImage(img, 1.0/255, (416, 416), (0, 0, 0), swapRB = True, crop = False)
    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layerOutputs  = net.forward(output_layers_names)


    boxes = []
    confidences = []
    class_ids = []

    for output in layerOutputs:
        for detection in output:
            scores = detection[:5]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0]* width)
                center_y = int(detection[1]*height)

                w = int(detection[2]*width)
                h = int(detection[3]*height)
                x = int(center_x - w/2)
                y = int(center_y - h/2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0, 255, size=(len(boxes), 3))

    for i in indexes.flatten():
        x,y, w, h= boxes[i]
        label = str(classes[class_ids[i]])
        confidence = str(round(confidences[i], 2))
        color = colors[i]
        cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
        cv2.putText(img, label + "I" + confidence, (x, y+20), font, 2, (255, 255, 255), 2)

    cv2.imshow("output", img)
    key = cv2.waitKey(0)
    if key ==27:
        break

cam.release()
cv2.destroyAllWindows()
