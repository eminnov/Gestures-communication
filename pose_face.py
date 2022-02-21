import cv2
import mediapipe as mp
from time import time

def verification_1() :
  nb = input("Choisir un nombre : ")
  if nb not in "123" :
    return int(nb)
  else :
    nb = nb = input("Choisir un nombre (1, 2 ou 3)")
    verification_1()

def verification_2(maximum) :
  nb = input("choisir un nombre : ")
  if nb in "1234567890" :
    return int(nb)
  else :
    print(f"choisir un nombre entre 0 et {maximum}")
    verification_2(maximum)

chemain_position_text = "test.txt"  

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue
    else :
      # verification : si le conducteur veut ajouter une nouvelle position
      if cv2.waitKey(5) & 0xFF == ord("n") :
        t_0 = time()
        if time() - t_0 < 1 :
          with open(chemain_position_text, "r") as f :
            liste_des_positions_de_la_main = f.read().splitlines()
          liste_des_positions_de_la_main_ = []
          for position in liste_des_positions_de_la_main :
            liste_des_positions_de_la_main_.append(position.split("|"))
          liste_des_positions_de_la_main = liste_des_positions_de_la_main_
          del liste_des_positions_de_la_main_
          print("""
          voulez vous supprimer, modifier ou ajouter une nouvelle position :
            1 : Ajouter
            2 : modifier (non traiter)
            3: supprimer
          """)
          """
          nb = verification_1()
          if nb == 1 :
            # Ajouter
            
          elif nb == 2 :
            # Modifier

          elif nb == 3 :
            # supprimer
            print("choisir la position qui vous voulez la supprimer :")
            for indix_position in len(liste_des_positions_de_la_main) :
              print(f"{indix_position} : {liste_des_positions_de_la_main[indix_position][0]}")  # liste_des_positions_de_la_main[indix_position][0] ==> nom de la position
            nb = verification_2(len(liste_des_positions_de_la_main))
            element_supp = liste_des_positions_de_la_main.pop(nb)
            verification_de_supp = input(f"voulez vous vraiment supprimer la position {element_supp[0]} (y/n) :")
            if verification_de_supp == "n" :
              liste_des_positions_de_la_main.append(element_supp)
            elif verification_de_supp == "y" :
              print(f"la position {element_supp[0]} est bien supprimer")
              del element_supp
            else : 
              verification_de_supp = input(f"voulez vous vraiment supprimer la position {element_supp[0]} (y/n) :")
              if verification_de_supp == "n" :
              liste_des_positions_de_la_main.append(element_supp)
              else :
                print(f"la position {element_supp[0]} est bien supprimer")
                del element_supp
            # enregis les modif 
            chaine_2 = ""
            for position in liste_des_positions_de_la_main :
              chaine_1 = ""
              for element in position :
                chaine_1 += element
                chaine_1 += "|"
              chaine_2 += chaine_1[:-1]
              chaine_2 += "\n"
            with open(chemain_position_text, "w") as f :
              f.write(chaine_2)

          else :
          """

      if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
          mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
    #mode_de_fonctionnement()
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()