#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 22:35:52 2023

@author: chaimanemir
"""

import pandas as pd
import streamlit as st
from churn_prediction_ia import predict_churn

def main():
    st.title("Prédiction de Churn")

    # Zone de saisie pour les données
    st.header("Entrez les données pour la prédiction:")
    uploaded_file = st.file_uploader("Téléchargez vos données pour la prédiction ici", type=["csv"])

    # Vérifier si un fichier a été téléchargé
    if uploaded_file is not None:
        # Lire le fichier CSV en un DataFrame
        df = pd.read_csv(uploaded_file)

        # Bouton pour effectuer la prédiction
        if st.button("Prédire"):
            # Obtenez la prédiction
            prediction = predict_churn(df)

            # Affichez la prédiction
            st.subheader("Résultat :")
            st.write("Churn prédit:", prediction)
            if prediction ==0 :
                st.write("Client wont churn")
            elif prediction ==1 :
                st.write("Client will likely  churn")

if __name__ == "__main__":
    main()
