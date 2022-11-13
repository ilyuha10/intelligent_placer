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
    <li>Лист бумаги целиком помещается в кадр</li>
    <li>Фон - светлый</li>
    <li>Отсутствие пересвеченных и серо-черных областей</li>
    </ul>
  </li>
  <li>Фигура
  <ul>
    <li>Фигура - выпуклый многоугольник с не более чем 10 вершинами</li>
    <li>Фигура задается темным маркером на листе А4, расположенном в вертикальном положении</li>
    <li>Минимальное расстояние от границ фигуры до границ листа - 1 см</li>
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
<li>Преобразовать изображение в чб, сгладить изображение и c помощью алгоритма Кэнни выделить границы многоугольника и объектов с фотографии.</li>
<li>Разделить контуры многоугольника и объектов. Думаю логично воспользоваться тем, что многоугольник изображается на белом листе А4, соответвенно вокргу него должен преобладать белый цвет</li>
  <li>Определить размеры многоугольника и предметов.</li>
<li>Первое (после перебора в лоб), что приходит в голову, это так сказать "человекоподобный алгоритм" - то как размещал бы предметы я.
  Берем предметы в порядке убывания площадей и пытаемся их разместить в углу незанятой предметами зоны. В приоритете размещать в углу той стороны многоугольника, которая наиболее похожа по размерам с одной из сторон предмета(надеюсь понятно написал).(Возможно это вообще окажется лишним, но так бы размещал я в реале:))
Тут встает вопрос: что значит разместить предмет круглой формы с указанными выше требованиями? Предлагаю при размещении таких объектов просто строить некоторый bounding box и уже его размещать. Также если на одном из шагов алгоритма площадь оставшейся зоны окажется меньше суммы площадей объектов, то алгоритм выводит false</li>
</ul>
<p>Еще подумываю над разумностью использования методов машинного обучения. Вместо размещения предметов в лоб, мне кажется, можно обучить программу на примере n фото тому помещаются ли предметы в многоугольник или нет. И с помощью условного knn уже на тестовых данных выводить тру или фолс. Единственное, тут нужно будет сильнее подзапариться с фотками) </p>
<p>P.S. над алгоритмом еще можно будет подумать</p>

