from site_text_classifier import SiteTextClassifier

clf = SiteTextClassifier(
    "D:\Desktop\python_projects_2022\sitesClassifier\classifier_model\saves_models\\"
)
print("po")
text = "Игрок забил гол в ворота! А ещё он был футболистом!"
# print(clf.predict([text]))
print(clf.predict([text]))
