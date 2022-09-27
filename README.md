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
<li>Разделить контуры многоугольника и объектов. Думаю логично воспользоваться тем, что многоугольник изображается на белом листе А4, соответвенно вокргу него должен преобладать белый цвет</li>
<li>Cопоставить полученные изображения объектов с уже имеющимися предметами из images\things с помощью особых точек.</li>
<li>Первое (после перебора в лоб), что приходит в голову, это так сказать "человекоподобный алгоритм" - то как размещал бы предметы я.
  Берем предметы в порядке убывания площадей и пытаемся их разместить в углу незанятой предметами зоны. В приоритете размещать в углу той стороны многоугольника, которая наиболее похожа по размерам с одной из сторон предмета(надеюсь понятно написал).(Возможно это вообще окажется лишним, но так бы размещал я в реале:))
Тут встает вопрос: что значит разместить предмет круглой формы с указанными выше требованиями? Предлагаю при размещении таких объектов просто строить некоторый bounding box и уже его размещать. Также если на одном из шагов алгоритма площадь оставшейся зоны окажется меньше суммы площадей объектов, то алгоритм выводит false</li>
  <p>P.S. над алгоритмом еще можно будет подумать</p>
</ul>
<p>Стоит еще подумать над алгоритмом размещения)</p>
