<h2>Постановка задачи</h2>
<p>На вход алгоритма поступает фотография, на которой запечатлено несколько предметов на фоне images\backgroung.jpg и многоугольник, с ограничениями указанными ниже.
Предметы, которые могут находиться на фотографии заранее известны, и их фотографии находятся в images\things. На выходе алгоритм возвращает True, если данные предметы можно разместить в заданной многоугольником области, и соответственно, False иначе</p>

<h1>Требования</h1>
<ul>
  <li>Фотография
  <ul>
    <li>Формат .jpg</li>
    <li>Минимальное разрешение 632 х 1080 </li>
    <li>Фотография делается вертикально под углом 85-95 градусов</li>
    <li>Фотография делается на высоте 30 - 60 сантиметров над поверхностью</li>
    <li>Отсутствие пересвеченных и серо-черных областей</li>
    </ul>
  </li>
  <li>Фигура
  <ul>
    <li>Фигура - выпуклый многоугольник с не более чем 10 вершинами</li>
    <li>Фигура задается темным маркером на листе А4, расположенном в вертикальном положении</li>
    </ul>
  </li>
  <li>Предметы
    <ul>
      <li>Предметы полностью помещаются в кадре</li>
      <li>Предметы на фото не должны пересекаться друг с другом и с листом</li>
    <li>Предметы на фото не повторяются</li>
    </ul>
  
  </li>
</ul>

<h2>План работы</h2>
<ul>
<li> С помощью алгоритма Кэнни выделить границы многоугольника и объектов с фотографии + избавиться от шумов</li>
<li>Cопоставить полученные изображения объектов с уже имеющимися предметами из images\things. Тут я пока вижу 2 варианта: 
<ul>
<li>Находить норму разности вектора признаков шаблонных объектов и объектов с фотографии</li>
<li>Сравнивать объекты с помощью особых точек</li>
</ul></li>
<li>Для проверки вхождения объектов в заданный многоугольник можно сортировать объекты по убыванию площадей и проверять сначала вхождение наибольших предметов в заданную область. Ну а дальше перебирать))</li>
</ul>
<p>Стоит еще подумать над тем как хранить объекты и многоугольник в программе, ну и над алгоритмом размещения)</p>
