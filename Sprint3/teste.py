import cv2, dlib, numpy as np, pickle, os, time

PREDICTOR = "shape_predictor_68_face_landmarks.dat" 
RECOG = "dlib_face_recognition_resnet_model_v1.dat"
DB_FILE = "db.pkl"
THRESH = 0.6

db = pickle.load(open(DB_FILE, "rb")) if os.path.exists(DB_FILE) else {}
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(PREDICTOR)
rec = dlib.face_recognition_model_v1(RECOG)

cap = cv2.VideoCapture(0)
validando = False

print("[E]=Cadastrar  [V]=Validar ON/OFF  [Q]=Sair")

while True:
    ok, frame = cap.read()
    if not ok:
        print("Erro na leitura do frame da câmera.")
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rects = detector(rgb, 1)

    if rects:
        for r in rects:
            shape = sp(rgb, r)
            chip = dlib.get_face_chip(rgb, shape)
            vec = np.array(rec.compute_face_descriptor(chip), dtype=np.float32)

            if validando and db:
                nome, dist = "Desconhecido", 999
                for n, v in db.items():
                    d = np.linalg.norm(vec - v)
                    if d < dist:
                        nome, dist = n, d
                if dist > THRESH:
                    nome = "Desconhecido"

                color = (0, 255, 0) if nome != "Desconhecido" else (0, 0, 255)
                cv2.rectangle(frame, (r.left(), r.top()), (r.right(), r.bottom()), color, 2)
                cv2.putText(frame, f"{nome}", (r.left(), r.top() - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

            #landmarks 
            for i in range(0, 68):
                x, y = shape.part(i).x, shape.part(i).y
                cv2.circle(frame, (x, y), 2, (255, 0, 0), -1)

    else:
        cv2.putText(frame, "Nenhuma face detectada.", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Faces", frame)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break
    if k == ord('v'):
        validando = not validando
    if k == ord('e') and len(rects) == 1:
        nome = input("Nome: ").strip()
        if nome:
            db[nome] = vec
            pickle.dump(db, open(DB_FILE, "wb"))
            print("Salvo:", nome)

cap.release()
cv2.destroyAllWindows()
