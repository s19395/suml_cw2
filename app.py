import streamlit as st
import pickle
from datetime import datetime
startTime = datetime.now()
# import znanych nam bibliotek

filename = "model2.sv"
model = pickle.load(open(filename,'rb'))
# otwieramy wcześniej wytrenowany model

# o ile wcześniej kodowaliśmy nasze zmienne, to teraz wprowadzamy etykiety z ich nazewnictwem
def main():

	st.set_page_config(page_title="Czy wyzdrowiejesz w ciągu tygodnia?")
	overview = st.container()
	left, center, right = st.columns([1,3,1])
	prediction = st.container()

	st.image("https://wallpapertag.com/wallpaper/full/3/2/6/447068-top-medical-desktop-backgrounds-1920x1440-windows-10.jpg")

	with overview:
		st.title("Czy wyzdrowiejesz w ciągu tygodnia")

	with center:
                age_input = st.number_input("Wprowadź wiek", 1, 100, 30, 1)
                height_input = st.number_input("Wprowadź wzrost", 50, 220, 170, 10)
                symptoms_slider = st.slider("Liczby występujących objawów", min_value=0, max_value=5)
                conditions_slider = st.slider( "Liczba chorób współistniejących", min_value=0, max_value=5)

	data = [[symptoms_slider, age_input,  conditions_slider, height_input]]
	recovery = model.predict(data)
	s_confidence = model.predict_proba(data)

	with prediction:
		st.header("Czy dana osoba wyzdrowieje w ciągu tygodnia? {0}".format("Tak" if recovery[0] == 0 else "Nie"))
		st.subheader("Pewność predykcji {0:.2f} %".format(s_confidence[0][recovery][0] * 100))

if __name__ == "__main__":
    main()
