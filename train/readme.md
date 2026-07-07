# Описание

Загружаем датасет Iris. Где:

`X` - признаки цветка: 
  * sepal length
  * sepal width
  * petal length
  * petal width

`y` - правильные классы:
  * setosa
  * versicolor
  * virginica

`train_test_split` делит данные на обучающую и тестовую выборку.

`LogisticRegression` обучается на `X_train` и `y_train`

`accuracy_score` проверяет качество модели на тестовой выборке.

`joblib.dump` сохраняет модель в app/model.pkl.