# ecommerce_costumer_churn_prediction
Ceci est un ensemble de données d'une entreprise de commerce électronique.

Nous allons réalisé une analyse des clients qui se désabonnent du service de l'entreprise et créer créer un modèle de prédiction du désabonnement fiable.

### Features du dataset : 

- **CustomerID:** Identifiant unique du client
- **Churn:** Indicateur de désabonnement
- **Tenure:** Durée d'appartenance du client à l'organisation
- **PreferredLoginDevice:** Appareil de connexion préféré du client
- **CityTier:** Niveau de la ville
- **WarehouseToHome:** Distance entre l'entrepôt et le domicile du client
- **PreferredPaymentMode:** Mode de paiement préféré du client
- **Gender:** Genre du client
- **HourSpendOnApp:** Nombre d'heures passées sur l'application mobile ou le site web
- **NumberOfDeviceRegistered:** Nombre total d'appareils enregistrés pour un client particulier
- **PreferedOrderCat:** Catégorie de commande préférée du client le mois dernier
- **SatisfactionScore:** Score de satisfaction du client sur le service
- **MaritalStatus:** Situation matrimoniale du client
- **NumberOfAddress:** Nombre total d'adresses ajoutées pour un client particulier
- **OrderAmountHikeFromlastYear:** Pourcentage d'augmentation de la commande depuis l'année dernière
- **CouponUsed:** Nombre total de coupons utilisés le mois dernier
- **OrderCount:** Nombre total de commandes passées le mois dernier
- **DaySinceLastOrder:** Jours depuis la dernière commande du client
- **CashbackAmount:** Montant moyen de cashback le mois dernier


- **Objectif :**
  - Construire un modèle prédictif capable d'identifier avec précision les clients susceptibles de quitter l'entreprise (churn) en se basant sur les variables fournies. Cela peut aider l'entreprise à prendre des mesures proactives pour fidéliser ces clients et réduire le taux de churn.

- **Analyse exploratoire :**
  - Effectuer une analyse exploratoire approfondie des données clients fournies afin de comprendre le comportement et les caractéristiques des clients. Cela inclut l'analyse de motifs et de tendances dans les variables. Cette analyse peut aider l'entreprise à mieux comprendre ses clients et à orienter ses prises de décision futures.


### Plan

**Aperçu des ensembles de données**

1. Examiner les données clients fournies pour se familiariser avec les variables et leur structure.
2. Vérifier la qualité des données, les valeurs manquantes et les éventuelles erreurs.
3. Déterminer si un prétraitement des données est nécessaire.

**Analyse exploratoire des données**

1. Analyser la distribution des variables pour identifier d'éventuels outliers ou anomalies.
2. Examiner la relation entre les variables pour identifier d'éventuelles corrélations ou tendances.
3. Visualiser les données pour obtenir des insights sur le comportement et les caractéristiques des clients.

**Prétraitement**

1. Nettoyer les données en traitant les valeurs manquantes, en convertissant les variables en types de données appropriés en traitant tout problème de qualité des données.
2. Sélectionner les variables les plus importantes pour la construction du modèle prédictif.

**Apprentissage automatique**

1. Tester plusieurs modèles ML /DL adéquats avec notre objectif.
2. Construire un modèle prédictif capable d'identifier les clients susceptibles de quitter l'entreprise.

**Évaluation du modèle**

1. Utiliser les métriques adéquates pour tester la performance du modèle.
2. Réajuster  les paramètres de modèle si necessaire.
3. Retraiter les données d'entraînement si necessaires.
